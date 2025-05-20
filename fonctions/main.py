from pathlib import Path

from colorama import Fore

from fonctions import frontend, core, import_export, fonctions_user

def jeu(mail, password, score:dict, niveau:dict, file_game:Path, file_user:Path):

    liste_domaine = ["reseau_informatique", "systemes_informatiques", "programmation"]
    choix_menu_principale = 1
    score = score
    niveau = niveau

    while choix_menu_principale:
        choix_menu_principale = frontend.menu(frontend.menu_principal)
        if choix_menu_principale == 1:
            while choix_menu_principale:
                choix_domaine = frontend.menu_domaine(frontend.menu_choix_domaine)

                if choix_domaine == 4:
                    break

                while choix_domaine:
                    score,niveau[liste_domaine[choix_domaine-1]] = core.condition_jeu(liste_domaine, choix_domaine, score, niveau[liste_domaine[choix_domaine - 1]], file_game)
                    break

        elif choix_menu_principale == 2:
            frontend.afficher_score(score)

        elif choix_menu_principale == 3:
            import_export.sauvegarde(mail, password, score, niveau, file_user)
            print("À bientôt :) !!!")
            return score, niveau

def run(file_of_game:Path, file_user:Path):
    status_connexion:bool = False
    flag_logout:bool = False
    user_info:dict = {}
    choix = 1

    while choix or not choix:
        if not status_connexion:
            choix = input(Fore.LIGHTWHITE_EX + frontend.menu_global)  # Demande du choix

        if flag_logout:
            status_connexion = False

        if choix == "1" or status_connexion:# ce choix connecte l'utilisateur et s'il est déja connecté le donner accès au code de la condition.
            if not status_connexion:
                email, password = fonctions_user.ask_login()
                user_info, status_connexion = fonctions_user.login(email, password, file_user)

            if status_connexion:
                score = user_info["score"]
                niveau = user_info["niveau"]
                print(f"Bienvenue {user_info["nom"]}")
                while choix or not choix:
                    choix = input(frontend.menu_game)
                    if choix == "1":
                        score, niveau  = jeu(user_info["email"], user_info["password"], score, niveau, file_of_game, file_user)
                    elif choix== "2":
                        print(f"nom: {user_info["nom"]}\nemail: {user_info["email"]}\npassword: {user_info["password"]}")
                    elif choix == "3":
                        status_connexion = True
                        flag_logout = True
                        choix = "4"
                        print("Déconnexion !!!")
                        break
            else:
                print("")
                print(Fore.RED + "Identifiant incorrect")


        elif choix == "2":# récupérer un mot de passe perdu
            nom, email, password = fonctions_user.ask_register()
            user = fonctions_user.register(nom, email, password, file_user)
            user_info, status_connexion = fonctions_user.login(user["email"], user["password"], file_user)
            score = user_info["score"]
            niveau = user_info["niveau"]


        elif choix == "3":# Déconnexion
            email = input("Veuillez saisir votre adresse email : ")
            while not email:
                email = input("Veuillez saisir votre adresse email : ")
            user_info, status_connexion = fonctions_user.forgot_password(email, file_user)
            if status_connexion:
                score = user_info["score"]
                niveau = user_info["niveau"]


        elif choix == "4":
            if not flag_logout:
                print("À bientôt !!!")
            break


        else:
            print("Choix incorrect, veuillez réessayer. ")
if __name__ == "__main__":
    file_quizz = Path().cwd().parent / "data/data_base_of_quizz_game.json"
    file_users = Path().cwd().parent / "data/count_user.json"

    run(file_quizz, file_users)

