import os
import re
import shutil

workspace_dir = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com'

# 1. Rename files with @ver= in their names
renamed_count = 0
for root, dirs, files in os.walk(workspace_dir):
    if '.git' in root or '.gemini' in root or 'node_modules' in root:
        continue
    for file in files:
        if '@ver=' in file:
            old_path = os.path.join(root, file)
            new_name = re.sub(r'@ver=[0-9\.]+', '', file)
            new_path = os.path.join(root, new_name)
            
            # If target already exists, just remove the @ver= file to avoid duplicates
            if os.path.exists(new_path):
                os.remove(old_path)
            else:
                os.rename(old_path, new_path)
            renamed_count += 1

print(f"Renamed {renamed_count} files to remove @ver=")

# 2. Update HTML files to remove @ver= from href and src attributes
html_count = 0
for root, dirs, files in os.walk(workspace_dir):
    if '.git' in root or '.gemini' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html') or file.endswith('.1'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                continue
            
            if '@ver=' in content:
                # Remove @ver=number
                new_content = re.sub(r'@ver=[0-9\.]+', '', content)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                html_count += 1

print(f"Updated {html_count} HTML files to remove @ver= from links.")
