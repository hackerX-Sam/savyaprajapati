import os

workspace_dir = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com'
target = '</head>'
replacement = '''<style>
/* Make header absolutely positioned so the cover photo reaches the top boundary of the screen */
header[data-elementor-type="header"] {
    position: absolute !important;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 999;
    background: transparent !important;
}
.elementor-83, .elementor-10, .elementor-page {
    margin-top: 0px !important;
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
                
                if 'header[data-elementor-type="header"] {' not in content:
                    if target in content:
                        content = content.replace(target, replacement)
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        count += 1
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

print(f"Total files updated with absolute header CSS: {count}")
