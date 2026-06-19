import os

workspace_dir = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com'
target = '</head>'
replacement = '''<style>
  body nav.elementor-nav-menu--main ul.elementor-nav-menu li.menu-item a.elementor-item,
  body nav.elementor-nav-menu--main ul.elementor-nav-menu li.menu-item a.elementor-item.elementor-item-active {
      font-size: 28px !important;
      font-weight: bold !important;
      letter-spacing: 1.5px !important;
  }
</style>
</head>'''

count = 0

for root, dirs, files in os.walk(workspace_dir):
    for file in files:
        if file.endswith('.html') or file.endswith('.1'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if we already added it
                if 'body nav.elementor-nav-menu--main ul.elementor-nav-menu' not in content:
                    if target in content:
                        content = content.replace(target, replacement)
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        count += 1
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

print(f"Total files updated with forced nav font style: {count}")
