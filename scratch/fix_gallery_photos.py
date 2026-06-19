import os
import re

file_path = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Hardcoded array of known good photos from the site
good_photos = [
    "https://ik.imagekit.io/logicsync/tr:w-2000/photo%202.JPG",
    "https://ik.imagekit.io/logicsync/IMG.112.jpg?updatedAt=1780925347803",
    "https://ik.imagekit.io/logicsync/0eba3533-9e9f-4609-b167-5d137b160e3e.jpg",
    "https://ik.imagekit.io/logicsync/ce247119-0ef3-483f-90f3-a0275ec101d1.jpg?updatedAt=1780925325760",
    "https://ik.imagekit.io/logicsync/tr:w-1500/photo%203.JPG",
    "https://ik.imagekit.io/logicsync/tr:w-1500/photo%204.JPG"
]

images_to_use = []
while len(images_to_use) < 40:
    images_to_use.extend(good_photos)
images_to_use = images_to_use[:40]

gallery_html = """
<section class="custom-gradient-gallery-section" style="width: 100%; margin: 60px 0; overflow: hidden;">
    <div class="custom-gradient-gallery" style="display: grid; grid-template-columns: repeat(10, 1fr); gap: 0; width: 100%;">
"""

for i, url in enumerate(images_to_use):
    col = i % 10
    
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

# Replace the existing custom-gradient-gallery-section
pattern = re.compile(r'<section class="custom-gradient-gallery-section".*?</section>', re.DOTALL)
if pattern.search(html):
    html = pattern.sub(gallery_html, html)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Gallery fixed with non-empty photos.")
else:
    print("Could not find the custom gallery section.")
