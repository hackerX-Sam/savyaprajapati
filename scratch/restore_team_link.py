import os

old_string = '<li class="menu-item"><a href="javascript:void(0);" class="elementor-sub-item" style="color: #000 !important; font-weight: 500;">TEAM</a></li>'
new_string = '<li class="menu-item"><a href="/team.1" class="elementor-sub-item" style="color: #000 !important; font-weight: 500;">TEAM</a></li>'

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
