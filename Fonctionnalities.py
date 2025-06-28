import os
import subprocess
from pytube import YouTube


def Download_mp3(url,path):
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    audio_file = audio.download(output_path=path)

    base, ext = os.path.splitext(audio_file)
    mp3_file = base + ".mp3"

    # Conversion avec ffmpeg
    command = [
        "ffmpeg",
        "-i", audio_file,
        "-vn",  # no video
        "-ab", "192k",
        "-ar", "44100",
        "-y",  # overwrite without asking
        mp3_file
    ]

    try:
        subprocess.run(command, check=True)
        os.remove(audio_file)  # Supprimer le fichier source (webm/mp4)
        print(f"Téléchargé et converti : {mp3_file}")
    except subprocess.CalledProcessError as e:
        print("Erreur ffmpeg :", e)


def Download_mp4(url,path):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download(output_path=path)