import os

old_url = 'https://ik.imagekit.io/logicsync/iageyyhrjr.png'
new_url = 'wp-content/uploads/lotus_white.png'

for filepath in ['c:/Users/samir/OneDrive/Desktop/confidential/ninaanddarek.com/team.1', 'c:/Users/samir/OneDrive/Desktop/confidential/ninaanddarek.com/team/index.html']:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_url in content:
        content = content.replace(old_url, new_url)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
