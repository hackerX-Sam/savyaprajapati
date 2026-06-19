import re
content = open('c:/Users/samir/OneDrive/Desktop/confidential/ninaanddarek.com/team.1', 'r', encoding='utf-8').read()
urls = set(re.findall(r'[^\"\']+\.png', content))
for u in urls:
    if 'favicon' not in u and 'iconmonstr' not in u:
        print(u)
