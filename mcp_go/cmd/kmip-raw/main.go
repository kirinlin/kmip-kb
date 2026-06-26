package main

import (
	"fmt"
	"os"
	"path/filepath"

	"github.com/kirinlin/kmip-kb/mcp_go/internal/raw"
	"github.com/mark3labs/mcp-go/server"
)

func main() {
	root := repoRoot()
	rawRoot := filepath.Join(root, "raw")

	idx, err := raw.BuildIndex(rawRoot)
	if err != nil {
		fmt.Fprintf(os.Stderr, "kmip-raw: failed to build index: %v\n", err)
		os.Exit(1)
	}

	s := raw.NewServer(idx)
	if err := server.ServeStdio(s); err != nil {
		fmt.Fprintf(os.Stderr, "kmip-raw: server error: %v\n", err)
		os.Exit(1)
	}
}

// repoRoot returns the repository root directory.
// Checks KMIP_KB_ROOT env var first, then walks up from the executable
// to find the directory containing a "kb" subdirectory.
func repoRoot() string {
	if root := os.Getenv("KMIP_KB_ROOT"); root != "" {
		return root
	}
	exe, err := os.Executable()
	if err != nil {
		return "."
	}
	dir := filepath.Dir(exe)
	for i := 0; i < 10; i++ {
		if _, err := os.Stat(filepath.Join(dir, "kb")); err == nil {
			return dir
		}
		parent := filepath.Dir(dir)
		if parent == dir {
			break
		}
		dir = parent
	}
	if cwd, err := os.Getwd(); err == nil {
		return cwd
	}
	return "."
}
