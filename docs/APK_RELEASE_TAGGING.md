# APK Release Tagging Convention

## Tag Format

```
apk-v<major>.<minor>.<patch>
```

Examples:
- `apk-v1.0.0` — Initial release
- `apk-v1.1.0` — Feature update
- `apk-v1.1.1` — Bugfix
- `apk-v2.0.0` — Major rewrite

## GitHub Release Asset

Each APK release must include exactly one `.apk` file as a release asset, named:

```
Ntronix-App-v<major>.<minor>.<patch>.apk
```

Example: `Ntronix-App-v1.0.0.apk`

## How to Publish an APK Release

1. Build the release APK:
   ```bash
   cd /path/to/ntronix_app
   flutter build apk --release --split-per-abi
   # OR for a fat APK:
   flutter build apk --release
   ```

2. Create a GitHub release (via CLI or web):
   ```bash
   # Using gh CLI:
   gh release create apk-v1.2.0 \
     --title "Ntronix App v1.2.0" \
     --notes "Release notes here..." \
     build/app/outputs/flutter-apk/app-release.apk#Ntronix-App-v1.2.0.apk

   # OR via GitHub web UI:
   #   Tags → apk-v1.2.0
   #   Upload Ntronix-App-v1.2.0.apk as asset
   ```

## How the Website Consumes It

The website (`js/app-download.js`) calls:
```
GET https://api.github.com/repos/ntronix44/ntronOS/releases
```

It filters by `tag_name` starting with `apk-`, picks the latest non-draft
release, extracts the `.apk` asset download URL, and renders a smart download
button with version + date + release notes.

## Backward Compatibility

If the GitHub API call fails (PAT expired, rate-limited, network issue), the
website falls back to the static `/Ntronix-App-v1.0.0.apk` file — so the
download link never breaks.
