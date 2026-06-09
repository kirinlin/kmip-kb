# kmip-dev

Crawls `https://docs.oasis-open.org/kmip/` and mirrors the full documentation tree locally as Markdown (HTML pages) and raw XML.

## Disclaimer

This repository contains independently written notes, summaries, implementation guidance, examples, and metadata based on the OASIS KMIP specification. The official KMIP specification is copyrighted by OASIS Open. This repository is not an official OASIS publication and does not contain the official specification text.

## Prerequisites

- Python 3.11+ with `requests` and `beautifulsoup4`
- [PullMD](https://github.com/AeternaLabsHQ/pullmd) running locally (default `http://localhost:3000`, override with `PULLMD_URL`)

## Usage

```sh
python scripts/kmip_crawler.py
```

This crawls the KMIP docs site, then downloads every page concurrently. Progress and errors are logged to `logs/kmip_crawler-{timestamp}.log`.

### Options

| Flag | Default | Description |
|---|---|---|
| `--out DIR` | `raw` | Output root directory |
| `--workers N` | `4` | Parallel download workers |
| `--save-urls FILE` | `./raw/kmip_urls.txt` | File to write discovered URLs |
| `--urls FILE` | — | Skip crawl; use a previously saved URL list |
| `--no-skip` | — | Re-download files that already exist |

### Resume a partial download

```sh
python scripts/kmip_crawler.py --urls ./raw/kmip_urls.txt
```

## Output layout

```
raw/
  kmip/
    kmip-spec/
      v2.1/
        kmip-spec-v2.1.md
        ...
    kmip-profiles/
      ...
logs/
  kmip_crawler-20260609_101500.log
```

HTML pages are saved as `.md` (converted via PullMD). Directory index pages become `index.md`. XML test-case files are saved as-is.
