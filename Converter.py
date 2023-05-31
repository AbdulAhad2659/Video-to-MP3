import os
import subprocess
from tkinter import Tk, filedialog, messagebox


def convert_to_mp3(video_file, output_file):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", video_file,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "192k",
        "-ar", "44100",
        "-y", output_file
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        messagebox.showinfo("Success", "Video has been successfully converted.")

    except subprocess.CalledProcessError as e:
        messagebox.showinfo("Error", "Failed to convert.")


root = Tk()
root.withdraw()

input_file = filedialog.askopenfilename(
    title="Select a video file",
    filetypes=[("Video files", "*.mp4"), ("All files", "*.*")]
)

save_path = filedialog.askdirectory(title = "Select output folder")
convert_to_mp3(input_file, save_path + "/audio only.mp3")
