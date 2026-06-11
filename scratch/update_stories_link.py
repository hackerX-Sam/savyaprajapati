import os
import re

workspace_dir = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com"
extensions = ('.html', '.1')
skip_dirs = {'.git', 'scratch', 'wp-content', 'wp-includes', '.gemini'}

print("Scanning files for STORIES menu item...")
files_to_update = []

# Regex pattern matching menu-item-95 list item blocks and capturing prefix, href, and suffix
# Example: <li class="...menu-item-95..."><a href="stories.1" class="elementor-item">STORIES</a>
pattern = re.compile(
    r'(<li\s+class="[^"]*menu-item-95[^"]*".*?href=")([^"]*)(".*?>STORIES</a>)',
    re.DOTALL
)

new_url = "https://weddingsbysabhya.pic-time.com/client"

for root, dirs, files in os.walk(workspace_dir):
    # Skip directories we want to ignore
    dirs[:] = [d for d in dirs if d not in skip_dirs]
    
    for file in files:
        if file.endswith(extensions):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                matches = list(pattern.finditer(content))
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
        
        # We replace the link and also ensure we add target="_blank" rel="noopener noreferrer" for clean external navigation
        # Let's replace the matches using a replacement function
        def replace_link(match):
            prefix = match.group(1)
            old_href = match.group(2)
            suffix = match.group(3)
            
            # Add target="_blank" to suffix if it isn't already there
            new_suffix = suffix
            if 'target="_blank"' not in suffix:
                # Insert target="_blank" rel="noopener noreferrer" inside the anchor tag
                # Anchor tag starts with the closing quote of href (which is in match group 3, as the first character)
                # Let's insert it right after the first double quote
                new_suffix = suffix[0] + ' target="_blank" rel="noopener noreferrer"' + suffix[1:]
                
            return f"{prefix}{new_url}{new_suffix}"
            
        new_content, count = pattern.subn(replace_link, content)
        
        if count > 0:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {os.path.relpath(fp, workspace_dir)}: {count} replacements.")
            updated_count += 1
        else:
            print(f"No replacements made in {os.path.relpath(fp, workspace_dir)}")
    except Exception as e:
        print(f"Error updating {fp}: {e}")

print(f"Successfully updated {updated_count} files.")
