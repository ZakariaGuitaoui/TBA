"""class character"""
import random

class Character:
    """class character"""
    def __init__(self, name, description, current_room, msgs,\
 item_to_give=None, required_items=None):
        """mise en place"""
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
        self.msg_index = 0  # Ajout de l'attribut msg_index pour suivre la phrase courante
        self.item_to_give = item_to_give  # L'objet à donner au joueur
# Liste des objets que le PNJ attend, peut être vide si aucun objet n'est attendu
        self.required_items = required_items if isinstance(required_items, list)\
 else [required_items] if required_items else []


    def __str__(self):
        """mise en place"""
        return f"{self.name}: {self.description}: {self.current_room}: {self.msgs}"

    def move(self):
        """Déplace le PNJ vers une pièce voisine et affiche un message de déplacement."""
        # Vérifie que la pièce actuelle a des sorties
        if not self.current_room.exits:
            print(f"{self.name} ne peut pas se déplacer car il \
n'y a pas de sorties dans la pièce {self.current_room.name}.")
            return False

        # Choisit de se déplacer ou pas (50% de chance)
        if random.choice([True, False]):
            # Retirer le PNJ de la pièce actuelle
            self.current_room.remove_character(self)

            # Choisir une nouvelle pièce aléatoire parmi les sorties de la pièce actuelle
            new_room = random.choice(list(self.current_room.exits.values()))

            # Afficher un message indiquant où le PNJ se déplace
            print(f"\n{self.name} se déplace de {self.current_room.name} vers {new_room.name}.")

            # Mettre à jour la pièce actuelle du PNJ
            self.current_room = new_room

            # Ajouter le PNJ à la nouvelle pièce
            self.current_room.add_character(self)

            return True  # Le PNJ a bougé avec succès

        else:
            print(f"\n{self.name} reste dans {self.current_room.name}.")\
                   # Message lorsque le PNJ ne se déplace pas
            return False  # Le PNJ a choisi de ne pas se déplacer
        return False  # Le PNJ a choisi de ne pas se déplacer

    def get_msg(self, player):
        """Retourne un message différent en fonction des\
 objets que possède le joueur et de ce que le PNJ attend."""
        # Vérifier si le joueur possède les objets nécessaires
        missing_items = [item for item in self.required_items if not player.has_item(item)]

        if missing_items:
            # Si le joueur ne possède pas les objets requis, ne dire que les objets manquants
            missing_item_names = ', '.join([item.name for item in missing_items])\
  # Accéder au nom de chaque objet manquant
            return f"{self.name} vous dit: 'Je vois qu'il vous\
 manque {missing_item_names}. Vous devez être plus équipé pour avancer.'"

        # Si tous les objets requis sont présents, continuer avec les messages standard
        if not self.msgs:
            return f"{self.name} n'a rien à dire pour le moment."

        msg = self.msgs[self.msg_index]
        self.msg_index += 1

        # Si on a atteint la fin des messages, réinitialiser l'index
        if self.msg_index >= len(self.msgs):
            self.msg_index = 0

            # Donner un objet au joueur si le PNJ en a un à offrir
            if self.item_to_give:
                player.add_item(self.item_to_give)  # Ajouter l'objet à l'inventaire du joueur
                msg += f"\n{self.name} vous donne {self.item_to_give.name}."
                self.item_to_give = None  # L'objet a été donné

        return msg
