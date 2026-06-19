import os
import sys

old_string = '<a href="/stories.1" class="elementor-item">STORIES</a>'
new_string = '<a href="https://weddingsbysabhya.pic-time.com/client" target="_blank" class="elementor-item">STORIES</a>'

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return
        
    if old_string in content:
        new_content = content.replace(old_string, new_string)
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated link in {filepath}")
        except Exception as e:
            print(f"Failed to write {filepath}: {e}")

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.gemini' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html') or file.endswith('.1'):
            filepath = os.path.join(root, file)
            process_file(filepath)

print("Finished updating stories link!")
