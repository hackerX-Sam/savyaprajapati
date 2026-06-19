with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We know exactly how it looks from grep output
# <img decoding="async" width="400" src="https://ninaanddarek.com/wp-content/uploads/2023/04/floral-icon-elopement.png" class="lazyload" alt="" style="width: 400px; max-width: 100%; margin: 0 auto; display: block;" />

# But we can just search for the image string.
start_idx = 0
found = 0

while True:
    idx = html.find('floral-icon-elopement.png', start_idx)
    if idx == -1:
        break
    found += 1
    if found > 1:
        # Delete from the start of <img to the end of />
        img_start = html.rfind('<img', 0, idx)
        img_end = html.find('>', idx)
        
        if img_start != -1 and img_end != -1:
            html = html[:img_start] + html[img_end+1:]
            # DO NOT ADVANCE start_idx, because we just deleted what was at start_idx!
            # The next occurrence will naturally slide into our view.
        else:
            start_idx = idx + 1
    else:
        start_idx = idx + 1

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Total found: {found}. Extra removed.")
