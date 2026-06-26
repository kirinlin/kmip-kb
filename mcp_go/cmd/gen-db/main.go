// gen-db builds a pre-indexed SQLite database from the kb/ directory and
// writes it to the given output path. Run this before `go build -tags embed`.
package main

import (
	"flag"
	"fmt"
	"os"

	"github.com/kirinlin/kmip-kb/mcp_go/internal/kb"
)

func main() {
	kbRoot := flag.String("kb", "", "path to kb/ directory (required)")
	out := flag.String("out", "", "output .db file path (required)")
	flag.Parse()

	if *kbRoot == "" || *out == "" {
		fmt.Fprintln(os.Stderr, "usage: gen-db -kb <kb-dir> -out <output.db>")
		os.Exit(1)
	}

	if _, err := os.Stat(*kbRoot); err != nil {
		fmt.Fprintf(os.Stderr, "gen-db: kb directory not found: %v\n", err)
		os.Exit(1)
	}

	fmt.Fprintf(os.Stderr, "gen-db: indexing %s ...\n", *kbRoot)
	idx, err := kb.BuildIndex(*kbRoot)
	if err != nil {
		fmt.Fprintf(os.Stderr, "gen-db: index failed: %v\n", err)
		os.Exit(1)
	}

	// VACUUM INTO requires the target to not already exist.
	os.Remove(*out)

	if err := idx.WriteTo(*out); err != nil {
		fmt.Fprintf(os.Stderr, "gen-db: write failed: %v\n", err)
		os.Exit(1)
	}

	info, _ := os.Stat(*out)
	size := int64(0)
	if info != nil {
		size = info.Size()
	}
	fmt.Fprintf(os.Stderr, "gen-db: wrote %s (%.1f KB)\n", *out, float64(size)/1024)
}
