from pytube import YouTube
from pytube.cli import on_progress
import os

userLink = input("YouTube Video Link: ")

yt = YouTube(userLink, on_progress_callback=on_progress)

video = yt.streams.filter(only_audio=True).first()

path = "./Downloaded"

if not os.path.exists(path):
    os.makedirs(path)

downFile = video.download(output_path=path)

base, ext = os.path.splitext(downFile)
newFile = base + ".mp3"
os.rename(downFile, newFile)

print(yt.title + " has been successfully downloaded")
