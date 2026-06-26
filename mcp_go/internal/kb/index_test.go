package kb

import (
	"os"
	"path/filepath"
	"testing"
)

// article writes a minimal valid KB markdown file and returns its path.
func article(t *testing.T, root, relPath, content string) {
	t.Helper()
	full := filepath.Join(root, relPath)
	if err := os.MkdirAll(filepath.Dir(full), 0755); err != nil {
		t.Fatalf("mkdir %s: %v", filepath.Dir(full), err)
	}
	if err := os.WriteFile(full, []byte(content), 0644); err != nil {
		t.Fatalf("write %s: %v", full, err)
	}
}

func buildTestIndex(t *testing.T) (*Index, string) {
	t.Helper()
	root := t.TempDir()

	article(t, root, "operations/encrypt.md", `---
title: Encrypt
category: operation
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.17"
status: reviewed
related: ["decrypt", "symmetric-key"]
keywords: ["encrypt", "cipher", "AES"]
tag_hex: "420031"
xml_text: "Encrypt"
---
# Encrypt

Performs encryption of plaintext data using the specified cryptographic parameters.
`)

	article(t, root, "operations/decrypt.md", `---
title: Decrypt
category: operation
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.18"
status: reviewed
related: ["encrypt", "symmetric-key"]
keywords: ["decrypt", "cipher", "AES"]
---
# Decrypt

Performs decryption of ciphertext data.
`)

	article(t, root, "objects/symmetric-key.md", `---
title: Symmetric Key
category: object
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "2.2"
status: reviewed
related: ["key-block"]
keywords: ["symmetric", "AES", "key material"]
tag_hex: "420064"
xml_text: "SymmetricKey"
---
# Symmetric Key

A Symmetric Key is a Managed Cryptographic Object containing a symmetric key.
`)

	article(t, root, "attributes/state.md", `---
title: State
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.8"
status: draft
related: []
keywords: ["state", "lifecycle", "active", "deactivated"]
tag_hex: "420083"
xml_text: "State"
---
# State

The State attribute represents the lifecycle state of a Managed Object.
`)

	// File without front matter — should be silently skipped.
	article(t, root, "README.md", "# Just a readme\n")

	idx, err := BuildIndex(root)
	if err != nil {
		t.Fatalf("BuildIndex: %v", err)
	}
	return idx, root
}

// ---- BuildIndex ----

func TestBuildIndex_counts(t *testing.T) {
	idx, _ := buildTestIndex(t)
	results, err := idx.ListArticles("", "")
	if err != nil {
		t.Fatalf("ListArticles: %v", err)
	}
	if len(results) != 4 {
		t.Errorf("got %d articles, want 4", len(results))
	}
}

// ---- Search ----

func TestSearch_basic(t *testing.T) {
	idx, _ := buildTestIndex(t)
	results, err := idx.Search("encrypt", "", "", "", 10)
	if err != nil {
		t.Fatalf("Search: %v", err)
	}
	if len(results) == 0 {
		t.Fatal("expected results, got none")
	}
	// "encrypt" keyword is in both encrypt and decrypt docs; encrypt should rank first.
	if results[0].Slug != "operations/encrypt" {
		t.Errorf("top result slug = %q, want operations/encrypt", results[0].Slug)
	}
}

func TestSearch_emptyQuery(t *testing.T) {
	idx, _ := buildTestIndex(t)
	results, err := idx.Search("", "", "", "", 10)
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if results != nil {
		t.Error("empty query should return nil")
	}
}

func TestSearch_categoryFilter(t *testing.T) {
	idx, _ := buildTestIndex(t)
	results, err := idx.Search("AES", "object", "", "", 10)
	if err != nil {
		t.Fatalf("Search: %v", err)
	}
	for _, r := range results {
		if r.Category != "object" {
			t.Errorf("result %q has category %q, want object", r.Slug, r.Category)
		}
	}
	if len(results) == 0 {
		t.Error("expected at least one object result for 'AES'")
	}
}

func TestSearch_statusFilter(t *testing.T) {
	idx, _ := buildTestIndex(t)
	results, err := idx.Search("state lifecycle", "", "draft", "", 10)
	if err != nil {
		t.Fatalf("Search: %v", err)
	}
	for _, r := range results {
		if r.Status != "draft" {
			t.Errorf("result %q has status %q, want draft", r.Slug, r.Status)
		}
	}
}

func TestSearch_specVersionFilter(t *testing.T) {
	idx, _ := buildTestIndex(t)
	// symmetric-key is in 1.0; encrypt is not.
	results, err := idx.Search("AES key", "", "", "1.0", 10)
	if err != nil {
		t.Fatalf("Search: %v", err)
	}
	for _, r := range results {
		found := false
		for _, v := range r.SpecVersions {
			if v == "1.0" {
				found = true
				break
			}
		}
		if !found {
			t.Errorf("result %q does not include spec version 1.0 (versions: %v)", r.Slug, r.SpecVersions)
		}
	}
}

func TestSearch_limit(t *testing.T) {
	idx, _ := buildTestIndex(t)
	results, err := idx.Search("AES", "", "", "", 1)
	if err != nil {
		t.Fatalf("Search: %v", err)
	}
	if len(results) > 1 {
		t.Errorf("got %d results with limit=1", len(results))
	}
}

// ---- GetArticle ----

func TestGetArticle_exactSlug(t *testing.T) {
	idx, _ := buildTestIndex(t)
	full, cands, err := idx.GetArticle("operations/encrypt")
	if err != nil {
		t.Fatalf("GetArticle: %v", err)
	}
	if cands != nil {
		t.Errorf("expected no candidates, got %v", cands)
	}
	if full == "" {
		t.Error("expected full content, got empty")
	}
	if full[:3] != "---" {
		t.Error("full content should start with front matter delimiter")
	}
}

func TestGetArticle_trailingSlug(t *testing.T) {
	idx, _ := buildTestIndex(t)
	// "encrypt" alone should match "operations/encrypt" (only one match).
	full, cands, err := idx.GetArticle("encrypt")
	if err != nil {
		t.Fatalf("GetArticle: %v", err)
	}
	if cands != nil {
		t.Errorf("expected no candidates, got %v", cands)
	}
	if full == "" {
		t.Error("expected content for trailing match")
	}
}

func TestGetArticle_notFound(t *testing.T) {
	idx, _ := buildTestIndex(t)
	full, cands, err := idx.GetArticle("nonexistent")
	if err != nil {
		t.Fatalf("GetArticle: %v", err)
	}
	if full != "" {
		t.Error("expected empty content for missing slug")
	}
	// Should return some candidate slugs for suggestions.
	if len(cands) == 0 {
		t.Error("expected candidate slugs for suggestions")
	}
}

// ---- ListArticles ----

func TestListArticles_noFilter(t *testing.T) {
	idx, _ := buildTestIndex(t)
	results, err := idx.ListArticles("", "")
	if err != nil {
		t.Fatalf("ListArticles: %v", err)
	}
	if len(results) != 4 {
		t.Errorf("got %d, want 4", len(results))
	}
}

func TestListArticles_categoryFilter(t *testing.T) {
	idx, _ := buildTestIndex(t)
	results, err := idx.ListArticles("operation", "")
	if err != nil {
		t.Fatalf("ListArticles: %v", err)
	}
	if len(results) != 2 {
		t.Errorf("got %d operation articles, want 2", len(results))
	}
	for _, r := range results {
		if r.Category != "operation" {
			t.Errorf("unexpected category %q", r.Category)
		}
	}
}

func TestListArticles_statusFilter(t *testing.T) {
	idx, _ := buildTestIndex(t)
	results, err := idx.ListArticles("", "draft")
	if err != nil {
		t.Fatalf("ListArticles: %v", err)
	}
	if len(results) != 1 {
		t.Errorf("got %d draft articles, want 1", len(results))
	}
	if results[0].Slug != "attributes/state" {
		t.Errorf("unexpected slug %q", results[0].Slug)
	}
}

// ---- GetRelatedExplicit ----

func TestGetRelatedExplicit(t *testing.T) {
	idx, _ := buildTestIndex(t)
	related, err := idx.GetRelatedExplicit("operations/encrypt")
	if err != nil {
		t.Fatalf("GetRelatedExplicit: %v", err)
	}
	if len(related) != 2 {
		t.Errorf("got %d related slugs, want 2: %v", len(related), related)
	}
	found := false
	for _, r := range related {
		if r == "decrypt" {
			found = true
		}
	}
	if !found {
		t.Errorf("expected 'decrypt' in related, got %v", related)
	}
}

func TestGetRelatedExplicit_notFound(t *testing.T) {
	idx, _ := buildTestIndex(t)
	_, err := idx.GetRelatedExplicit("nonexistent")
	if err == nil {
		t.Error("expected error for missing slug")
	}
}

// ---- GetArticleTitle ----

func TestGetArticleTitle(t *testing.T) {
	idx, _ := buildTestIndex(t)
	title := idx.GetArticleTitle("operations/encrypt")
	if title != "Encrypt" {
		t.Errorf("got %q, want Encrypt", title)
	}
	// Bare slug trailing match.
	title = idx.GetArticleTitle("decrypt")
	if title != "Decrypt" {
		t.Errorf("bare slug: got %q, want Decrypt", title)
	}
	// Missing slug returns empty.
	if title = idx.GetArticleTitle("nope"); title != "" {
		t.Errorf("missing: got %q", title)
	}
}
