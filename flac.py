import tkinter as tk
from tkinter import filedialog
import os
import subprocess
from tkinter import messagebox
from tqdm import tqdm

def convert_flac_to_mp3():
    flac_file_path = source_entry.get()
    if flac_file_path:
        mp3_file_path = os.path.splitext(os.path.basename(flac_file_path))[0] + ".mp3"
        destination_folder = destination_entry.get()
    if destination_folder:
        mp3_file_path = os.path.join(destination_folder, mp3_file_path)
    if os.path.exists(mp3_file_path):
        os.remove(mp3_file_path)

    cmd = ["ffmpeg", "-i", flac_file_path, "-b:a", "320k", mp3_file_path]

root = tk.Tk()
root.title("FLAC to MP3 Converter")

source_label = tk.Label(root, text="Source File:")
source_label.grid(row=0, column=0)

destination_label = tk.Label(root, text="Destination Folder:")
destination_label.grid(row=1, column=0)

source_entry = tk.Entry(root)
source_entry.grid(row=0, column=1)

destination_entry = tk.Entry(root)
destination_entry.grid(row=1, column=1)

source_button = tk.Button(root, text="Browse...", command=lambda: source_entry.insert(0, filedialog.askopenfilename(title="Select FLAC file", filetypes=[("FLAC files", "*.flac")])))
source_button.grid(row=0, column=2)

destination_button = tk.Button(root, text="Browse...", command=lambda: destination_entry.insert(0, filedialog.askdirectory(title="Select Destination Folder")))
destination_button.grid(row=1, column=2)

convert_button = tk.Button(root, text="Convert File", command=convert_flac_to_mp3)
convert_button.grid(row=2, columnspan=3)

root.mainloop()
