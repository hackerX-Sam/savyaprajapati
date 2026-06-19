import os
import re

nav_pattern = re.compile(r'(<nav[^>]*elementor-nav-menu__container[^>]*>)(.*?)(</nav>)', re.DOTALL)

new_items = """
    <li class="menu-item"><a href="/about.1" class="elementor-item">ABOUT</a></li>
    <li class="menu-item"><a href="/stories.1" class="elementor-item">STORIES</a></li>
    <li class="menu-item"><a href="/inspiration/index.html" class="elementor-item">INSPIRATION</a></li>
    <li class="menu-item"><a href="/team.1" class="elementor-item">BEHIND THE LENS</a></li>
    <li class="menu-item"><a href="/contact.1" class="elementor-item">CONTACT</a></li>
"""

def clean_nav(match):
    prefix = match.group(1)
    inner = match.group(2)
    suffix = match.group(3)
    
    ul_open_match = re.search(r'<ul[^>]*class="[^"]*elementor-nav-menu[^"]*"[^>]*>', inner)
    if ul_open_match:
        ul_open = ul_open_match.group(0)
        return f"{prefix}\n\t\t\t\t{ul_open}{new_items}</ul>\t\t\t{suffix}"
    
    return match.group(0)

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return
        
    new_content, count = nav_pattern.subn(clean_nav, content)
    
    if new_content != content:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {filepath} ({count} replacements)")
        except Exception as e:
            print(f"Failed to write {filepath}: {e}")

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.gemini' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html') or file.endswith('.1'):
            filepath = os.path.join(root, file)
            process_file(filepath)
