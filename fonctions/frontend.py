from colorama import Fore

menu_global = """
1.Connexion
2.Inscription
3.Mot de passe oublié
4.Quitter
Veuillez saisir votre choix : """

menu_game = """
1.Lancer le jeu
2.Info user
3.Déconnexion
Veuillez saisir votre choix : """

menu_principal = Fore.MAGENTA + """
#                    Bienvenu Dans QuizzGame
#            QuizzGame est un jeu qui vous permet de 
#            tester votre culture générale en informatique.
#            
#            1) Jouer
#            
#            2) Voire le score
#            
#            3)Sauvegarder et quitter
Veuillez entrer votre choix: """

menu_choix_domaine = Fore.LIGHTCYAN_EX +  """
        Dans quelle domaine de l'informatique 
        souhaitez vous tester votre culture générale?
        
        1) Réseau Informatique
            
        2) Systèmes Informatiques
            
        3) Programmation
        
        4)Revenir au menu principal
Veuillez entrer votre choix: """

menu_accueil = """
1. Inscription
2. Connexion
3.Mot de passe oublié
4.Quitter
Veuillez entré votre choix: """


def menu(m: str) -> int:

    """
    Cette fonction affiche le menu principal
    et elle retourne le choix
    :param m:
    :return: int
    """

    choix = input(m)

    while not choix.isdigit() or not (1 <= int(choix) <= 3):
        print("")
        print(Fore.RED + "x"*100)
        print("""
                            Veuillez entrer une valeur correcte svp.
        """)
        print("x"*100)
        choix = input(Fore.BLACK + m)


    return int(choix)

def menu_domaine(m: str):
    choix = input(m)

    while not choix.isdigit() or not (1 <= int(choix) <= 4):
        print("Veuillez entrer une valeur correcte svp.")
        choix = input(m)

    if 1 <= int(choix) <= 4:
        return int(choix)

def afficher_questions(element:dict) -> str:

    """
    Cette fonction prend en compte le dictionnaire
    qui contient toutes les questions dans un tableau
    et elle renvoie la réponse du joueur.
    :param element: Dict
    :return: str
    """

    reponse = input(Fore.LIGHTBLUE_EX + f"""
{element["question"]}

    1){element["choix"][0]}
    2){element["choix"][1]}
    3){element["choix"][2]}
    4){element["choix"][3]}

veuillez entrez le N° de la bonne réponse:""")
    while not reponse.isdigit() or not (1<= int(reponse) <= 4):
        reponse = input(Fore.LIGHTBLUE_EX + f"""
{element["question"]}

    1){element["choix"][0]}
    2){element["choix"][1]}
    3){element["choix"][2]}
    4){element["choix"][3]}

veuillez entrez le N° de la bonne réponse:""")

    return element["choix"][int(reponse)-1]

def afficher_score(score:dict[str,dict[str,int]]):

    """
    Cette fonction affiche tous les scores disponibles
    :param score: dict
    :return: None
    """
    flag = True
    for element in score.items():

        for niveau in element[1]:

            if element[1][niveau]:
                flag = False
                if "_" in element[0]:
                    liste = element[0].split("_")
                    print(Fore.LIGHTBLUE_EX + f"Votre score en {liste[0].capitalize()} {liste[1].capitalize()} de niveau {niveau} est {element[1][niveau]}")
                else:
                    print(Fore.LIGHTBLUE_EX + f"Votre score en {element[0].capitalize()} de niveau {niveau} est {element[1][niveau]}")

    if flag:
        print('')
        print(Fore.LIGHTBLUE_EX + "Votre score est de 0 à tous les niveau des différents domaines")



