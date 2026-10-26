"""Shneiderman's map of Human-Centered AI, redrawn after Shneiderman (2022), figure 1.2.

A stack of three aspirations (human values, individual goals, design
aspirations) resting on the book's three ideas (HCAI framework, design
metaphors, governance structures); five stakeholder groups bracketed on the
left, three threats pressing in from the right. Redrawn in the course palette
so the text is legible on a dark slide.

Writes figures/hcai-overview.svg with live text; run `make figures` to
regenerate it and outline the text into lectures/img/.
"""

from pathlib import Path

W, H = 1760, 860

TEXT = "#fafafa"
MUTED = "#b8c4c8"
GREEN = "#2a9d8f"  # persian-green, css/_palette.scss
SAFFRON = "#e9c46a"  # saffron
SANDY = "#f4a261"  # sandy-brown
SIENNA = "#e76f51"  # burnt-sienna


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


def box(x, y, w, h, colour, rx=28, width=4, opacity=0.18):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
        f'fill="{colour}" fill-opacity="{opacity}" stroke="{colour}" stroke-width="{width}"/>'
    )


parts = []

# ---- centre stack -----------------------------------------------------------
CX = 800
LAYERS = [
    # (title, subtitle lines, width, colour)
    ("Human Values", ["Rights, Justice & Dignity"], 560, GREEN),
    ("Individual Goals", ["Self-efficacy, Creativity, Responsibility & Social Connections"], 800, SAFFRON),
    ("Design Aspirations", ["Reliable, Safe & Trustworthy", "Team, Organization, Industry & Government"], 820, SANDY),
]
y = 110
for title, sub, w, colour in LAYERS:
    h = 110 if len(sub) == 1 else 150
    parts.append(box(CX - w / 2, y, w, h, colour, rx=h / 2 if title == "Human Values" else 22))
    parts.append(text([title], CX, y + 36, size=38, weight=700))
    parts.append(text(sub, CX, y + 36 + 22 + 18 * len(sub), size=27, fill=MUTED))
    y += h + 22

IDEAS = [
    (["HCAI", "Framework"], "Part 2", GREEN),
    (["Design", "Metaphors"], "Part 3", SAFFRON),
    (["Governance", "Structures"], "Part 4", SIENNA),
]
bw, bh, gap = 262, 270, 18
x0 = CX - (3 * bw + 2 * gap) / 2
for i, (lines, part, colour) in enumerate(IDEAS):
    x = x0 + i * (bw + gap)
    parts.append(box(x, y, bw, bh, colour, rx=20, width=6, opacity=0.25))
    parts.append(text(lines, x + bw / 2, y + 110, size=40, weight=700))
    parts.append(text([f"({part})"], x + bw / 2, y + 210, size=30, fill=MUTED))
bottom = y + bh

# ---- stakeholders (left) -----------------------------------------------------
STAKE = ["Researchers", "Developers", "Business leaders", "Policy-makers", "Users"]
sx, top = 250, 110
pitch = (bottom - top) / len(STAKE)
for i, s in enumerate(STAKE):
    cy = top + pitch * (i + 0.5)
    parts.append(
        f'<ellipse cx="{sx}" cy="{cy:.1f}" rx="118" ry="{pitch / 2 - 8:.1f}" '
        f'fill="{GREEN}" fill-opacity="0.18" stroke="{GREEN}" stroke-width="4"/>'
    )
    parts.append(text([s], sx, cy, size=29))
# bracket
bx = sx - 150
parts.append(
    f'<path d="M{bx + 60} {top} Q{bx} {top} {bx} {top + 60} V{bottom - 60} '
    f'Q{bx} {bottom} {bx + 60} {bottom}" fill="none" stroke="{GREEN}" stroke-width="6"/>'
)
parts.append(
    f'<text font-size="40" font-weight="700" fill="{GREEN}" text-anchor="middle" '
    f'transform="translate({bx - 40} {(top + bottom) / 2}) rotate(-90)">Stakeholders</text>'
)

# ---- threats (right) ---------------------------------------------------------
THREATS = [["Malicious", "actors"], ["Bias"], ["Flawed", "software"]]
tx_tip, tx_head, tx_tail = 1280, 1370, 1570  # arrow tip (pointing left), head base, tail
th_top, th_bot = 150, bottom - 10
tpitch = (th_bot - th_top) / len(THREATS)
for i, lines in enumerate(THREATS):
    cy = th_top + tpitch * (i + 0.5)
    hw = 54  # half-height of shaft
    hh = 100  # half-height of head
    pts = (
        f"{tx_tip},{cy:.1f} {tx_head},{cy - hh:.1f} {tx_head},{cy - hw:.1f} "
        f"{tx_tail},{cy - hw:.1f} {tx_tail},{cy + hw:.1f} {tx_head},{cy + hw:.1f} "
        f"{tx_head},{cy + hh:.1f}"
    )
    parts.append(
        f'<polygon points="{pts}" fill="{SIENNA}" fill-opacity="0.22" '
        f'stroke="{SIENNA}" stroke-width="4" stroke-linejoin="round"/>'
    )
    parts.append(text(lines, (tx_head + tx_tail) / 2 + 10, cy, size=28))
# spine joining the tails
parts.append(
    f'<rect x="{tx_tail}" y="{th_top}" width="80" height="{th_bot - th_top}" rx="16" '
    f'fill="{SIENNA}" fill-opacity="0.22" stroke="{SIENNA}" stroke-width="4"/>'
)
parts.append(
    f'<text font-size="40" font-weight="700" fill="{SIENNA}" text-anchor="middle" '
    f'transform="translate({tx_tail + 120} {(th_top + th_bot) / 2}) rotate(-90)">Threats</text>'
)

parts.append(text(["Human-Centered AI"], CX, 50, size=42, weight=700))

svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
    f'width="{W}" height="{H}" font-family="Noto Sans">\n'
    "  <title>Human-Centered AI: human values, individual goals and design aspirations, "
    "supported by the HCAI framework, design metaphors and governance structures, "
    "with stakeholders on one side and threats on the other</title>\n  "
    + "\n  ".join(parts)
    + "\n</svg>\n"
)

Path(__file__).with_suffix(".svg").write_text(svg)
