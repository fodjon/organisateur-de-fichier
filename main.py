import os
import shutil

path = input("Chemin du ficher : ")
extention = input("Choisissez l'extension à trier : ")
if os.path.exists(path):
    fichiers = os.listdir(path)
    for fichier in fichiers:
        if fichier.endswith(f".{extention}"):
            sous_dossier = os.path.join(path, extention)
            chemin_actuel = os.path.join(path, fichier)
            chemin_sous_dossier = os.path.join(sous_dossier, fichier)
            os.makedirs(sous_dossier, exist_ok=True)
            shutil.move(chemin_actuel, chemin_sous_dossier)
            print(f"{fichier} -> {chemin_sous_dossier}")
else:
    print("Le ficher n'existe pas")