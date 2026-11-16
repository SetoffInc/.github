# SetoffInc/.github

This repo holds the public profile shown at [github.com/SetoffInc](https://github.com/SetoffInc). GitHub renders [`profile/README.md`](profile/README.md) on the organisation page.

## Editing

- **Copy and ASCII art:** edit `profile/README.md`. Keep the art plain ASCII: no Japanese characters, and no Unicode box-drawing characters, which misalign in some fonts.
- **Memes:** captioned images live in `profile/assets/`. Any new meme needs an entry under credits.
- **Before you push:**

  ```bash
  python3 scripts/check.py
  ```

## Rules

- **This repo is public. Every other Setoff repo stays private.** Don't link to private repos, internal hostnames, file paths or env files. `scripts/check.py` blocks the common cases, and review covers the rest.
- **Keep images in this repo** and credit every meme format and template source.
