# Define the Room class.

class Room:
    """
    La class des differentes Room (salles) qui sont dans le jeu

    Attributs: 
        name (str) : Le nom de la piece
        items (str) : Les objets de la piece
        descritption (str) : La description de la piece
        exits (dict) : Les differentes sorties de la piece

    Methodes:
        get_exit : voir si la direction demandee par le joueur existe ou non
        get_exit_string : renvoyer la description des sorties
        get_long_description : renvoyer une longue description de la sortie
        __init__ : constructeur de la classe
    """
    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
