# SetoffInc/.github

This repo holds the public profile shown at [github.com/SetoffInc](https://github.com/SetoffInc). GitHub renders [`profile/README.md`](profile/README.md) on the organisation page.

## Editing

- **Copy:** edit `profile/README.md`. No Japanese characters in the text; the check enforces it.
- **Stack logos:** `profile/assets/stack/` holds one 64×64 tile per technology (dark rounded square, logo in brand colour). Add a tile in the same style and an `<img>` in the stack row.
- **Memes:** captioned images live in `profile/assets/`. Any new meme needs an entry under credits.
- **Before you push:**

  ```bash
  python3 scripts/check.py
  ```

## Rules

- **This repo is public. Every other Setoff repo stays private.** Don't link to private repos, internal hostnames, file paths or env files. `scripts/check.py` blocks the common cases, and review covers the rest.
- **Keep images in this repo** and credit every artwork, meme format, template and icon source.
