import os
import re

gallery_path = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\gallery.1'
index_path = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\index.html'

# 1. Extract images
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

image_urls = re.findall(r'https://ik\.imagekit\.io/[^"\'\s>]+(?:jpg|jpeg|png|JPG|JPEG|PNG)', html)
ig_urls = re.findall(r'https://scontent[^"\'\s>]+(?:jpg|jpeg|png)', html)

all_urls = list(set(image_urls + ig_urls))
all_urls = [u.replace('&amp;', '&') for u in all_urls if 'placeholder' not in u]

images_to_use = all_urls[:40]

# 2. Build the Gallery HTML
gallery_html = """
<div data-elementor-type="wp-page" data-elementor-id="999" class="elementor elementor-999" data-elementor-post-type="page">
    <section class="elementor-section elementor-top-section elementor-element elementor-section-boxed elementor-section-height-default elementor-section-height-default" style="margin-top: 150px; margin-bottom: 100px; padding: 20px;">
        <div class="elementor-container elementor-column-gap-default">
            <div class="elementor-column elementor-col-100 elementor-top-column elementor-element">
                <div class="elementor-widget-wrap elementor-element-populated">
                    <div class="elementor-element elementor-widget elementor-widget-heading" style="text-align: center; margin-bottom: 50px;">
                        <h1 class="elementor-heading-title elementor-size-xl" style="font-family: 'Pinyon Script', cursive; font-size: 60px; color: #fff; font-weight: normal;">A Glimpse into Our Love Stories</h1>
                        <p style="color: #bababa; font-size: 18px; margin-top: 10px;">Destination and elopement wedding photography that feels nostalgic and cinematic.</p>
                    </div>
                    
                    <div class="custom-photo-gallery" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 40px; padding: 20px;">
"""

for url in images_to_use:
    gallery_html += f"""
                        <div class="photo-frame" style="background: #e8e8e4; padding: 15px 15px 45px 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); transform: rotate({(id(url) % 5) - 2}deg); transition: transform 0.3s ease, box-shadow 0.3s ease;">
                            <div class="photo-inner" style="width: 100%; aspect-ratio: 4/5; background-image: url('{url}'); background-size: cover; background-position: center; filter: sepia(0.2) contrast(1.1) brightness(0.9);"></div>
                        </div>
    """

gallery_html += """
                    </div>
                </div>
            </div>
        </div>
    </section>
</div>
"""

# Style block for hover effects
gallery_html += """
<style>
.photo-frame:hover {
    transform: scale(1.05) rotate(0deg) !important;
    box-shadow: 0 15px 35px rgba(0,0,0,0.7) !important;
    z-index: 10;
}
.custom-photo-gallery {
    align-items: center;
}
</style>
"""

# 3. Read gallery.1 and replace content
with open(gallery_path, 'r', encoding='utf-8') as f:
    gallery_content = f.read()

# Replace metadata
gallery_content = gallery_content.replace('<title>Gallery - Sabhya Prajapati</title>', '<title>Gallery - Sabhya Prajapati | Nostalgic Photography</title>')
gallery_content = gallery_content.replace('content="Few words about us, and our philosophy.', 'content="View our nostalgic and cinematic gallery of elopements and weddings.')

# Extract everything before the wp-page div and everything from the footer onwards
start_marker = '<div data-elementor-type="wp-page"'
end_marker = '<footer data-elementor-type="footer"'

if start_marker in gallery_content and end_marker in gallery_content:
    parts_before = gallery_content.split(start_marker, 1)
    before_content = parts_before[0]
    
    parts_after = parts_before[1].split(end_marker, 1)
    after_content = end_marker + parts_after[1]
    
    # Write new file
    with open(gallery_path, 'w', encoding='utf-8') as f:
        f.write(before_content + gallery_html + '\n\t\t\t\t' + after_content)
    print("gallery.1 successfully updated.")
else:
    print("Markers not found in gallery.1")
