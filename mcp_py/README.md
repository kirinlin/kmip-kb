# KMIP MCP Servers

Two FastMCP servers expose the KMIP knowledge base and raw source documents over stdio.

## Servers

| Server | Script | Start script | Indexes |
|---|---|---|---|
| `kmip-kb` | `kmip_kb_server.py` | `start_kmip-kb.sh` | `kb/` — 450+ authored KB articles |
| `kmip-raw` | `kmip_raw_server.py` | `start_kmip-raw.sh` | `raw/` — 250+ crawled raw spec docs |

## Dependencies

```bash
pip install -r mcp_py/requirements.txt
# or let the start scripts manage a venv automatically on first run
```

## Running via MCP (normal use)

The servers are wired in `.mcp.json` and start automatically when Claude Code loads the project. No manual action required.

## Running manually (debug / direct stdio)

```bash
python mcp_py/kmip_kb_server.py
python mcp_py/kmip_raw_server.py
```

## Quick tests

Run from the repo root. These call tool functions directly without starting an MCP transport.

### kmip-kb

```bash
# How many articles are indexed?
python -c "import mcp_py.kmip_kb_server as s; print(len(s._docs), 'docs')"

# Search
python -c "
import mcp_py.kmip_kb_server as s
print(s.search_kb('symmetric key creation', limit=3))
"

# List articles in a category
python -c "
import mcp_py.kmip_kb_server as s
print(s.list_articles(category='operation'))
"

# Fetch a specific article
python -c "
import mcp_py.kmip_kb_server as s
print(s.get_article('operations/create')[:500])
"

# Related articles
python -c "
import mcp_py.kmip_kb_server as s
print(s.get_related('operations/create'))
"
```

### kmip-raw

```bash
# How many raw docs are indexed?
python -c "import mcp_py.kmip_raw_server as s; print(len(s._docs), 'docs')"

# List final-only canonical documents
python -c "
import mcp_py.kmip_raw_server as s
print(s.list_docs())
"

# List docs for a specific family and version
python -c "
import mcp_py.kmip_raw_server as s
print(s.list_docs(doc_type='kmip-spec', version='2.1', final_only=False))
"

# Search across all raw docs (including drafts)
python -c "
import mcp_py.kmip_raw_server as s
print(s.search_raw('TTLV encoding structure', final_only=False, limit=5))
"

# Search within a specific doc family
python -c "
import mcp_py.kmip_raw_server as s
print(s.search_raw('key wrapping', doc_type='kmip-spec', version='2.1'))
"

# Fetch the first page of a raw doc (raw files are large — use pagination)
python -c "
import mcp_py.kmip_raw_server as s
print(s.get_doc('kmip/kmip-spec/v2.1/kmip-spec-v2.1', char_offset=0, max_chars=2000))
"

# Fetch the next page
python -c "
import mcp_py.kmip_raw_server as s
print(s.get_doc('kmip/kmip-spec/v2.1/kmip-spec-v2.1', char_offset=20000, max_chars=20000))
"
```

## Tool reference

### kmip-kb tools

| Tool | Signature | Purpose |
|---|---|---|
| `search_kb` | `(query, category, status, spec_version, limit)` | BM25 search over KB articles |
| `get_article` | `(slug)` | Full article content by slug |
| `list_articles` | `(category, status)` | Browse articles by metadata |
| `get_related` | `(slug, limit)` | Explicit `related:` links + BM25 neighbours |

### kmip-raw tools

| Tool | Signature | Purpose |
|---|---|---|
| `search_raw` | `(query, doc_type, version, final_only, limit)` | BM25 search over raw spec docs |
| `get_doc` | `(slug, char_offset, max_chars)` | Paginated raw document retrieval |
| `list_docs` | `(doc_type, version, final_only)` | Browse raw docs by type/version |

`get_doc` returns a header line showing total size and current range so you know whether to fetch more pages:
```
<!-- slug: kmip/kmip-spec/v2.1/kmip-spec-v2.1 | total: 693536 chars | showing: 0–20000 -->
```
