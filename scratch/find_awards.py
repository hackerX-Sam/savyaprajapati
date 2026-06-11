import re

file_path = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\index.html"

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

print("Searching for images, awards, or features in index.html...")
keywords = ["award", "feature", "nobackground", "june", "looks", "lane", "rising", "way up", "wp-content/uploads/"]

for idx, line in enumerate(lines):
    line_num = idx + 1
    # Check for keywords
    for kw in keywords:
        if kw.lower() in line.lower() and ("<img" in line or "elementor-element" in line or "section" in line or "meta" in line):
            print(f"Line {line_num}: [{kw}] {line.strip()[:150]}")
            break
