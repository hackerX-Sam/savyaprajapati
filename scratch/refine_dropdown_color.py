import os

old_string = '''<ul class="sub-menu elementor-nav-menu--dropdown" style="background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); padding: 10px; margin-top: 10px; border-radius: 4px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
<li class="menu-item"><a href="javascript:void(0);" class="elementor-sub-item" style="color: #000 !important;">TEAM</a></li>
<li class="menu-item"><a href="javascript:void(0);" class="elementor-sub-item" style="color: #000 !important;">TESTIMONIAL</a></li>
</ul>'''.replace('\n', '')

new_string = '''<ul class="sub-menu elementor-nav-menu--dropdown" style="background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(25px); -webkit-backdrop-filter: blur(25px); border: 1px solid rgba(255, 255, 255, 0.2); padding: 10px; margin-top: 10px; border-radius: 8px;">
<li class="menu-item"><a href="javascript:void(0);" class="elementor-sub-item" style="color: #fff !important; text-shadow: 0 1px 3px rgba(0,0,0,0.3);">TEAM</a></li>
<li class="menu-item"><a href="javascript:void(0);" class="elementor-sub-item" style="color: #fff !important; text-shadow: 0 1px 3px rgba(0,0,0,0.3);">TESTIMONIAL</a></li>
</ul>'''.replace('\n', '')

count = 0
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.gemini' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html') or file.endswith('.1'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except:
                continue
            
            if old_string in content:
                new_content = content.replace(old_string, new_string)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                print(f"Updated {filepath}")

print(f"Finished updating {count} files.")
