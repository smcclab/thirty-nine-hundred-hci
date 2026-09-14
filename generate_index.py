#!/usr/bin/env python3
"""
Builds the index.html page: a hero header (course image + description from
_config.toml) followed by links to each built html file, styled by the shared
site stylesheet (build/style.css, compiled from css/site.scss).

Beside the index it also writes the crawler/agent files, all from `site_url`
in _config.toml:
  sitemap.xml    every HTML page and PDF, lastmod from the source .md's mtime
  robots.txt     allow-all plus the sitemap URL (note: GitHub Pages only honours
                 a robots.txt at the domain root, so this one is informational
                 unless the site is served from the root of its domain)
  llms.txt       the llms.txt convention: course summary + links to the
                 rendered .md sibling of every page (built by `make markdown`)
  llms-full.txt  those .md files concatenated in index order
"""
import json
import sys
import tomllib
from datetime import datetime, timezone
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
        # pandoc --title-prefix (SEO_OPTS in the Makefile) renders the <title>
        # as "<course title> – <page title>"; the listing wants the page title.
        if TITLE_PREFIX and title.startswith(TITLE_PREFIX + " – "):
            title = title[len(TITLE_PREFIX) + 3:]
        return title
    else:
        return ""


TITLE_PREFIX = ""  # set from _config.toml `title` in __main__


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


def footer_html(info: dict) -> str:
    """Copyright/licence footer. The standalone doc pages get the equivalent
    fragment from templates/footer.html (via pandoc --include-after-body);
    here it is built from `year` and `author` in _config.toml, so keep the
    template's hard-coded year in sync with the toml by hand."""
    year = escape(info.get("year", ""))
    author = escape(info.get("author", ""))
    out = '    <footer class="site-footer">\n'
    out += (f'        <p>© {year} {author}, '
            'The Australian National University.\n'
            '        Except where otherwise noted, this work is licensed under a\n'
            '        <a href="https://creativecommons.org/licenses/by/4.0/" '
            'rel="license">Creative Commons Attribution 4.0 International '
            'Licence</a>.</p>\n')
    out += '    </footer>\n'
    return out


def meta_description(info: dict) -> str:
    """First paragraph of the course description, whitespace-collapsed."""
    description = info.get("description", "").strip()
    if not description:
        return ""
    first = re.split(r'\n\s*\n', description)[0]
    return " ".join(first.split())


def head_html(info: dict, base_path: Path) -> str:
    """<head> for the index: title, description, canonical, Open Graph, and a
    schema.org Course record so search engines can show it as a course."""
    title = info["title"]
    site_url = info.get("site_url", "")
    description = meta_description(info)
    out = '    <meta charset="utf-8">\n'
    out += '    <meta name="viewport" content="width=device-width, initial-scale=1">\n'
    out += f'    <title>{escape(title)}</title>\n'
    if description:
        out += f'    <meta name="description" content="{escape(description)}">\n'
    out += f'    <meta name="author" content="{escape(info.get("author", ""))}">\n'
    out += '    <link rel="stylesheet" href="style.css">\n'
    if site_url:
        out += f'    <link rel="canonical" href="{escape(site_url)}">\n'
        out += f'    <link rel="alternate" type="text/plain" href="{escape(site_url)}llms.txt" title="llms.txt">\n'
        out += '    <meta property="og:type" content="website">\n'
        out += f'    <meta property="og:url" content="{escape(site_url)}">\n'
        out += f'    <meta property="og:site_name" content="{escape(title)}">\n'
        out += f'    <meta property="og:title" content="{escape(title)}">\n'
        if description:
            out += f'    <meta property="og:description" content="{escape(description)}">\n'
        course_image = info.get("course_image")
        if course_image and (base_path / course_image).exists():
            out += f'    <meta property="og:image" content="{escape(site_url + course_image)}">\n'
            out += '    <meta name="twitter:card" content="summary_large_image">\n'
        else:
            out += '    <meta name="twitter:card" content="summary">\n'
        course = {
            "@context": "https://schema.org",
            "@type": "Course",
            "name": title,
            "description": description,
            "url": site_url,
            "provider": {
                "@type": "CollegeOrUniversity",
                "name": "The Australian National University",
                "url": "https://www.anu.edu.au/",
            },
            "author": {"@type": "Person", "name": info.get("author", "")},
            "inLanguage": "en-AU",
            "isAccessibleForFree": True,
            "license": "https://creativecommons.org/licenses/by/4.0/",
        }
        if course_image and (base_path / course_image).exists():
            course["image"] = site_url + course_image
        if info.get("course_codes"):
            course["courseCode"] = info["course_codes"]
        out += ('    <script type="application/ld+json">'
                + json.dumps(course, ensure_ascii=False)
                + '</script>\n')
    return out


def generate_index(info: dict, base_path: Path) -> str:
    """Generate HTML index page with links to built files"""
    html = '<!DOCTYPE html>\n<html lang="en-AU">\n<head>\n'
    html += head_html(info, base_path)
    html += '</head>\n<body>\n'
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
    html += footer_html(info)

    html += """
</body>
</html>"""
    return html


def html_file_li_string(html_path: Path, base_path: Path) -> str:
    """
    Writes a <li> str related to a single html document in the index. Searches for possible extra files (pdf, docx, pptx)
    """
    out = "        <li>"
    title = get_html_page_title(html_path) or html_path.stem
    html_rel_path = str(html_path.relative_to(base_path))
    # The title itself is the primary link: descriptive link text reads better
    # for screen readers and search engines than a bare "[html]".
    out += f'<a href="{html_rel_path}">{escape(title)}</a>'
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


def content_sections(base_path: Path) -> list[tuple[str, list[Path]]]:
    """(section name, sorted html files) in index order — the same walk the
    index page does, shared with the sitemap and llms.txt writers."""
    order = {name: i for i, name in enumerate(SECTION_ORDER)}
    dirs = [d for d in base_path.iterdir() if d.is_dir() and d.name not in SKIP_DIRS]
    dirs.sort(key=lambda d: (order.get(d.name, len(order)), d.name))
    return [(d.name, sorted(d.glob('*.html'))) for d in dirs if any(d.glob('*.html'))]


def lastmod(html_path: Path, base_path: Path) -> str:
    """ISO date for <lastmod>: the source markdown's mtime if it exists (CI
    restores git mtimes, so this tracks the last content commit), else the
    built file's."""
    source = Path(html_path.relative_to(base_path)).with_suffix(".md")
    target = source if source.exists() else html_path
    ts = datetime.fromtimestamp(target.stat().st_mtime, tz=timezone.utc)
    return ts.strftime("%Y-%m-%d")


def sitemap_xml(info: dict, base_path: Path) -> str:
    site_url = info["site_url"]
    urls = [(site_url, datetime.now(tz=timezone.utc).strftime("%Y-%m-%d"))]
    for _, html_files in content_sections(base_path):
        for html_path in html_files:
            date = lastmod(html_path, base_path)
            urls.append((site_url + str(html_path.relative_to(base_path)), date))
            pdf_path = html_path.with_suffix(".pdf")
            if pdf_path.exists():
                urls.append((site_url + str(pdf_path.relative_to(base_path)), date))
    out = '<?xml version="1.0" encoding="UTF-8"?>\n'
    out += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for loc, date in urls:
        out += f'  <url><loc>{escape(loc)}</loc><lastmod>{date}</lastmod></url>\n'
    out += '</urlset>\n'
    return out


def robots_txt(info: dict) -> str:
    return ("User-agent: *\nAllow: /\n\n"
            f"Sitemap: {info['site_url']}sitemap.xml\n")


def llms_txt(info: dict, base_path: Path) -> str:
    """https://llmstxt.org/ — H1, blockquote summary, then sections of links
    to the rendered markdown of every page (falling back to the HTML where a
    page has no .md sibling, e.g. the hand-written ones)."""
    site_url = info["site_url"]
    out = f"# {info['title']}\n\n"
    summary = meta_description(info)
    if summary:
        out += f"> {summary}\n\n"
    out += (f"{info.get('institution', '')}, {info.get('year', '')}. "
            f"Convened by {info.get('author', '')}. ")
    out += ("Content is CC BY 4.0. Every page below is available as rendered "
            "Markdown (citations resolved) at the linked .md URL; the same path "
            "with .html is the web page and, for lectures and assessments, "
            ".pdf is a print version. The full site as one file is at "
            f"{site_url}llms-full.txt\n\n")
    for section, html_files in content_sections(base_path):
        out += f"## {section.capitalize()}\n\n"
        for html_path in html_files:
            title = get_html_page_title(html_path) or html_path.stem
            md_path = html_path.with_suffix(".md")
            target = md_path if md_path.exists() else html_path
            out += f"- [{title}]({site_url}{target.relative_to(base_path)})\n"
        out += "\n"
    return out


def llms_full_txt(info: dict, base_path: Path) -> str:
    out = f"# {info['title']}\n\n"
    for section, html_files in content_sections(base_path):
        for html_path in html_files:
            md_path = html_path.with_suffix(".md")
            if not md_path.exists():
                continue
            out += f"\n\n---\n\n<!-- {section}/{md_path.name} -->\n\n"
            out += md_path.read_text(encoding="utf-8").strip() + "\n"
    return out


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: script.py output_file build_directory")
        sys.exit(1)

    with open("_config.toml", "rb") as f:
        info = tomllib.load(f)
    TITLE_PREFIX = info["title"]

    output_file = Path(sys.argv[1]) # output file
    base_dir = Path(sys.argv[2]) # base dir

    with open(output_file, 'w') as f:
        f.write(generate_index(info, base_dir))

    if info.get("site_url"):
        (base_dir / "sitemap.xml").write_text(sitemap_xml(info, base_dir), encoding="utf-8")
        (base_dir / "robots.txt").write_text(robots_txt(info), encoding="utf-8")
        (base_dir / "llms.txt").write_text(llms_txt(info, base_dir), encoding="utf-8")
        (base_dir / "llms-full.txt").write_text(llms_full_txt(info, base_dir), encoding="utf-8")
    else:
        print("Warning: no site_url in _config.toml — skipping sitemap/robots/llms.txt",
              file=sys.stderr)
