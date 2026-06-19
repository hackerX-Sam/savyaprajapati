import os

file_path = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace font size in the custom injected CSS
content = content.replace("font-size: 13px !important;", "font-size: 16px !important;")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Navigation text made bigger successfully.")
