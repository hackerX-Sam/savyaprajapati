import urllib.request
import urllib.error

urls = [
    "http://localhost:8080/team",
    "http://localhost:8080/team.1"
]

print("Verifying server responses for Team pages...")
for url in urls:
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req) as response:
            status = response.status
            content_type = response.info().get('Content-Type', '')
            body = response.read().decode('utf-8', errors='ignore')
            
            print(f"\nURL: {url}")
            print(f"Status: {status}")
            print(f"Content-Type: {content_type}")
            
            # Verify specific contents
            has_title = "Meet The Team" in body
            has_sabhya = "Sabhya Prajapati" in body
            has_grid = "team-grid-container" in body
            
            # Count image wrappers (borders)
            wrapper_count = body.count("class=\"team-image-wrapper\"")
            
            # Count images (only background image remains)
            image_count = body.count("https://ik.imagekit.io/logicsync/")
            
            print(f"  Contains 'Meet The Team' title: {has_title}")
            print(f"  Contains 'Sabhya Prajapati' member: {has_sabhya}")
            print(f"  Contains grid container: {has_grid}")
            print(f"  Image wrappers (borders) found: {wrapper_count}")
            print(f"  Image Kit URLs found: {image_count}")
            
            if status == 200 and has_title and has_grid and wrapper_count == 12:
                print("  => SUCCESS!")
            else:
                print("  => FAILURE (Checks failed)")
                
    except urllib.error.HTTPError as e:
        print(f"\nURL: {url}")
        print(f"HTTP Error: {e.code}")
    except Exception as e:
        print(f"\nURL: {url}")
        print(f"Connection Error: {e}")
