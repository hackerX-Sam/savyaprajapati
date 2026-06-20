import re

gallery_path = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\gallery.1'

with open(gallery_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the grid columns
old_grid = 'display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 40px; padding: 20px;'
new_grid = 'display: grid; grid-template-columns: repeat(5, 1fr); gap: 40px; padding: 20px;'
content = content.replace(old_grid, new_grid)

# 2. Extract the frames and limit to 25
# Find where the gallery starts
gallery_start = content.find('<div class="custom-photo-gallery"')
gallery_end = content.find('</div>\n                </div>\n            </div>\n        </div>\n    </section>\n</div>', gallery_start)

if gallery_start != -1 and gallery_end != -1:
    gallery_section = content[gallery_start:gallery_end]
    
    # Use regex to find all photo frames
    frames = re.findall(r'<div class="photo-frame".*?</div>\s*</div>', gallery_section, flags=re.DOTALL)
    
    if len(frames) > 25:
        # Reconstruct the section with only 25 frames
        # The section has the opening div
        opening_div = gallery_section[:gallery_section.find('>') + 1]
        
        new_gallery_section = opening_div + '\n'
        for frame in frames[:25]:
            new_gallery_section += '                        ' + frame + '\n'
            
        content = content.replace(gallery_section, new_gallery_section)
        
        with open(gallery_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated grid format to 5x5 and limited to 25 photos.")
    else:
        with open(gallery_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated grid format to 5 columns.")
else:
    print("Could not find gallery section.")
