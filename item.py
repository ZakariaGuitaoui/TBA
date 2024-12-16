# Classe Item pour gérer les objets
class Item:
    def __init__(self, weight, name, description):
        """Initialise un objet Item avec son poids, nom et description."""
        self.weight = weight  # Le poids de l'objet, en kilogrammes ou autre unité
        self.name = name  # Le nom de l'objet
        self.description = description  # Une description textuelle de l'objet

    def __str__(self):
        """Retourne une représentation textuelle de l'objet."""
        return f"Nom : {self.name}\nPoids : {self.weight} kg\nDescription : {self.description}"

# Fonctions pour gérer l'inventaire
def creer_inventaire():
    """Crée et retourne un inventaire vide (un dictionnaire)."""
    return {}

def ajouter_item(inventaire, item):
    """Ajoute un item à l'inventaire. Remplace si le nom existe déjà."""
    if not isinstance(item, Item):
        print("Erreur : Seuls les objets de type 'Item' peuvent être ajoutés à l'inventaire.")
        return

    if item.name in inventaire:
        print(f"Attention : L'objet '{item.name}' existe déjà et sera remplacé.")
    inventaire[item.name] = item
    print(f"L'objet '{item.name}' a été ajouté à l'inventaire.")

def retirer_item(inventaire, nom_item):
    """Retire un item de l'inventaire par son nom."""
    if nom_item in inventaire:
        del inventaire[nom_item]
        print(f"L'objet '{nom_item}' a été retiré de l'inventaire.")
    else:
        print(f"Erreur : Aucun objet nommé '{nom_item}' n'a été trouvé dans l'inventaire.")

def afficher_inventaire(inventaire):
    """Affiche tous les objets dans l'inventaire."""
    if not inventaire:
        print("L'inventaire est vide.")
    else:
        print("Contenu de l'inventaire :")
        for item in inventaire.values():
            print(f"- {item.name} ({item.weight} kg): {item.description}")
