import urllib.request
import urllib.error

url = "https://ik.imagekit.io/logicsync/tr:w-2000/CEOL0925f.JPG?updatedAt=1780925356765"
try:
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    with urllib.request.urlopen(req) as response:
        print("URL:", url)
        print("Status:", response.status)
        print("Content-Type:", response.info().get('Content-Type'))
        if 'ik-error' in response.info():
            print("ik-error:", response.info().get('ik-error'))
except urllib.error.HTTPError as e:
    print("HTTP Error status:", e.code)
    if 'ik-error' in e.headers:
        print("ik-error:", e.headers['ik-error'])
except Exception as e:
    print("Other Error:", e)
