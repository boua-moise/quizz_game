from pathlib import Path

from colorama import Fore

from fonctions import import_export, frontend


def verifier_reponse(reponse:str, element:dict) -> int:
    """
    Cette fonction vérifie la réponse du Joueur
    et incrémente son score si la réponse est juste
    :param reponse: str
    :param element: dict
    :return: int
    """
    score = 0
    if reponse == element["reponse"]:
        score = element["points"]
        print(Fore.LIGHTGREEN_EX + "validé:",score)
        return score
    print(Fore.RED + "non validé:",score)
    return score

def level(domaine:str, file_of_game:Path, niveau:str) -> tuple:

    """
    Cette fonction dépend de ses paramètres
    pour choisir un niveau de jeu
    :param file_of_game:
    :param domaine: Str
    :param niveau: str
    :return: tuple
    """

    niveau = niveau
    data = import_export.exported(file_of_game)
    data = data[domaine]
    score = 0

    if "_" in domaine:
        liste = domaine.split("_")
        print('')
        print(Fore.GREEN + f"Bienvenue vous êtes au niveau {niveau} du domaine {liste[0].capitalize()} {liste[1].capitalize()}")
    else:
        print('')
        print(Fore.GREEN + f"Bienvenue vous êtes au niveau {niveau} du domaine {domaine}")

    for element in data[niveau]:

        reponse = frontend.afficher_questions(element)
        sc = verifier_reponse(reponse, element)

        if sc:
            score += sc

    return score, data

def level_validate(domaine:list[str], choice:int, score:dict, niveau:str, file_of_game:Path):

    """
    cette fonction gère les niveaux dans le jeu.
    :param file_of_game:
    :param domaine: List[str]
    :param choice: int
    :param score: dict
    :param niveau: str
    :return:
    """

    liste_niveau = ["Facile", "Intermédiaire", "Difficile"]

    score = score
    domaine = domaine
    index_level = liste_niveau.index(niveau)
    niveau = niveau.capitalize()
    if (liste_niveau.index(niveau) + 1) < 3:
        score_recu, data = level(domaine[choice-1], file_of_game, niveau)
        validate_level = point_moyen(data,niveau)
        score[domaine[choice - 1]][niveau] = score_recu

        if score_recu >= validate_level:
            print('')
            print(Fore.LIGHTWHITE_EX + "Bravo !!! Votre score après jeu:",score[domaine[choice-1]][niveau])
            print('')

            if "_" in domaine[choice - 1]:
                liste = domaine[choice - 1].split("_")
                print(Fore.LIGHTMAGENTA_EX + f"Félicitation vous passez au niveau {liste_niveau[index_level+1]} du domaine {liste[0].capitalize()} {liste[1].capitalize()}")
            else:
                print(Fore.LIGHTMAGENTA_EX + f"Félicitation vous passez au niveau {liste_niveau[index_level+1]} du domaine {domaine[choice-1].capitalize()}")
            return score, liste_niveau[index_level+1]
        else:
            print('')
            print(Fore.LIGHTWHITE_EX + f"Dommage :) Votre score après jeu: {Fore.RED} {score[domaine[choice - 1]][niveau]} {Fore.LIGHTWHITE_EX} ne vous permet pas de passer au niveau suivant.\nAvoir au moins {Fore.LIGHTGREEN_EX} {validate_level} {Fore.LIGHTWHITE_EX} pour passer au niveau suivant.")
            print('')
    else:
        if "_" in domaine[choice-1]:
            liste = domaine[choice-1].split("_")
            print(Fore.LIGHTMAGENTA_EX + f"Félicitation vous avez terminer tous les niveaux du domaine {liste[0].capitalize()} {liste[1].capitalize()}")
        else:
            print(Fore.LIGHTMAGENTA_EX + f"Félicitation vous avez terminer tous les niveaux du domaine {domaine[choice-1]}")

    return score, niveau

def point_moyen(data:list[dict[str, dict]], niveau: str) -> int:

    """
    Cette fonction calcule automatiquement
    le point moyen pour valider un niveau
    :param data: dict
    :param niveau: str
    :return: float
    """

    moyen = 0

    data = data[niveau]

    for element in data:
        moyen += element["points"]

    moyen = round(((moyen*70)/100))
    return moyen

def condition_jeu(domaine, choix, score, niveau:str, file_of_game:Path):

    domaine = domaine

    score = score

    score, niveau = level_validate(domaine, choix, score, niveau, file_of_game)

    return score, niveau
