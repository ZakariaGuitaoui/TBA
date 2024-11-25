# Define the Player class.
class Player():
    """
    Cette classe represente le player (joueur) du jeu.

    Attributs :
    name (str) : Le nom choisi par le joueur
    current_room : La piece ou se situe le joueur

    Methode :
        __init__ : Constructeur de la classe
    
    """
    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    
