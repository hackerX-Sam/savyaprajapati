import re
import random

gallery_path = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\gallery.1'

with open(gallery_path, 'r', encoding='utf-8') as f:
    gallery_content = f.read()

start = gallery_content.find('<div class="custom-gradient-gallery"')
end = gallery_content.find('</section>', start)

if start != -1 and end != -1:
    gallery_section = gallery_content[start:end]
    
    # Extract all background-image URLs
    urls = re.findall(r"background-image:\s*url\('([^']+)'\);", gallery_section)
    
    if len(urls) > 0:
        # Shuffle the URLs randomly
        random.shuffle(urls)
        
        replace_count = 0
        def replacer(match):
            global replace_count
            if replace_count < len(urls):
                new_url = urls[replace_count]
                replace_count += 1
                return f"background-image: url('{new_url}');"
            else:
                return match.group(0)
                
        new_gallery_section = re.sub(
            r"background-image:\s*url\('([^']+)'\);",
            replacer,
            gallery_section
        )
        
        gallery_content = gallery_content[:start] + new_gallery_section + gallery_content[end:]
        
        with open(gallery_path, 'w', encoding='utf-8') as f:
            f.write(gallery_content)
            
        print(f"Successfully shuffled {len(urls)} images in the gallery box.")
    else:
        print("No image URLs found to shuffle.")
else:
    print("Could not find gallery section.")
