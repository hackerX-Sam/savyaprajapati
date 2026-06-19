import os

replacements = {
    '<li class="menu-item"><a href="/about.1" class="elementor-item">about</a></li>': '<li class="menu-item"><a href="/about.1" class="elementor-item">ABOUT</a></li>',
    '<li class="menu-item"><a href="/stories.1" class="elementor-item">stories</a></li>': '<li class="menu-item"><a href="/stories.1" class="elementor-item">STORIES</a></li>',
    '<li class="menu-item"><a href="/inspiration/index.html" class="elementor-item">inspiration</a></li>': '<li class="menu-item"><a href="/inspiration/index.html" class="elementor-item">INSPIRATION</a></li>',
    '<li class="menu-item"><a href="/team.1" class="elementor-item">behind the lens</a></li>': '<li class="menu-item"><a href="/team.1" class="elementor-item">BEHIND THE LENS</a></li>',
    '<li class="menu-item"><a href="/contact.1" class="elementor-item">contact</a></li>': '<li class="menu-item"><a href="/contact.1" class="elementor-item">CONTACT</a></li>'
}

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return
        
    new_content = content
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)
    
    if new_content != content:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
        except Exception as e:
            print(f"Failed to write {filepath}: {e}")

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.gemini' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html') or file.endswith('.1'):
            filepath = os.path.join(root, file)
            process_file(filepath)
