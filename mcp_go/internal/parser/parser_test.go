package parser

import (
	"os"
	"path/filepath"
	"testing"
)

func writeTmp(t *testing.T, name, content string) string {
	t.Helper()
	dir := t.TempDir()
	path := filepath.Join(dir, name)
	if err := os.WriteFile(path, []byte(content), 0644); err != nil {
		t.Fatalf("write temp file: %v", err)
	}
	return path
}

func TestParseFile_valid(t *testing.T) {
	content := "---\ntitle: My Doc\ncategory: operation\n---\n# Body\n\nSome text.\n"
	path := writeTmp(t, "doc.md", content)
	dir := filepath.Dir(path)

	doc, err := ParseFile(dir, path)
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if doc == nil {
		t.Fatal("expected doc, got nil")
	}
	if doc.Slug != "doc" {
		t.Errorf("slug = %q, want %q", doc.Slug, "doc")
	}
	if Str(doc.FM, "title") != "My Doc" {
		t.Errorf("title = %q", Str(doc.FM, "title"))
	}
	if doc.Body == "" {
		t.Error("body should not be empty")
	}
	if doc.Full != content {
		t.Error("full content mismatch")
	}
}

func TestParseFile_noFrontMatter(t *testing.T) {
	path := writeTmp(t, "plain.md", "# Just a heading\n\nNo front matter here.\n")
	doc, err := ParseFile(filepath.Dir(path), path)
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if doc != nil {
		t.Error("expected nil for file without front matter")
	}
}

func TestParseFile_malformedYAML(t *testing.T) {
	path := writeTmp(t, "bad.md", "---\ntitle: [unclosed\n---\nbody\n")
	doc, err := ParseFile(filepath.Dir(path), path)
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if doc != nil {
		t.Error("expected nil for malformed YAML")
	}
}

func TestParseFile_subdir(t *testing.T) {
	root := t.TempDir()
	sub := filepath.Join(root, "operations")
	if err := os.MkdirAll(sub, 0755); err != nil {
		t.Fatal(err)
	}
	path := filepath.Join(sub, "create.md")
	if err := os.WriteFile(path, []byte("---\ntitle: Create\n---\nbody\n"), 0644); err != nil {
		t.Fatal(err)
	}
	doc, err := ParseFile(root, path)
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if doc == nil {
		t.Fatal("expected doc, got nil")
	}
	if doc.Slug != "operations/create" {
		t.Errorf("slug = %q, want %q", doc.Slug, "operations/create")
	}
}

func TestStr(t *testing.T) {
	fm := map[string]any{"key": "value", "num": 42}
	if got := Str(fm, "key"); got != "value" {
		t.Errorf("got %q", got)
	}
	if got := Str(fm, "missing"); got != "" {
		t.Errorf("got %q, want empty", got)
	}
	if got := Str(fm, "num"); got != "" {
		t.Errorf("non-string should return empty, got %q", got)
	}
}

func TestStrSlice(t *testing.T) {
	fm := map[string]any{
		"list_any":    []any{"a", "b", "c"},
		"list_str":    []string{"x", "y"},
		"not_a_slice": "hello",
	}

	got := StrSlice(fm, "list_any")
	if len(got) != 3 || got[0] != "a" || got[2] != "c" {
		t.Errorf("list_any: got %v", got)
	}
	got = StrSlice(fm, "list_str")
	if len(got) != 2 || got[0] != "x" {
		t.Errorf("list_str: got %v", got)
	}
	if got = StrSlice(fm, "missing"); got != nil {
		t.Errorf("missing: got %v", got)
	}
	if got = StrSlice(fm, "not_a_slice"); got != nil {
		t.Errorf("not_a_slice: got %v", got)
	}
}
