# Org profile design (short)

**Intent.** Make github.com/SetoffInc attractive to engineers we want to hire: show the stack and how we build, with a nerdy AI-company feel. Private repos stay private and are never described.

**Goals.** Stack and engineering principles, an animated terminal hero, an original swole-vs-small meme, a hiring call to action.
**Non-goals.** Product marketing for accounting firms, live stats.
**Anti-goals.** Leaking anything about private repos or internal infrastructure; looking like a generic widget-built profile.

**Approaches considered.**
- A. README + generated SVGs kept in this repo (chosen): unique look, no external dependencies, easy edits via one script.
- B. Third-party widgets (typing SVGs, skill icons, badges): fastest, generic, depends on other servers.
- C. A + scheduled Action regenerating live stats: needs a token and risks leaking private-repo data.

**Decisions.** A ledger concept: navy ruled paper, debit red, credit green, amber totals with an accountant's double rule. The hero is an animated agent run that ends balanced, and it respects reduced motion. The meme is drawn from scratch to avoid copyright and hot-linking. `scripts/check.py` guards against private references; CI checks the SVGs match the generator.

**Left to the builder.** Hiring contact (currently setoff.tax), org description and website in org settings.

## Revision, 2026-11-16

Feedback on the first version: the generated SVG hero and the drawn meme looked poor, and the page described engineering internals instead of the company.

- **Aesthetic:** ASCII art and Japanese motifs in GitHub code blocks: Mt. Fuji and a rising sun, block-letter wordmark, セットオフ set vertically, and a kanji title on each section.
- **Content:** the company at large (what Setoff and Protas are), the stack, hiring and credits. The agent-permission internals are gone.
- **Memes:** real Buff Doge vs. Cheems and Expanding Brain templates from Imgflip, captioned for Setoff, with format origins credited. Neither template is free-licensed; the owner accepted that.
- **Removed:** `scripts/build.py` and the generated SVGs. `scripts/check.py` now checks image size, alt text and meme credits as well as private references.

## Revision 2, 2026-11-16

The owner asked for no Japanese characters. The vertical katakana, kanji headings and tagline are gone; the ASCII Fuji, sun and waves stay. `scripts/check.py` fails on any Japanese character in the README.

## Revision 3, 2026-11-16

The owner found the ASCII art and the code-block stack and product boxes poor. Now: Hokusai's Great Wave (public domain, Met scan via Wikimedia Commons) as the header image, uncropped as the owner asked; a row of brand-coloured logo tiles for the stack (Simple Icons CC0, Lobe Icons MIT for OpenAI and AWS); a paragraph plus two bullets for Setoff and Protas. All ASCII art removed.
