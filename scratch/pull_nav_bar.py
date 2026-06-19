import os

workspace_dir = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com'
target = '</head>'
replacement = '''<style>
/* Globally pull the navigation bar up closer to the logo */
.elementor-element-fdcd67e {
    margin-top: -35px !important;
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
                
                # if the file already has the old inline style block with -15px, we replace it
                if 'margin-top: -15px !important;' in content:
                    content = content.replace('margin-top: -15px !important;', 'margin-top: -35px !important;')
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    count += 1
                elif 'margin-top: -35px !important;' not in content:
                    # Append it if it doesn't exist
                    if target in content:
                        content = content.replace(target, replacement)
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        count += 1
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

print(f"Total files updated with nav bar margin -35px: {count}")
