import os
import shutil
import json

base_dir = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com'
gallery_file = os.path.join(base_dir, 'gallery.1')
gallery_dir = os.path.join(base_dir, 'gallery')
gallery_index = os.path.join(gallery_dir, 'index.html')

# 1. Move gallery.1 to gallery/index.html
if os.path.exists(gallery_file):
    if not os.path.exists(gallery_dir):
        os.makedirs(gallery_dir)
    shutil.move(gallery_file, gallery_index)
    print("Moved gallery.1 to gallery/index.html")

# 2. Update server.js
server_js = os.path.join(base_dir, 'server.js')
if os.path.exists(server_js):
    with open(server_js, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace("'gallery.1'", "'gallery/index.html'")
    
    with open(server_js, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated server.js")

# 3. Clean up vercel.json
vercel_json = os.path.join(base_dir, 'vercel.json')
if os.path.exists(vercel_json):
    with open(vercel_json, 'r', encoding='utf-8') as f:
        try:
            v_data = json.load(f)
            
            # Remove the specific gallery header
            if 'headers' in v_data:
                v_data['headers'] = [h for h in v_data['headers'] if h.get('source') != '/gallery']
            
            # Remove the rewrites array if it only has gallery
            if 'rewrites' in v_data:
                v_data['rewrites'] = [r for r in v_data['rewrites'] if r.get('source') != '/gallery']
                if not v_data['rewrites']:
                    del v_data['rewrites']
            
            with open(vercel_json, 'w', encoding='utf-8') as fw:
                json.dump(v_data, fw, indent=2)
            print("Cleaned vercel.json")
        except Exception as e:
            print("Error parsing vercel.json:", e)
