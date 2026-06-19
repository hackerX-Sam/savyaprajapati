import sys

filepath = 'c:/Users/samir/OneDrive/Desktop/confidential/ninaanddarek.com/index.html'
try:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
except Exception as e:
    print('Error reading:', e)
    sys.exit(1)

# Find the leaf design
leaf_html = '''
<div class="elementor-element elementor-widget elementor-widget-image" style="text-align: center; margin-top: 60px; margin-bottom: 20px;">
    <div class="elementor-widget-container">
        <img decoding="async" width="300" height="57" src="https://ninaanddarek.com/wp-content/uploads/2023/04/floral-icon-elopement-300x57.png" class="attachment-medium size-medium lazyload" alt="" style="margin: 0 auto; display: block;" />
    </div>
</div>
'''

if leaf_html in content:
    content = content.replace(leaf_html, '')
    print('Found and removed the leaf design from the bottom.')
else:
    print('Could not find exact leaf design string.')

# Find the hero section. In Elementor, the first section usually has 'elementor-top-section'.
# Actually, let's find the first </section> after the <div data-elementor-type="wp-page"> tag.
start_idx = content.find('data-elementor-type="wp-page"')
if start_idx == -1:
    print('Could not find start of wp-page content')
    sys.exit(1)

first_section_end = content.find('</section>', start_idx)
if first_section_end == -1:
    print('Could not find first section end')
    sys.exit(1)

insert_idx = first_section_end + 10  # after </section>

new_content = content[:insert_idx] + '\n' + leaf_html + content[insert_idx:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Successfully moved the leaf design to below the first section (cover photos).')
