import re

gallery_path = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\gallery.1'

new_urls = [
    "https://ik.imagekit.io/logicsync/ChatGPT%20Image%20Jun%206,%202026,%2012_14_45%20AM.png?updatedAt=1780685171693",
    "https://ik.imagekit.io/logicsync/ChatGPT%20Image%20Jun%206,%202026,%2012_24_52%20AM.png?updatedAt=1780685743756",
    "https://ik.imagekit.io/logicsync/_DSC3476%20(1).jpg?updatedAt=1780925338185",
    "https://ik.imagekit.io/logicsync/IMG_2878.JPG",
    "https://ik.imagekit.io/logicsync/1.jpg"
]

with open(gallery_path, 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('<div class="custom-gradient-gallery"')
end = content.find('</section>', start)

if start != -1 and end != -1:
    gallery_section = content[start:end]
    
    # We will replace the first 5 background-image urls found in the gallery section
    # Let's use a function to keep state of how many we replaced
    replace_count = 0
    def replacer(match):
        global replace_count
        if replace_count < len(new_urls):
            new_url = new_urls[replace_count]
            replace_count += 1
            return f"background-image: url('{new_url}');"
        else:
            return match.group(0) # don't change
            
    new_gallery_section = re.sub(
        r"background-image:\s*url\('([^']+)'\);",
        replacer,
        gallery_section
    )
    
    content = content[:start] + new_gallery_section + content[end:]
    
    with open(gallery_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully inserted {replace_count} new images.")
else:
    print("Could not find gallery section.")
