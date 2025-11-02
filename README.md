<div align="center">

##🎞️ MOVING-ART  
### _Turn any video into pure ASCII magic — right in your terminal._  

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Made with ❤️ by  Phoenix](https://img.shields.io/badge/Made%20with%20❤️%20by-%20Phoenix-red)](https://github.com/mikey177013)

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfMSwcXISpSqJlesWPK7CEu9iQplhBHTJLEfMiBtNSrsWZmhczr7x-RE8z&s=10" width="80%">

</div>

---

## 🌀 Overview

**Moving-Art** transforms ordinary videos into **ASCII art animations** that play directly inside your **terminal** — complete with **sound**, **frame control**, and smooth performance.

It’s part retro cinema, part code art. Perfect for hackers, artists, and anyone who loves watching pixels dance.

---

## ✨ Features

- 🎬 **Real-time ASCII rendering** — every frame turned into text characters.  
- 🔊 **Synchronized sound playback** via FFmpeg (`ffplay`).  
- ⚙️ **Customizable FPS** and **terminal width** for your system performance.  
- 💻 Works across **Windows**, **Linux**, and **macOS**.  
- 🧩 Built using **OpenCV** and **NumPy** for speed and precision.  

---

## 🧰 Installation

Make sure you’ve got Python 3.8+ and FFmpeg installed.

```bash
# Clone the repo
git clone https://github.com/mikey177013/Moving-art
cd Moving-art

 run:

pip install opencv-python numpy

🧠 FFmpeg Setup

Linux / macOS

sudo apt install ffmpeg

Windows
Download from ffmpeg.org/download and add it to your PATH.


---

🕹️ Usage

python3 index.py

Then follow the on-screen prompts:

Enter the path to the video file: sample.mp4
Enter terminal width (default 80): 100
Enter FPS (default: use video FPS): 0

That’s it. Sit back and watch your movie turn into a storm of ASCII pixels — with perfect sync sound.

```

---

⚡ Performance Tips

Reduce width to 60–80 for smoother playback.

Use video FPS = 0 to auto-sync with actual file FPS.

Close heavy processes before running — ASCII rendering is CPU-intensive.

Works best in full-screen terminal mode.



---

📂 Project Structure
```
Moving-art/
├── main.py              # Main player script
├── README.md            # Project documentation
├── requirements.txt     # Dependencies (optional)
└── sample_videos/       # (Optional) demo videos
```

---

💡 Tech Stack

Component	Description

Python	Core language
OpenCV	Frame extraction & resizing
NumPy	Frame normalization
FFmpeg	Audio playback
ASCII Renderer	Custom frame-to-character converter



---

🧔 Credits

Developed by Phoenix 
Maintained under the MIT License

If you like this project — give it a ⭐ on GitHub!


---
```
<div align="center">“Where pixels meet poetry — and every frame tells a story.”
<br>— Master Phoenix

</div>
```
---
