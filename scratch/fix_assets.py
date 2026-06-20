import os
import glob

base_dir = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com'

files_to_fix = [
    os.path.join(base_dir, 'gallery', 'index.html'),
    os.path.join(base_dir, 'stories', 'index.html')
]

for filepath in files_to_fix:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Fix relative asset links by making them absolute to the root
        replacements = [
            ('href="wp-content/', 'href="/wp-content/'),
            ('src="wp-content/', 'src="/wp-content/'),
            ('href="wp-includes/', 'href="/wp-includes/'),
            ('src="wp-includes/', 'src="/wp-includes/')
        ]
        
        for old, new in replacements:
            content = content.replace(old, new)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed asset paths in {os.path.basename(os.path.dirname(filepath))}/index.html")
    else:
        print(f"File not found: {filepath}")
