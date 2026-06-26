package raw

import (
	"context"
	"fmt"
	"math"
	"strings"

	"github.com/mark3labs/mcp-go/mcp"
	"github.com/mark3labs/mcp-go/server"
)

const serverInstructions = `KMIP Raw Spec Documents — 250+ crawled Markdown files covering every OASIS KMIP ` +
	`specification, profiles, usage guide, test cases, and use cases across all versions (v1.0–v3.0). ` +
	`Use search_raw to locate documents, then get_doc to read their content. ` +
	`Raw documents are large; get_doc supports char_offset/max_chars pagination.`

// NewServer wires the three raw-doc MCP tools to an mcp-go server.
func NewServer(idx *Index) *server.MCPServer {
	s := server.NewMCPServer("kmip-raw", "1.0.0", server.WithInstructions(serverInstructions))

	// search_raw
	s.AddTool(mcp.NewTool("search_raw",
		mcp.WithDescription("BM25 full-text search over raw KMIP spec documents. Returns ranked results with slug, title, doc_type, version, and score."),
		mcp.WithString("query", mcp.Required(), mcp.Description("Free-text search query")),
		mcp.WithString("doc_type", mcp.Description("Filter by document family: kmip-spec (alias: spec), kmip-profiles (alias: profiles), kmip-ug (alias: ug), kmip-testcases (alias: testcases), usecases, kmip-addtl-msg-enc, kmip-asym-key-profile, kmip-cs-profile, kmip-sa-sed-profile, kmip-suite-b-profile, kmip-sym-foundry-profile, kmip-sym-key-profile, kmip-opaque-obj-profile, kmip-tape-lib-profile")),
		mcp.WithString("version", mcp.Description("Filter by version string, e.g. \"2.1\", \"1.4\", \"3.0\"")),
		mcp.WithBoolean("final_only", mcp.Description("Only return canonical top-level docs (not intermediate draft/stage subdirs). Default true.")),
		mcp.WithNumber("limit", mcp.Description("Maximum results to return (default 10)")),
	), func(ctx context.Context, req mcp.CallToolRequest) (*mcp.CallToolResult, error) {
		return handleSearchRaw(idx, req)
	})

	// get_doc
	s.AddTool(mcp.NewTool("get_doc",
		mcp.WithDescription("Retrieve a raw KMIP spec document by slug, with optional pagination via char_offset/max_chars."),
		mcp.WithString("slug", mcp.Required(), mcp.Description("Document slug (full path or bare stem match)")),
		mcp.WithNumber("char_offset", mcp.Description("Character position to start reading (default 0)")),
		mcp.WithNumber("max_chars", mcp.Description("Maximum characters to return (default 20000)")),
	), func(ctx context.Context, req mcp.CallToolRequest) (*mcp.CallToolResult, error) {
		return handleGetDoc(idx, req)
	})

	// list_docs
	s.AddTool(mcp.NewTool("list_docs",
		mcp.WithDescription("List all raw KMIP spec documents with slug, doc_type, version, and title. Optionally filtered."),
		mcp.WithString("doc_type", mcp.Description("Filter by document family")),
		mcp.WithString("version", mcp.Description("Filter by version string")),
		mcp.WithBoolean("final_only", mcp.Description("Only canonical top-level docs (default true)")),
	), func(ctx context.Context, req mcp.CallToolRequest) (*mcp.CallToolResult, error) {
		return handleListDocs(idx, req)
	})

	return s
}

func handleSearchRaw(idx *Index, req mcp.CallToolRequest) (*mcp.CallToolResult, error) {
	query := req.GetString("query", "")
	docType := req.GetString("doc_type", "")
	version := req.GetString("version", "")
	finalOnly := req.GetBool("final_only", true)
	limit := req.GetInt("limit", 10)
	if limit <= 0 {
		limit = 10
	}

	results, err := idx.Search(query, docType, version, finalOnly, limit)
	if err != nil {
		return mcp.NewToolResultText(fmt.Sprintf("Search error: %v", err)), nil
	}
	if len(results) == 0 {
		return mcp.NewToolResultText("No results found."), nil
	}

	var sb strings.Builder
	fmt.Fprintf(&sb, "## Raw doc search results for %q\n\n", query)
	for i, r := range results {
		score := math.Abs(r.Score)
		fmt.Fprintf(&sb, "### %d. %s\n", i+1, r.Title)
		fmt.Fprintf(&sb, "- **slug**: `%s`\n", r.Slug)
		fmt.Fprintf(&sb, "- **doc_type**: %s | **version**: %s | **final**: %v\n", r.DocType, r.Version, r.IsFinal)
		if r.Description != "" {
			fmt.Fprintf(&sb, "- **description**: %s\n", r.Description)
		}
		fmt.Fprintf(&sb, "- **score**: %.4f\n\n", score)
	}
	return mcp.NewToolResultText(sb.String()), nil
}

func handleGetDoc(idx *Index, req mcp.CallToolRequest) (*mcp.CallToolResult, error) {
	slug := strings.TrimSpace(req.GetString("slug", ""))
	charOffset := req.GetInt("char_offset", 0)
	maxChars := req.GetInt("max_chars", 20000)
	if maxChars <= 0 {
		maxChars = 20000
	}

	content, err := idx.GetDoc(slug, charOffset, maxChars)
	if err != nil {
		return mcp.NewToolResultText(fmt.Sprintf("Error: %v", err)), nil
	}
	return mcp.NewToolResultText(content), nil
}

func handleListDocs(idx *Index, req mcp.CallToolRequest) (*mcp.CallToolResult, error) {
	docType := req.GetString("doc_type", "")
	version := req.GetString("version", "")
	finalOnly := req.GetBool("final_only", true)

	results, err := idx.ListDocs(docType, version, finalOnly)
	if err != nil {
		return mcp.NewToolResultText(fmt.Sprintf("Error: %v", err)), nil
	}

	var sb strings.Builder
	fmt.Fprintf(&sb, "## Raw Docs (%d)\n\n", len(results))
	for _, r := range results {
		finalStr := "no"
		if r.IsFinal {
			finalStr = "yes"
		}
		fmt.Fprintf(&sb, "- `%s` | %s | %s | final=%s | %s\n",
			r.Slug, r.DocType, r.Version, finalStr, r.Title)
	}
	return mcp.NewToolResultText(sb.String()), nil
}
