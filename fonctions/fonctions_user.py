import random
from pathlib import Path

from fonctions import import_export

def ask_register() -> tuple[str, str, str] | None:
    nom:str = input("Veuillez saisir votre nom et prénom: ")
    email:str = input("Veuillez saisir votre adresse email : ")
    password:str = input("Veuillez saisir votre mot de passe : ")


    if verify_register_info(nom, email, password):
        return nom, email, password
    else:
        print("")
        print("Veuillez entré des données valident svp :)\nUne adresse valide.\nVotre mot de passe doit avoir une longueur de 8 caractères ou plus.\nVotre nom et prénom ne doivent contenir aucun chiffre")
        return ask_register()

def register(nom:str, email: str, password: str, file_of_user:Path):
    new_user:dict = {
        "nom": nom,
        "email": email,
        "password": password,
        "score": {
        "reseau_informatique": {
            "Facile": 0,
            "Intermédiaire": 0,
            "Difficile": 0
        },
        "systemes_informatiques": {
            "Facile": 0,
            "Intermédiaire": 0,
            "Difficile": 0
        },
        "programmation": {
            "Facile": 0,
            "Intermédiaire": 0,
            "Difficile": 0
        },
    },
        "niveau": {
        "reseau_informatique": "Facile",
        "systemes_informatiques": "Facile",
        "programmation": "Facile"
    }
    }

    db_content:dict = import_export.exported(file_of_user)
    db_content["Users"].append(new_user)
    import_export.imported(file_of_user, db_content)
    print("Inscription réussie !")
    return new_user

def verify_register_info(nom:str, email: str, password: str):
    nom = nom.strip()
    email = email.strip()
    password = password.strip()
    flag = False
    if (nom and email and password) and (len(password) >= 8) and ("@" in email and "." in email and len(nom)>=2):
        if (len(email)>=5) and not (False in ([False for caract in nom if caract.isdigit()])):
            flag = True

    return flag


def ask_login() -> tuple[str,str]:
    email:str = input("Veuillez saisir votre adresse email : ")
    password:str = input("Veuillez saisir votre mot de passe : ")

    return email, password

def login(email: str, password: str, file_of_user:Path) -> tuple[dict,bool]:
    connected:bool = False
    db_content:dict = import_export.exported(file_of_user)

    for user in db_content["Users"]:
        if email == user["email"] and password == user["password"]:
            connected = True
            return user, connected

    return {}, connected


def forgot_password(email: str, file_of_user):
    flag_mail:bool = False
    password:str = ""

    db_content:dict = import_export.exported(file_of_user)
    users:list[dict] = db_content["Users"]

    for user in users:  # Parcours de la liste des comptes enregistrés

        if email == user["email"]:  # Vérification de l'existence de l'email
            verification_code = str(random.randint(1000, 9999))  # Génération d'un code aléatoire à 4 chiffres
            print(f"Code de vérification : {verification_code}")
            user_code = input("Veuillez entrer le code affiché : ")

            while user_code != verification_code:
                print("Le code saisi est incorrect. ")
                verification_code = str(random.randint(1000, 9999)) # Génération d'un code aléatoire à 4 chiffres
                print(f"Code de vérification : {verification_code}")
                user_code = input("Veuillez entrer le code affiché : ")

            new_password = input("Entrez votre nouveau mot de passe : ")
            while not (new_password.strip() and (len(new_password) >= 8)):
                new_password = input("Entrez votre nouveau mot de passe d'au moins 8 caractères : ")
            user["password"] = new_password  # Mise à jour du nouveau mot de passe
            password = user["password"]
            db_content["Users"] = users
            import_export.imported(file_of_user, db_content)
            print("Mot de passe mis à jour avec succès !")
            flag_mail = True
            break
        

    if flag_mail:
        user_info,connected = login(email, password, file_of_user)
        print('Connecté !!!')
        return user_info, connected
    else:
        print("Erreur: Veuillez reprendre svp")
        return {}, flag_mail


if __name__ == "__main__":
    print(ask_register())
    file_users = Path().cwd().parent / "data/count_user.json"
    print(login("", "", file_users))

