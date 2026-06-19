with open('index.html', 'r', encoding='utf-8') as f:
    html_new = f.read()

start_idx = 0
found = 0

while True:
    idx = html_new.find('floral-icon-elopement.png', start_idx)
    if idx == -1:
        break
    found += 1
    if found > 1:
        # Delete this occurrence
        div_start = html_new.rfind('<div class="elementor-element elementor-widget elementor-widget-image"', 0, idx)
        div_end = html_new.find('</div>\n</div>', idx)
        
        if div_start != -1 and div_end != -1:
            html_new = html_new[:div_start] + html_new[div_end+13:]
            # We don't advance start_idx because the string shrank
        else:
            # If we didn't find the exact div wrapper, just try to remove the img tag itself
            img_start = html_new.rfind('<img', 0, idx)
            img_end = html_new.find('>', idx)
            if img_start != -1 and img_end != -1:
                html_new = html_new[:img_start] + html_new[img_end+1:]
            else:
                start_idx = idx + 1
    else:
        start_idx = idx + 1

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_new)
print(f"Found {found} leaves, kept 1.")
