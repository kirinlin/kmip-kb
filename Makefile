.PHONY: build build-kb build-kb-embed build-raw build-all gen-db test test-kb test-raw test-parser clean report crawl

MCP_GO_DIR := mcp_go
BIN_DIR    := $(MCP_GO_DIR)/bin
KB_DB      := $(MCP_GO_DIR)/internal/kb/data/kb.db
REPO_ROOT  := $(shell git rev-parse --show-toplevel)

build: build-all

build-all: build-kb build-raw

build-kb:
	cd $(MCP_GO_DIR) && go build -o bin/kmip-kb ./cmd/kmip-kb

# gen-db: build the pre-indexed SQLite database from kb/ for embedding.
# Must be run before build-kb-embed.
gen-db:
	cd $(MCP_GO_DIR) && go run ./cmd/gen-db -kb $(REPO_ROOT)/kb -out internal/kb/data/kb.db

# build-kb-embed: generate the DB then produce a self-contained binary with it embedded.
build-kb-embed: gen-db
	cd $(MCP_GO_DIR) && go build -tags embed -o bin/kmip-kb ./cmd/kmip-kb

build-raw:
	cd $(MCP_GO_DIR) && go build -o bin/kmip-raw ./cmd/kmip-raw

test:
	cd $(MCP_GO_DIR) && go test ./...

test-parser:
	cd $(MCP_GO_DIR) && go test ./internal/parser/...

test-kb:
	cd $(MCP_GO_DIR) && go test ./internal/kb/...

test-raw:
	cd $(MCP_GO_DIR) && go test ./internal/raw/...

clean:
	rm -rf $(BIN_DIR)

report:
	python ./scripts/status_report.py

crawl:
	python ./scripts/kmip_crawler.py
