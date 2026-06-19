import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all img tags containing floral-icon-elopement
pattern = r'<img[^>]*floral-icon-elopement[^>]*>'
matches = list(re.finditer(pattern, html))

print(f"Found {len(matches)} leaf images.")

# Delete all but the first one by just removing the <img> tag
# Doing this in reverse order so indices don't shift
if len(matches) > 1:
    for m in reversed(matches[1:]):
        html = html[:m.start()] + html[m.end():]

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Extra leaves deleted.")
