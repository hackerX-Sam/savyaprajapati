import os
import re

desired_nav = '''
    <li class="menu-item"><a href="/about.1" class="elementor-item">ABOUT</a></li>
    <li class="menu-item"><a href="https://weddingsbysabhya.pic-time.com/client" target="_blank" class="elementor-item">STORIES</a></li>
    <li class="menu-item"><a href="javascript:void(0);" class="elementor-item">GALLERY</a></li>
    <li class="menu-item menu-item-has-children"><a href="javascript:void(0);" class="elementor-item">BEHIND THE LENS</a><ul class="sub-menu elementor-nav-menu--dropdown" style="background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(25px); -webkit-backdrop-filter: blur(25px); border: 1px solid rgba(255, 255, 255, 0.2); padding: 10px; margin-top: 10px; border-radius: 8px;"><li class="menu-item"><a href="/team.1" class="elementor-sub-item" style="color: #000 !important; font-weight: 500;">TEAM</a></li><li class="menu-item"><a href="javascript:void(0);" class="elementor-sub-item" style="color: #000 !important; font-weight: 500;">TESTIMONIAL</a></li></ul></li>
    <li class="menu-item"><a href="/contact.1" class="elementor-item">CONTACT</a></li>
'''

nav_regex = re.compile(r'(<nav[^>]*>)(.*?)(</nav>)', re.DOTALL)

def clean_nav(match):
    nav_open = match.group(1)
    nav_content = match.group(2)
    nav_close = match.group(3)
    
    ul_match = re.search(r'<ul[^>]*class="[^"]*elementor-nav-menu[^"]*"[^>]*>', nav_content)
    if ul_match:
        ul_open = ul_match.group(0)
        return f"{nav_open}\n{ul_open}{desired_nav}</ul>\n{nav_close}"
    else:
        return match.group(0)

count_files = 0
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
                
            new_content, count = nav_regex.subn(clean_nav, content)
            
            if count > 0 and new_content != content:
                try:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count_files += 1
                except:
                    pass

print(f"Fixed navigation in {count_files} files.")
