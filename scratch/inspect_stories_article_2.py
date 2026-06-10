import re

def inspect_stories_article_2():
    html_path = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\stories\index.html"
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    articles = re.findall(r'<article[^>]*>[\s\S]*?</article>', content)
    if len(articles) >= 2:
        print("Stories Second article HTML:")
        print(articles[1])
    else:
        print(f"Only found {len(articles)} articles")

if __name__ == "__main__":
    inspect_stories_article_2()
