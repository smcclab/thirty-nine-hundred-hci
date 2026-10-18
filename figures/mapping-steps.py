"""Steps in the mapping process, redrawn after Baalman (2022), figure 1.2.

Seven stages around a loop: gesture, sensor, electronic circuits,
computational model, output model, output media, and the performer's
perception, which closes the loop back to the next gesture. The shapes follow
the book (triangle for the gesture and the media, circle for the sensor and
the performer, squares for the electronic and computational stages, dashed
where the book draws them dashed). Redrawn in the course palette because the
original's pale pink line work is unreadable on a projector.

Writes figures/mapping-steps.svg with live text; run `make figures` to
regenerate it and outline the text into lectures/img/.
"""

import math
from pathlib import Path

W, H = 1400, 1040
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


def shape(kind, cx, cy, s, colour, dash=""):
    style = (
        f'fill="{colour}" fill-opacity="0.18" stroke="{colour}" stroke-width="4"'
        + (f' stroke-dasharray="{dash}"' if dash else "")
    )
    if kind == "circle":
        return f'<circle cx="{cx}" cy="{cy}" r="{s}" {style}/>'
    if kind == "square":
        return f'<rect x="{cx - s}" y="{cy - s}" width="{2 * s}" height="{2 * s}" rx="8" {style}/>'
    # triangle, apex up, drawn a little larger so the text fits
    t = s * 1.3
    pts = f"{cx},{cy - t} {cx + t * 0.95},{cy + t * 0.6} {cx - t * 0.95},{cy + t * 0.6}"
    return f'<polygon points="{pts}" {style}/>'


# (label lines, shape, colour, dash) in loop order, starting from the gesture
STAGES = [
    (["Gesture"], "triangle", GREEN, ""),
    (["Sensor"], "circle", GREEN, ""),
    (["Electronic", "circuits"], "square", SAFFRON, ""),
    (["Computational", "model"], "square", SAFFRON, "14 10"),
    (["Output", "model"], "square", SIENNA, "14 10"),
    (["Output", "media"], "triangle", SIENNA, "4 8"),
    (["Performer", "(perception)"], "circle", GREEN, "4 8"),
]

CX, CY, RING, S = 700, 530, 380, 108
n = len(STAGES)
# start at the left and go clockwise
angles = [math.pi + 2 * math.pi * i / n for i in range(n)]
pos = [(CX + RING * math.cos(a), CY + RING * math.sin(a)) for a in angles]

parts = [
    "<defs>"
    '<marker id="head" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" '
    'markerHeight="6" orient="auto-start-reverse">'
    f'<path d="M0 0 L10 5 L0 10 Z" fill="{MUTED}"/></marker></defs>',
]

# arcs between consecutive stages, trimmed so they start and end outside the shapes
GAP = 0.36  # radians to leave clear at each end
for i in range(n):
    a1 = angles[i] + GAP
    a2 = angles[(i + 1) % n] - GAP
    x1, y1 = CX + RING * math.cos(a1), CY + RING * math.sin(a1)
    x2, y2 = CX + RING * math.cos(a2), CY + RING * math.sin(a2)
    dash = ' stroke-dasharray="4 10"' if i == n - 1 else ""
    parts.append(
        f'<path d="M{x1:.1f} {y1:.1f} A{RING} {RING} 0 0 1 {x2:.1f} {y2:.1f}" '
        f'fill="none" stroke="{MUTED}" stroke-width="5"{dash} marker-end="url(#head)"/>'
    )

for (lines, kind, colour, dash), (x, y) in zip(STAGES, pos):
    parts.append(shape(kind, x, y, S, colour, dash))
    dy = 14 if kind == "triangle" else 0
    size = 30 if any(len(t) > 11 for t in lines) else (33 if len(lines) > 1 else FONT)
    parts.append(text(lines, x, y + dy, size=size))

parts.append(text(["the mapping", "loop"], CX, CY, size=44, weight=700, fill=MUTED))

svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
    f'width="{W}" height="{H}" font-family="Noto Sans">\n'
    "  <title>Steps in the mapping process: gesture, sensor, electronic circuits, "
    "computational model, output model, output media, perception</title>\n  "
    + "\n  ".join(parts)
    + "\n</svg>\n"
)

Path(__file__).with_suffix(".svg").write_text(svg)
