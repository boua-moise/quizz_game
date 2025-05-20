import json
from pathlib import Path

def exported(file):
    with open(file, "r", encoding="UTF-8") as f:
        bd_content: dict = json.load(f)
        return bd_content

def imported(file,content):
    with open(file, "w", encoding="UTF-8") as f:
        json.dump(content, f, indent=4, ensure_ascii=False)

def sauvegarde(email: str, password: str, score, niveau:dict, file_of_game:Path):
    db_content: dict = exported(file_of_game)
    for user in db_content["Users"]:
        if email == user["email"] and password == user["password"]:
            user["score"] = score
            user["niveau"] = niveau
            print("Données sauvegardées avec succès...")
    imported(file_of_game, db_content)

if __name__ == "__main__":
    file_quizz = Path().cwd().parent / "data/data_base_of_quizz_game.json"
    file_users = Path().cwd().parent / "data/count_user.json"

    print(Path().cwd().parent)
    contenu = exported(file_quizz)
    print(contenu)
    contenu = exported(file_users)
    print(contenu)

