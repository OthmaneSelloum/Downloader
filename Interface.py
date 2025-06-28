import customtkinter as ctk

# Configuration de l'apparence
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Création de la fenêtre principale
app = ctk.CTk()
app.title("Téléchargeur YouTube")
app.geometry("500x200")

# Label d'instruction
label = ctk.CTkLabel(app, text="Entrez l'URL :", font=("Arial", 16))
label.pack(pady=10)

# Champ de saisie de l'URL
entry = ctk.CTkEntry(app, width=400)
entry.pack(pady=10)

# Bouton MP3
btn_mp3 = ctk.CTkButton(app, text="Télécharger MP3", command=lambda: print("MP3 button clicked"))
btn_mp3.pack(pady=5)

# Bouton MP4
btn_mp4 = ctk.CTkButton(app, text="Télécharger MP4", command=lambda: print("MP4 button clicked"))
btn_mp4.pack(pady=5)

# Boucle principale
app.mainloop()
