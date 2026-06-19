import os

file_path = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the 125% portrait padding with a 66.6% horizontal rectangle padding
html = html.replace('padding-bottom: 125% !important;', 'padding-bottom: 66.6% !important;')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Frame shape adjusted to horizontal rectangular successfully.")
