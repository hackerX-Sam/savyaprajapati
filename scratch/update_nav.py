import os
import re

new_items = """
    <li class="menu-item"><a href="/about.1" class="elementor-item">about</a></li>
    <li class="menu-item"><a href="/stories.1" class="elementor-item">stories</a></li>
    <li class="menu-item"><a href="/inspiration/index.html" class="elementor-item">inspiration</a></li>
    <li class="menu-item"><a href="/team.1" class="elementor-item">behind the lens</a></li>
    <li class="menu-item"><a href="/contact.1" class="elementor-item">contact</a></li>
"""

# The regex matches <ul ... class="...elementor-nav-menu...">...</ul>
ul_pattern = re.compile(r'(<ul[^>]*class="[^"]*elementor-nav-menu[^"]*"[^>]*>)(.*?)(</ul>)', re.DOTALL)

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Failed to read {filepath}: {e}")
        return
        
    new_content, count = ul_pattern.subn(rf'\g<1>{new_items}\g<3>', content)
    
    if count > 0:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath} ({count} replacements)")
        except Exception as e:
            print(f"Failed to write {filepath}: {e}")

# Process all files recursively
for root, dirs, files in os.walk('.'):
    # Exclude unwanted directories
    if '.git' in root or '.gemini' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html') or file.endswith('.1'):
            filepath = os.path.join(root, file)
            process_file(filepath)
