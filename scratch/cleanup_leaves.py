import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We want to remove all <div class="elementor-element elementor-widget elementor-widget-image">...<img ...floral-icon-elopement.png...>...</div>
# Because the previous regex might have missed some due to exact spacing or nested divs.
# Let's find exactly the blocks containing floral-icon-elopement.png that were added by the scripts.

pattern = r'<div class="elementor-element elementor-widget elementor-widget-image"[^>]*>\s*<div class="elementor-widget-container">\s*<img[^>]*floral-icon-elopement\.png[^>]*>\s*</div>\s*</div>'

matches = list(re.finditer(pattern, html, re.DOTALL))
print(f'Found {len(matches)} leaf blocks with full div wrapper')

if len(matches) > 1:
    for match in reversed(matches[1:]):
        html = html[:match.start()] + html[match.end():]
        
# Now let's just find ANY remaining standalone <img ... floral-icon-elopement.png ...> tags that aren't the first one in the file.
img_pattern = r'<img[^>]*floral-icon-elopement(?:-1)?\.png[^>]*>'
all_imgs = list(re.finditer(img_pattern, html, re.DOTALL))
print(f'Found {len(all_imgs)} leaf images overall')

if len(all_imgs) > 1:
    # If they are just loose <img> tags, or wrapped in something else, we can just delete the loose <img> tags
    # Wait, we need to make sure we don't break HTML by leaving empty <div>s.
    # The first leaf image is the one we want to keep.
    # Let's see if we can find the <div> wrapper by backtracking.
    for match in reversed(all_imgs[1:]):
        start = match.start()
        end = match.end()
        # check if it is wrapped in <div class="elementor-widget-container">
        wrapper_start = html.rfind('<div class="elementor-element elementor-widget elementor-widget-image"', max(0, start-500), start)
        wrapper_end = html.find('</div>\n</div>', end, min(len(html), end+100))
        if wrapper_start != -1 and wrapper_end != -1:
            # delete the whole wrapper
            html = html[:wrapper_start] + html[wrapper_end+13:]
        else:
            # just delete the img
            html = html[:start] + html[end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Cleanup done.')
