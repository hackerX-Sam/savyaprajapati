import os

filepath = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\about.1'
target = '</head>'
replacement = '''<style>
/* Pull about page cover photo up */
.elementor-83 {
    margin-top: -180px !important;
    position: relative;
    z-index: 1;
}
header {
    position: relative;
    z-index: 10;
}
</style>
</head>'''

try:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target in content and '/* Pull about page cover photo up */' not in content:
        content = content.replace(target, replacement)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated about.1")
    else:
        print("Target not found or already updated.")
except Exception as e:
    print(f"Error: {e}")
