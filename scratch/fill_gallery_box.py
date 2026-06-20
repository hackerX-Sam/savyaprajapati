import re

index_path = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\index.html'
gallery_path = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\gallery.1'

# 1. Extract all valid images from index.html
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

image_urls = re.findall(r'https://ik\.imagekit\.io/[^"\'\s>]+(?:jpg|jpeg|png|JPG|JPEG|PNG)', html)
ig_urls = re.findall(r'https://scontent[^"\'\s>]+(?:jpg|jpeg|png)', html)

all_urls = list(set(image_urls + ig_urls))
# Filter out placeholders or any broken looking URLs
valid_urls = [u.replace('&amp;', '&') for u in all_urls if 'placeholder' not in u and len(u) > 10]

# We want a multiple of 10 to fill the grid perfectly. E.g. 40 images.
# If we have less than 40, we duplicate some to reach exactly 40.
target_count = 40
images_to_use = []
while len(images_to_use) < target_count:
    for url in valid_urls:
        if len(images_to_use) < target_count:
            images_to_use.append(url)
        else:
            break

# 2. Rebuild the gallery grid HTML
grid_html = ""
for url in images_to_use:
    grid_html += f"""
        <div class="gallery-cell" style="width: 100%; aspect-ratio: 4/5; overflow: hidden; position: relative;">
            <div style="width: 100%; height: 100%; background-image: url('{url}'); background-size: cover; background-position: center; filter: sepia(0.3) contrast(1.1) brightness(0.9); transition: transform 0.5s ease;"></div>
        </div>
    """

# 3. Replace in gallery.1
with open(gallery_path, 'r', encoding='utf-8') as f:
    gallery_content = f.read()

# Find the custom-gradient-gallery div
grid_start = gallery_content.find('<div class="custom-gradient-gallery"')
if grid_start != -1:
    # Find the end of this div. We can just use the closing </section> since we know it's inside the section
    section_end = gallery_content.find('</section>', grid_start)
    if section_end != -1:
        # Reconstruct the section inner content
        grid_opening = gallery_content[grid_start:gallery_content.find('>', grid_start) + 1]
        
        new_grid_block = grid_opening + grid_html + '\n    </div>'
        
        # We need to replace from grid_start to the end of the div
        # To be safe, let's just replace everything inside the section
        section_start = gallery_content.rfind('<section class="custom-gradient-gallery-section"', 0, grid_start)
        old_section = gallery_content[section_start:section_end + len('</section>')]
        
        # The section has the gradient overlays as well. Let's see what was originally there.
        # It had <div class="gradient-overlay left"></div> etc.
        # Let's just recreate the whole section
        new_section = f"""<section class="custom-gradient-gallery-section" style="width: 100%; margin: 60px 0; overflow: hidden; display: flex; justify-content: center; padding: 0 20px;">
    {new_grid_block}
</section>"""
        
        gallery_content = gallery_content.replace(old_section, new_section)
        
        # Re-add hover styles if they were lost
        if ".gallery-cell div:hover" not in gallery_content:
            style_block = """
<style>
.gallery-cell div:hover {
    transform: scale(1.05);
    filter: sepia(0) contrast(1.2) brightness(1.1) !important;
}
</style>
"""
            gallery_content += style_block

        with open(gallery_path, 'w', encoding='utf-8') as f:
            f.write(gallery_content)
        print(f"Gallery updated with exactly {target_count} images.")
    else:
        print("Could not find section end.")
else:
    print("Could not find custom-gradient-gallery div.")
