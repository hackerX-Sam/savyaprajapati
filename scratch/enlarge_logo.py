import os

file_path = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the specific height of the logo image
html = html.replace('height: 60px;', 'height: 120px;')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Logo enlarged successfully.")
