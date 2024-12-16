# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.retour = [""]
        self.inventaire = None

    dico = {
        "N": ["nord", "n"], "S": ["sud" ,"s"], "E" : ["est", "e"],
        "O": ["ouest", "o"], "U": ["up", "u"], "D" : ["down", "d"]
    }


    def move(self, direction):
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

        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        self.history.append(self.current_room)
        self.current_room = next_room
        print(self.current_room.get_long_description())
        print(self.get_history())
        return True

    