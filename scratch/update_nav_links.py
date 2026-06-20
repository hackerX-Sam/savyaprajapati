import os

workspace_dir = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com'
targets = [
    '<a href="javascript:void(0);" class="elementor-item">GALLERY</a>',
    '<a href="#" class="elementor-item">GALLERY</a>'
]
replacement = '<a href="/gallery" class="elementor-item">GALLERY</a>'

count = 0

for root, dirs, files in os.walk(workspace_dir):
    for file in files:
        if file.endswith('.html') or file.endswith('.1') or file.endswith('.json') or file.endswith('.txt'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                updated = False
                for target in targets:
                    if target in content:
                        content = content.replace(target, replacement)
                        updated = True
                
                # Also check menu_structure.json if it exists
                if file == 'menu_structure.json' or file == 'nav_menu.txt':
                     if 'javascript:void(0);' in content and 'GALLERY' in content:
                         content = content.replace('javascript:void(0);', '/gallery')
                         updated = True

                if updated:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    count += 1
                    print(f"Updated: {filepath}")
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

print(f"Total files updated: {count}")
