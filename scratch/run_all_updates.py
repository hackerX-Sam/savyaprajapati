import os
import subprocess

scripts_dir = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\scratch'
blacklist = [
    'build_gallery.py', 'fix_gallery_photos.py', 'box_gallery.py', 'fix_gallery_box.py',
    'revert_home_header.py', 'revert_nav.py', 'undo_header_revert.py', 'update_stories_link.py',
    'fix_ver_links.py'
]

# Get all .py files with their mtime
py_files = []
for file in os.listdir(scripts_dir):
    if file.endswith('.py') and not file.startswith('find_') and not file.startswith('inspect_') and not file.startswith('check_') and not file.startswith('verify_') and file not in blacklist:
        filepath = os.path.join(scripts_dir, file)
        mtime = os.path.getmtime(filepath)
        py_files.append((filepath, mtime))

# Sort by mtime
py_files.sort(key=lambda x: x[1])

# Only run scripts modified after 17-06-2026 18:00:00
# Unix timestamp for 2026-06-17 18:00:00 is approx 1781632800 (let's just filter by a known file's timestamp)
start_time = os.path.getmtime(os.path.join(scripts_dir, 'update_css.py'))

for filepath, mtime in py_files:
    if mtime >= start_time:
        print(f"Running {os.path.basename(filepath)}...")
        subprocess.run(['python', filepath], cwd=r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com')

print("All scripts executed.")
