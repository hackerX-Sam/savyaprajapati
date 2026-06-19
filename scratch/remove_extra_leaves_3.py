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
        div_start = html_new.rfind('<div class="elementor-element elementor-widget elementor-widget-image"', 0, idx)
        div_end = html_new.find('</div>\n</div>', idx)
        
        if div_start != -1 and div_end != -1 and div_start > idx - 500:
            html_new = html_new[:div_start] + html_new[div_end+13:]
            start_idx = div_start
        else:
            img_start = html_new.rfind('<img', 0, idx)
            img_end = html_new.find('>', idx)
            if img_start != -1 and img_end != -1 and img_start > idx - 200:
                html_new = html_new[:img_start] + html_new[img_end+1:]
                start_idx = img_start
            else:
                start_idx = idx + 1
    else:
        start_idx = idx + 1

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_new)
print("Done!")
