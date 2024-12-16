# Description: Game class

# Import modules
from item import Item
from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        command_vide = Command("","saute la ligne", Actions.vide, 0)
        self.commands[""] = command_vide
        back = Command("Back","<direction> : revenire à la dernière room", Actions.back, 0)
        self.commands["back"] = back
        history = Command("history"," Afficher l'historique", Actions.history, 0)
        self.commands["history"] = history
        # Setup rooms

        gare = Room("StCharles", "la gare de Saint Charles en plein centre ville de Marseille.")
        self.rooms.append(gare)
        vport = Room("Vieux_Port", "le vieux port de Marseille, lieu de rendez-vous et de rencontre.")
        self.rooms.append(vport)
        ruestfe = Room("Rue-Stfe", "la rue Saint Feriol, iconique pour ses boutiques et sa proximité avec le Port.")
        self.rooms.append(ruestfe)
        terrasses = Room("Terrasses", "les Terrasses du Port, le centre commercial phare de Marseille avec son rooftop à couper le souffle.")
        self.rooms.append(terrasses)
        terrasses_1 = Room("Terrasses_1", "le premier étage des terrasses du port.")
        self.rooms.append(terrasses_1)
        prado = Room("Le_Prado", "le Prado, un endroit magique pour les touristes et les locaux en face de la mer.")
        self.rooms.append(prado)
        bar = Room("Bar", "un bar animé où l'on peut trouver des supporters de l'Olympique de Marseille.")
        self.rooms.append(bar)
        quartiern = Room("Quartier_Nord", "Les quartiers nord de Marseille à éviter.")
        self.rooms.append(quartiern)        
        Notre_dame = Room("Nôtre Dame",  "Notre dame de la guarde le point le plus haut de Marseille.")
        self.rooms.append(Notre_dame)

        # Create exits for rooms

        forest.exits = {"N" : cave, "E" : tower, "S" : castle, "O" : None}
        tower.exits = {"N" : cottage, "E" : None, "S" : swamp, "O" : forest}
        cave.exits = {"N" : None, "E" : cottage, "S" : forest, "O" : None}
        cottage.exits = {"N" : None, "E" : None, "S" : tower, "O" : cave}
        swamp.exits = {"N" : tower, "E" : None, "S" : None, "O" : castle}
        castle.exits = {"N" : forest, "E" : swamp, "S" : None, "O" : None}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = gare

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()