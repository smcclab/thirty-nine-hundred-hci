"""The question of mapping, redrawn after Baalman (2022), figure 1.1.

Two clusters joined by a loop: the environment (performer, audience, other
factors) on the left, the output media (audio, video, light, mechatronics,
other media) on the right, and "mapping" as the connection between them. The
book's hatched pink-on-cream drawing does not survive projection, so this is
the same diagram in the course palette on a transparent background.

Writes figures/mapping-question.svg with live text; run `make figures` to
regenerate it and outline the text into lectures/img/.
"""

from pathlib import Path

W, H = 1600, 960
FONT = 36

TEXT = "#fafafa"
MUTED = "#b8c4c8"
GREEN = "#2a9d8f"  # persian-green, css/_palette.scss
SAFFRON = "#e9c46a"  # saffron
SIENNA = "#e76f51"  # burnt-sienna


def text(lines, x, y, size=FONT, weight=400, fill=TEXT):
    line = 1.25 * size
    first = y - (len(lines) - 1) * line / 2 + 0.36 * size
    tspans = "".join(
        f'<tspan x="{x:.1f}" y="{first + i * line:.1f}">{t}</tspan>'
        for i, t in enumerate(lines)
    )
    return (
        f'<text font-size="{size}" font-weight="{weight}" fill="{fill}" '
        f'text-anchor="middle">{tspans}</text>'
    )


def cluster(cx, cy, r, title, items, colour):
    """A large tinted circle with smaller labelled circles inside it."""
    out = [
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{colour}" fill-opacity="0.18" '
        f'stroke="{colour}" stroke-width="4"/>',
        text([title], cx, cy - r - 34, size=48, weight=700, fill=colour),
    ]
    for lines, dx, dy, ir in items:
        out.append(
            f'<circle cx="{cx + dx}" cy="{cy + dy}" r="{ir}" fill="#15272e" '
            f'fill-opacity="0.85" stroke="{colour}" stroke-width="3"/>'
        )
        out.append(text(lines, cx + dx, cy + dy, size=34))
    return out


LX, RX, CY, R = 360, 1240, 500, 320

parts = [
    "<defs>"
    '<marker id="head" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" '
    'markerHeight="6" orient="auto-start-reverse">'
    f'<path d="M0 0 L10 5 L0 10 Z" fill="{MUTED}"/></marker></defs>',
    *cluster(
        LX, CY, R, "Environment",
        [
            (["Performer"], -100, -130, 120),
            (["Audience"], -110, 125, 120),
            (["Other", "factors"], 140, 10, 115),
        ],
        GREEN,
    ),
    *cluster(
        RX, CY, R, "Media",
        [
            (["Video"], -120, -160, 95),
            (["Audio"], 100, -160, 95),
            (["Light"], 190, 50, 85),
            (["Mechatronics"], -120, 40, 130),
            (["Other", "media"], 70, 190, 95),
        ],
        SAFFRON,
    ),
    # the loop: environment -> media over the top, media -> environment underneath
    f'<path d="M{LX + 225} {CY - R + 85} Q 800 20 {RX - 225} {CY - R + 85}" '
    f'fill="none" stroke="{MUTED}" stroke-width="5" marker-end="url(#head)"/>',
    f'<path d="M{RX - 225} {CY + R - 85} Q 800 980 {LX + 225} {CY + R - 85}" '
    f'fill="none" stroke="{MUTED}" stroke-width="5" marker-end="url(#head)"/>',
    text(["Mapping"], 800, CY - 30, size=60, weight=700, fill=SIENNA),
    text(["gesture", "→ output"], 800, CY + 70, size=34, fill=MUTED),
]

svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
    f'width="{W}" height="{H}" font-family="Noto Sans">\n'
    "  <title>The question of mapping: the environment, the output media, "
    "and the loop between them</title>\n  "
    + "\n  ".join(parts)
    + "\n</svg>\n"
)

Path(__file__).with_suffix(".svg").write_text(svg)
