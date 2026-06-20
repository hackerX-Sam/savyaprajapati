import re

gallery_path = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\gallery.1'

with open(gallery_path, 'r', encoding='utf-8') as f:
    content = f.read()

gallery_start = content.find('<div class="custom-photo-gallery"')
gallery_end = content.find('</div>\n                </div>\n            </div>\n        </div>\n    </section>\n</div>', gallery_start)

if gallery_start != -1 and gallery_end != -1:
    gallery_section = content[gallery_start:gallery_end]
    
    # We want to keep the opening div of custom-photo-gallery but remove everything inside it.
    opening_div = gallery_section[:gallery_section.find('>') + 1]
    
    new_gallery_section = opening_div + '\n                    ' # Empty inside
    
    content = content.replace(gallery_section, new_gallery_section)
    
    with open(gallery_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Gallery frames removed successfully.")
else:
    print("Could not find gallery section.")
