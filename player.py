"""class player defini le joueur"""


class Player:
    """class player"""
    def __init__(self, name):
        """mise en place"""
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = []  # Liste d'objets du joueur


    dico = {
        "N": ["nord", "n"], "S": ["sud", "s"], "E": ["est", "e"],
        "O": ["ouest", "o"], "U": ["up", "u"], "D": ["down", "d"]
    }

    def move(self, direction):
        """changer de piece"""
        # Valider l'entrée utilisateur
        direction = direction.lower()
        next_room = None

        for key, values in self.dico.items():
            if direction in values:
                if self.current_room is not None:
                    next_room = self.current_room.exits.get(key)
                break
        else:
            print("Commande invalide\n")
            return False

        # Vérifier si next_room est accessible
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        # Mettre à jour la salle actuelle
        self.history.append(self.current_room)
        self.current_room = next_room
        print(self.current_room.get_long_description())
        print(self.get_history())
        return True

    def get_history(self):
        """recuperer l'historique du player"""
        if not self.history:
            print("\nVous n'avez pas encore visité de salle.\n")
        else :
            ddd = [room.name for room in self.history]
            print("\nVous avez deja visité les salles suivantes : \n" + "\n".join(ddd))


    def add_item(self, item):
        """Ajoute un objet à l'inventaire du joueur."""
        self.inventory.append(item)

    def drop_item(self, item):
        """Retirer un objet de l'inventaire du joueur."""
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print(f"L'objet '{item.name}' n'est pas dans votre inventaire.")

    def show_inventory(self):
        """Affiche l'inventaire du joueur."""
        if not self.inventory:
            return "L'inventaire est vide."
        return "\n".join(str(item) for item in self.inventory)



    def get_drop(self, item_name):
        """Retourne l'objet à déposer si trouvé dans l'inventaire,
        ou None si l'objet n'existe pas."""
        for item in self.inventory:
            if item.name == item_name:
                return item
        print(f"L'objet '{item_name}' n'est pas dans votre inventaire.")
        return None


    def moveback(self):
        """
        Permet au joueur de revenir dans la salle précédente.
        
        Returns:
            bool: True si le joueur revient dans la salle précédente, False sinon.
        """
        # Vérifier si l'historique contient des salles précédentes
        if not self.history:
            print("Vous êtes déjà à votre point de départ, impossible de revenir en arrière.\n")
            return False

        # Retirer la dernière salle de l'historique et revenir à la précédente
        previous_room = self.history.pop()
        self.current_room = previous_room

        # Afficher la description de la salle précédente
        print(f"\nVous revenez dans la salle précédente : {self.current_room.name}")
        print(self.current_room.get_long_description())
        print(self.get_history())
        return True

    def has_item(self, item):
        """Vérifie si le joueur possède un objet donné."""
        for inv_item in self.inventory:
            if inv_item.name.lower() == item.name.lower() :  # Comparer les noms des objets
                return True
        return False
