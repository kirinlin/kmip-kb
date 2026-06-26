package kb

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"io/fs"
	"os"
	"path/filepath"
	"strings"

	"github.com/kirinlin/kmip-kb/mcp_go/internal/parser"
	_ "modernc.org/sqlite"
)

// Article is a fully parsed KB article ready for indexing and serving.
type Article struct {
	Slug         string
	Title        string
	Category     string
	Status       string
	SpecVersions []string
	Related      []string
	Keywords     []string
	TagHex       string
	XMLText      string
	Full         string
}

// Index holds the in-memory SQLite database and the ordered article list.
type Index struct {
	db       *sql.DB
	articles []*Article
}

// BuildIndex scans kbRoot recursively, parses every .md file, and loads a SQLite
// in-memory FTS5 index for BM25 search.
func BuildIndex(kbRoot string) (*Index, error) {
	db, err := sql.Open("sqlite", ":memory:")
	if err != nil {
		return nil, fmt.Errorf("open sqlite: %w", err)
	}

	if err := initSchema(db); err != nil {
		return nil, fmt.Errorf("init schema: %w", err)
	}

	var paths []string
	_ = filepath.WalkDir(kbRoot, func(path string, d fs.DirEntry, err error) error {
		if err != nil || d.IsDir() {
			return err
		}
		if strings.HasSuffix(path, ".md") {
			paths = append(paths, path)
		}
		return nil
	})

	// Deterministic sort for consistent IDF weights across runs.
	sortStrings(paths)

	idx := &Index{db: db}

	tx, err := db.Begin()
	if err != nil {
		return nil, err
	}
	metaStmt, err := tx.Prepare(`INSERT INTO kb_meta(slug,path,title,category,status,spec_versions,related,keywords,tag_hex,xml_text,full_content) VALUES(?,?,?,?,?,?,?,?,?,?,?)`)
	if err != nil {
		_ = tx.Rollback()
		return nil, err
	}
	ftsStmt, err := tx.Prepare(`INSERT INTO kb_fts(slug,text_body) VALUES(?,?)`)
	if err != nil {
		_ = tx.Rollback()
		return nil, err
	}

	for _, path := range paths {
		doc, err := parser.ParseFile(kbRoot, path)
		if err != nil || doc == nil {
			continue
		}
		fm := doc.FM
		title := parser.Str(fm, "title")
		if title == "" {
			continue
		}
		art := &Article{
			Slug:         doc.Slug,
			Title:        title,
			Category:     parser.Str(fm, "category"),
			Status:       parser.Str(fm, "status"),
			SpecVersions: parser.StrSlice(fm, "spec_versions"),
			Related:      parser.StrSlice(fm, "related"),
			Keywords:     parser.StrSlice(fm, "keywords"),
			TagHex:       parser.Str(fm, "tag_hex"),
			XMLText:      parser.Str(fm, "xml_text"),
			Full:         doc.Full,
		}

		versionsJSON, _ := json.Marshal(art.SpecVersions)
		relatedJSON, _ := json.Marshal(art.Related)
		keywordsJSON, _ := json.Marshal(art.Keywords)

		_, err = metaStmt.Exec(
			art.Slug, path, art.Title, art.Category, art.Status,
			string(versionsJSON), string(relatedJSON), string(keywordsJSON),
			art.TagHex, art.XMLText, art.Full,
		)
		if err != nil {
			continue
		}

		textBody := buildKBTextBody(art, doc.Body)
		_, err = ftsStmt.Exec(art.Slug, textBody)
		if err != nil {
			continue
		}

		idx.articles = append(idx.articles, art)
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
		CREATE TABLE kb_meta (
			slug          TEXT PRIMARY KEY,
			path          TEXT,
			title         TEXT,
			category      TEXT,
			status        TEXT,
			spec_versions TEXT,
			related       TEXT,
			keywords      TEXT,
			tag_hex       TEXT,
			xml_text      TEXT,
			full_content  TEXT
		);
		CREATE VIRTUAL TABLE kb_fts USING fts5(
			slug UNINDEXED,
			text_body
		);
	`)
	return err
}

// buildKBTextBody constructs the searchable text for a KB article:
// title + keywords + slug words + first 3000 chars of body.
func buildKBTextBody(art *Article, body string) string {
	parts := []string{art.Title}
	if len(art.Keywords) > 0 {
		parts = append(parts, strings.Join(art.Keywords, " "))
	}
	slugWords := strings.NewReplacer("/", " ", "-", " ").Replace(art.Slug)
	parts = append(parts, slugWords)
	if len(body) > 3000 {
		body = body[:3000]
	}
	parts = append(parts, body)
	return strings.Join(parts, " ")
}

// SearchResult is a single ranked search hit.
type SearchResult struct {
	Slug         string
	Title        string
	Category     string
	Status       string
	SpecVersions []string
	Keywords     []string
	TagHex       string
	XMLText      string
	Score        float64
}

// Search runs an FTS5 BM25 query and post-filters by category/status/specVersion.
func (idx *Index) Search(query, category, status, specVersion string, limit int) ([]SearchResult, error) {
	if strings.TrimSpace(query) == "" {
		return nil, nil
	}

	// Over-fetch before Go-side post-filter; limit 500 is generous enough.
	rows, err := idx.db.Query(`
		SELECT m.slug, m.title, m.category, m.status, m.spec_versions, m.keywords, m.tag_hex, m.xml_text, kb_fts.rank
		FROM kb_fts
		JOIN kb_meta m ON m.slug = kb_fts.slug
		WHERE kb_fts MATCH ?
		ORDER BY rank
		LIMIT 500
	`, query)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var results []SearchResult
	for rows.Next() {
		var r SearchResult
		var versionsJSON, keywordsJSON string
		if err := rows.Scan(&r.Slug, &r.Title, &r.Category, &r.Status, &versionsJSON, &keywordsJSON, &r.TagHex, &r.XMLText, &r.Score); err != nil {
			continue
		}
		_ = json.Unmarshal([]byte(versionsJSON), &r.SpecVersions)
		_ = json.Unmarshal([]byte(keywordsJSON), &r.Keywords)

		if category != "" && r.Category != category {
			continue
		}
		if status != "" && r.Status != status {
			continue
		}
		if specVersion != "" && !containsStr(r.SpecVersions, specVersion) {
			continue
		}
		results = append(results, r)
		if len(results) >= limit {
			break
		}
	}
	return results, nil
}

// GetArticle looks up an article by exact slug, then by trailing component match.
func (idx *Index) GetArticle(slug string) (string, []string, error) {
	var full string
	err := idx.db.QueryRow(`SELECT full_content FROM kb_meta WHERE slug = ?`, slug).Scan(&full)
	if err == nil {
		return full, nil, nil
	}

	// Fallback: match on trailing slug component.
	var candidates []string
	rows, err2 := idx.db.Query(`SELECT slug, full_content FROM kb_meta WHERE slug LIKE ?`, "%/"+slug)
	if err2 != nil {
		return "", nil, err
	}
	defer rows.Close()
	var matched string
	for rows.Next() {
		var s, fc string
		if rows.Scan(&s, &fc) == nil {
			candidates = append(candidates, s)
			if matched == "" {
				matched = fc
			}
		}
	}
	if len(candidates) == 1 {
		return matched, nil, nil
	}
	if len(candidates) > 1 {
		return "", candidates, nil
	}

	// Collect all slugs for suggestion.
	allRows, _ := idx.db.Query(`SELECT slug FROM kb_meta ORDER BY slug`)
	if allRows != nil {
		defer allRows.Close()
		for allRows.Next() {
			var s string
			if allRows.Scan(&s) == nil {
				candidates = append(candidates, s)
			}
		}
	}
	return "", candidates, nil
}

// ListArticles returns slug/category/status/title for all articles, optionally filtered.
func (idx *Index) ListArticles(category, status string) ([]SearchResult, error) {
	q := `SELECT slug, title, category, status, spec_versions, keywords, tag_hex, xml_text FROM kb_meta`
	var args []any
	var where []string
	if category != "" {
		where = append(where, "category = ?")
		args = append(args, category)
	}
	if status != "" {
		where = append(where, "status = ?")
		args = append(args, status)
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
		var versionsJSON, keywordsJSON string
		if err := rows.Scan(&r.Slug, &r.Title, &r.Category, &r.Status, &versionsJSON, &keywordsJSON, &r.TagHex, &r.XMLText); err != nil {
			continue
		}
		_ = json.Unmarshal([]byte(versionsJSON), &r.SpecVersions)
		_ = json.Unmarshal([]byte(keywordsJSON), &r.Keywords)
		results = append(results, r)
	}
	return results, nil
}

// GetRelatedExplicit returns the front-matter related slugs for a given article.
func (idx *Index) GetRelatedExplicit(slug string) ([]string, error) {
	var relatedJSON string
	err := idx.db.QueryRow(`SELECT related FROM kb_meta WHERE slug = ?`, slug).Scan(&relatedJSON)
	if err != nil {
		return nil, err
	}
	var related []string
	_ = json.Unmarshal([]byte(relatedJSON), &related)
	return related, nil
}

// GetArticleTitle returns the title for a slug, used when rendering related lists.
func (idx *Index) GetArticleTitle(slug string) string {
	// Try exact match first, then trailing component.
	var title string
	_ = idx.db.QueryRow(`SELECT title FROM kb_meta WHERE slug = ?`, slug).Scan(&title)
	if title != "" {
		return title
	}
	_ = idx.db.QueryRow(`SELECT title FROM kb_meta WHERE slug LIKE ?`, "%/"+slug).Scan(&title)
	return title
}

// GetArticleKeywordsAndTitle returns title+keywords for a slug, used to form a BM25 neighbour query.
func (idx *Index) GetArticleKeywordsAndTitle(slug string) (string, []string) {
	var title, keywordsJSON string
	_ = idx.db.QueryRow(`SELECT title, keywords FROM kb_meta WHERE slug = ?`, slug).Scan(&title, &keywordsJSON)
	var kw []string
	_ = json.Unmarshal([]byte(keywordsJSON), &kw)
	return title, kw
}

func containsStr(ss []string, s string) bool {
	for _, v := range ss {
		if v == s {
			return true
		}
	}
	return false
}

func sortStrings(ss []string) {
	// Simple insertion sort — fast enough for ~500 paths at startup.
	for i := 1; i < len(ss); i++ {
		for j := i; j > 0 && ss[j] < ss[j-1]; j-- {
			ss[j], ss[j-1] = ss[j-1], ss[j]
		}
	}
}

// WriteTo serializes the index to a SQLite file at path using VACUUM INTO.
// The output file must not already exist.
func (idx *Index) WriteTo(path string) error {
	_, err := idx.db.Exec("VACUUM INTO ?", path)
	return err
}

// OpenFromBytes opens a pre-built SQLite index from an embedded byte slice.
// It writes the bytes to a temporary file, opens it immutable read-only, then
// removes the temp file (safe on Linux; on other platforms the file lingers
// until the OS cleans /tmp).
func OpenFromBytes(data []byte) (*Index, error) {
	f, err := os.CreateTemp("", "kmip-kb-*.db")
	if err != nil {
		return nil, fmt.Errorf("create temp db: %w", err)
	}
	tmpPath := f.Name()
	if _, err := f.Write(data); err != nil {
		f.Close()
		os.Remove(tmpPath)
		return nil, fmt.Errorf("write embedded db: %w", err)
	}
	if err := f.Close(); err != nil {
		os.Remove(tmpPath)
		return nil, fmt.Errorf("close temp db: %w", err)
	}

	// immutable=1 prevents SQLite from writing -wal/-shm files alongside the temp file.
	db, err := sql.Open("sqlite", "file:"+tmpPath+"?immutable=1")
	if err != nil {
		os.Remove(tmpPath)
		return nil, fmt.Errorf("open embedded db: %w", err)
	}
	if err := db.Ping(); err != nil {
		db.Close()
		os.Remove(tmpPath)
		return nil, fmt.Errorf("ping embedded db: %w", err)
	}

	// Unlink the file now; the open FD keeps the data alive on Linux.
	// On Windows this is a no-op error that we ignore.
	os.Remove(tmpPath)

	return &Index{db: db}, nil
}
