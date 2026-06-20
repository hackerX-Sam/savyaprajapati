import os
import re

base_dir = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com'

files_to_fix = [
    os.path.join(base_dir, 'gallery', 'index.html'),
    os.path.join(base_dir, 'stories', 'index.html')
]

for filepath in files_to_fix:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Use regex to match href='wp-content/' or href="wp-content/"
        new_content = re.sub(r'href=([\'"])wp-content/', r'href=\1/wp-content/', content)
        new_content = re.sub(r'src=([\'"])wp-content/', r'src=\1/wp-content/', new_content)
        new_content = re.sub(r'href=([\'"])wp-includes/', r'href=\1/wp-includes/', new_content)
        new_content = re.sub(r'src=([\'"])wp-includes/', r'src=\1/wp-includes/', new_content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed asset paths in {os.path.basename(os.path.dirname(filepath))}/index.html")
        else:
            print(f"No changes needed for {os.path.basename(os.path.dirname(filepath))}/index.html")
    else:
        print(f"File not found: {filepath}")
