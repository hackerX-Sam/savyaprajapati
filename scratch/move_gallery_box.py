import re

index_path = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\index.html'
gallery_path = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\gallery.1'

# 1. Read index.html and extract the gallery box
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

gallery_start = index_content.find('<section class="custom-gradient-gallery-section"')
gallery_end = index_content.find('</section>', gallery_start)

if gallery_start != -1 and gallery_end != -1:
    gallery_end += len('</section>')
    gallery_box_html = index_content[gallery_start:gallery_end]
    
    # Remove from index.html
    new_index_content = index_content[:gallery_start] + index_content[gallery_end:]
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_index_content)
    print("Gallery box removed from index.html.")
    
    # 2. Insert into gallery.1
    with open(gallery_path, 'r', encoding='utf-8') as f:
        gallery_content = f.read()
        
    # We want to place it in the blank space. 
    # Previously, there was <div class="custom-photo-gallery" ...>
    target_start = gallery_content.find('<div class="custom-photo-gallery"')
    target_end = gallery_content.find('</div>', target_start)
    
    if target_start != -1 and target_end != -1:
        target_end += len('</div>')
        
        # Replace the custom-photo-gallery div with our new gallery box
        # The new box is a <section>, which is fine inside the elementor widget wrap or container
        new_gallery_content = gallery_content[:target_start] + gallery_box_html + gallery_content[target_end:]
        
        with open(gallery_path, 'w', encoding='utf-8') as f:
            f.write(new_gallery_content)
        print("Gallery box inserted into gallery.1.")
    else:
        print("Could not find insertion point in gallery.1.")
else:
    print("Could not find gallery box in index.html.")
