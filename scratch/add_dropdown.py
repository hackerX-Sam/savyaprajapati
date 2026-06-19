import os

old_string = '<li class="menu-item"><a href="/team.1" class="elementor-item">BEHIND THE LENS</a></li>'

new_string = '''<li class="menu-item menu-item-has-children"><a href="javascript:void(0);" class="elementor-item">BEHIND THE LENS</a>
<ul class="sub-menu elementor-nav-menu--dropdown" style="background: #1a1a1a; padding: 10px; margin-top: 10px;">
<li class="menu-item"><a href="javascript:void(0);" class="elementor-sub-item">TEAM</a></li>
<li class="menu-item"><a href="javascript:void(0);" class="elementor-sub-item">TESTIMONIAL</a></li>
</ul>
</li>'''

# Removing newlines from new_string to keep it compact or just replacing it as is.
new_string = new_string.replace('\n', '')

count = 0
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.gemini' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html') or file.endswith('.1'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except:
                continue
            
            if old_string in content:
                new_content = content.replace(old_string, new_string)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                print(f"Updated {filepath}")

print(f"Finished updating {count} files.")
