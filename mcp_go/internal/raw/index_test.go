package raw

import (
	"os"
	"path/filepath"
	"testing"
)

// rawDoc writes a raw spec markdown file under root at the given relative path.
func rawDoc(t *testing.T, root, relPath, content string) {
	t.Helper()
	full := filepath.Join(root, relPath)
	if err := os.MkdirAll(filepath.Dir(full), 0755); err != nil {
		t.Fatalf("mkdir %s: %v", filepath.Dir(full), err)
	}
	if err := os.WriteFile(full, []byte(content), 0644); err != nil {
		t.Fatalf("write %s: %v", full, err)
	}
}

func buildTestRawIndex(t *testing.T) *Index {
	t.Helper()
	root := t.TempDir()

	// Ensure raw/kmip/ exists so BuildIndex doesn't exit.
	if err := os.MkdirAll(filepath.Join(root, "kmip"), 0755); err != nil {
		t.Fatal(err)
	}

	rawDoc(t, root, "kmip/kmip-spec/v2.1/kmip-spec-v2.1.md", `---
title: KMIP Specification v2.1
description: The Key Management Interoperability Protocol version 2.1
url: https://docs.oasis-open.org/kmip/kmip-spec/v2.1/kmip-spec-v2.1.html
---
# KMIP Specification v2.1

This document specifies the KMIP protocol for key management interoperability.
The TTLV encoding defines how messages are structured on the wire.
`)

	rawDoc(t, root, "kmip/kmip-spec/v2.1/csd01/kmip-spec-v2.1-csd01.md", `---
title: KMIP Specification v2.1 csd01
description: Committee Specification Draft 01
url: https://docs.oasis-open.org/kmip/kmip-spec/v2.1/csd01/kmip-spec-v2.1-csd01.html
---
# KMIP Specification v2.1 Committee Specification Draft 01
`)

	rawDoc(t, root, "kmip/kmip-spec/v2.0/kmip-spec-v2.0.md", `---
title: KMIP Specification v2.0
description: The Key Management Interoperability Protocol version 2.0
---
# KMIP Specification v2.0

This is the v2.0 specification for KMIP key management protocol.
`)

	rawDoc(t, root, "kmip/kmip-profiles/v2.1/kmip-profiles-v2.1.md", `---
title: KMIP Profiles v2.1
description: KMIP profiles and conformance requirements
---
# KMIP Profiles v2.1

Profiles define conformance requirements for KMIP implementations.
The baseline profile requires TLS and TTLV encoding.
`)

	rawDoc(t, root, "kmip/kmip-ug/v2.1/kmip-ug-v2.1.md", `---
title: KMIP Usage Guide v2.1
description: Guidance for KMIP implementors and users
---
# KMIP Usage Guide v2.1

This guide provides practical examples for KMIP operations.
`)

	// index.md should be skipped.
	rawDoc(t, root, "kmip/index.md", "---\ntitle: Index\n---\n# Index\n")

	// File without title should be skipped.
	rawDoc(t, root, "kmip/kmip-spec/v1.4/notitle.md", "---\ndescription: no title here\n---\nbody\n")

	idx, err := BuildIndex(root)
	if err != nil {
		t.Fatalf("BuildIndex: %v", err)
	}
	return idx
}

// ---- extractPathMeta ----

func TestExtractPathMeta(t *testing.T) {
	cases := []struct {
		slug       string
		wantType   string
		wantVer    string
		wantFinal  bool
	}{
		{
			slug:      "kmip/kmip-spec/v2.1/kmip-spec-v2.1",
			wantType:  "kmip-spec",
			wantVer:   "2.1",
			wantFinal: true,
		},
		{
			slug:      "kmip/kmip-spec/v2.1/csd01/kmip-spec-v2.1-csd01",
			wantType:  "kmip-spec",
			wantVer:   "2.1",
			wantFinal: false,
		},
		{
			slug:      "kmip/kmip-profiles/v1.4/kmip-profiles-v1.4",
			wantType:  "kmip-profiles",
			wantVer:   "1.4",
			wantFinal: true,
		},
		{
			slug:      "kmip/kmip-ug/v2.0/os/kmip-ug-v2.0-os",
			wantType:  "kmip-ug",
			wantVer:   "2.0",
			wantFinal: false,
		},
		{
			// Non-kmip prefix → empty results.
			slug:      "other/stuff/v1.0/file",
			wantType:  "",
			wantVer:   "",
			wantFinal: false,
		},
	}

	for _, tc := range cases {
		dt, ver, final := extractPathMeta(tc.slug)
		if dt != tc.wantType {
			t.Errorf("slug %q: doc_type = %q, want %q", tc.slug, dt, tc.wantType)
		}
		if ver != tc.wantVer {
			t.Errorf("slug %q: version = %q, want %q", tc.slug, ver, tc.wantVer)
		}
		if final != tc.wantFinal {
			t.Errorf("slug %q: is_final = %v, want %v", tc.slug, final, tc.wantFinal)
		}
	}
}

// ---- BuildIndex ----

func TestBuildIndex_counts(t *testing.T) {
	idx := buildTestRawIndex(t)
	// 5 docs (csd01 draft + 4 finals); index.md and no-title doc skipped.
	results, err := idx.ListDocs("", "", false)
	if err != nil {
		t.Fatalf("ListDocs: %v", err)
	}
	if len(results) != 5 {
		t.Errorf("got %d docs, want 5", len(results))
	}
}

func TestBuildIndex_finalOnly(t *testing.T) {
	idx := buildTestRawIndex(t)
	results, err := idx.ListDocs("", "", true)
	if err != nil {
		t.Fatalf("ListDocs: %v", err)
	}
	// csd01 draft should be excluded.
	if len(results) != 4 {
		t.Errorf("got %d final docs, want 4", len(results))
	}
	for _, r := range results {
		if !r.IsFinal {
			t.Errorf("doc %q should be final", r.Slug)
		}
	}
}

// ---- Search ----

func TestSearch_basic(t *testing.T) {
	idx := buildTestRawIndex(t)
	results, err := idx.Search("TTLV encoding", "", "", true, 5)
	if err != nil {
		t.Fatalf("Search: %v", err)
	}
	if len(results) == 0 {
		t.Fatal("expected results, got none")
	}
}

func TestSearch_emptyQuery(t *testing.T) {
	idx := buildTestRawIndex(t)
	results, err := idx.Search("   ", "", "", true, 5)
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if results != nil {
		t.Error("blank query should return nil")
	}
}

func TestSearch_docTypeFilter(t *testing.T) {
	idx := buildTestRawIndex(t)
	results, err := idx.Search("KMIP", "kmip-profiles", "", true, 10)
	if err != nil {
		t.Fatalf("Search: %v", err)
	}
	for _, r := range results {
		if r.DocType != "kmip-profiles" {
			t.Errorf("result %q has doc_type %q, want kmip-profiles", r.Slug, r.DocType)
		}
	}
	if len(results) == 0 {
		t.Error("expected at least one profile result")
	}
}

func TestSearch_docTypeAlias(t *testing.T) {
	idx := buildTestRawIndex(t)
	// "spec" is an alias for "kmip-spec".
	aliased, err := idx.Search("KMIP", "spec", "", true, 10)
	if err != nil {
		t.Fatalf("Search (alias): %v", err)
	}
	canonical, err := idx.Search("KMIP", "kmip-spec", "", true, 10)
	if err != nil {
		t.Fatalf("Search (canonical): %v", err)
	}
	if len(aliased) != len(canonical) {
		t.Errorf("alias 'spec' returned %d results, canonical 'kmip-spec' returned %d", len(aliased), len(canonical))
	}
}

func TestSearch_versionFilter(t *testing.T) {
	idx := buildTestRawIndex(t)
	results, err := idx.Search("KMIP", "", "2.0", true, 10)
	if err != nil {
		t.Fatalf("Search: %v", err)
	}
	for _, r := range results {
		if r.Version != "2.0" {
			t.Errorf("result %q has version %q, want 2.0", r.Slug, r.Version)
		}
	}
}

func TestSearch_finalOnlyFalse(t *testing.T) {
	idx := buildTestRawIndex(t)
	withDrafts, err := idx.Search("KMIP", "kmip-spec", "2.1", false, 10)
	if err != nil {
		t.Fatalf("Search: %v", err)
	}
	withoutDrafts, err := idx.Search("KMIP", "kmip-spec", "2.1", true, 10)
	if err != nil {
		t.Fatalf("Search: %v", err)
	}
	if len(withDrafts) <= len(withoutDrafts) {
		t.Errorf("withDrafts (%d) should be > withoutDrafts (%d)", len(withDrafts), len(withoutDrafts))
	}
}

// ---- GetDoc ----

func TestGetDoc_fullContent(t *testing.T) {
	idx := buildTestRawIndex(t)
	content, err := idx.GetDoc("kmip/kmip-spec/v2.1/kmip-spec-v2.1", 0, 20000)
	if err != nil {
		t.Fatalf("GetDoc: %v", err)
	}
	if content == "" {
		t.Fatal("expected content, got empty")
	}
	// Should include the header comment.
	if content[:4] != "<!--" {
		t.Errorf("content should start with <!-- header, got: %q", content[:20])
	}
}

func TestGetDoc_pagination(t *testing.T) {
	idx := buildTestRawIndex(t)
	first, err := idx.GetDoc("kmip/kmip-spec/v2.1/kmip-spec-v2.1", 0, 50)
	if err != nil {
		t.Fatalf("GetDoc first page: %v", err)
	}
	second, err := idx.GetDoc("kmip/kmip-spec/v2.1/kmip-spec-v2.1", 50, 50)
	if err != nil {
		t.Fatalf("GetDoc second page: %v", err)
	}
	if first == second {
		t.Error("consecutive pages should differ")
	}
}

func TestGetDoc_notFound(t *testing.T) {
	idx := buildTestRawIndex(t)
	_, err := idx.GetDoc("nonexistent/doc", 0, 20000)
	if err == nil {
		t.Error("expected error for missing doc")
	}
}

func TestGetDoc_trailingSlugMatch(t *testing.T) {
	idx := buildTestRawIndex(t)
	content, err := idx.GetDoc("kmip-profiles-v2.1", 0, 20000)
	if err != nil {
		t.Fatalf("GetDoc trailing match: %v", err)
	}
	if content == "" {
		t.Error("expected content for trailing slug match")
	}
}

// ---- ListDocs ----

func TestListDocs_docTypeFilter(t *testing.T) {
	idx := buildTestRawIndex(t)
	results, err := idx.ListDocs("kmip-ug", "", true)
	if err != nil {
		t.Fatalf("ListDocs: %v", err)
	}
	if len(results) != 1 {
		t.Errorf("got %d ug docs, want 1", len(results))
	}
	if results[0].DocType != "kmip-ug" {
		t.Errorf("doc_type = %q, want kmip-ug", results[0].DocType)
	}
}

func TestListDocs_versionFilter(t *testing.T) {
	idx := buildTestRawIndex(t)
	results, err := idx.ListDocs("", "2.1", true)
	if err != nil {
		t.Fatalf("ListDocs: %v", err)
	}
	for _, r := range results {
		if r.Version != "2.1" {
			t.Errorf("result %q has version %q, want 2.1", r.Slug, r.Version)
		}
	}
	if len(results) == 0 {
		t.Error("expected v2.1 docs")
	}
}

func TestResolveDocType(t *testing.T) {
	cases := map[string]string{
		"spec":     "kmip-spec",
		"profiles": "kmip-profiles",
		"ug":       "kmip-ug",
		"testcases": "kmip-testcases",
		"kmip-spec":     "kmip-spec",     // canonical passthrough
		"kmip-profiles": "kmip-profiles", // canonical passthrough
		"":         "",
	}
	for input, want := range cases {
		if got := resolveDocType(input); got != want {
			t.Errorf("resolveDocType(%q) = %q, want %q", input, got, want)
		}
	}
}
