import os
import re

file_path = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the wrapper div inline styles to remove padding and increase size
old_wrapper = 'class="custom-gradient-gallery-wrapper" style="max-width: 900px; width: 100%; padding: 25px; background: #ffffff; border: 1px solid #e0ddd5; box-shadow: 0 10px 40px rgba(0,0,0,0.08); border-radius: 8px;"'
new_wrapper = 'class="custom-gradient-gallery-wrapper" style="max-width: 1400px; width: 100%; padding: 0; background: transparent; border: none; box-shadow: 0 15px 50px rgba(0,0,0,0.15); border-radius: 8px; overflow: hidden;"'

html = html.replace(old_wrapper, new_wrapper)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Gallery box size and padding fixed successfully.")
