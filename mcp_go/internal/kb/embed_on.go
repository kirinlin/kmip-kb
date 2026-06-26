//go:build embed

package kb

import _ "embed"

//go:embed data/kb.db
var EmbeddedDB []byte
