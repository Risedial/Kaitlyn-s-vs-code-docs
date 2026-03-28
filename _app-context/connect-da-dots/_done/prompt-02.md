# Prompt 02: Write manifest.json — PWA Web App Manifest with Base64 Icons

## Prerequisites
- state.json flags that MUST be `true` before this prompt runs: `initialized`
- Files that MUST already exist: `fdn-pwa/manifest.json` (stub from step-01)

## Hard Constraints
1. **32,000 token output limit** — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. **No truncation** — When writing data entries (symptoms, variables, clusters), write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. **State sync required** — Read `connect-da-dots/state.json` at the start of every session. Complete the single assigned task. Update `state.json` to mark that step complete before exiting.
4. **No external dependencies** — No CDN, no npm, no external URLs in any generated file.
5. **File writes only via Write tool** — Never use bash heredoc or shell redirection to write application files.

## Task
Use the Write tool to overwrite `fdn-pwa/manifest.json` with a complete, valid Web App Manifest.

**Step 1 — Generate icon PNGs as base64.**
Use the Bash tool to run the following Python script, which generates minimal valid PNG icons with a black background and white "FDN" text:

```python
import base64, struct, zlib

def make_png(size, label="FDN"):
    """Generate a minimal valid PNG: solid black background, white pixel border."""
    width = height = size
    # Create raw pixel data: black (0,0,0) for all pixels
    row = b'\x00' + b'\x00\x00\x00' * width  # filter byte + RGB pixels
    raw = row * height
    compressed = zlib.compress(raw)

    def chunk(ctype, data):
        c = ctype + data
        return struct.pack('>I', len(data)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)

    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    png = b'\x89PNG\r\n\x1a\n'
    png += chunk(b'IHDR', ihdr_data)
    png += chunk(b'IDAT', compressed)
    png += chunk(b'IEND', b'')
    return base64.b64encode(png).decode('ascii')

icon192 = make_png(192)
icon512 = make_png(512)
print(f"ICON192={icon192[:50]}...")
print(f"ICON512={icon512[:50]}...")

# Write to temp files for use in manifest
with open('/tmp/icon192.b64', 'w') as f:
    f.write(icon192)
with open('/tmp/icon512.b64', 'w') as f:
    f.write(icon512)
print("Icons written to /tmp/")
```

On Windows, write temp files to a known path (e.g., use Python's `tempfile` module or write directly to the project directory as `fdn-pwa/icon192.tmp` and `fdn-pwa/icon512.tmp`), then read their content.

**Step 2 — Write manifest.json.**
Use the Write tool to write `fdn-pwa/manifest.json` with the following structure, inserting the base64 strings from step 1 into the icon `src` fields as `data:image/png;base64,<base64string>`:

```json
{
  "name": "FDN Symptom Navigator",
  "short_name": "FDN Nav",
  "description": "FDN lab marker reference tool for clinical practitioners",
  "start_url": "./",
  "scope": "./",
  "display": "standalone",
  "orientation": "portrait-primary",
  "theme_color": "#000000",
  "background_color": "#000000",
  "categories": ["medical", "health", "productivity"],
  "icons": [
    {
      "src": "data:image/png;base64,<INSERT_192x192_BASE64_HERE>",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "data:image/png;base64,<INSERT_512x512_BASE64_HERE>",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any maskable"
    }
  ]
}
```

The `<INSERT_*_BASE64_HERE>` placeholders must be replaced with actual base64 PNG strings — not placeholder text.

Clean up any temporary icon files after writing manifest.json.

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/manifest.json` parses as valid JSON (use Python: `import json; json.load(open('fdn-pwa/manifest.json'))`)
- The JSON contains `name`, `short_name`, `display`, `start_url`, `scope`, `orientation`, `theme_color`, `background_color`, `categories`, and `icons` keys
- `icons` array has exactly 2 entries
- Each icon `src` begins with `data:image/png;base64,` (not a placeholder string)
- `display` value is exactly `"standalone"`
- `theme_color` is `"#000000"`

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-02"`
- `pendingSteps`: remove `"step-02"`
- `flags.manifestWritten`: set to `true`
