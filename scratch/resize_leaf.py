import sys

filepath = 'c:/Users/samir/OneDrive/Desktop/confidential/ninaanddarek.com/index.html'
try:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
except Exception as e:
    print('Error reading:', e)
    sys.exit(1)

# The one we inserted earlier
old_leaf = '<img decoding="async" width="300" height="57" src="https://ninaanddarek.com/wp-content/uploads/2023/04/floral-icon-elopement-300x57.png" class="attachment-medium size-medium lazyload" alt="" style="margin: 0 auto; display: block;" />'

new_leaf = '<img decoding="async" width="500" src="https://ninaanddarek.com/wp-content/uploads/2023/04/floral-icon-elopement.png" class="lazyload" alt="" style="width: 500px; max-width: 100%; margin: 0 auto; display: block;" />'

if old_leaf in content:
    content = content.replace(old_leaf, new_leaf)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Successfully made the leaf bigger!')
else:
    print('Could not find the exact leaf HTML to replace.')
