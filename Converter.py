import os
import subprocess
from tkinter import Tk, filedialog

def convert_to_mp3(input_file, output_file):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "192k",
        "-ar", "44100",
        "-y", output_file
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Video has been successfully converted.")

    except subprocess.CalledProcessError as e:
        print("Failed to convert.")


root = Tk()
root.withdraw()

input_file = filedialog.askopenfilename(
    title="Select a video file",
    filetypes=[("Video files", "*.mp4;*.avi;*.mov"), ("All files", "*.*")]
)

