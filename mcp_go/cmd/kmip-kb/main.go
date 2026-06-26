package main

import (
	"fmt"
	"os"
	"path/filepath"

	"github.com/kirinlin/kmip-kb/mcp_go/internal/kb"
	"github.com/mark3labs/mcp-go/server"
)

func main() {
	idx, err := openIndex()
	if err != nil {
		fmt.Fprintf(os.Stderr, "kmip-kb: %v\n", err)
		os.Exit(1)
	}

	s := kb.NewServer(idx)
	if err := server.ServeStdio(s); err != nil {
		fmt.Fprintf(os.Stderr, "kmip-kb: server error: %v\n", err)
		os.Exit(1)
	}
}

func openIndex() (*kb.Index, error) {
	if len(kb.EmbeddedDB) > 0 {
		return kb.OpenFromBytes(kb.EmbeddedDB)
	}

	root := repoRoot()
	kbRoot := filepath.Join(root, "kb")
	if _, err := os.Stat(kbRoot); err != nil {
		return nil, fmt.Errorf("kb/ directory not found at %s (set KMIP_KB_ROOT or build with -tags embed)", kbRoot)
	}
	return kb.BuildIndex(kbRoot)
}

// repoRoot returns the repository root, used only in the non-embedded path.
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
