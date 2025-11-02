div align="center">

# 🎞️ Moving-Art  
### *Watch your videos come alive in ASCII — right inside your terminal.*

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Made by Phoenix](https://img.shields.io/badge/Made%20by-Phoenix-orange.svg)](https://github.com/mikey177013)

</div>

---

## 🌀 Overview

**Moving-Art** turns any normal video into a **moving ASCII animation** — directly in your terminal window.  
It’s lightweight, hypnotic, and strangely satisfying to watch.

Built purely in **Python**, it uses **OpenCV** to process frames and display them as ASCII characters in real-time.  
Perfect for devs who love art, or artists who love code.

---

## ⚙️ Requirements

- Python 3.8 or higher  
- FFmpeg (for audio playback)  
- Terminal with UTF-8 support  

---

## 📦 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/mikey177013/Moving-art.git
cd Moving-art
pip install opencv-python numpy


---

▶️ Usage

Place your video file in the same folder (or use the included vid.mp4), then run:

python3 index.py

You’ll be asked to enter:

Enter path to video: vid.mp4
Enter terminal width (default 80): 100
Enter FPS (default: use video FPS): 0

That’s it. Sit back and enjoy your video turn into ASCII art — frame by frame.


---

💡 Tips for Smooth Playback

Use smaller terminal widths (like 60–80) if playback lags.

Keep your terminal window full screen for best visuals.

The higher the FPS, the smoother (but heavier) it gets.

Works best with shorter, high-contrast videos.



---

📂 Folder Structure

Moving-art/
├── index.py      # Main script
└── vid.mp4       # Sample video


---

🧠 How It Works

Step	Description

1️⃣	OpenCV extracts each video frame
2️⃣	Frame is resized and brightness analyzed
3️⃣	Brightness → ASCII character mapping
4️⃣	Frame printed in terminal sequentially
5️⃣	FFmpeg (ffplay) handles sound playback



---

🪄 Example Output

.:--=++********######********++=-:.
  .=++==----:::::::::::::::----===++=.
  .:=++*#%%@@@@@@%%%%%@@@@@@%%#*++=-.

(Yeah, that’s your movie, reborn as text art.)


---

🧾 License

This project is licensed under the MIT License — use it, modify it, break it, remix it.
Just don’t forget to give credit 😉


---

<div align="center">Created with ❤️ by Phoenix

> “Code is just art that runs.”



</div>
```
---