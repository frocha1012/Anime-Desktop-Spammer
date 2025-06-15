
# Anime Pop-Up Spammer

A fun and completely harmless prank app that spawns animated character GIFs around your screen. Each version is themed after a different anime character, and you can run them individually to experience the chaos.

## 🎮 What It Does

- Spawns 2 animated characters every second.
- Clicking on any character spawns more.
- Automatically stops at 100 characters to avoid freezing your PC.
- Press `Esc` at any time to instantly close all windows.

## 📦 What's Included

Each subfolder (e.g., `lain-iwakura`, `rei-ayanami`, etc.) contains:
- A themed `.exe` for that character (inside `dist/`)
- The Python source code used to build it
- An icon and any extra resources

## 🚀 How to Use

1. Go to the [Releases](https://github.com/YOUR_USERNAME/YOUR_REPO/releases) tab.
2. Download the `.exe` file for your favorite character.
3. Run it and watch your screen fill up with pop-up versions of them.
4. Press `Esc` to clean it all up.

## 🛡 Harmless Fun

- No files are modified, no registry entries made.
- No internet calls after start (except to fetch the GIF if using online links).
- Good for laughs, not for malware.

## 🛠 Want to Make Your Own Character?

1. Copy one of the folders (e.g., `rei-ayanami`) as a template.
2. Replace the icon (`.ico`) and update the GIF URL in the `.py` file.
3. Run:
```bash
pip install pyqt5 requests
pyinstaller --onefile --noconsole --icon=your_icon.ico your_script.py
Done! Your new prank .exe is ready.

Made for fun. Troll responsibly 😎
