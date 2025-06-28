import os
from pytube import YouTube
from moviepy.editor import AudioFileClip


def Download_mp3(url):
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    audio_file = audio.download()

    mp3_file = os.path.splitext(audio_file)[0] + ".mp3"
    AudioFileClip(audio_file).write_audiofile(mp3_file)
    os.remove(audio_file)  # Supprime l’ancien fichier (facultatif)


def Download_mp4(url):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download()