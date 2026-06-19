import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The leaf string from move_leaf.py is:
# <div class="elementor-element elementor-widget elementor-widget-image" style="text-align: center; margin-top: 60px; margin-bottom: 20px;">
#     <div class="elementor-widget-container">
#         <img decoding="async" width="500" src="https://ninaanddarek.com/wp-content/uploads/2023/04/floral-icon-elopement.png" class="lazyload" alt="" style="width: 500px; max-width: 100%; margin: 0 auto; display: block;" />
#     </div>
# </div>

# The exact match could have been modified by resize_leaf.py, etc.
# We will find all blocks containing 'floral-icon-elopement.png'
# The block starts with <div class="elementor-element elementor-widget elementor-widget-image" and ends with </div>\n</div>
pattern = r'<div class="elementor-element elementor-widget elementor-widget-image"[^>]*>\s*<div class="elementor-widget-container">\s*<img[^>]*floral-icon-elopement\.png[^>]*>\s*</div>\s*</div>'

matches = list(re.finditer(pattern, html, re.DOTALL))
print(f'Found {len(matches)} leaf blocks')

if len(matches) > 1:
    # Keep the first one, delete the rest
    for match in reversed(matches[1:]):
        html = html[:match.start()] + html[match.end():]
        
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Removed extra leaf blocks')
