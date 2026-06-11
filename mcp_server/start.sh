#!/usr/bin/env bash
# Starts the KMIP KB MCP server over stdio.
# On first run, installs Python dependencies into a venv if possible,
# or falls back to --user install if python3-venv is unavailable.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV="$SCRIPT_DIR/.venv"

if [ -x "$VENV/bin/python" ] && [ -x "$VENV/bin/pip" ]; then
    exec "$VENV/bin/python" "$SCRIPT_DIR/kmip_kb_server.py"
fi

# Try to create a venv
if python3 -m venv "$VENV" 2>/dev/null; then
    echo "[kmip-kb] Installing dependencies into venv..." >&2
    "$VENV/bin/pip" install -q -r "$SCRIPT_DIR/requirements.txt"
    exec "$VENV/bin/python" "$SCRIPT_DIR/kmip_kb_server.py"
else
    # venv unavailable — use user-installed packages
    echo "[kmip-kb] venv unavailable, checking user packages..." >&2
    if ! python3 -c "import mcp, yaml, rank_bm25" 2>/dev/null; then
        echo "[kmip-kb] Installing dependencies (--user --break-system-packages)..." >&2
        python3 -m pip install --user --break-system-packages -q \
            -r "$SCRIPT_DIR/requirements.txt"
    fi
    exec python3 "$SCRIPT_DIR/kmip_kb_server.py"
fi
