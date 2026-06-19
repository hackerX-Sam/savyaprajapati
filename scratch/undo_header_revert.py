import os
workspace_dir = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com'
target = 'body:not(.home) header[data-elementor-type="header"] {'
replacement = 'header[data-elementor-type="header"] {'
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
            except:
                pass
print(f"Re-applied header CSS fix to {count} files")
