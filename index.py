import json
from import_export_data  import importer, file

menu = """
        Choisir votre niveau de difficulté:
        
        1  - Facile
        2  - Intermediaire
        3  - Difficile
        
"""
print(menu)

choix = input("Veuillez saisir: ")

if choix == "1":
    #print(json.dumps(importer(file, "Facile"),indent = 2))
    niveau_facile_charge = importer(file,"Facile")
    print(niveau_facile_charge.keys())

if choix == "2":
    niveau_intermediaire_charge = importer(file,"Intermédiaire")
    print(niveau_intermediaire_charge.keys())

if choix == "3":
    niveau_difficile_charge = importer(file,"Difficile")
    print(niveau_difficile_charge.keys())
    

