import os
import tkinter as tk
from tkinter import filedialog
from mutagen.id3 import ID3


# 创建一个简单的 GUI 界面，允许用户使用 Windows 资源管理器选择一个文件夹
def choose_directory():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    path = filedialog.askdirectory()
    return path


def find_audio_files(folder):
    audio_extensions = ['mp3', 'flac', 'wav', 'aac', 'ogg']
    audio_files = [os.path.join(root, filename) for root, dirs, files in os.walk(folder) for filename in files if
                   any(filename.lower().endswith(ext) for ext in audio_extensions)]
    for file_path in audio_files:
        process_audio_file(file_path)


def process_audio_file(file_path):
    audio = ID3(file_path)
    tags = {}
    album = audio.get("TALB", [''])[0]
    name = audio.get('TIT2', [''])[0]
    tags['album'] = album
    tags['name'] = name
    print(tags)


path = choose_directory()
find_audio_files(path)
