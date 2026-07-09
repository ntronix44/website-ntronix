with open(r'C:\Users\Ntronix\Desktop\ntronix_website\Website\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Old GitHub private URL
old_url = 'https://github.com/ntronix44/ntronOS/releases/download/app-v1.0.0/app-release.apk'
new_url = '/Ntronix-App-v1.0.0.apk'

count = content.count(old_url)
if count > 0:
    content = content.replace(old_url, new_url)
    with open(r'C:\Users\Ntronix\Desktop\ntronix_website\Website\index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"SUCCESS: Replaced {count} occurrences of private GitHub URL")
    print(f"New URL: {new_url}")
else:
    print("FAILED: URL not found")
