import cv2
import os
import time
import subprocess
import numpy as np
from shutil import get_terminal_size
from threading import Thread

# ---------------------------- ASCII CONVERSION ---------------------------- #
def convert_frame_to_ascii(frame, width=80, color=False):
    """
    Convert a video frame to ASCII art.
    Supports grayscale and optional color output.
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
        colored = ""
        for i, row in enumerate(resized):
            for j, pixel in enumerate(row):
                b, g, r = pixel
                char = ascii_img[i, j]
                colored += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
            colored += "\n"
        return colored
    else:
        return "\n".join("".join(row) for row in ascii_img)

# ---------------------------- SOUND PLAYER ---------------------------- #
def play_audio(video_path):
    """
    Play audio from the given video using ffplay (FFmpeg).
    Suppresses video display from ffplay (sound only).
    """
    try:
        subprocess.run(
            [
                "ffplay",
                "-nodisp",   # no display
                "-autoexit", # stop when done
                "-loglevel", "quiet",
                video_path
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except FileNotFoundError:
        print("⚠️ FFmpeg not found. Install it to enable sound (https://ffmpeg.org).")

# ---------------------------- VIDEO PLAYER ---------------------------- #
def play_video_in_terminal(video_path, width=80, fps=None, color=False, with_sound=True):
    """
    Play video in ASCII form in terminal, with optional sound playback.
    """
    if not os.path.exists(video_path):
        print(f"❌ Error: File not found -> {video_path}")
        return

    cap = cv2.VideoCapture(video_path)
    video_fps = cap.get(cv2.CAP_PROP_FPS) or 24
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    delay = 1.0 / (fps or video_fps)
    term_width = get_terminal_size().columns

    print(f"\n🎬 Playing '{os.path.basename(video_path)}' with sound: {'ON' if with_sound else 'OFF'}")
    print("-" * term_width)

    # Start audio playback in a separate thread
    if with_sound:
        audio_thread = Thread(target=play_audio, args=(video_path,), daemon=True)
        audio_thread.start()
        time.sleep(0.5)  # slight delay for sync alignment

    try:
        start_time = time.time()
        frame_count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            ascii_frame = convert_frame_to_ascii(frame, width, color)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(ascii_frame)

            frame_count += 1
            progress = frame_count / total_frames
            bar = int(progress * (term_width - 20))
            print(f"\n[{('=' * bar).ljust(term_width - 20)}] {progress*100:5.1f}%")

            elapsed = time.time() - start_time
            expected = frame_count * delay
            sleep_time = expected - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)

    except KeyboardInterrupt:
        print("\n⏹️ Playback stopped by user.")

    finally:
        cap.release()
        print("\n✅ Video finished.")
        if with_sound:
            audio_thread.join(timeout=1)

# ---------------------------- MAIN ---------------------------- #
if __name__ == "__main__":
    video_path = input("🎥 Enter video path: ").strip()
    width_input = input("📏 Enter terminal width (default 80): ").strip()
    fps_input = input("🎞️  Enter FPS (0 = auto): ").strip()
    color_choice = input("🌈 Enable color output? (y/n): ").strip().lower()
    sound_choice = input("🔊 Play sound? (y/n): ").strip().lower()

    width = int(width_input) if width_input.isdigit() else 80
    fps = int(fps_input) if fps_input.isdigit() and int(fps_input) > 0 else None
    color = color_choice in ("y", "yes")
    with_sound = sound_choice in ("y", "yes")

    play_video_in_terminal(video_path, width, fps, color, with_sound)