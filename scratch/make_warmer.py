import os
import glob

# Files to target
css_dir = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\wp-content\uploads\elementor\css"
files = glob.glob(os.path.join(css_dir, "post-1297.css*"))

# Also include index.html just in case we put anything there
files.append(r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\index.html")

old_color = "#F4EFE6"
# Even warmer white
new_color = "#EFE8DF"

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_color in content:
        content = content.replace(old_color, new_color)
        # Also replace lower case if it exists
        content = content.replace(old_color.lower(), new_color)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Color updated to a warmer shade successfully.")
