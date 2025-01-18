"""class game"""
# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
DEBUG = False

class Game:
    """class game"""

    # Constructor
    def __init__(self):
        """mise en place du jeu"""
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.item = {}
        self.character = {}



    # Setup the game
    def setup(self):
        """mise en place du jeu"""
        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        take = Command("take", " <objet> : sprendre l'objet", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " <objet> : retirer l'objet", Actions.drop, 1)
        self.commands["drop"] = drop
        look = Command("look", " : afficher les objets de la piece", Actions.look, 0)
        self.commands["look"] = look
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)",
         Actions.go, 1)
        self.commands["go"] = go
        vide = Command(" ", "saute la ligne sans message d'erreur", Actions.vide, 0)
        self.commands[""] = vide
        back = Command("back", "retourner en arriere", Actions.back, 0)
        self.commands["back"] = back
        history = Command("history", "retourner en arriere", Actions.history, 0)
        self.commands["history"] = history
        inventory = Command("inventory", " : afficher votre inventaire", Actions.inventory, 0)
        self.commands["check"] = inventory
        talk = Command("talk", " <someone> : parler à un personnage non joueur", Actions.talk, 1)
        self.commands["talk"] = talk
        # Setup rooms

        gare = Room("StCharles", "la gare de Saint Charles en plein centre ville de Marseille.")
        self.rooms.append(gare)
        vport = Room("Vieux_Port", "le vieux port de Marseille, de rencontre.")
        self.rooms.append(vport)
        ruestfe = Room("Rue-Stfe", "la rue Saint Feriol,\
 connue pour ses boutiques et sa proximité avec le Port.")
        self.rooms.append(ruestfe)
        terrasses = Room("Terrasses", "les Terrasses du Port,\
 le centre commercial phare de Marseille avec son rooftop à couper le souffle.")
        self.rooms.append(terrasses)
        terrasses_1 = Room("Terrasses_1", "le premier étage des terrasses du port.")
        self.rooms.append(terrasses_1)
        prado = Room("Le_Prado", "le Prado,\
 un endroit magique pour les touristes et les locaux en face de la mer.")
        self.rooms.append(prado)
        cafe = Room("Café", "un café animé où l'on peut trouver des supporters\
 de l'Olympique de Marseille.")
        self.rooms.append(cafe)
        quartiern = Room("Quartier_Nord", "Les quartiers nord de Marseille à éviter.")
        self.rooms.append(quartiern)
        notre_dame = Room("Nôtre Dame",  "Notre dame de la garde\
 le point le plus haut de Marseille.")
        self.rooms.append(notre_dame)

        # Create exits for rooms

        gare.exits = {"N" : cafe,"E" : ruestfe ,"S" : terrasses}
        vport.exits = {"N" : ruestfe,"E" : prado,"O" : terrasses}
        ruestfe.exits = {"E" : notre_dame, "S" : vport, "O" : gare}
        terrasses.exits = {"N" : gare, "E" : vport, "U" : terrasses_1}
        terrasses_1.exits = {"D" : terrasses}
        prado.exits = {"N" : notre_dame, "O" : vport}
        cafe.exits = {"S" : gare, "N" : quartiern}
        quartiern.exits = {"S" : cafe}
        notre_dame.exits = {"O" : ruestfe, "S" : prado}

        # ajout des objets aux salles de base
        cagoule = Item("cagoule", "une cagoule qui vous permet de passer inaperçu", 0.2)
        gare.add_item(cagoule)
        telescope = Item("telescope", "un télescope cassé", 7)
        notre_dame.add_item(telescope)
        croissant = Item("croissant", "un croissant bien bon", 0.1)
        prado.add_item(croissant)
        malette = Item("malette", "une malette signée pécheur du vieux port", 6)
        maillot= Item("maillot", "un maillot de l'om", 0.7)
        centeuros = Item("100$", "Une belle somme d'argent", 0.1)
        pain = Item("pain", "du pain parfait pour attirer les pigeons", 1)

        # ajout des pnj
        mvoyageur = Character("Voyageur",\
             "Ce mysterieux voyageur semble vous regarder, il serait surement \
                interréssant d'aller lui parler", gare,\
                     ["Ehh", "Psssssttt", "Viens par ici j'ai quelque chose pour toi",\
                         "Voici une malette pour toi. Bon courage !"], item_to_give=malette)
        gare.add_character(mvoyageur)
        pecheurg = Character("Pécheur", "Ce pécheur n'a pas l'air commode mais\
 semble chercher quelque chose. Aller le voir serait une bonne idée.", vport, \
["Eh toi !", "Oh tu me\
 ramènes ma malette, tiens voici du pain en échange !"],\
 item_to_give=pain, required_items=malette)
        vport.add_character(pecheurg)
        pigeon = Character("Pigeon","Des pigeons enragés\
 vous attendent, leur chef souhaite vous parler", \
notre_dame, ["Rooouu, Rouu", "Les pigeons s'envolent et laissent 100$"]\
    , item_to_give=centeuros, required_items=pain)
        notre_dame.add_character(pigeon)
        vendeurom = Character("Vendeur", "Ce vendeur de l'om vous \
dévisage, il a surement remarqué que vous n'étiez pas d'ici, trouvez un moyen pour\
 qu'il vous apprécie", terrasses_1,\
 ["Tu n'es pas d'ici toi", "tiens, un conseil achète ce magnifique maillot\
 de l'om il te servira !", \
"Tiens prends ça c'est la maison qui offre"], item_to_give=maillot, required_items=centeuros)
        terrasses_1.add_character(vendeurom)
        supporters = Character("Supporters", "Ces supporters n'accepterons qu'un fan de l'om", \
prado, ["Quel magnifique maillot", "Bienvenue parmis nous !"], required_items=maillot)
        cafe.add_character(supporters)


        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = gare


    def check_defeat(self):
        """Vérifie si le joueur remplit les conditions de défaite."""
        bagage_item = next((item for item in self.player.inventory \
            if item.name.lower() == 'cagoule'), None)
        if self.player.current_room.name == "Quartier_Nord" and not bagage_item: \
             # Si l'objet "maillot" est trouvé dans l'inventaire
            print("\nVous êtes entré dans les Quartiers Nord sans cagoule. \
Les habitants vous ont demasqué. C'est trop dangereux...\n"
                  "Vous avez perdu !")
            self.finished = True  # Terminer le jeu
            return True

    def move_npcs(self):
        """Déplace tous les PNJs après chaque tour et affiche \
un message de débogage si nécessaire."""
        if DEBUG:
            print("[DEBUG] Déplacement des PNJs")  # Affichage dans le mode débogage

        un_pnj_bouge = False  # Variable pour suivre si un PNJ a bougé

        for room in self.rooms:
            for npc in room.character[:]:  # Itération sur une copie pour éviter les problèmes
                if npc.move():  # Si le PNJ se déplace
                    un_pnj_bouge = True  # Un PNJ a bougé, on met à True

                    if DEBUG:  # Afficher des informations si en mode débogage
                        print(f"[DEBUG] {npc.name} n'a pas bougé de {npc.current_room.name}.")

    # Retourne True si au moins un PNJ s'est déplacé, sinon False
        if DEBUG:
            if not un_pnj_bouge:
                print("[DEBUG] Aucun PNJ n'a bougé.")

        return un_pnj_bouge  # Retourne True si un PNJ a bougé, sinon False

    # Play the game
    def play(self):
        """chaque tour de jeu"""
        if DEBUG:
            print("Le jeu peut commencer")

        self.setup()

        self.print_welcome()

        self.move_npcs()

        # Boucle principale du jeu
        while not self.finished:

            # Obtenir la commande du joueur
            command_string = input("> ")
            self.process_command(command_string)

        return None

    # Process the command entered by the player
    def process_command(self, command_string):
        """savoir lacommande tapée par le player"""
        # Séparer la commande et les arguments
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # Si la commande n'est pas reconnue
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez\
 'help' pour voir la liste des commandes disponibles.\n")
        else:
            command = self.commands[command_word]
            command.action(self, self, list_of_words, command.number_of_parameters)
        self.check_defeat()


    # Print the welcome message
    def print_welcome(self):
        """dire bonjour"""
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure ! Vous incarnez \
un supporter du QSG en reconversion.\nVous souhaitez commencer a supporter le sublime\
 Olympique de Marseille.\nPour ce faire vous devez integrer un groupe de supporter. Bonne chance !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())


def main():
    """boucle principale"""
    # Create a game object and play the game
    Game().play()


if __name__ == "__main__":
    main()
