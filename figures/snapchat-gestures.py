"""Snapchat's hidden navigation before and after the February 2018 redesign.

Both phones show what the app actually showed: the camera, with nothing on
screen to say that four swipes lead anywhere. The dashed arrows are the
invisible gestures and the boxes are where they went. The redesign kept the
gestures and moved the destinations, which is the point of the case study:
people who had memorised the old map found it changed under them.

Sources: Snap Inc. Q3 2017 earnings call (the "difficult to understand or hard
to use" admission) and press coverage of the 29 November 2017 announcement.
Writes figures/snapchat-gestures.svg with live text; run `make figures` to
regenerate it and outline the text into lectures/img/.
"""

from pathlib import Path

W, H = 1720, 1000
FONT = 24

TEXT = "#fafafa"
MUTED = "#b8c4c8"
GREEN = "#2a9d8f"  # persian-green, css/_palette.scss
SAFFRON = "#e9c46a"  # saffron
SIENNA = "#e76f51"  # burnt-sienna
CHARCOAL = "#264653"
DARK = "#15272e"


def text(lines, x, y, size=FONT, weight=400, fill=TEXT, anchor="middle"):
    line = 1.25 * size
    first = y - (len(lines) - 1) * line / 2 + 0.36 * size
    tspans = "".join(
        f'<tspan x="{x:.1f}" y="{first + i * line:.1f}">{t}</tspan>'
        for i, t in enumerate(lines)
    )
    return (
        f'<text font-size="{size}" font-weight="{weight}" fill="{fill}" '
        f'text-anchor="{anchor}">{tspans}</text>'
    )


def box(lines, cx, cy, w, h, colour):
    """A destination box: coloured outline, first line bold."""
    out = [
        f'<rect x="{cx - w / 2:.1f}" y="{cy - h / 2:.1f}" width="{w}" height="{h}" '
        f'rx="12" fill="{colour}" fill-opacity="0.14" stroke="{colour}" stroke-width="3"/>'
    ]
    line = 1.25 * FONT
    first = cy - (len(lines) - 1) * line / 2 + 0.36 * FONT
    for i, t in enumerate(lines):
        weight = 700 if i == 0 else 400
        fill = colour if i == 0 else TEXT
        out.append(
            f'<text x="{cx:.1f}" y="{first + i * line:.1f}" font-size="{FONT}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="middle">{t}</text>'
        )
    return out


def arrow(x1, y1, x2, y2, label, lx, ly, colour):
    """Dashed arrow (an invisible gesture) with its name beside it."""
    return [
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{colour}" '
        f'stroke-width="3" stroke-dasharray="8 8" marker-end="url(#head)"/>',
        text([label], lx, ly, size=20, fill=MUTED),
    ]


def phone(cx, cy):
    """A phone showing only the camera view."""
    pw, ph = 220, 400
    sx, sy = cx - pw / 2 + 12, cy - ph / 2 + 12
    sw, sh = pw - 24, ph - 24
    return [
        f'<rect x="{cx - pw / 2}" y="{cy - ph / 2}" width="{pw}" height="{ph}" rx="30" '
        f'fill="{DARK}" stroke="{TEXT}" stroke-width="4"/>',
        f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="20" fill="{CHARCOAL}"/>',
        # a hint of a viewfinder scene
        f'<circle cx="{cx - 40}" cy="{cy - 70}" r="22" fill="{SAFFRON}" fill-opacity="0.5"/>',
        f'<path d="M{sx} {cy + 60} L{cx - 50} {cy - 10} L{cx + 10} {cy + 50} '
        f'L{cx + 60} {cy + 10} L{sx + sw} {cy + 80} L{sx + sw} {sy + sh - 20} '
        f'L{sx} {sy + sh - 20} Z" fill="{GREEN}" fill-opacity="0.35"/>',
        # shutter button, the only control on screen
        f'<circle cx="{cx}" cy="{cy + ph / 2 - 50}" r="26" fill="none" '
        f'stroke="{TEXT}" stroke-width="5"/>',
        text(["camera"], cx, cy - ph / 2 - 18, size=20, fill=MUTED),
    ]


def panel(cx, title, left, right, left_col, right_col, footer):
    """One phone with its four hidden gestures and their destinations."""
    cy = 500
    pw, ph = 220, 400
    parts = [text([title], cx, 60, size=34, weight=700)]
    parts += phone(cx, cy)
    # left page (swipe right) and right page (swipe left)
    bh = lambda lines: 40 + 30 * len(lines)
    parts += arrow(cx - pw / 2 - 6, cy, cx - pw / 2 - 60, cy, "swipe right",
                   cx - pw / 2 - 33, cy - 24, left_col)
    parts += box(left, cx - pw / 2 - 175, cy, 230, bh(left), left_col)
    parts += arrow(cx + pw / 2 + 6, cy, cx + pw / 2 + 60, cy, "swipe left",
                   cx + pw / 2 + 33, cy - 24, right_col)
    parts += box(right, cx + pw / 2 + 175, cy, 230, bh(right), right_col)
    # profile below (swipe down) and memories above (swipe up)
    parts += arrow(cx, cy + ph / 2 + 6, cx, cy + ph / 2 + 60, "swipe down",
                   cx + 92, cy + ph / 2 + 36, GREEN)
    parts += box(["Profile", "settings, friends"], cx, cy + ph / 2 + 110, 220, 84, GREEN)
    parts += arrow(cx, cy - ph / 2 - 36, cx, cy - ph / 2 - 90, "swipe up",
                   cx + 82, cy - ph / 2 - 62, GREEN)
    parts += box(["Memories", "saved snaps"], cx, cy - ph / 2 - 135, 220, 84, GREEN)
    parts.append(text(footer, cx, 920, size=24, fill=MUTED))
    return parts


parts = [
    "<defs>"
    '<marker id="head" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" '
    'markerHeight="5" orient="auto-start-reverse">'
    f'<path d="M0 0 L10 5 L0 10 Z" fill="{MUTED}"/></marker></defs>',
    *panel(
        410,
        "Before (2017)",
        ["Chat", "messages,", "newest first"],
        ["Stories", "friends, newest first;", "then Discover:", "publishers"],
        GREEN,
        GREEN,
        ["Nothing on screen says", "any of this exists."],
    ),
    *panel(
        1310,
        "After (Feb 2018)",
        ["Friends", "messages and", "friends' stories, in", "an order chosen", "by an algorithm"],
        ["Discover", "publishers,", "celebrities,", "Snap Map"],
        SAFFRON,
        SAFFRON,
        ["Same hidden gestures.", "The destinations moved."],
    ),
    f'<line x1="860" y1="110" x2="860" y2="890" stroke="{MUTED}" stroke-width="2" '
    'stroke-dasharray="4 10"/>',
]

svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
    f'width="{W}" height="{H}" font-family="Noto Sans">\n'
    "  <title>Snapchat's hidden gesture navigation before and after the 2018 redesign</title>\n  "
    + "\n  ".join(parts)
    + "\n</svg>\n"
)

Path(__file__).with_suffix(".svg").write_text(svg)
