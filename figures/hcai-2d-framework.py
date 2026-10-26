"""The two-dimensional HCAI framework, redrawn after Shneiderman (2022), figure 8.4.

Human control on the vertical axis, computer automation on the horizontal.
Four quadrants with the book's examples, and the two failure regions,
excessive human control and excessive automation, as bands along the top and
right edges. The reliable, safe and trustworthy region is top right.

Writes figures/hcai-2d-framework.svg with live text; run `make figures` to
regenerate it and outline the text into lectures/img/.
"""

from pathlib import Path

W, H = 1300, 1150

TEXT = "#fafafa"
MUTED = "#b8c4c8"
GREEN = "#2a9d8f"
SIENNA = "#e76f51"


def text(lines, x, y, size=34, weight=400, fill=TEXT, anchor="middle"):
    lines = [t.replace("&", "&amp;") for t in lines]
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


# outer plot area (includes the two grey bands)
L, T, R, B = 200, 110, 1230, 1000
BAND = 70  # width of the excessive-control / excessive-automation bands
# inner (green) area
iL, iT, iR, iB = L, T + BAND, R - BAND, B

parts = [
    "<defs>"
    '<linearGradient id="field" x1="0" x2="1" y1="1" y2="0">'
    f'<stop offset="0" stop-color="{MUTED}" stop-opacity="0.25"/>'
    f'<stop offset="0.55" stop-color="{GREEN}" stop-opacity="0.45"/>'
    f'<stop offset="1" stop-color="{GREEN}" stop-opacity="0.75"/>'
    "</linearGradient></defs>",
    # failure bands: along the top and down the right edge
    f'<path d="M{L} {T + BAND} V{T} H{R} V{B} H{R - BAND} V{T + BAND} Z" '
    f'fill="{SIENNA}" fill-opacity="0.28" stroke="{SIENNA}" stroke-width="4" stroke-linejoin="round"/>',
    # the green field
    f'<rect x="{iL}" y="{iT}" width="{iR - iL}" height="{iB - iT}" '
    f'fill="url(#field)" stroke="{MUTED}" stroke-width="3"/>',
    text(["Excessive Human Control"], (iL + iR) / 2, T + BAND / 2, size=34, weight=700),
    f'<text font-size="34" font-weight="700" fill="{TEXT}" text-anchor="middle" '
    f'transform="translate({R - BAND / 2} {(iT + iB) / 2}) rotate(90)">Excessive Automation</text>',
]

# quadrants
pad, mid_gap = 22, 18
qw = (iR - iL - 2 * pad - mid_gap) / 2
qh = (iB - iT - 2 * pad - mid_gap) / 2
Q = {
    "tl": (iL + pad, iT + pad),
    "tr": (iL + pad + qw + mid_gap, iT + pad),
    "bl": (iL + pad, iT + pad + qh + mid_gap),
    "br": (iL + pad + qw + mid_gap, iT + pad + qh + mid_gap),
}
for x, y in Q.values():
    parts.append(
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{qw:.1f}" height="{qh:.1f}" rx="36" '
        f'fill="none" stroke="{TEXT}" stroke-opacity="0.7" stroke-width="4"/>'
    )

ins = 34
x, y = Q["tl"]
parts.append(text(["Human Mastery"], x + ins, y + 50, size=36, weight=700, anchor="start"))
parts.append(text(["Bicycle", "Piano"], x + ins, y + 135, size=32, anchor="start"))
x, y = Q["tr"]
parts.append(text(["Reliable, Safe", "& Trustworthy"], x + qw - ins, y + 70, size=36, weight=700, anchor="end"))
parts.append(text(["Elevator", "Camera"], x + qw - ins, y + 175, size=32, anchor="end"))
x, y = Q["bl"]
parts.append(text(["Music box", "Landmine"], x + ins, y + qh - 105, size=32, anchor="start"))
x, y = Q["br"]
parts.append(text(["Pacemaker", "Airbag"], x + qw - ins, y + qh - 125, size=32, anchor="end"))
parts.append(text(["Computer Control"], x + qw - ins, y + qh - 42, size=36, weight=700, anchor="end"))

# axes
parts += [
    text(["High"], L - 60, iT + 12, size=32, fill=MUTED, anchor="end"),
    text(["Low"], L - 60, iB - 12, size=32, fill=MUTED, anchor="end"),
    f'<text font-size="38" font-weight="700" fill="{TEXT}" text-anchor="middle" '
    f'transform="translate(70 {(iT + iB) / 2}) rotate(-90)">Human Control</text>',
    text(["Low"], iL + 10, B + 50, size=32, fill=MUTED, anchor="start"),
    text(["High"], iR - 10, B + 50, size=32, fill=MUTED, anchor="end"),
    text(["Computer Automation"], (iL + iR) / 2, B + 50, size=38, weight=700),
    text(["Human-Centered AI"], (iL + iR) / 2, 55, size=42, weight=700),
]

svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
    f'width="{W}" height="{H}" font-family="Noto Sans">\n'
    "  <title>Two-dimensional HCAI framework: human control against computer automation, "
    "with reliable, safe and trustworthy systems high on both, and excessive human control "
    "or excessive automation as failure bands</title>\n  "
    + "\n  ".join(parts)
    + "\n</svg>\n"
)

Path(__file__).with_suffix(".svg").write_text(svg)
