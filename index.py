import cv2
import os
import time
import subprocess
import numpy as np
from threading import Thread

# ---------------------------- ASCII CONVERSION ---------------------------- #
def convert_frame_to_ascii(frame, width=80, color=False):
    """
    Convert a video frame to ASCII art (grayscale or color).
    """
    ascii_chars = np.asarray(list(" .:-=+*#%@"))
    h, w, _ = frame.shape
    height = int(h * width / w / 2)
    if height < 1:
        height = 1

    resized = cv2.resize(frame, (width, height))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    indices = (gray / 255 * (len(ascii_chars) - 1)).astype(np.int32)
    ascii_img = ascii_chars[indices]

    if color:
        result = []
        for i, row in enumerate(resized):
            line = []
            for j, pixel in enumerate(row):
                b, g, r = pixel
                char = ascii_img[i, j]
                line.append(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
            result.append("".join(line))
        return "\n".join(result)
    else:
        return "\n".join("".join(row) for row in ascii_img)

# ---------------------------- SOUND PLAYER ---------------------------- #
def play_audio(video_path):
    """
    Play video audio via ffplay silently in background (no video output).
    """
    try:
        subprocess.run(
            [
                "ffplay",
                "-nodisp",
                "-autoexit",
                "-loglevel", "quiet",
                video_path
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except FileNotFoundError:
        print("⚠️ FFmpeg not found. Install FFmpeg for audio support.")

# ---------------------------- VIDEO PLAYER ---------------------------- #
def play_video_in_terminal(video_path, width=80, fps=None, color=False, with_sound=True):
    """
    Plays ASCII video smoothly with optional color and sound.
    """
    if not os.path.exists(video_path):
        print(f"❌ Error: File not found -> {video_path}")
        return

    cap = cv2.VideoCapture(video_path)
    video_fps = cap.get(cv2.CAP_PROP_FPS) or 24
    delay = 1.0 / (fps or video_fps)

    # Start audio thread
    if with_sound:
        audio_thread = Thread(target=play_audio, args=(video_path,), daemon=True)
        audio_thread.start()
        time.sleep(0.3)  # short delay to sync sound

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            ascii_frame = convert_frame_to_ascii(frame, width, color)

            # Faster screen refresh using escape codes instead of clear command
            print("\033[H\033[J", end="")  # moves cursor to top & clears screen
            print(ascii_frame)

            time.sleep(delay)

    except KeyboardInterrupt:
        print("\n⏹️ Interrupted by user.")

    finally:
        cap.release()
        print("\n✅ Playback finished.")

# ---------------------------- MAIN ---------------------------- #
if __name__ == "__main__":
    video_path = input("🎥 Enter video path: ").strip()
    width_input = input("📏 Enter width (default 80): ").strip()
    fps_input = input("🎞️ FPS (0 = auto): ").strip()
    color_choice = input("🌈 Enable color? (y/n): ").strip().lower()
    sound_choice = input("🔊 Play sound? (y/n): ").strip().lower()

    width = int(width_input) if width_input.isdigit() else 80
    fps = int(fps_input) if fps_input.isdigit() and int(fps_input) > 0 else None
    color = color_choice in ("y", "yes")
    with_sound = sound_choice in ("y", "yes")

    play_video_in_terminal(video_path, width, fps, color, with_sound)