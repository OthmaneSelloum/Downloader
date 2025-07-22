from tkinter import filedialog
import customtkinter as ctk
import Fonctionnalities as fn

download_path = ""

# Fonction pour choisir un dossier
def choisir_dossier():
    global download_path
    path = filedialog.askdirectory()
    if path:
        download_path = path
        label_path.configure(text=f"Dossier : {path}")


# Configuration de l'apparence
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Création de la fenêtre principale
app = ctk.CTk()
app.title("Téléchargeur YouTube")
app.geometry("700x300")

# Label d'instruction
label = ctk.CTkLabel(app, text="Entrez l'URL :", font=("Arial", 16))
label.pack(pady=10)

# Champ de saisie de l'URL
entry = ctk.CTkEntry(app, width=400)
entry.pack(pady=10)

# Choix du dossier
btn_choisir = ctk.CTkButton(app, text="Choisir un dossier", command=choisir_dossier)
btn_choisir.pack(pady=5)

label_path = ctk.CTkLabel(app, text="Dossier : Aucun", font=("Arial", 12))
label_path.pack(pady=5)


# Bouton MP3
btn_mp3 = ctk.CTkButton(app, text="Télécharger MP3", command=lambda:fn.Download_mp3(entry.get(),download_path))
btn_mp3.pack(pady=5)

# Bouton MP4
btn_mp4 = ctk.CTkButton(app, text="Télécharger MP4", command=lambda:fn.Download_mp4(entry.get(),download_path))
btn_mp4.pack(pady=5)

# Boucle principale
app.mainloop()
