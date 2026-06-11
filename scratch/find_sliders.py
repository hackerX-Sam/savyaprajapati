import re

def main():
    path = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\jackie-gabs-isle-of-skye-elopement\index.html"
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all image URLs
    img_urls = re.findall(r'https?://[^\s"\'>]+\.(?:jpg|jpeg|png|gif|webp)', content, re.IGNORECASE)
    print(f"Total image URLs found in post: {len(img_urls)}")
    for i, url in enumerate(img_urls):
        print(f"{i}: {url}")

if __name__ == "__main__":
    main()
