import re

with open(r'C:\Users\Ntronix\Desktop\ntronix_website\Website\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the dark-bg section (the bottom "Get the App" section)
old2 = '''                    <div class="store-badge-row dark-bg" style="justify-content: center;">
                        <a href="#" class="store-badge playstore" target="_blank" rel="noopener">
                            <i class="ri-google-play-fill"></i>
                            <span class="badge-text">
                                <span class="small">GET IT ON</span>
                                Google Play
                            </span>
                        </a>
                        <a href="#" class="store-badge appstore" target="_blank" rel="noopener">
                            <i class="ri-apple-fill"></i>
                            <span class="badge-text">
                                <span class="small">DOWNLOAD ON</span>
                                App Store
                            </span>
                        </a>
                        <a href="#" class="store-badge apk-download" target="_blank" rel="noopener">
                            <i class="ri-download-2-line"></i>
                            <span class="badge-text">
                                <span class="small">DIRECT</span>
                                APK Download
                            </span>
                        </a>
                    </div>'''

new2 = '''                    <div class="store-badge-row dark-bg" style="justify-content: center;">
                        <!-- Direct APK Download, first, triggers immediate download -->
                        <a href="https://github.com/ntronix44/ntronOS/releases/download/app-v1.0.0/app-release.apk"
                           class="store-badge apk-download"
                           download="Ntronix-App-v1.0.0.apk"
                           target="_blank" rel="noopener">
                            <i class="ri-download-2-line"></i>
                            <span class="badge-text">
                                <span class="small">DIRECT</span>
                                APK Download
                            </span>
                        </a>
                        <a href="#" class="store-badge playstore" target="_blank" rel="noopener">
                            <i class="ri-google-play-fill"></i>
                            <span class="badge-text">
                                <span class="small">GET IT ON</span>
                                Google Play
                            </span>
                        </a>
                        <a href="#" class="store-badge appstore" target="_blank" rel="noopener">
                            <i class="ri-apple-fill"></i>
                            <span class="badge-text">
                                <span class="small">DOWNLOAD ON</span>
                                App Store
                            </span>
                        </a>
                    </div>'''

if old2 in content:
    content = content.replace(old2, new2, 1)
    with open(r'C:\Users\Ntronix\Desktop\ntronix_website\Website\index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: Fixed dark-bg section too")
else:
    print("dark-bg old string not found")
    idx = content.find('store-badge-row dark-bg')
    if idx >= 0:
        print(f"Found at {idx}, showing context:")
        print(content[idx:idx+500])
