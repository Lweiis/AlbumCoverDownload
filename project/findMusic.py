import os
import tkinter as tk
from tkinter import filedialog


# 使用 Windows 资源管理器选择一个文件夹
def choose_directory():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    return path


def find_audio_files(music_folder):
    audio_extensions = ['mp3', 'flac', 'wav', 'aac', 'ogg']
    audio_files = [os.path.join(root, filename) for root, dirs, files in os.walk(music_folder) for filename in files if
                   any(filename.lower().endswith(ext) for ext in audio_extensions)]
    return audio_files


def find_music():
    return find_audio_files(choose_directory())
