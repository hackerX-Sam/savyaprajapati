import os
import re

workspace_dir = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com"

# We want to replace menu links for TEAM from about.1 to team.1
# Let's inspect files first and then perform replacement.

extensions = ('.html', '.1')
skip_dirs = {'.git', 'scratch', 'wp-content', 'wp-includes', '.gemini'}

# We look for a pattern like:
# <li class="...menu-item-4470..."><a href="...about.1..." ...>TEAM</a></li>
# Or simply replacing the href when it's in the TEAM menu item.
# Let's find matches first.

# We'll use regex or simple replacements.
# Let's define the targets:
# 1. href="about.1" class="elementor-sub-item"
# 2. href="../about.1" class="elementor-sub-item"

target_sub = 'class="elementor-sub-item"'

print("Scanning files for TEAM menu links...")
files_to_update = []

for root, dirs, files in os.walk(workspace_dir):
    # Skip directories we want to ignore
    dirs[:] = [d for d in dirs if d not in skip_dirs]
    
    for file in files:
        if file.endswith(extensions):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                # Check if it contains elements related to the TEAM menu item
                # Let's see if we find any occurrence of "about.1" and "TEAM" together in menu-item-4470
                # menu-item-4470 is the ID for the TEAM menu item
                matches = re.findall(r'menu-item-4470.*?about\.1', content, re.DOTALL)
                if matches:
                    files_to_update.append((file_path, len(matches)))
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

print(f"Found {len(files_to_update)} files that need updating.")
for fp, count in files_to_update:
    print(f"  {os.path.relpath(fp, workspace_dir)}: {count} matches")

# Let's perform the actual replacements
updated_count = 0
for fp, _ in files_to_update:
    try:
        with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # We replace the href inside the menu-item-4470 block or globally for the sub-item
        # To be safe, let's use a regex replacement specifically targeting menu-item-4470 blocks:
        # Pattern: (class="[^"]*menu-item-4470[^"]*".*?href=")([^"]*about\.1)(".*?>TEAM</a>)
        # We can compile this regex and replace group 2 with the team equivalent.
        
        def replace_link(match):
            prefix = match.group(1)
            link = match.group(2)
            suffix = match.group(3)
            new_link = link.replace('about.1', 'team.1')
            return f"{prefix}{new_link}{suffix}"
            
        pattern = re.compile(r'(class="[^"]*menu-item-4470[^"]*".*?href=")([^"]*about\.1)(".*?>TEAM</a>)', re.DOTALL)
        
        new_content, count = pattern.subn(replace_link, content)
        
        if count > 0:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {os.path.relpath(fp, workspace_dir)}: {count} replacements.")
            updated_count += 1
        else:
            print(f"No replacements made in {os.path.relpath(fp, workspace_dir)} (regex did not match fully).")
    except Exception as e:
        print(f"Error updating {fp}: {e}")

print(f"Successfully updated {updated_count} files.")
