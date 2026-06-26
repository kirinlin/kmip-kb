package parser

import (
	"os"
	"path/filepath"
	"strings"

	"gopkg.in/yaml.v3"
)

// Doc holds the parsed content of a single Markdown file with YAML front matter.
type Doc struct {
	Slug string
	Path string
	FM   map[string]any
	Body string // everything after closing ---
	Full string // complete raw file content
}

// ParseFile reads a Markdown file, splits its YAML front matter, and returns a Doc.
// Returns (nil, nil) for files without front matter or missing required fields.
func ParseFile(root, path string) (*Doc, error) {
	raw, err := os.ReadFile(path)
	if err != nil {
		return nil, err
	}
	full := string(raw)

	if !strings.HasPrefix(full, "---") {
		return nil, nil
	}

	// Find closing ---
	rest := full[3:]
	idx := strings.Index(rest, "\n---")
	if idx < 0 {
		return nil, nil
	}
	yamlSrc := rest[:idx]
	body := strings.TrimSpace(rest[idx+4:])

	var fm map[string]any
	if err := yaml.Unmarshal([]byte(yamlSrc), &fm); err != nil || fm == nil {
		return nil, nil
	}

	rel, err := filepath.Rel(root, path)
	if err != nil {
		return nil, err
	}
	slug := strings.TrimSuffix(filepath.ToSlash(rel), ".md")

	return &Doc{
		Slug: slug,
		Path: path,
		FM:   fm,
		Body: body,
		Full: full,
	}, nil
}

// Str safely extracts a string field from a front-matter map.
func Str(fm map[string]any, key string) string {
	v, ok := fm[key]
	if !ok {
		return ""
	}
	s, _ := v.(string)
	return s
}

// StrSlice safely extracts a []string field from a front-matter map.
// Handles both []any and []string underlying types.
func StrSlice(fm map[string]any, key string) []string {
	v, ok := fm[key]
	if !ok {
		return nil
	}
	switch t := v.(type) {
	case []string:
		return t
	case []any:
		out := make([]string, 0, len(t))
		for _, item := range t {
			if s, ok := item.(string); ok {
				out = append(out, s)
			}
		}
		return out
	}
	return nil
}
