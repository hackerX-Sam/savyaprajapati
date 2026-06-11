import os
import re

workspace_dir = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com"
extensions = ('.html', '.1')
skip_dirs = {'.git', 'scratch', 'wp-content', 'wp-includes', '.gemini'}

print("Scanning files for 'FOR PHOTOGRAPHERS' menu links...")
files_to_update = []

target = "FOR PHOTOGRAPHERS"
replacement = "BEHIND THE LENS"

for root, dirs, files in os.walk(workspace_dir):
    # Skip directories we want to ignore
    dirs[:] = [d for d in dirs if d not in skip_dirs]
    
    for file in files:
        if file.endswith(extensions):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                # Check for ">FOR PHOTOGRAPHERS</a>"
                # This ensures we only change the menu item anchor tag texts
                matches = list(re.finditer(rf'>{target}</a>', content))
                if matches:
                    files_to_update.append((file_path, len(matches)))
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

print(f"Found {len(files_to_update)} files that need updating.")
for fp, count in files_to_update:
    print(f"  {os.path.relpath(fp, workspace_dir)}: {count} matches")

# Perform the replacements
updated_count = 0
for fp, _ in files_to_update:
    try:
        with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        new_content = content.replace(f">{target}</a>", f">{replacement}</a>")
        
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.relpath(fp, workspace_dir)}")
        updated_count += 1
    except Exception as e:
        print(f"Error updating {fp}: {e}")

print(f"Successfully updated {updated_count} files.")
