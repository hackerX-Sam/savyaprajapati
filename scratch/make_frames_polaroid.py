import re

gallery_path = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\gallery.1'

with open(gallery_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Make the container wider so frames are bigger
content = content.replace(
    '<div class="elementor-container elementor-column-gap-default">',
    '<div class="elementor-container elementor-column-gap-default" style="max-width: 1600px; width: 95%;">',
    1 # Only replace the first occurrence (which might not be the right one, let's be more specific)
)
# Let's revert and do a more specific replacement for the container
content = content.replace('<div class="elementor-container elementor-column-gap-default" style="max-width: 1600px; width: 95%;">', '<div class="elementor-container elementor-column-gap-default">')

# The correct container is right after the gallery section opening
section_str = 'style="margin-top: 250px; margin-bottom: 100px; padding: 20px;">\n        <div class="elementor-container elementor-column-gap-default">'
new_section_str = 'style="margin-top: 250px; margin-bottom: 100px; padding: 20px;">\n        <div class="elementor-container elementor-column-gap-default" style="max-width: 1600px; width: 95%;">'
content = content.replace(section_str, new_section_str)

# 2. Update the photo frames
# We need to replace:
# background: #e8e8e4; padding: 15px 15px 45px 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); transform: rotate(Xdeg); transition: transform 0.3s ease, box-shadow 0.3s ease;
# with:
# background: #fdfbf7; padding: 20px 20px 80px 20px; box-shadow: 0 12px 30px rgba(0,0,0,0.6); transform: rotate(Xdeg); transition: transform 0.3s ease, box-shadow 0.3s ease; border: 1px solid #dcd9d0;

def frame_replacer(match):
    rotation = match.group(1)
    return f'style="background: #fdfbf7; padding: 20px 20px 80px 20px; box-shadow: 0 12px 35px rgba(0,0,0,0.7); border: 1px solid #e0dcd2; transform: rotate({rotation}deg); transition: transform 0.3s ease, box-shadow 0.3s ease;"'

content = re.sub(
    r'style="background: #e8e8e4; padding: 15px 15px 45px 15px; box-shadow: 0 10px 25px rgba\(0,0,0,0\.5\); transform: rotate\(([-]?\d)deg\); transition: transform 0\.3s ease, box-shadow 0\.3s ease;"',
    frame_replacer,
    content
)

# 3. Update the inner photo to be square (polaroid) and have a border
content = content.replace('aspect-ratio: 4/5;', 'aspect-ratio: 1/1; border: 1px solid #222;')

# 4. Also increase the grid gap to allow breathing room for the bigger frames
content = content.replace('gap: 40px;', 'gap: 50px;')

with open(gallery_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Gallery updated to be bigger and more polaroid-like.")
