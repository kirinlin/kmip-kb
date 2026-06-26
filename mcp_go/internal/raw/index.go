package raw

import (
	"database/sql"
	"fmt"
	"io/fs"
	"os"
	"path/filepath"
	"regexp"
	"strings"

	"github.com/kirinlin/kmip-kb/mcp_go/internal/parser"
	_ "modernc.org/sqlite"
)

var versionRE = regexp.MustCompile(`^v(\d+\.\d+)$`)

// RawDoc holds metadata for a single raw spec document.
type RawDoc struct {
	Slug        string
	Title       string
	Description string
	DocType     string
	Version     string
	IsFinal     bool
	Full        string
}

// Index holds the in-memory SQLite database for raw spec documents.
type Index struct {
	db *sql.DB
}

// BuildIndex scans rawRoot for .md spec files, validates the raw/kmip/ subtree exists,
// and builds a SQLite FTS5 index. Exits with a diagnostic if raw/kmip/ is missing.
func BuildIndex(rawRoot string) (*Index, error) {
	kmipDir := filepath.Join(rawRoot, "kmip")
	entries, err := os.ReadDir(kmipDir)
	if err != nil || len(entries) == 0 {
		fmt.Fprintf(os.Stderr,
			"kmip-raw: raw/kmip/ directory is absent or empty.\n"+
				"Run `python scripts/kmip_crawler.py` to populate it first.\n")
		os.Exit(1)
	}

	db, err := sql.Open("sqlite", ":memory:")
	if err != nil {
		return nil, fmt.Errorf("open sqlite: %w", err)
	}
	if err := initSchema(db); err != nil {
		return nil, fmt.Errorf("init schema: %w", err)
	}

	var paths []string
	_ = filepath.WalkDir(rawRoot, func(path string, d fs.DirEntry, err error) error {
		if err != nil || d.IsDir() {
			return err
		}
		if !strings.HasSuffix(path, ".md") {
			return nil
		}
		if filepath.Base(path) == "index.md" {
			return nil
		}
		paths = append(paths, path)
		return nil
	})
	sortStrings(paths)

	idx := &Index{db: db}

	tx, _ := db.Begin()
	metaStmt, err := tx.Prepare(`INSERT INTO raw_meta(slug,path,title,description,doc_type,version,is_final,full_content) VALUES(?,?,?,?,?,?,?,?)`)
	if err != nil {
		_ = tx.Rollback()
		return nil, err
	}
	ftsStmt, err := tx.Prepare(`INSERT INTO raw_fts(slug,text_body) VALUES(?,?)`)
	if err != nil {
		_ = tx.Rollback()
		return nil, err
	}

	for _, path := range paths {
		doc, err := parser.ParseFile(rawRoot, path)
		if err != nil || doc == nil {
			continue
		}
		title := parser.Str(doc.FM, "title")
		if title == "" {
			continue
		}
		description := parser.Str(doc.FM, "description")
		docType, version, isFinal := extractPathMeta(doc.Slug)

		rd := &RawDoc{
			Slug:        doc.Slug,
			Title:       title,
			Description: description,
			DocType:     docType,
			Version:     version,
			IsFinal:     isFinal,
			Full:        doc.Full,
		}

		isFinalInt := 0
		if rd.IsFinal {
			isFinalInt = 1
		}
		_, err = metaStmt.Exec(rd.Slug, path, rd.Title, rd.Description, rd.DocType, rd.Version, isFinalInt, rd.Full)
		if err != nil {
			continue
		}
		textBody := buildRawTextBody(rd, doc.Body)
		_, err = ftsStmt.Exec(rd.Slug, textBody)
		if err != nil {
			continue
		}
	}

	metaStmt.Close()
	ftsStmt.Close()
	if err := tx.Commit(); err != nil {
		return nil, fmt.Errorf("commit: %w", err)
	}
	return idx, nil
}

func initSchema(db *sql.DB) error {
	_, err := db.Exec(`
		CREATE TABLE raw_meta (
			slug         TEXT PRIMARY KEY,
			path         TEXT,
			title        TEXT,
			description  TEXT,
			doc_type     TEXT,
			version      TEXT,
			is_final     INTEGER,
			full_content TEXT
		);
		CREATE VIRTUAL TABLE raw_fts USING fts5(
			slug UNINDEXED,
			text_body
		);
	`)
	return err
}

// extractPathMeta derives doc_type, version, and is_final from a slug of the form:
//
//	kmip/<doc-family>/v<x.y>/[stage/]<file>
func extractPathMeta(slug string) (docType, version string, isFinal bool) {
	parts := strings.SplitN(slug, "/", -1)
	// Expected layout: kmip / <family> / v<x.y> / [stage/] filename
	if len(parts) < 4 || parts[0] != "kmip" {
		return "", "", false
	}
	docType = parts[1]
	// Find the v<x.y> segment.
	for i, p := range parts[2:] {
		if m := versionRE.FindStringSubmatch(p); m != nil {
			version = m[1]
			// isFinal if the file is the next segment (i+3 == len-1 means exactly one segment after version).
			isFinal = (i + 3) == len(parts)-1
			return
		}
	}
	return docType, "", false
}

// buildRawTextBody constructs the searchable text for a raw document:
// title + description + doc_type words + version + first 5000 chars of body.
func buildRawTextBody(rd *RawDoc, body string) string {
	dtWords := strings.ReplaceAll(rd.DocType, "-", " ")
	parts := []string{rd.Title, rd.Description, dtWords, rd.Version}
	if len(body) > 5000 {
		body = body[:5000]
	}
	parts = append(parts, body)
	return strings.Join(parts, " ")
}

// SearchResult is one ranked search hit from the raw index.
type SearchResult struct {
	Slug        string
	Title       string
	Description string
	DocType     string
	Version     string
	IsFinal     bool
	Score       float64
}

// Search runs an FTS5 BM25 query and post-filters by docType, version, finalOnly.
func (idx *Index) Search(query, docType, version string, finalOnly bool, limit int) ([]SearchResult, error) {
	if strings.TrimSpace(query) == "" {
		return nil, nil
	}
	rows, err := idx.db.Query(`
		SELECT m.slug, m.title, m.description, m.doc_type, m.version, m.is_final, raw_fts.rank
		FROM raw_fts
		JOIN raw_meta m ON m.slug = raw_fts.slug
		WHERE raw_fts MATCH ?
		ORDER BY rank
		LIMIT 500
	`, query)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	// Canonical doc_type aliases (mirrors Python server logic).
	resolvedType := resolveDocType(docType)

	var results []SearchResult
	for rows.Next() {
		var r SearchResult
		var isFinalInt int
		if err := rows.Scan(&r.Slug, &r.Title, &r.Description, &r.DocType, &r.Version, &isFinalInt, &r.Score); err != nil {
			continue
		}
		r.IsFinal = isFinalInt == 1

		if finalOnly && !r.IsFinal {
			continue
		}
		if resolvedType != "" && r.DocType != resolvedType {
			continue
		}
		if version != "" && r.Version != version {
			continue
		}
		results = append(results, r)
		if len(results) >= limit {
			break
		}
	}
	return results, nil
}

// GetDoc retrieves a raw document's content with optional char_offset/max_chars pagination.
func (idx *Index) GetDoc(slug string, charOffset, maxChars int) (string, error) {
	var full, title, docType, version string
	var isFinalInt int
	err := idx.db.QueryRow(`SELECT full_content, title, doc_type, version, is_final FROM raw_meta WHERE slug = ?`, slug).
		Scan(&full, &title, &docType, &version, &isFinalInt)
	if err != nil {
		// Try trailing match.
		rows, err2 := idx.db.Query(`SELECT full_content, title, doc_type, version, is_final FROM raw_meta WHERE slug LIKE ?`, "%/"+slug)
		if err2 != nil {
			return "", err
		}
		defer rows.Close()
		if rows.Next() {
			if rows.Scan(&full, &title, &docType, &version, &isFinalInt) != nil {
				return "", err
			}
		} else {
			return "", fmt.Errorf("document %q not found", slug)
		}
	}

	total := len(full)
	if charOffset > total {
		charOffset = total
	}
	end := charOffset + maxChars
	if end > total {
		end = total
	}
	chunk := full[charOffset:end]

	isFinalStr := "no"
	if isFinalInt == 1 {
		isFinalStr = "yes"
	}
	header := fmt.Sprintf("<!-- slug: %s | doc_type: %s | version: %s | final: %s | total_chars: %d | showing: %d–%d -->\n\n",
		slug, docType, version, isFinalStr, total, charOffset, end)
	return header + chunk, nil
}

// ListDocs returns metadata rows, optionally filtered.
func (idx *Index) ListDocs(docType, version string, finalOnly bool) ([]SearchResult, error) {
	q := `SELECT slug, title, description, doc_type, version, is_final FROM raw_meta`
	var args []any
	var where []string
	resolvedType := resolveDocType(docType)
	if resolvedType != "" {
		where = append(where, "doc_type = ?")
		args = append(args, resolvedType)
	}
	if version != "" {
		where = append(where, "version = ?")
		args = append(args, version)
	}
	if finalOnly {
		where = append(where, "is_final = 1")
	}
	if len(where) > 0 {
		q += " WHERE " + strings.Join(where, " AND ")
	}
	q += " ORDER BY slug"

	rows, err := idx.db.Query(q, args...)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var results []SearchResult
	for rows.Next() {
		var r SearchResult
		var isFinalInt int
		if err := rows.Scan(&r.Slug, &r.Title, &r.Description, &r.DocType, &r.Version, &isFinalInt); err != nil {
			continue
		}
		r.IsFinal = isFinalInt == 1
		results = append(results, r)
	}
	return results, nil
}

// resolveDocType maps short aliases to canonical doc_type directory names.
func resolveDocType(dt string) string {
	switch dt {
	case "spec":
		return "kmip-spec"
	case "profiles":
		return "kmip-profiles"
	case "ug":
		return "kmip-ug"
	case "testcases":
		return "kmip-testcases"
	case "":
		return ""
	default:
		return dt // pass through canonical names unchanged
	}
}

func sortStrings(ss []string) {
	for i := 1; i < len(ss); i++ {
		for j := i; j > 0 && ss[j] < ss[j-1]; j-- {
			ss[j], ss[j-1] = ss[j-1], ss[j]
		}
	}
}
