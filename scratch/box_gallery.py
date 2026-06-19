import os
import re

file_path = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

pattern = re.compile(r'<section class="custom-gradient-gallery-section".*?</section>', re.DOTALL)

match = pattern.search(html)
if match:
    section_html = match.group(0)
    
    # Replace the opening tags to add the wrapper box
    old_start = '<section class="custom-gradient-gallery-section" style="width: 100%; margin: 60px 0; overflow: hidden;">\n    <div class="custom-gradient-gallery" style="display: grid; grid-template-columns: repeat(10, 1fr); gap: 0; width: 100%;">'
    new_start = '<section class="custom-gradient-gallery-section" style="width: 100%; margin: 60px 0; overflow: hidden; display: flex; justify-content: center; padding: 0 20px;">\n    <div class="custom-gradient-gallery-wrapper" style="max-width: 900px; width: 100%; padding: 25px; background: #ffffff; border: 1px solid #e0ddd5; box-shadow: 0 10px 40px rgba(0,0,0,0.08); border-radius: 8px;">\n        <div class="custom-gradient-gallery" style="display: grid; grid-template-columns: repeat(10, 1fr); gap: 0; width: 100%; border-radius: 4px; overflow: hidden;">'
    
    section_html = section_html.replace(old_start, new_start)
    
    # Replace closing tags
    section_html = section_html.replace('    </div>\n</section>', '        </div>\n    </div>\n</section>')
    
    html = html[:match.start()] + section_html + html[match.end():]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Gallery boxed successfully.")
else:
    print("Could not find the custom gallery section.")
