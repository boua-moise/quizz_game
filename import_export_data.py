import json

file = "data_base_of_quizz_game.json"

def importer(f:str,niveau:str) -> dict[list[dict]]:
    with open(f, 'r') as file:
        contenu = json.load(file)
    return contenu[niveau]

# def exporter(file:str, data:dict[list[dict]]) -> bool:
#     json.dump(data, file)
#     pass

if __name__ == "__main__":
    print(importer(file, "Difficile"))