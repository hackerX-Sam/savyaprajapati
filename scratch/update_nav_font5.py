import os

workspace_dir = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com'
target = '<style>.elementor-nav-menu .elementor-item { font-size: 42px !important; font-weight: bold !important; letter-spacing: 2px !important; }</style>'
replacement = '<style>.elementor-nav-menu .elementor-item { font-size: 60px !important; font-weight: bold !important; letter-spacing: 2px !important; }</style>'

count = 0

for root, dirs, files in os.walk(workspace_dir):
    for file in files:
        if file.endswith('.html') or file.endswith('.1'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if target in content:
                    content = content.replace(target, replacement)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    count += 1
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

print(f"Total files updated with 60px nav font: {count}")
