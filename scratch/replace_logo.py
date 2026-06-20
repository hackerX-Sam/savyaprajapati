import re

gallery_path = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\gallery.1'

with open(gallery_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We only care about the custom-gradient-gallery section
start = content.find('<div class="custom-gradient-gallery"')
end = content.find('</section>', start)

if start != -1 and end != -1:
    gallery_section = content[start:end]
    
    # Replacement photo (a nice one from the list)
    replacement_url = 'https://ik.imagekit.io/logicsync/ce247119-0ef3-483f-90f3-a0275ec101d1.jpg'
    
    # We will replace all .png URLs which are likely logos/ChatGPT generated placeholders
    # ChatGPT Image...png
    new_gallery_section = re.sub(
        r'https://ik\.imagekit\.io/logicsync/ChatGPT%20Image[^"\']*?\.png',
        replacement_url,
        gallery_section
    )
    
    content = content[:start] + new_gallery_section + content[end:]
    
    with open(gallery_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Logo/PNG images successfully removed and replaced with a photo.")
else:
    print("Could not find gallery section.")
