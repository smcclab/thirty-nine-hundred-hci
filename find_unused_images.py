#!/usr/bin/env python3
"""
Find images in lectures/img that are not referenced in any markdown file.
"""

import os
import re
from pathlib import Path

def find_markdown_files(lectures_dir):
    """Find all markdown files in the lectures directory."""
    return list(Path(lectures_dir).glob("*.md"))

def find_images(img_dir):
    """Find all image files in the img directory."""
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.bmp'}
    images = []
    
    img_path = Path(img_dir)
    if img_path.exists():
        for file in img_path.iterdir():
            if file.is_file() and file.suffix.lower() in image_extensions:
                images.append(file)
    
    return images

def extract_image_references(markdown_file):
    """Extract all image references from a markdown file."""
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()

    references = set()

    # Markdown image syntax: ![alt](path)
    references.update(re.findall(r'!\[.*?\]\(([^)]+)\)', content))

    # HTML img tags: <img src="path">
    references.update(re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content))

    # YAML frontmatter: data-background-image: img/filename (no quotes, outside comments)
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith('<!--'):
            continue
        m = re.search(r'data-background-image:\s*(\S+)', stripped)
        if m:
            references.add(m.group(1))

    # Pandoc heading attribute: background-image="img/filename"
    references.update(re.findall(r'background-image=["\']([^"\']+)["\']', content))

    return references

def normalize_path(ref_path, base_dir):
    """Normalize a reference path to match actual file paths."""
    # Remove any leading ./
    ref_path = ref_path.lstrip('./')
    img_path = Path(ref_path)
    return img_path.name

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Find (and optionally delete) unused images.')
    parser.add_argument('--delete', action='store_true', help='Delete unused images')
    args = parser.parse_args()

    lectures_dir = "lectures"
    img_dir = os.path.join(lectures_dir, "img")

    md_files = find_markdown_files(lectures_dir)
    images = find_images(img_dir)

    if not md_files or not images:
        print("No markdown files or images found.")
        return

    print(f"Found {len(md_files)} markdown files")
    print(f"Found {len(images)} images")

    all_references = set()
    for md_file in md_files:
        refs = extract_image_references(md_file)
        normalized_refs = {normalize_path(ref, lectures_dir) for ref in refs}
        all_references.update(normalized_refs)

    print(f"Found {len(all_references)} unique image references\n")

    unused_images = [img for img in images if img.name not in all_references]

    if not unused_images:
        print("No unused images found.")
        return

    print(f"Found {len(unused_images)} unused images:")
    for img in sorted(unused_images):
        print(f"  {img}")

    if args.delete:
        for img in unused_images:
            img.unlink()
            print(f"Deleted: {img}")
        print(f"\nDeleted {len(unused_images)} unused images.")
    else:
        print("\nRun with --delete to remove them.")

if __name__ == "__main__":
    main()
