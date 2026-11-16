# SetoffInc/.github

This repo holds the public profile shown at [github.com/SetoffInc](https://github.com/SetoffInc). GitHub renders [`profile/README.md`](profile/README.md) on the organisation page.

## Editing

- **Copy:** edit `profile/README.md`.
- **Terminal hero and meme:** edit the text near the top of `scripts/build.py`, then regenerate:

  ```bash
  python3 scripts/build.py && python3 scripts/check.py
  ```

  Commit the regenerated files in `profile/assets/`. CI fails if they drift from the script.

## Rules

- **This repo is public. Every other Setoff repo stays private.** Don't link to private repos, internal hostnames, file paths or env files. `scripts/check.py` blocks the common cases, and review covers the rest.
- **Keep images in this repo.** No third-party widgets or hot-linked images.
- **Keep the stack list current.** It is what candidates read.
