import os

# Common browser install paths
browsers = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "chrome_x86": r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "firefox": r"C:\Program Files\Mozilla Firefox\firefox.exe",
    "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "brave": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
}

# Check which browsers are installed
available = {}

for name, path in browsers.items():
    if os.path.exists(path):
        available[name] = path

# Output result
if available:
    print("✅ Installed Browsers Detected:\n")
    for name, path in available.items():
        print(f"{name.upper()} ➤ {path}")
else:
    print("❌ Koi browser detected nahi hua standard path se.")
