#!/usr/bin/env python3
import sys
import os
import yaml
import tomllib

def extract_title(md_file):
    """Extract title from YAML front matter"""
    with open(md_file, 'r') as f:
        content = f.read()
        # Find YAML front matter between --- markers
        if content.startswith('---'):
            end = content.find('---', 3)
            if end != -1:
                front_matter = content[3:end]
                try:
                    metadata = yaml.safe_load(front_matter)
                    return metadata.get('title', os.path.basename(md_file))
                except yaml.YAMLError:
                    return os.path.basename(md_file)
    return os.path.basename(md_file)

def generate_index(info, md_files):
    """Generate HTML index page with links to slides and PDFs"""
    title = info["title"]
    institution = info["institution"]
    author = info["author"]

    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 2em auto; padding: 0 1em; }}
        h1 {{ color: #333; }}
        ol {{ line-height: 1.6; }}
        a {{ color: #0066cc; text-decoration: none;}}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <h3>{author}</h3>
    <h3>{institution}</h3>
    <ol>
"""
    
    for md_file in sorted(md_files):
        basename = os.path.basename(md_file)[:-3]  # Remove .md extension
        title = extract_title(md_file)
        html += f'        <li>{title} '
        html += f'[<a href="reveal/{basename}.html">HTML</a>] '
        html += f'[<a href="beamer/{basename}.pdf">PDF</a>]'
        html += '</li>\n'
    
    html += """    </ol>
</body>
</html>"""
    
    return html

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: script.py output_file markdown_files...")
        sys.exit(1)
    
    with open("_config.toml", "rb") as f:
        info = tomllib.load(f)

    output_file = sys.argv[1]
    md_files = sys.argv[2:]
    
    with open(output_file, 'w') as f:
        f.write(generate_index(info, md_files))