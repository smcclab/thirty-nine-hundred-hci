"""Read-only reconnaissance of the Canvas course.

Prints the front page, modules (+ items), pages, folders and files so we can see
how the course is currently organised and match that structure when pushing the
2026 materials. Makes no changes.

Usage:
    python canvas/inspect_course.py
"""

import textwrap

from canvas_api import Canvas, course_id


def main():
    c = Canvas()
    cid = course_id()

    course, _ = c.get(f"courses/{cid}", params={"include[]": "storage_quota_used_mb"})
    print(f"# Course {cid}: {course.get('name')}")
    print(f"  code={course.get('course_code')}  "
          f"default_view={course.get('default_view')}  "
          f"front_page_set={bool(course.get('front_page'))}")

    # A full lecture push is ~119 MB, so report headroom. This also answers
    # whether superseded files in overwrite replacement chains keep consuming
    # quota: run it before and after a push and compare `used`.
    quota = course.get("storage_quota_mb")
    used = course.get("storage_quota_used_mb")
    if quota is not None and used is not None:
        print(f"  storage: {used:.0f} / {quota:.0f} MB used "
              f"({quota - used:.0f} MB free)")
    elif quota is not None:
        print(f"  storage quota: {quota:.0f} MB (usage not reported)")
    print()

    # Front page
    try:
        fp, _ = c.get(f"courses/{cid}/front_page")
        print("## Front page")
        print(f"  title: {fp.get('title')}  url: {fp.get('url')}")
        body = fp.get("body") or ""
        print(textwrap.indent(textwrap.shorten(body, 1500), "    "))
        print()
    except SystemExit:
        print("## Front page: none\n")

    # Modules + items
    modules = c.get_all(f"courses/{cid}/modules", params={"include[]": "items"})
    print(f"## Modules ({len(modules)})")
    for m in modules:
        print(f"  [{m['id']}] {m['name']}  (items={m.get('items_count')})")
        for it in m.get("items", []) or []:
            extra = it.get("content_id", "")
            print(f"      - ({it['type']}) {it.get('title')}  "
                  f"content_id={extra}  url={it.get('html_url','')}")
    print()

    # Pages
    pages = c.get_all(f"courses/{cid}/pages")
    print(f"## Pages ({len(pages)})")
    for p in pages:
        print(f"  - {p.get('title')}  (url={p.get('url')}, "
              f"published={p.get('published')})")
    print()

    # Folders
    folders = c.get_all(f"courses/{cid}/folders")
    print(f"## Folders ({len(folders)})")
    for f in folders:
        print(f"  [{f['id']}] {f.get('full_name')}  (files={f.get('files_count')})")
    print()

    # Files
    files = c.get_all(f"courses/{cid}/files", params={"sort": "folder_id"})
    print(f"## Files ({len(files)})")
    for f in files:
        size_mb = (f.get("size") or 0) / 1_048_576
        print(f"  [{f['id']}] {f.get('display_name')}  "
              f"({f.get('content-type')}, {size_mb:.1f} MB, folder_id={f.get('folder_id')})")


if __name__ == "__main__":
    main()
