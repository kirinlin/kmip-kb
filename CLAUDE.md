# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This project downloads KMIP (Key Management Interoperability Protocol) specification documents from `https://docs.oasis-open.org/kmip/` and converts them to Markdown, storing them in `raw/` with a folder structure that mirrors the original URL path.

## Script

`scripts/kmip_crawler.py` — unified crawl + download in one pass.

```
python scripts/kmip_crawler.py [--out raw] [--workers 4] [--save-urls ./raw/kmip_urls.txt] [--urls FILE] [--no-skip]
```

| Flag | Default | Effect |
|---|---|---|
| `--out` | `raw` | Output root directory |
| `--workers` | `4` | Parallel download workers |
| `--save-urls` | `./raw/kmip_urls.txt` | Where to write discovered URLs |
| `--urls FILE` | *(crawl first)* | Skip crawl; load URLs from an existing file |
| `--no-skip` | *(off)* | Re-download files that already exist |

Requires PullMD running locally. Override the default `http://localhost:3000` with `PULLMD_URL` env var.

## Behaviour

- HTML pages → Markdown via PullMD (`frontmatter=true`). XML files → downloaded directly.
- URL path structure under `docs.oasis-open.org` is preserved under `--out`.
- Logs written to `./logs/kmip_crawler-{timestamp}.log` (directory is gitignored but kept via placeholder `.gitignore`).
- `raw/` contents and the script itself are gitignored — local-only artifacts.
- Python dependencies: `requests`, `beautifulsoup4`.
