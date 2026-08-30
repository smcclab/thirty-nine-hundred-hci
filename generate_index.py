#!/usr/bin/env python3
"""
Builds the index.html page: a hero header (course image + description from
_config.toml) followed by links to each built html file, styled by the shared
site stylesheet (build/style.css, compiled from css/site.scss).
"""
import sys
import tomllib
from html import escape
from pathlib import Path
import re

# Directories under build/ that are not content sections: canvas/ holds the
# Canvas assignment fragments and pre-push backups (local builds only).
SKIP_DIRS = {"canvas", "img"}

# Preferred section order; anything else follows alphabetically.
SECTION_ORDER = ["lectures", "assessments", "workshops", "resources"]


def get_html_page_title(html_path: Path) -> str:
    """
    Extract the page title from an HTML file using regex.
    """
    with html_path.open('r', encoding='utf-8') as file:
        content = file.read()
    match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    if match:
        title = match.group(1)
        title = re.sub(r'\s+', ' ', title).strip()
        return title
    else:
        return ""


def hero_html(info: dict, base_path: Path) -> str:
    """The hero header: course image (if present in the build), title, byline."""
    title = escape(info["title"])
    byline = " · ".join(
        escape(info[key]) for key in ("author", "institution", "year") if info.get(key)
    )
    out = '    <header class="hero">\n'
    course_image = info.get("course_image")
    if course_image:
        if (base_path / course_image).exists():
            out += f'        <img src="{escape(course_image)}" alt="{title}">\n'
        else:
            print(f"Warning: course_image not found in build: {course_image}",
                  file=sys.stderr)
    out += f'        <h1>{title}</h1>\n'
    out += f'        <p class="byline">{byline}</p>\n'
    out += '    </header>\n'
    return out


def description_html(info: dict) -> str:
    """The course description as paragraphs (blank-line separated in the toml)."""
    description = info.get("description", "").strip()
    if not description:
        return ""
    out = '    <section class="course-description">\n'
    for paragraph in re.split(r'\n\s*\n', description):
        out += f'        <p>{escape(" ".join(paragraph.split()))}</p>\n'
    out += '    </section>\n'
    return out


def generate_index(info: dict, base_path: Path) -> str:
    """Generate HTML index page with links to built files"""
    title = escape(info["title"])
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
"""
    html += hero_html(info, base_path)
    html += description_html(info)

    # subdirectories of the base_path are the headings.
    subdirectories = [item for item in base_path.iterdir()
                      if item.is_dir() and item.name not in SKIP_DIRS]
    order = {name: i for i, name in enumerate(SECTION_ORDER)}
    subdirectories.sort(key=lambda d: (order.get(d.name, len(order)), d.name))

    html += '    <section class="section-listing">\n'
    for dir in subdirectories:
        print(f"Processing directory: {dir.name}")
        html_files = sorted(dir.glob('*.html'))
        if not html_files:
            continue
        html += f'    <h2>{escape(dir.name.capitalize())}</h2>\n'

        # html files contained within dir are the list items.
        html += f'    <ol>\n'
        for html_path in html_files:
            print(f"  Processing HTML file: {html_path}")
            html += html_file_li_string(html_path, base_path)
        html += f'    </ol>\n'
    html += '    </section>\n'

    html += """
</body>
</html>"""
    return html


def html_file_li_string(html_path: Path, base_path: Path) -> str:
    """
    Writes a <li> str related to a single html document in the index. Searches for possible extra files (pdf, docx, pptx)
    """
    out = "        <li>"
    out += get_html_page_title(html_path) or html_path.stem
    html_rel_path = str(html_path.relative_to(base_path))
    out += f' [<a href="{html_rel_path}">html</a>]'
    # link PDF if it exists
    pdf_path = html_path.with_suffix(".pdf")
    if pdf_path.exists():
        out += f' [<a href="{str(pdf_path.relative_to(base_path))}">pdf</a>]'
    # link docx if it exists
    docx_path = html_path.with_suffix(".docx")
    if docx_path.exists():
        out += f' [<a href="{str(docx_path.relative_to(base_path))}">docx</a>]'
    # link pptx if it exists
    pptx_path = html_path.with_suffix(".pptx")
    if pptx_path.exists():
        out += f' [<a href="{str(pptx_path.relative_to(base_path))}">pptx</a>]'
    out+= "</li>\n"
    return out


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: script.py output_file build_directory")
        sys.exit(1)

    with open("_config.toml", "rb") as f:
        info = tomllib.load(f)

    output_file = Path(sys.argv[1]) # output file
    base_dir = Path(sys.argv[2]) # base dir

    with open(output_file, 'w') as f:
        f.write(generate_index(info, base_dir))
