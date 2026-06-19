import os

file_path = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the max-width to make it slightly bigger
html = html.replace('max-width: 1050px !important;', 'max-width: 1200px !important;')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Grid size adjusted to be a little bigger successfully.")
