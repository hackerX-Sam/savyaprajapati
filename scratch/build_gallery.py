import os
import re

file_path = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Extract images
image_urls = re.findall(r'https://ik\.imagekit\.io/[^"\'\s>]+(?:jpg|jpeg|png|JPG|JPEG|PNG)', html)
# Also get instagram images if we need more
ig_urls = re.findall(r'https://scontent[^"\'\s>]+(?:jpg|jpeg|png)', html)

all_urls = list(set(image_urls + ig_urls))
# Clean up any escaped chars
all_urls = [u.replace('&amp;', '&') for u in all_urls if 'placeholder' not in u]

# We need 40 images for a 10x4 grid
images_to_use = []
while len(images_to_use) < 40 and all_urls:
    images_to_use.extend(all_urls)
images_to_use = images_to_use[:40]

# 2. Build the Gallery HTML
gallery_html = """
<section class="custom-gradient-gallery-section" style="width: 100%; margin: 60px 0; overflow: hidden;">
    <div class="custom-gradient-gallery" style="display: grid; grid-template-columns: repeat(10, 1fr); gap: 0; width: 100%;">
"""

for i, url in enumerate(images_to_use):
    # Determine which column this is (0 to 9)
    col = i % 10
    
    # Apply CSS filters to enforce the gradient look requested
    # Col 0, 1: Warm / Reddish brown
    # Col 2, 3, 4: B&W / Dark / Contrast
    # Col 5, 6: Cool / Grey / Light
    # Col 7, 8, 9: Dark / Moody
    
    filter_css = ""
    if col in [0]:
        filter_css = "sepia(0.6) hue-rotate(-20deg) saturate(1.5) brightness(0.8)"
    elif col in [1]:
        filter_css = "sepia(0.3) hue-rotate(-10deg) brightness(1.1)"
    elif col in [2]:
        filter_css = "sepia(0.8) hue-rotate(-30deg) saturate(1.2) brightness(0.6)"
    elif col in [3, 4]:
        filter_css = "grayscale(1) contrast(1.2)"
    elif col in [5]:
        filter_css = "sepia(0.2) hue-rotate(10deg) saturate(0.8) brightness(0.9)"
    elif col in [6]:
        filter_css = "sepia(0.4) hue-rotate(-15deg) brightness(1.05)"
    elif col in [7]:
        filter_css = "grayscale(0.6) brightness(0.7) contrast(1.1)"
    elif col in [8, 9]:
        filter_css = "grayscale(0.8) brightness(0.5) contrast(1.2)"

    gallery_html += f"""
        <div class="gallery-item" style="aspect-ratio: 4/5; background-image: url('{url}'); background-size: cover; background-position: center; filter: {filter_css}; transition: filter 0.3s ease;"></div>
    """

gallery_html += """
    </div>
</section>
"""

# Insert after the "Let's connect!" button section
# The section is <section class="elementor-section ... elementor-element-d2fd4d2" ... </section>
# We will find the end of this section and insert our gallery.

parts = html.split('data-id="d2fd4d2"')
if len(parts) == 2:
    # Find the closing </section> for this part
    end_of_section = parts[1].find('</section>') + len('</section>')
    new_html = parts[0] + 'data-id="d2fd4d2"' + parts[1][:end_of_section] + gallery_html + parts[1][end_of_section:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Gallery successfully added after Let's connect.")
else:
    print("Could not find the Let's connect section.")
