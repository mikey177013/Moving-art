import cv2
import os
import time
import subprocess
import numpy as np
from threading import Thread
from pathlib import Path
import mimetypes
import shutil

# ========================= ASCII CONVERSION ========================= #
def convert_frame_to_ascii(frame, width=80, color=False):
    """
    Convert a video frame or image into ASCII art.
    """
    ascii_chars = np.asarray(list(" .:-=+*#%@"))
    h, w, _ = frame.shape
    height = max(1, int(h * width / w / 2))

    resized = cv2.resize(frame, (width, height))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    indices = (gray / 255 * (len(ascii_chars) - 1)).astype(np.int32)
    ascii_img = ascii_chars[indices]

    if color:
        lines = []
        for i, row in enumerate(resized):
            colored_row = []
            for j, pixel in enumerate(row):
                b, g, r = pixel
                char = ascii_img[i, j]
                colored_row.append(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
            lines.append("".join(colored_row))
        return "\n".join(lines)
    else:
        return "\n".join("".join(row) for row in ascii_img)

# ========================= AUDIO HANDLER ========================= #
def play_audio(video_path):
    """
    Play the audio track of the video using FFplay.
    """
    try:
        subprocess.run(
            ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", video_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except FileNotFoundError:
        print("⚠️ FFmpeg not found. Please install it from https://ffmpeg.org")

# ========================= VIDEO PLAYER ========================= #
def play_video_in_terminal(video_path, width=80, fps=None, color=False, with_sound=True):
    """
    Play video as ASCII art in the terminal, optionally with color and sound.
    """
    if not os.path.exists(video_path):
        print(f"❌ File not found: {video_path}")
        return

    cap = cv2.VideoCapture(video_path)
    video_fps = cap.get(cv2.CAP_PROP_FPS) or 24
    delay = 1.0 / (fps or video_fps)

    # Auto-fit width to terminal size
    term_cols = shutil.get_terminal_size().columns
    width = min(width, term_cols - 4)

    if with_sound:
        Thread(target=play_audio, args=(video_path,), daemon=True).start()
        time.sleep(0.4)  # sync sound and video

    print("\033[?25l", end="")  # Hide cursor
    try:
        start_time = time.time()
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            ascii_frame = convert_frame_to_ascii(frame, width, color)
            print("\033[H" + ascii_frame)  # No flicker terminal overwrite
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\n⏹️ Playback stopped by user.")
    finally:
        cap.release()
        print("\033[?25h")  # Show cursor
        print("\n✅ Playback finished.")

# ========================= IMAGE HANDLER ========================= #
def show_image_in_ascii(image_path, width=80, color=False):
    """
    Convert and display a single image as ASCII art.
    """
    if not os.path.exists(image_path):
        print(f"❌ File not found: {image_path}")
        return

    image = cv2.imread(image_path)
    if image is None:
        print("❌ Unsupported or corrupted image.")
        return

    # Auto-fit to terminal width
    term_cols = shutil.get_terminal_size().columns
    width = min(width, term_cols - 4)

    ascii_art = convert_frame_to_ascii(image, width, color)
    print(ascii_art)
    print("\n✅ Image displayed as ASCII.")

# ========================= TYPE DETECTOR ========================= #
def is_video_file(path):
    mime_type, _ = mimetypes.guess_type(path)
    return mime_type and mime_type.startswith("video")

def is_image_file(path):
    mime_type, _ = mimetypes.guess_type(path)
    return mime_type and mime_type.startswith("image")

# ========================= MAIN ========================= #
if __name__ == "__main__":
    media_path = input("🎥 Media path (image or video): ").strip()
    width = input("📏 Width (default 80): ").strip()
    fps = input("🎞️ FPS (0 = auto): ").strip()
    color = input("🌈 Enable color? (y/n): ").strip().lower() in ("y", "yes")
    sound = input("🔊 Play sound? (y/n): ").strip().lower() in ("y", "yes")

    width = int(width) if width.isdigit() else 80
    fps = int(fps) if fps.isdigit() and int(fps) > 0 else None

    if is_video_file(media_path):
        play_video_in_terminal(media_path, width, fps, color, sound)
    elif is_image_file(media_path):
        show_image_in_ascii(media_path, width, color)
    else:
        print("❌ Unsupported file type. Please provide a valid image or video.")