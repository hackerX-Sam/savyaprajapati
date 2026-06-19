from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

leaves = soup.find_all('img', src=lambda s: s and 'floral-icon-elopement' in s)
print(f"Found {len(leaves)} leaves.")

if len(leaves) > 1:
    for leaf in leaves[1:]: # Skip the first one
        # Try to find the wrapper <div class="elementor-widget-image">
        parent = leaf.parent
        while parent and parent.name == 'div' and 'elementor-widget-image' not in parent.get('class', []):
            parent = parent.parent
        
        if parent and parent.name == 'div' and 'elementor-widget-image' in parent.get('class', []):
            parent.decompose()
        else:
            leaf.decompose()

    with open('index.html', 'w', encoding='utf-8') as f:
        # Since bs4 can alter formatting, we only replace the modified soup string if it looks okay,
        # but bs4 pretty formatting might change the whole file. 
        # Alternatively, we can just use the string replacements.
        pass

# Let's use pure string manipulation based on find()
html_new = html
start_idx = 0
found = 0

while True:
    idx = html_new.find('floral-icon-elopement.png', start_idx)
    if idx == -1:
        break
    found += 1
    if found > 1:
        # Delete this occurrence
        # Find the <div class="elementor-element elementor-widget elementor-widget-image" before it
        div_start = html_new.rfind('<div class="elementor-element elementor-widget elementor-widget-image"', 0, idx)
        div_end = html_new.find('</div>\n</div>', idx)
        
        if div_start != -1 and div_end != -1:
            html_new = html_new[:div_start] + html_new[div_end+13:]
            # We don't advance start_idx because the string shrank
        else:
            start_idx = idx + 1
    else:
        start_idx = idx + 1

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_new)
print("Removed extra leaves using string search.")
