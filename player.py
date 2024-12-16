class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []


    dico = {
        "N": ["nord", "n"], "S": ["sud", "s"], "E": ["est", "e"],
        "O": ["ouest", "o"], "U": ["up", "u"], "D": ["down", "d"]
    }

    def move(self, direction):
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
        self.current_room = next_room
        self.history.append(self.current_room)
        print(self.current_room.get_long_description())
        print(self.get_history())
        return True

    def get_history(self):
        if not self.history:
            return f"\nVous n'avez pas encore visité de salle.\n"
        else :
            ddd = [room.name for room in self.history]
            return f"\n\nVous avez deja visité les salles suivantes : \n" + "\n".join(ddd)




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

