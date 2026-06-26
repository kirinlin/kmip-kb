//go:build !embed

package kb

// EmbeddedDB is nil when built without -tags embed; the server falls back to
// scanning the kb/ directory on disk.
var EmbeddedDB []byte
