import os

file_path = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the 100% square padding with a 125% vertical rectangle padding
html = html.replace('padding-bottom: 100% !important;', 'padding-bottom: 125% !important;')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Frame shape adjusted to rectangular successfully.")
