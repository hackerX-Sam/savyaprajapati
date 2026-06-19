import sys

filepath = 'c:/Users/samir/OneDrive/Desktop/confidential/ninaanddarek.com/index.html'
try:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
except Exception as e:
    print('Error reading:', e)
    sys.exit(1)

start_idx = content.find('id="sb_instagram"')
if start_idx == -1:
    print('Could not find sb_instagram')
    sys.exit(1)

# Find the start of the <div id="sb_instagram" ...>
div_start = content.rfind('<div', 0, start_idx)

# Find matching closing div
open_divs = 0
i = div_start
closing_div_end = -1
while i < len(content):
    if content.startswith('<div', i):
        open_divs += 1
        i += 4
    elif content.startswith('</div', i):
        open_divs -= 1
        if open_divs == 0:
            closing_div_end = content.find('>', i) + 1
            break
        i += 5
    else:
        i += 1

if closing_div_end == -1:
    print("Could not find closing div for sb_instagram")
    sys.exit(1)

leaf_html = '''
<div class="elementor-element elementor-widget elementor-widget-image" style="text-align: center; margin-top: 60px; margin-bottom: 20px;">
    <div class="elementor-widget-container">
        <img decoding="async" width="300" height="57" src="https://ninaanddarek.com/wp-content/uploads/2023/04/floral-icon-elopement-300x57.png" class="attachment-medium size-medium lazyload" alt="" style="margin: 0 auto; display: block;" />
    </div>
</div>
'''

new_content = content[:closing_div_end] + leaf_html + content[closing_div_end:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Successfully added leaf design below the Instagram feed!')
