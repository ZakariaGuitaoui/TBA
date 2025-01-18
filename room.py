"""class room"""
# Define the Room class.

class Room:
    """
    La classe des différentes pièces du jeu, chaque pièce est \
définie par un nom, une description, des objets et des sorties.
    
    Attributs : 
        name (str) : Le nom de la pièce.
        description (str) : La description de la pièce.
        items (list) : Les objets présents dans la pièce.
        exits (dict) : Les différentes sorties de la pièce, \
avec la direction comme clé et la pièce voisine comme valeur.

    Méthodes:
        get_exit : Vérifie si la direction demandée par le \
joueur est valide (si la sortie existe).
        get_exit_string : Retourne une description des sorties \
de la pièce.
        get_long_description : Retourne une description complète \
de la pièce, y compris les sorties.
        add_exit : Ajoute une sortie à la pièce.
        add_item : Ajoute un objet à la pièce.
    """

    # Définir le constructeur.
    def __init__(self, name, description):
        """mise en place"""
        self.name = name
        self.description = description
        self.items = []  # Liste des objets dans la pièce
        self.exits = {}  # Dictionnaire des sorties de la pièce
        self.character = [] # Dictionnaire des caracteres

    # Définir la méthode pour ajouter des sorties à la pièce.
    def add_exit(self, direction, room):
        """
        Ajoute une sortie à la pièce. La direction est associée à une autre pièce.
        
        Args:
            direction (str): La direction de la sortie (par exemple, 'nord', 'sud').
            room (Room): La pièce voisine dans la direction donnée.
        """
        self.exits[direction] = room

    # Ajouter un objet à la pièce.
    def add_item(self, item):
        """Ajoute un objet à la liste des objets dans la pièce."""
        self.items.append(item)

    def get_item(self, item_name):
        """Retourne un objet de la pièce si trouvé, ou None si l'objet n'existe pas."""
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def remove_item(self, item):
        """Retire un objet de la pièce."""
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"L'objet '{item.name}' n'est pas dans cette pièce.")

    def drop_item(self, item):
        """Dépose un objet dans la pièce, et l'enlève de l'inventaire du joueur."""
        self.add_item(item)  # Ajouter l'objet à la pièce

    def add_character(self, character):
        """
        Ajoute un personnage dans la pièce.

        Args:
            character (Character): Le personnage à ajouter.
        """
        self.character.append(character)  # Ajoute le personnage sans restriction.
        character.current_room = self
        return f"{character.name} a été ajouté à la pièce {self.name}."

    def remove_character(self, character):
        """Retire un personnage de la pièce."""
        if character in self.character:
            self.character.remove(character)


    # Méthode pour obtenir la sortie dans une direction donnée.
    def get_exit(self, direction):
        """recuperer une sortie"""
        # Retourne la pièce voisine dans la direction donnée si elle existe.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None

    # Retourne une chaîne décrivant les sorties de la pièce.
    def get_exit_string(self):
        """recuperer une sortie"""
        exit_string = "Sorties: "
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Retourne une description longue de la pièce, y compris les objets et les sorties.
    def get_long_description(self):
        """
        Retourne une description longue de la pièce.
        """
        # Objets
        if self.items:
            items_description = "Objets dans cette pièce: " \
+ ", ".join([item.name for item in self.items])
        else:
            items_description = "Aucun objet ici."

        # Personnages
        if self.character:
            character_description = "Personnes présentes : \
" + ", ".join([character.name for character in self.character])
        else:
            character_description = "Personne à l'horizon."

        # Retourne la description complète
        return (f"\nVous êtes dans {self.description}.\n\n"
                f"{items_description}\n"
                f"{character_description}\n"
                f"{self.get_exit_string()}\n")
