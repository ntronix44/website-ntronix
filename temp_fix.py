with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove the download badges block between phone mockup close and flex row close
old_badges_wrong = '''                    \n                    <!-- Download app row below the flex items -->\n                    <div class="mt-10 text-center reveal stagger-4">\n                        <p class="text-white/40 text-sm mb-4">Download the Ntronix companion app</p>\n                        <div class="store-badge-row" style="justify-content: center;">\n                            <a href="#" class="store-badge playstore" target="_blank" rel="noopener">\n                                <i class="ri-google-play-fill"></i>\n                                <span class="badge-text">\n                                    <span class="small">GET IT ON</span>\n                                    Google Play\n                                </span>\n                            </a>\n                            <a href="#" class="store-badge appstore" target="_blank" rel="noopener">\n                                <i class="ri-apple-fill"></i>\n                                <span class="badge-text">\n                                    <span class="small">DOWNLOAD ON</span>\n                                    App Store\n                                </span>\n                            </a>\n                            <a href="#" class="store-badge apk-download" target="_blank" rel="noopener">\n                                <i class="ri-download-2-line"></i>\n                                <span class="badge-text">\n                                    <span class="small">DIRECT</span>\n                                    APK Download\n                                </span>\n                            </a>\n                        </div>\n                    </div>\n                '''

count = text.count(old_badges_wrong)
print(f"Badges to remove: {count}")
if count == 1:
    text = text.replace(old_badges_wrong, '\n                ', 1)
    print("Removed badges from wrong location")
else:
    print(f"Unexpected count: {count}")
    # Try to find it
    idx = text.find('Download the Ntronix')
    print(f"Found at {idx}")
    print(repr(text[idx-20:idx+200]))

# 2. Now add badges under the powerwall card, inside left column
# Find: after the closing </div> of hes-glass-card, before the left column div close
old_inside_left = '''                    </div>\n                    \n                    <!-- Right: Professional phone mockup -->'''

badges_inside = '''                    </div>\n                    \n                    <!-- Download badges under powerwall card -->\n                    <div class="mt-6 text-center sm:text-left">\n                        <p class="text-white/40 text-xs mb-3">Download the Ntronix companion app</p>\n                        <div class="store-badge-row left">\n                            <a href="#" class="store-badge playstore" target="_blank" rel="noopener">\n                                <i class="ri-google-play-fill"></i>\n                                <span class="badge-text">\n                                    <span class="small">GET IT ON</span>\n                                    Google Play\n                                </span>\n                            </a>\n                            <a href="#" class="store-badge appstore" target="_blank" rel="noopener">\n                                <i class="ri-apple-fill"></i>\n                                <span class="badge-text">\n                                    <span class="small">DOWNLOAD ON</span>\n                                    App Store\n                                </span>\n                            </a>\n                            <a href="#" class="store-badge apk-download" target="_blank" rel="noopener">\n                                <i class="ri-download-2-line"></i>\n                                <span class="badge-text">\n                                    <span class="small">DIRECT</span>\n                                    APK Download\n                                </span>\n                            </a>\n                        </div>\n                    </div>\n                    \n                    <!-- Right: Professional phone mockup -->'''

count2 = text.count(old_inside_left)
print(f"Insertion point: {count2}")
if count2 == 1:
    text = text.replace(old_inside_left, badges_inside, 1)
    print("Added badges under powerwall card")
else:
    print(f"Unexpected count: {count2}")

with open('index.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(text)

# Verify
print(f"'Download the Ntronix' count: {text.count('Download the Ntronix')}")
print(f"App section still has badges: {'Get the App' in text}")
