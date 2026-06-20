import re

index_path = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\index.html'
gallery_path = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\gallery.1'

# The 5 URLs the user explicitly requested:
user_urls = [
    "https://ik.imagekit.io/logicsync/ChatGPT%20Image%20Jun%206,%202026,%2012_14_45%20AM.png?updatedAt=1780685171693",
    "https://ik.imagekit.io/logicsync/ChatGPT%20Image%20Jun%206,%202026,%2012_24_52%20AM.png?updatedAt=1780685743756",
    "https://ik.imagekit.io/logicsync/_DSC3476%20(1).jpg?updatedAt=1780925338185",
    "https://ik.imagekit.io/logicsync/IMG_2878.JPG",
    "https://ik.imagekit.io/logicsync/1.jpg"
]

# 1. Extract valid ImageKit URLs from index.html
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# We only use ImageKit URLs because Instagram URLs expire or are truncated
image_urls = re.findall(r'https://ik\.imagekit\.io/[^"\'\s>]+(?:jpg|jpeg|png|JPG|JPEG|PNG)', html)

all_urls = list(set(image_urls))
valid_urls = [u.replace('&amp;', '&') for u in all_urls if 'placeholder' not in u and 'ChatGPT' not in u]

# We need 40 images in total. 5 from the user, 35 from valid_urls
target_count = 40
images_to_use = user_urls.copy()

while len(images_to_use) < target_count:
    for url in valid_urls:
        if len(images_to_use) < target_count:
            images_to_use.append(url)
        else:
            break

# 2. Update gallery.1
with open(gallery_path, 'r', encoding='utf-8') as f:
    gallery_content = f.read()

start = gallery_content.find('<div class="custom-gradient-gallery"')
end = gallery_content.find('</section>', start)

if start != -1 and end != -1:
    gallery_section = gallery_content[start:end]
    
    replace_count = 0
    def replacer(match):
        global replace_count
        if replace_count < len(images_to_use):
            new_url = images_to_use[replace_count]
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
    print(f"Replaced {replace_count} images successfully using safe ImageKit URLs.")
else:
    print("Could not find gallery section.")
