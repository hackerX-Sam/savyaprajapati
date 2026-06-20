import re
import os

gallery_path = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\gallery.1'

with open(gallery_path, 'r', encoding='utf-8') as f:
    content = f.read()

gallery_start = content.find('<div class="custom-photo-gallery"')
gallery_end = content.find('</div>\n                </div>\n            </div>\n        </div>\n    </section>\n</div>', gallery_start)

if gallery_start != -1 and gallery_end != -1:
    gallery_section = content[gallery_start:gallery_end]
    frames = re.findall(r'<div class="photo-frame".*?</div>\s*</div>', gallery_section, flags=re.DOTALL)
    
    print(f"Current frames count: {len(frames)}")
    
    if len(frames) != 25:
        if len(frames) < 25:
            # duplicate some frames to reach 25
            diff = 25 - len(frames)
            for i in range(diff):
                frames.append(frames[i % len(frames)])
        else:
            # truncate to 25
            frames = frames[:25]
            
        opening_div = gallery_section[:gallery_section.find('>') + 1]
        new_gallery_section = opening_div + '\n'
        for frame in frames:
            new_gallery_section += '                        ' + frame + '\n'
            
        content = content.replace(gallery_section, new_gallery_section)
        
        with open(gallery_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated frames to exactly 25.")
    else:
        print("Already exactly 25 frames.")
else:
    print("Could not find gallery section.")
