package kb

import (
	"context"
	"fmt"
	"math"
	"strings"

	"github.com/mark3labs/mcp-go/mcp"
	"github.com/mark3labs/mcp-go/server"
)

const serverInstructions = `KMIP Knowledge Base — 452 original-prose articles covering KMIP 1.0–2.1 ` +
	`operations, attributes, objects, TTLV encoding, profiles, concepts, workflows, and examples. ` +
	`Use search_kb first, then get_article to read full content.`

// NewServer wires the four KB MCP tools to an mcp-go server.
func NewServer(idx *Index) *server.MCPServer {
	s := server.NewMCPServer("kmip-kb", "1.0.0", server.WithInstructions(serverInstructions))

	// search_kb
	s.AddTool(mcp.NewTool("search_kb",
		mcp.WithDescription("BM25 full-text search over KMIP KB articles. Returns ranked results with slug, title, category, status, keywords, and BM25 score."),
		mcp.WithString("query", mcp.Required(), mcp.Description("Free-text search query")),
		mcp.WithString("category", mcp.Description("Filter by category: operation, attribute, object, concept, encoding, enumerations, structures, messages, profile, reference, workflow, example, usage-guide, schema, index")),
		mcp.WithString("status", mcp.Description("Filter by status: stub, draft, reviewed")),
		mcp.WithString("spec_version", mcp.Description("Filter to articles that cover this KMIP version (e.g. \"2.1\", \"1.4\")")),
		mcp.WithNumber("limit", mcp.Description("Maximum results to return (default 10)")),
	), func(ctx context.Context, req mcp.CallToolRequest) (*mcp.CallToolResult, error) {
		return handleSearchKB(idx, req)
	})

	// get_article
	s.AddTool(mcp.NewTool("get_article",
		mcp.WithDescription("Retrieve the full Markdown content (front matter + prose) of a KB article by slug."),
		mcp.WithString("slug", mcp.Required(), mcp.Description("Article slug, e.g. \"operations/encrypt\" or bare name \"encrypt\"")),
	), func(ctx context.Context, req mcp.CallToolRequest) (*mcp.CallToolResult, error) {
		return handleGetArticle(idx, req)
	})

	// list_articles
	s.AddTool(mcp.NewTool("list_articles",
		mcp.WithDescription("List all KB articles with slug, category, status, and title. Optionally filtered."),
		mcp.WithString("category", mcp.Description("Filter by category")),
		mcp.WithString("status", mcp.Description("Filter by status: stub, draft, reviewed")),
	), func(ctx context.Context, req mcp.CallToolRequest) (*mcp.CallToolResult, error) {
		return handleListArticles(idx, req)
	})

	// get_related
	s.AddTool(mcp.NewTool("get_related",
		mcp.WithDescription("Find articles related to a given KB article: explicitly linked articles from front matter, plus BM25-ranked neighbours."),
		mcp.WithString("slug", mcp.Required(), mcp.Description("Article slug")),
		mcp.WithNumber("limit", mcp.Description("Maximum BM25 neighbour results (default 5)")),
	), func(ctx context.Context, req mcp.CallToolRequest) (*mcp.CallToolResult, error) {
		return handleGetRelated(idx, req)
	})

	return s
}

func handleSearchKB(idx *Index, req mcp.CallToolRequest) (*mcp.CallToolResult, error) {
	query := req.GetString("query", "")
	category := req.GetString("category", "")
	status := req.GetString("status", "")
	specVersion := req.GetString("spec_version", "")
	limit := req.GetInt("limit", 10)
	if limit <= 0 {
		limit = 10
	}

	results, err := idx.Search(query, category, status, specVersion, limit)
	if err != nil {
		// FTS5 syntax errors are user errors; return a helpful message.
		return mcp.NewToolResultText(fmt.Sprintf("Search error: %v", err)), nil
	}
	if len(results) == 0 {
		return mcp.NewToolResultText("No results found."), nil
	}

	var sb strings.Builder
	fmt.Fprintf(&sb, "## Search results for %q\n\n", query)
	for i, r := range results {
		score := math.Abs(r.Score)
		fmt.Fprintf(&sb, "### %d. %s\n", i+1, r.Title)
		fmt.Fprintf(&sb, "- **slug**: `%s`\n", r.Slug)
		fmt.Fprintf(&sb, "- **category**: %s | **status**: %s\n", r.Category, r.Status)
		if len(r.SpecVersions) > 0 {
			fmt.Fprintf(&sb, "- **spec_versions**: %s\n", strings.Join(r.SpecVersions, ", "))
		}
		if r.TagHex != "" {
			fmt.Fprintf(&sb, "- **tag**: `%s`", r.TagHex)
			if r.XMLText != "" {
				fmt.Fprintf(&sb, " / `%s`", r.XMLText)
			}
			sb.WriteString("\n")
		}
		if len(r.Keywords) > 0 {
			fmt.Fprintf(&sb, "- **keywords**: %s\n", strings.Join(r.Keywords, ", "))
		}
		fmt.Fprintf(&sb, "- **score**: %.4f\n\n", score)
	}
	return mcp.NewToolResultText(sb.String()), nil
}

func handleGetArticle(idx *Index, req mcp.CallToolRequest) (*mcp.CallToolResult, error) {
	slug := strings.TrimSpace(req.GetString("slug", ""))

	full, candidates, err := idx.GetArticle(slug)
	if err != nil {
		return mcp.NewToolResultText(fmt.Sprintf("Error: %v", err)), nil
	}
	if full != "" {
		return mcp.NewToolResultText(full), nil
	}

	// Not found — return suggestions.
	var sb strings.Builder
	fmt.Fprintf(&sb, "Article %q not found.\n\n", slug)
	if len(candidates) > 0 {
		sb.WriteString("Possible matches:\n")
		shown := candidates
		if len(shown) > 20 {
			shown = shown[:20]
		}
		for _, c := range shown {
			fmt.Fprintf(&sb, "  - `%s`\n", c)
		}
	}
	return mcp.NewToolResultText(sb.String()), nil
}

func handleListArticles(idx *Index, req mcp.CallToolRequest) (*mcp.CallToolResult, error) {
	category := req.GetString("category", "")
	status := req.GetString("status", "")

	results, err := idx.ListArticles(category, status)
	if err != nil {
		return mcp.NewToolResultText(fmt.Sprintf("Error: %v", err)), nil
	}

	var sb strings.Builder
	fmt.Fprintf(&sb, "## KB Articles (%d)\n\n", len(results))
	for _, r := range results {
		fmt.Fprintf(&sb, "- `%s` | %s | %s | %s\n", r.Slug, r.Category, r.Status, r.Title)
	}
	return mcp.NewToolResultText(sb.String()), nil
}

func handleGetRelated(idx *Index, req mcp.CallToolRequest) (*mcp.CallToolResult, error) {
	slug := strings.TrimSpace(req.GetString("slug", ""))
	limit := req.GetInt("limit", 5)
	if limit <= 0 {
		limit = 5
	}

	explicit, err := idx.GetRelatedExplicit(slug)
	if err != nil {
		return mcp.NewToolResultText(fmt.Sprintf("Article %q not found.", slug)), nil
	}

	var sb strings.Builder
	fmt.Fprintf(&sb, "## Related articles for `%s`\n\n", slug)

	sb.WriteString("### Explicitly related (front matter)\n\n")
	if len(explicit) == 0 {
		sb.WriteString("*(none)*\n\n")
	} else {
		for _, rel := range explicit {
			title := idx.GetArticleTitle(rel)
			if title != "" {
				fmt.Fprintf(&sb, "- `%s` — %s\n", rel, title)
			} else {
				fmt.Fprintf(&sb, "- `%s`\n", rel)
			}
		}
		sb.WriteString("\n")
	}

	// BM25 neighbours using title + keywords as query.
	title, kw := idx.GetArticleKeywordsAndTitle(slug)
	queryParts := []string{title}
	queryParts = append(queryParts, kw...)
	bm25Query := strings.Join(queryParts, " ")

	neighbours, err := idx.Search(bm25Query, "", "", "", limit+1)
	if err == nil && len(neighbours) > 0 {
		sb.WriteString("### BM25 neighbours\n\n")
		shown := 0
		for _, n := range neighbours {
			if n.Slug == slug {
				continue
			}
			score := math.Abs(n.Score)
			fmt.Fprintf(&sb, "- `%s` — %s *(score %.4f)*\n", n.Slug, n.Title, score)
			shown++
			if shown >= limit {
				break
			}
		}
	}

	return mcp.NewToolResultText(sb.String()), nil
}
