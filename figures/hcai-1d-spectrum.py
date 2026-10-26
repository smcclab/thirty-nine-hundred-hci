"""The misleading one-dimensional spectrum, redrawn after Shneiderman (2022), figure 8.1.

A single bar from human control to computer automation with a slider in the
middle: the view that designers must trade one off against the other.

Writes figures/hcai-1d-spectrum.svg with live text; run `make figures` to
regenerate it and outline the text into lectures/img/.
"""

from pathlib import Path

W, H = 1400, 380

TEXT = "#fafafa"
MUTED = "#b8c4c8"
GREEN = "#2a9d8f"
SAFFRON = "#e9c46a"


def text(lines, x, y, size=36, weight=400, fill=TEXT):
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


x1, x2, cy, bh = 200, 1200, 150, 44
cx = (x1 + x2) / 2
parts = [
    "<defs>"
    '<linearGradient id="bar" x1="0" x2="1" y1="0" y2="0">'
    f'<stop offset="0" stop-color="{MUTED}"/><stop offset="1" stop-color="{GREEN}"/>'
    "</linearGradient></defs>",
    f'<rect x="{x1}" y="{cy - bh / 2}" width="{x2 - x1}" height="{bh}" rx="8" '
    f'fill="url(#bar)" stroke="{TEXT}" stroke-width="3"/>',
    # slider knob, apex up
    f'<polygon points="{cx},{cy - 90} {cx + 60},{cy + bh / 2 + 10} {cx - 60},{cy + bh / 2 + 10}" '
    f'fill="{SAFFRON}" stroke="{TEXT}" stroke-width="4" stroke-linejoin="round"/>',
    text(["Human", "control"], x1, cy + 110),
    text(["Computer", "automation"], x2, cy + 110),
]

svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
    f'width="{W}" height="{H}" font-family="Noto Sans">\n'
    "  <title>A one-dimensional slider from human control to computer automation</title>\n  "
    + "\n  ".join(parts)
    + "\n</svg>\n"
)

Path(__file__).with_suffix(".svg").write_text(svg)
