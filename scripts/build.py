#!/usr/bin/env python3
"""Generates the SVGs in profile/assets.

Edit the text in HERO_LINES or MEME below, run `python3 scripts/build.py`, commit
the regenerated SVGs. CI fails if the committed SVGs drift from this script.
"""
from pathlib import Path
from xml.sax.saxutils import escape

ASSETS = Path(__file__).resolve().parent.parent / "profile" / "assets"

# Ledger palette: navy ruled paper, debit red, credit green, amber for totals.
INK = "#0F1B2D"
INK_DEEP = "#0A1322"
RULE = "#1F3350"
PAPER = "#E6EDF5"
MUTED = "#8BA3BF"
CREDIT = "#4CC38A"
DEBIT = "#F06A5D"
AMBER = "#F5B841"
MONO = "ui-monospace, SFMono-Regular, 'JetBrains Mono', Menlo, Consolas, 'Liberation Mono', monospace"

CHAR_W = 9.0  # advance of a 15px monospace glyph

# Hero terminal. Each line is a list of (text, colour) runs.
COMMAND = "protas reconcile --period 2026-Q3 --as you"
HERO_LINES = [
    [("  scope   ", CREDIT), ("snapshot of your permissions, your clients only", PAPER)],
    [("  fetch   ", CREDIT), ("12,408 bank lines, 11,937 ledger entries", PAPER)],
    [("  match   ", CREDIT), ("11,902 exact, 471 fuzzy, 35 need a human", PAPER)],
    [("  ask     ", AMBER), ("approve 35 proposals? ", PAPER), ("y", AMBER), ("  approved by you", MUTED)],
    [("  post    ", CREDIT), ("journal 2026-Q3-0412", PAPER)],
]
TOTALS = [
    [("  debits    ", DEBIT), ("4,812,330.17", PAPER)],
    [("  credits   ", CREDIT), ("4,812,330.17", PAPER)],
]
BALANCE = [("  Δ         ", AMBER), ("0.00", AMBER), ("   balanced", MUTED)]

MEME = {
    "left_title": "setoff engineer",
    "left": [
        "ships the RLS policy with the migration",
        "agents get your permissions, not root",
        "go test ./... before coffee",
    ],
    "right_title": "the spreadsheet era",
    "right": [
        "VLOOKUP across 14 tabs",
        "emails final_FINAL_v3.xlsx to self",
        "the macro is the access control",
    ],
}


def runs(parts):
    return "".join(f'<tspan fill="{c}">{escape(t)}</tspan>' for t, c in parts)


def ruling(width, height, top, step=28):
    lines = "".join(
        f'<line x1="0" y1="{y}" x2="{width}" y2="{y}"/>' for y in range(top, height, step)
    )
    return f'<g stroke="{RULE}" stroke-width="1" opacity=".55">{lines}</g>'


def hero():
    w, h = 880, 476
    tx, ty, tw, th = 40, 140, 800, 316
    x0, y0, lh = 64, ty + 64, 24
    cmd_x = x0 + 2 * CHAR_W

    body, t = [], 2.6
    for i, parts in enumerate(HERO_LINES):
        body.append(f'<text class="l" style="animation-delay:{t:.1f}s" x="{x0}" y="{y0 + (i + 1) * lh}">{runs(parts)}</text>')
        t += 0.55
    t += 0.35
    ty_tot = y0 + (len(HERO_LINES) + 2) * lh
    for i, parts in enumerate(TOTALS):
        body.append(f'<text class="l" style="animation-delay:{t:.1f}s" x="{x0}" y="{ty_tot + i * lh}">{runs(parts)}</text>')
        t += 0.35
    # Accountant's double rule under the totals, then the balance line.
    rule_x = x0 + 12 * CHAR_W
    rule_y = ty_tot + lh + 8
    body.append(
        f'<g class="l" style="animation-delay:{t:.1f}s" stroke="{AMBER}" stroke-width="1.5">'
        f'<line x1="{rule_x}" y1="{rule_y}" x2="{rule_x + 12 * CHAR_W}" y2="{rule_y}"/>'
        f'<line x1="{rule_x}" y1="{rule_y + 4}" x2="{rule_x + 12 * CHAR_W}" y2="{rule_y + 4}"/></g>'
    )
    t += 0.3
    bal_y = rule_y + lh + 2
    body.append(f'<text class="l" style="animation-delay:{t:.1f}s" x="{x0}" y="{bal_y}">{runs(BALANCE)}</text>')
    cursor_x = x0 + sum(len(s) for s, _ in BALANCE) * CHAR_W + 6
    body.append(
        f'<rect class="l cursor" style="animation-delay:{t:.1f}s,{t:.1f}s" x="{cursor_x:.0f}" y="{bal_y - 14}" width="9" height="18" fill="{AMBER}"/>'
    )

    n = len(COMMAND)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">
<title>setoff: an agent reconciles a quarter and the books balance</title>
<style>
text {{ font-family: {MONO}; font-size: 15px; white-space: pre; }}
.l {{ opacity: 0; animation: in .01s linear forwards; }}
.type {{ animation: type 1.8s steps({n}, end) .4s forwards; }}
.cursor {{ animation: in .01s linear forwards, blink 1.1s steps(1, end) infinite; }}
@keyframes in {{ to {{ opacity: 1; }} }}
@keyframes type {{ to {{ transform: translateX({n * CHAR_W:.0f}px); }} }}
@keyframes blink {{ 50% {{ opacity: 0; }} }}
@media (prefers-reduced-motion: reduce) {{
  .l, .cursor {{ animation: none; opacity: 1; }}
  .type {{ display: none; }}
}}
</style>
<rect width="{w}" height="{h}" rx="14" fill="{INK}"/>
{ruling(w, h, 34)}
<g stroke="{DEBIT}" stroke-width="1" opacity=".5"><line x1="20" y1="0" x2="20" y2="{h}"/><line x1="24" y1="0" x2="24" y2="{h}"/></g>
<text x="{tx}" y="78" fill="{PAPER}" style="font-size:46px;font-weight:700;letter-spacing:-1px">setoff</text>
<g stroke="{AMBER}" stroke-width="2"><line x1="{tx}" y1="92" x2="{tx + 166}" y2="92"/><line x1="{tx}" y1="98" x2="{tx + 166}" y2="98"/></g>
<text x="{tx + 196}" y="64" fill="{PAPER}">agents for tax work.</text>
<text x="{tx + 196}" y="88" fill="{MUTED}">every entry balances, or it does not post.</text>
<rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="10" fill="{INK_DEEP}" stroke="{RULE}"/>
<g fill="{RULE}"><circle cx="{tx + 22}" cy="{ty + 20}" r="5"/><circle cx="{tx + 40}" cy="{ty + 20}" r="5"/><circle cx="{tx + 58}" cy="{ty + 20}" r="5"/></g>
<text x="{tx + tw / 2:.0f}" y="{ty + 25}" fill="{MUTED}" text-anchor="middle" style="font-size:13px">~/ledger</text>
<text x="{x0}" y="{y0}"><tspan fill="{AMBER}">$ </tspan><tspan fill="{PAPER}">{escape(COMMAND)}</tspan></text>
<clipPath id="term"><rect x="{tx + 1}" y="{ty + 1}" width="{tw - 2}" height="{th - 2}" rx="9"/></clipPath>
<rect class="type" clip-path="url(#term)" x="{cmd_x:.0f}" y="{y0 - 16}" width="{n * CHAR_W + 4:.0f}" height="22" fill="{INK_DEEP}"/>
{chr(10).join(body)}
</svg>
'''


def buff(cx):
    """Double-biceps pose, drawn around x=0 and shifted to cx."""
    s, o = f'stroke="{INK}" stroke-width="3" stroke-linejoin="round"', AMBER
    arm = (
        f'<path d="M-84,-8 C-110,-32 -146,-20 -154,8 C-146,24 -110,26 -80,26 Z" fill="{o}" {s}/>'
        f'<path d="M-162,8 C-170,-20 -164,-48 -152,-64 L-130,-60 C-134,-36 -134,-12 -134,10 Z" fill="{o}" {s}/>'
        f'<circle cx="-142" cy="-72" r="15" fill="{o}" {s}/>'
    )
    return f'''<g transform="translate({cx},200)">
<g>{arm}<text x="-118" y="10" text-anchor="middle" fill="{INK}" style="font-size:13px;font-weight:700">Go</text></g>
<g transform="scale(-1,1)">{arm}</g>
<text x="118" y="10" text-anchor="middle" fill="{INK}" style="font-size:13px;font-weight:700">SQL</text>
<path d="M-14,-30 L14,-30 L24,-8 L-24,-8 Z" fill="{o}" {s}/>
<path d="M-92,-4 Q0,-20 92,-4 L58,140 Q0,152 -58,140 Z" fill="{o}" {s}/>
<path d="M-50,40 Q-25,56 -2,40 M2,40 Q25,56 50,40" fill="none" {s}/>
<g fill="none" stroke="{INK}" stroke-width="2.5">
<rect x="-24" y="64" width="20" height="18" rx="5"/><rect x="4" y="64" width="20" height="18" rx="5"/>
<rect x="-24" y="88" width="20" height="18" rx="5"/><rect x="4" y="88" width="20" height="18" rx="5"/>
<rect x="-22" y="112" width="18" height="16" rx="5"/><rect x="4" y="112" width="18" height="16" rx="5"/></g>
<path d="M-58,140 Q0,152 58,140 L60,180 L-60,180 Z" fill="{RULE}" {s}/>
<path d="M-50,180 L-46,228 L-10,228 L-6,180 M6,180 L10,228 L46,228 L50,180" fill="{o}" {s}/>
<circle cx="0" cy="-54" r="28" fill="{o}" {s}/>
<path d="M-22,-62 L22,-62 L20,-50 L4,-50 L0,-56 L-4,-50 L-20,-50 Z" fill="{INK}"/>
<path d="M-8,-38 Q2,-34 12,-40" fill="none" {s}/>
</g>'''


def small(cx):
    """Hunched over a printed spreadsheet."""
    s, o = f'stroke="{INK}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"', MUTED
    cells = "".join(
        f'<line x1="-66" y1="{y}" x2="66" y2="{y}"/>' for y in range(56, 142, 16)
    ) + "".join(f'<line x1="{x}" y1="40" x2="{x}" y2="146"/>' for x in range(-36, 66, 34))
    return f'''<g transform="translate({cx},200)">
<path d="M-12,150 L-16,228 L-30,230 M12,150 L16,228 L30,230" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"/>
<rect x="-20" y="26" width="40" height="128" rx="16" fill="{o}" {s} transform="rotate(6 0 26)"/>
<circle cx="8" cy="0" r="24" fill="{o}" {s}/>
<circle cx="0" cy="-2" r="2.5" fill="{INK}"/><circle cx="16" cy="-2" r="2.5" fill="{INK}"/>
<path d="M0,13 Q8,7 16,13" fill="none" {s}/>
<path d="M36,-18 Q42,-6 36,-2 Q30,-6 36,-18 Z" fill="#7FB8E6"/>
<rect x="-70" y="40" width="140" height="106" rx="2" fill="{PAPER}" stroke="{INK}" stroke-width="2.5"/>
<g stroke="{MUTED}" stroke-width="1">{cells}</g>
<text x="-31" y="101" fill="{DEBIT}" style="font-size:12px;font-weight:700">#REF!</text>
<path d="M-16,40 L-58,60 M18,40 L58,62" fill="none" {s}/>
<g transform="translate(-196,-74)">
<rect x="0" y="0" width="196" height="34" rx="8" fill="{PAPER}"/>
<path d="M168,34 L186,48 L180,34 Z" fill="{PAPER}"/>
<text x="98" y="22" text-anchor="middle" fill="{INK}" style="font-size:12px">who changed the formula</text>
</g>
</g>'''


def caption(x, y, lines, color, mark):
    return "".join(
        f'<text x="{x}" y="{y + i * 26}" fill="{color}"><tspan fill="{CREDIT if mark == "+" else DEBIT}">{mark} </tspan>{escape(t)}</text>'
        for i, t in enumerate(lines)
    )


def meme():
    w, h = 880, 560
    left, right = 225, 655
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">
<title>Meme: a buff setoff engineer next to a small figure from the spreadsheet era</title>
<style>text {{ font-family: {MONO}; font-size: 14px; white-space: pre; }}</style>
<rect width="{w}" height="{h}" rx="14" fill="{INK}"/>
{ruling(w, h, 34)}
<line x1="440" y1="28" x2="440" y2="{h - 28}" stroke="{MUTED}" stroke-width="1" stroke-dasharray="4 6"/>
<text x="{left}" y="56" text-anchor="middle" fill="{AMBER}" style="font-size:22px;font-weight:700">{escape(MEME["left_title"])}</text>
<text x="{right}" y="56" text-anchor="middle" fill="{MUTED}" style="font-size:22px;font-weight:700">{escape(MEME["right_title"])}</text>
{buff(left)}
{small(right)}
{caption(48, 470, MEME["left"], PAPER, "+")}
{caption(478, 470, MEME["right"], MUTED, "-")}
</svg>
'''


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    (ASSETS / "hero.svg").write_text(hero())
    (ASSETS / "meme.svg").write_text(meme())
    print("wrote", ", ".join(p.name for p in sorted(ASSETS.glob("*.svg"))))


if __name__ == "__main__":
    main()
