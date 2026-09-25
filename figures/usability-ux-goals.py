"""Draw usability goals nested inside user experience goals, as an SVG.

A conceptual redraw of the usability/UX goals diagram from Rogers, Sharp & Preece
(Interaction Design), so the slide cites the idea rather than reproducing a
published figure. Writes figures/usability-ux-goals.svg with live text; run
`make figures` to regenerate it and outline the text into lectures/img/.
"""

import math
from pathlib import Path

CX, CY = 500, 560
R_OUTER, R_INNER, R_CORE = 490, 292, 104
R_UX_LABEL, R_USABILITY_LABEL = 392, 200
FONT = 28
LINE = 1.2 * FONT

TEXT = "#fafafa"
GREEN = "#2a9d8f"  # persian-green, css/_palette.scss
SAFFRON = "#e9c46a"  # saffron
DARK = "#15272e"  # darker-charcoal, the deck background

# Clockwise from the top. Short labels sit near the horizontal, where the
# ring leaves least room either side.
USABILITY = [
    ["Efficient", "to use"],
    ["Effective", "to use"],
    ["Safe", "to use"],
    ["Easy to", "remember", "how to use"],
    ["Easy to", "learn"],
    ["Good", "utility"],
]
UX = [
    ["Fun"],
    ["Emotionally", "fulfilling"],
    ["Rewarding"],
    ["Helpful"],
    ["Supportive of", "creativity"],
    ["Motivating"],
    ["Aesthetically", "pleasing"],
    ["Entertaining"],
    ["Enjoyable"],
    ["Satisfying"],
]


def label(lines, x, y, weight=400, fill=TEXT, size=FONT):
    """Centred multi-line text; baselines set explicitly so every renderer agrees."""
    line = 1.2 * size
    first = y - (len(lines) - 1) * line / 2 + 0.36 * size
    tspans = "".join(
        f'<tspan x="{x:.1f}" y="{first + i * line:.1f}">{text}</tspan>'
        for i, text in enumerate(lines)
    )
    return (
        f'<text font-size="{size}" font-weight="{weight}" fill="{fill}" '
        f'text-anchor="middle">{tspans}</text>'
    )


def ring(labels, radius):
    out = []
    for i, lines in enumerate(labels):
        a = math.radians(-90 + i * 360 / len(labels))
        out.append(label(lines, CX + radius * math.cos(a), CY + radius * math.sin(a)))
    return out


parts = [
    label(["User experience goals"], CX, 26, weight=700, fill=SAFFRON, size=36),
    f'<circle cx="{CX}" cy="{CY}" r="{R_OUTER}" fill="{SAFFRON}" '
    f'fill-opacity="0.10" stroke="{SAFFRON}" stroke-width="4"/>',
    f'<circle cx="{CX}" cy="{CY}" r="{R_INNER}" fill="{GREEN}" '
    f'fill-opacity="0.22" stroke="{GREEN}" stroke-width="4"/>',
    f'<circle cx="{CX}" cy="{CY}" r="{R_CORE}" fill="{GREEN}"/>',
    label(["Usability", "goals"], CX, CY, weight=700, fill=DARK, size=32),
    *ring(USABILITY, R_USABILITY_LABEL),
    *ring(UX, R_UX_LABEL),
]

svg = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1056" '
    'width="1000" height="1056" font-family="Noto Sans">\n'
    "  <title>Usability goals nested inside user experience goals</title>\n  "
    + "\n  ".join(parts)
    + "\n</svg>\n"
)

Path(__file__).with_suffix(".svg").write_text(svg)
