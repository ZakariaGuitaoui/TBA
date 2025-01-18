"""class action"""
# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with
# the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:
    """class action definisssant les actions possibles"""
    def go(self, game, list_of_words, number_of_parameters):
        """Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False"""

        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction = list_of_words[1]
        # Move the player in the direction specified by the parameter.
        player.move(direction)
        return True

    def quit(self, game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(self, game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True


    def vide(self, game, list_of_words, number_of_parameters) :
        """reconnaitre et gérer une commande vide"""
        print("")
        return True


    def back(self, game, list_of_words, number_of_parameters):
        """retour en arriere"""
        player = game.player
        l = len(list_of_words)

    # Vérifier si le bon nombre de paramètres est fourni
        if l != number_of_parameters + 1:  # +1 car la commande elle-même est comptée
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            # Utilise MSG0 car aucun paramètre attendu
            return False

    # Appeler la méthode `moveback` du joueur pour revenir en arrière
        success = player.moveback()

        if not success:
            print("Impossible de revenir en arrière.")
            return False

        return True

    def inventory(self, game, list_of_words, number_of_parameters):
        """connnaitre l'inventaire du joueur"""
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        player = game.player
        inventory = player.show_inventory()  # Récupère directement la chaîne de l'inventaire
        print(inventory)  # Affiche la chaîne retournée par show_inventory
        return True

    def take(self, game, list_of_words, number_of_parameters):
        """recuperer un objt dans l'inventaire"""
    # Vérifier si le bon nombre de paramètres est fourni
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

    # Récupérer le nom de l'objet depuis la commande
        item_name = list_of_words[1]

    # Vérifier si l'objet existe dans la pièce actuelle
        player = game.player
        current_room = player.current_room
        item = current_room.get_item(item_name)

        if not item:
            print(f"L'objet '{item_name}' n'est pas dans cette pièce.")
            return False

    # Ajouter l'objet à l'inventaire du joueur
        player.add_item(item)

    # Retirer l'objet de la pièce
        current_room.remove_item(item)

        print(f"Vous avez pris l'objet: {item}")
        return True

    # Ajouter l'objet à l'inventaire du joueur
        player.add_item(item)

    # Retirer l'objet de la pièce
        current_room.drop_item(item)

        print(f"Vous avez pris l'objet: {item}")
        return True

    def drop(self, game, list_of_words, number_of_parameters):
        """deposer un objet de l'inventaire"""
    # Vérifier si le bon nombre de paramètres est fourni
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            # Utilise MSG1 car un paramètre est attendu
            return False

    # Récupérer le nom de l'objet depuis la commande
        item_name = list_of_words[1]

    # Vérifier si l'objet existe dans l'inventaire du joueur
        player = game.player
        item = player.get_drop(item_name)

        if not item:
            print(f"L'objet '{item_name}' n'est pas dans votre inventaire.")
            return False

    # Retirer l'objet de l'inventaire du joueur
        player.drop_item(item)

    # Ajouter l'objet à la pièce où se trouve le joueur
        current_room = player.current_room
        current_room.add_item(item)

        print(f"Vous avez déposé l'objet: {item}")
        return True

    def look(self, game, list_of_words, number_of_parameters):
        """
        Affiche la description de la pièce, y compris les objets présents.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

    # Récupérer le joueur et la pièce actuelle
        player = game.player
        current_room = player.current_room

    # Afficher la description de la pièce, y compris les objets
        print(current_room.get_long_description())  # Pas d'argument supplémentaire
        return True

    def history (self, game, list_of_words, number_of_parameters):
        """l'historique de jeu du player"""
        player = game.player
        l = len(list_of_words)

    # Vérifier si le bon nombre de paramètres est fourni
        if l != number_of_parameters + 1:  # +1 car la commande elle-même est comptée
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            # Utilise MSG0 car aucun paramètre attendu
            return False

        historique = player.get_history()
        print(historique)
        return True

    def talk(self, game, command_words, n):
        """Parler à un PNJ"""
        if len(command_words) < 2:
            print("\nVous devez spécifier à qui vous voulez parler. Exemple\
 : 'talk <nom du PNJ>'\n")
            return False

        npc_name = command_words[1].lower()  # Le nom exact du PNJ que le joueur veut rencontrer
        current_room = game.player.current_room

        # Rechercher le PNJ dans la salle actuelle en faisant une correspondance exacte
        found_npc = None
        for npc in current_room.character:
            # Vérification si le nom du PNJ correspond exactement au nom donné par le joueur
            if npc_name == npc.name.lower():  # Comparaison exacte du nom
                found_npc = npc
                break

        if not found_npc:
            print(f"\nIl n'y a personne dont le nom correspond\
 exactement à '{npc_name}' dans cette salle.\n")
            return False

        # Si le PNJ trouvé est "Les Supporters", gestion spéciale
        if "supporters" in found_npc.name.lower():
            maillot_item = next((item for item in game.player.inventory if \
                item.name.lower() == 'maillot'), None)
            if maillot_item:  # Si l'objet "maillot" est trouvé dans l'inventaire
                print("\nFélicitations ! Les Supporters ont adoré\
 votre magnifique maillot de l'OM, c'est le meilleur club ! Vous avez gagné en\
 parlant aux supporters avec un maillot !")
                game.finished = True  # La condition de victoire est atteinte, terminer le jeu
                return True

        # Si ce n'est pas "Les Supporters", dialogue normal
        print(f"\nVous parlez à {found_npc.name}: {found_npc.get_msg(game.player)}\n")
        return True
