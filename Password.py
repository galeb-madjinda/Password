import re
import hashlib

while True:
    mdp = input("Veuillez entrer un mot de passe : ")

    if len(mdp) < 8:
        print("Le mot de passe doit contenir au moins 8 caractères.")
    elif not re.search("[a-z]", mdp):
        print("Le mot de passe doit contenir au moins une lettre minuscule.")
    elif not re.search("[A-Z]", mdp):
        print("Le mot de passe doit contenir au moins une lettre majuscule.")
    elif not re.search("[0-9]", mdp):
        print("Le mot de passe doit contenir au moins un chiffre.")
    elif not re.search("[!@#$%^&*]", mdp):
        print("Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
    else:
        print("Le mot de passe est sécurisé.")
        
        cryptage = mdp.encode()
        print("Le mot de passe est crypté :")
        print(hashlib.md5(cryptage).hexdigest())
        break
