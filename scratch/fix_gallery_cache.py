import os
import glob
import json

base_dir = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com'

# 1. Update all HTML and .1 files to use /gallery/ instead of /gallery
files = glob.glob(os.path.join(base_dir, '*.html')) + \
        glob.glob(os.path.join(base_dir, '*.1')) + \
        glob.glob(os.path.join(base_dir, 'gallery', '*.html')) + \
        glob.glob(os.path.join(base_dir, 'stories', '*.html'))

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Replace exact href="/gallery" to href="/gallery/"
        new_content = content.replace('href="/gallery"', 'href="/gallery/"')
        
        if new_content != content:
            # write back carefully
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated links in {os.path.basename(filepath)}")
    except Exception as e:
        print(f"Skipping {os.path.basename(filepath)} due to {e}")

# 2. Update vercel.json
vercel_json = os.path.join(base_dir, 'vercel.json')
if os.path.exists(vercel_json):
    with open(vercel_json, 'r', encoding='utf-8') as f:
        v_data = json.load(f)
    
    # Add trailingSlash configuration to force directory behavior
    v_data['trailingSlash'] = True
    v_data['cleanUrls'] = True
    
    # Add explicit header for /gallery/
    has_gallery_header = False
    for h in v_data.get('headers', []):
        if h.get('source') in ['/gallery/', '/gallery/index.html', '/gallery']:
            has_gallery_header = True
            break
            
    if not has_gallery_header:
        v_data.setdefault('headers', []).append({
            "source": "/gallery/(.*)",
            "headers": [
                {
                    "key": "Content-Type",
                    "value": "text/html"
                }
            ]
        })
        v_data['headers'].append({
            "source": "/gallery/",
            "headers": [
                {
                    "key": "Content-Type",
                    "value": "text/html"
                }
            ]
        })
        
    with open(vercel_json, 'w', encoding='utf-8') as f:
        json.dump(v_data, f, indent=2)
    print("Updated vercel.json")
