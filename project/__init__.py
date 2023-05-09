from mutagen.id3 import ID3
from project.findMusic import *


def process_audio_file(file_path):
    audio = ID3(file_path)
    tags = {}
    # read tags
    # read cover
    print(audio.keys())
    album = audio.get("TALB", [''])[0]
    # read name
    name = audio.get('TIT2', [''])[0]
    tags['album'] = album
    tags['name'] = name
    print(tags)


lists = find_music()
