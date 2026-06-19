import re
content = open('c:/Users/samir/OneDrive/Desktop/confidential/ninaanddarek.com/index.html', 'r', encoding='utf-8').read()
matches = re.findall(r'<li class="menu-item">.*?</li>', content, re.IGNORECASE)
for m in matches[:10]:
    print(m)
