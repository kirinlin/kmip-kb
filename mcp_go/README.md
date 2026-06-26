# mcp_go — Go MCP Servers for the KMIP Knowledge Base

Go port of the Python FastMCP servers in `mcp_py/`. Produces two standalone binaries with no runtime dependencies — no Python, no venv, no pip.

## Servers

| Binary | MCP name | Data source | Tools |
|---|---|---|---|
| `kmip-kb` | `kmip-kb` | `kb/` — 452 authored articles | `search_kb`, `get_article`, `list_articles`, `get_related` |
| `kmip-raw` | `kmip-raw` | `raw/` — crawled OASIS spec docs | `search_raw`, `get_doc`, `list_docs` |

`kmip-raw` exits with a diagnostic if `raw/kmip/` is absent or empty. Run `python scripts/kmip_crawler.py` from the repo root to populate it.

## Build

```sh
# Both binaries → mcp_go/bin/
make build

# Individual
make build-kb
make build-raw
```

Or directly from this directory:

```sh
go build -o bin/kmip-kb ./cmd/kmip-kb
go build -o bin/kmip-raw ./cmd/kmip-raw
```

Cross-compilation works without CGO (pure-Go SQLite via `modernc.org/sqlite`):

```sh
GOOS=darwin  GOARCH=arm64 go build -o bin/kmip-kb-darwin-arm64  ./cmd/kmip-kb
GOOS=windows GOARCH=amd64 go build -o bin/kmip-kb-windows-amd64.exe ./cmd/kmip-kb
```

### Embedded distribution (kmip-kb only)

`kmip-kb` can be built as a single self-contained binary with the FTS5 index baked in — no `kb/` directory needed at runtime:

```sh
# Build the pre-indexed SQLite file, then compile it in with //go:embed
make build-kb-embed
```

Under the hood this is two steps: `make gen-db` writes `internal/kb/data/kb.db` from the current `kb/` tree, then `go build -tags embed` compiles it into the binary via `embed_on.go`. Without `-tags embed`, `embed_off.go` sets `EmbeddedDB = nil` and the server falls back to scanning `kb/` on disk.

`kmip-raw` has no embed mode — raw spec documents are too large to bundle.

## Test

```sh
make test          # all packages
make test-kb       # internal/kb only
make test-raw      # internal/raw only
make test-parser   # internal/parser only
```

38 tests, all using `t.TempDir()` fixtures — no dependency on `kb/` or `raw/`.

## Run

Both servers communicate over **stdio** (MCP JSON-RPC). They are not invoked directly; an MCP host (Claude Code, Claude Desktop) starts them as subprocesses.

### Repo root resolution

The binaries locate the repo root at startup using this priority order:

1. `KMIP_KB_ROOT` environment variable
2. Walk up from the executable until a directory containing `kb/` is found
3. Current working directory

### MCP config

Add to your MCP config (e.g. `.mcp.json` in the repo root or `~/.claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "kmip-kb": {
      "command": "/path/to/repo/mcp_go/bin/kmip-kb",
      "env": { "KMIP_KB_ROOT": "/path/to/repo" }
    },
    "kmip-raw": {
      "command": "/path/to/repo/mcp_go/bin/kmip-raw",
      "env": { "KMIP_KB_ROOT": "/path/to/repo" }
    }
  }
}
```

## Architecture

```
cmd/
├── gen-db/     Writes a pre-indexed kb.db file from kb/ (used by build-kb-embed)
├── kmip-kb/    Entry point: opens embedded DB or scans kb/ on disk, serves stdio MCP
└── kmip-raw/   Entry point: scans raw/ on disk, serves stdio MCP
internal/
├── parser/     YAML front-matter parser shared by both servers
├── kb/
│   ├── data/          Holds kb.db for embedding (gitignored except .gitignore)
│   ├── embed_on.go    //go:embed data/kb.db — compiled in with -tags embed
│   ├── embed_off.go   EmbeddedDB = nil — default build, falls back to disk scan
│   ├── index.go       Opens embedded DB or scans kb/**/*.md; builds SQLite FTS5 index
│   └── server.go      MCP tool handlers (thin wrappers over Index methods)
└── raw/
    ├── index.go   Scans raw/**/*.md; extracts doc_type/version/is_final from path
    └── server.go  MCP tool handlers
```

**Search** uses SQLite FTS5's built-in BM25 ranking. All documents are scored first, then post-filtered by metadata (category, status, spec_version / doc_type, version, final_only) — same approach as the Python servers to preserve correct IDF weights.

**Index** is built in memory (`:memory:`) on every startup. Startup time on the full corpus is under 500 ms. The embedded build pre-computes this into a file and reads it directly, avoiding the scan entirely.

## Dependencies

| Package | Role |
|---|---|
| `github.com/mark3labs/mcp-go` | MCP stdio server and tool registration |
| `modernc.org/sqlite` | Pure-Go SQLite with FTS5 (no CGO) |
| `gopkg.in/yaml.v3` | YAML front-matter parsing |
