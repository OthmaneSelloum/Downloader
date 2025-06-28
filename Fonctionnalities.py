import yt_dlp
import os

def Download_mp3(url, path):
    if not url or not path:
        print("URL ou chemin invalide.")
        return

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,  # Affiche les logs dans le terminal
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Téléchargement MP3 terminé.")
    except Exception as e:
        print("Erreur :", e)


def Download_mp4(url, path):
    if not url or not path:
        print("URL ou chemin invalide.")
        return

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'quiet': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Téléchargement MP4 terminé.")
    except Exception as e:
        print("Erreur :", e)
