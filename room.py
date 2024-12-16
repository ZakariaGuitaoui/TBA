# Define the Room class.

class Room:
    """
    The class of the different rooms that are in the game, each room define by a name, a description and an exit.

    Attributes: 
        name (str) : The room's name
        items (str) : The objects that are in the room
        descritption (str) : The room's description
        exits (dict) : The different exits in the room.

    Methodes:
        get_exit : check if the direction wanted by the player is allowed (if the room's exit exist)
        get_exit_string : return room's exit description
        get_long_description : return a long description of the room's exit
        __init__ : constructor of the class
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
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"
