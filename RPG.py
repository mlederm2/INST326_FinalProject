import random
import Creature
import json
import YouKilledMe


class RPG:
    
    def __init__(self, player, enemy_file, map_file):
        
        linelist=[]
        with open(map_file, "r", encoding="utf-8") as infile:
            for line in infile:        
                for character in line:
                    linelist.append(character)
            self.map.append(linelist)
            
        with open(enemy_file, "r", encoding="utf-8") as enemies:
                self.enemy = json.load(enemies)
                
        
        self.player_char = player

    
    def enemy_reaction(self, incoming_damage, current_hp, is_transformed):
        """
            Handles the enemy's combative response when attacked.

        Args:
            enemy_name (str): The name of the monster.
            current_hp (int): The monster's HP before the hit.
            max_hp (int): The monster's starting HP.
            incoming_damage (int): The damage the player is trying to deal.
            is_transformed (bool): Whether the monster has already mutated.
            
        Returns:
            tuple: (Damage Dealt, Current Health)
            
        Written By Derek Happy, Edits by Moshe Lederman
            """

        outgoing_damage = 0
        projected_hp = current_hp - incoming_damage

        #gives the enemy a random chance to dodge incoming attacks
        if random.random() < 0.20:
            #dodging attacks prevents damage from being dealt
            print(f"The {self.name} dodged your attack! 0 damage dealt.")
            current_hp+=incoming_damage
        #gives the enemy a chance to heal itself if its current health is less than
        # 1/3 its max health, and if it hasn't already healed
        elif projected_hp <= (self.HP * 0.3) and not is_transformed:
            print(f"--- WARNING: {self.name} is healing! ---")
            print(f"The {self.name} glows with a dark aura and hardens its skin.")
            current_hp, is_transformed = self.inventory_algorithm(["health_potion"],"health_potion",current_hp)
            is_transformed = True
        else:
            outgoing_damage = self.attack()
            
            
        return outgoing_damage, current_hp, is_transformed


    """ A RPG game that allows the player to do simple things like move, fight, and
    use an inventory


    """

    def inventory_algorithm(inventory, item_name, player_hp):
        """ 
        This algorithm provides a list of inventories. When a player requests an item, it
        checks the inventory list to see if it is available or not and applies it. When applied, the
        item is removed from the list.

        Args:
        inventory: list of items that can be used by players.
        item_name: the item the player wants to use.
        player_hp: current player health.
        enemy_frozen: Enemy freeze status.

        Returns:
        The updated status of the player and enemy frozen status.
        """
        enemy_frozen = False

        # To check if item exists in inventory
        if item_name not in inventory:
            print(f"'{item_name}' is not in your inventory!")
            return player_hp, enemy_frozen

        #To apply item effect
        if item_name == "health_potion":
            player_hp += 50
            print(f"Used Health Potion! HP restored. Current HP: {player_hp}")

        elif item_name == "mega_potion":
            player_hp += 100
            print(f"Used Mega Potion! HP fully boosted. Current HP: {player_hp}")

        elif item_name == "freeze_orb":
            enemy_frozen = True
            print("Used Freeze Orb! Enemy is now frozen!")

        #Remove item from inventory after use
        inventory.remove(item_name)
        print(f"'{item_name}' has been removed from your inventory.")
        return player_hp, enemy_frozen



    def combat_algorithim(self, creature1, creature2):
        """
        This algorithim provides the backbone for combat, calling the enemy
        intelligence when necessary and allowing the player to choose what to do
        on their turns

        Args:
            creature1: a creature assumed to be the player, has HP, name, and
                inventory attributes
            creature2: a creature assumed to be the monster that the players is
                fighting, has HP, and inventory attributes
                
        Side Effects:
            Can reduce HP of creatures 1 and 2

        Written by Moshe Lederman
        """

        c1HP = creature1.HP
        c2HP = creature2.HP

        currentturn = "c1"
        used_heal = False

        while c1HP > 0 or c2HP > 0:
            if currentturn == "c1":
                action = input("Please choose what action you would like to do \n Attack, Use Inventory, Defend \n")
                if action == "Attack":
                    dmg = creature1.attack()
                    c2HP -= dmg
                elif action == "Use Inventory":
                    item = input("Please choose what item to use: \n health_potion, mega_potion, or freeze_orb")
                    c1HP, enemy_frozen = self.inventory_algorithm(creature1.inventory, item, c1HP)
                elif action == "Defend":
                    c1armor += 1
                elif action == 'POWERWORDKILL':
                    print("POWERWORDKILL used, combat ended")
                    c2HP = 0
                else:
                    print("Sorry that action isn't defined, please try again")
                    continue
                currentturn = "c2"
            
            if currentturn == "c2":
                if enemy_frozen:
                    currentturn = "c1"
                    print(f"The {creature2.name} is frozen and loses its turn!")
                    continue
                else:
                    dmg, c2HP, used_heal = creature2.enemy_reaction(dmg, c2HP, used_heal)
                    c1HP-= (dmg-c1armor)
                    currentturn = "c1"
                
                
            
        if c1HP > 0 and c2HP <= 0:
            print(f"{creature1.name} won the combat")
        else:
            print(f"{creature1.name} lost the combat, better luck next time")



    def move_player(
        self,
        position: tuple[int, int], 
        direction: str, 
        game_map: list[list[str]]
    ) -> tuple[int, int]:
        """
        An algorithm that controls how the player moves around the map.

        It checks the direction the player wants to move and makes sure the move is
        valid.
        If the space is open and within the map, the player moves there. If not, 
        the player stays in the same spot.

        Args:
            position: Current (row, column) of the player
            direction: Direction to move ("up", "down", "left", "right")
            game_map: 2D grid representing the map

        Returns:
            The new (row, column) position after attempting the move

        Raises:
            ValueError: If the direction is invalid.
        """

        row, col = position

        moves = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }
        
        if direction == "POWERWORDKILL":
            raise YouKilledMe.YouKilledMe
        
        # Validate direction
        if direction not in moves:
            raise ValueError("Invalid direction. Choose up, down, left, or right.")

        #Calculate new position
        d_row, d_col = moves[direction]
        new_row = row + d_row
        new_col = col + d_col

        # Check map boundaries 
        if new_row < 0 or new_row >= len(game_map):
            return position
        if new_col < 0 or new_col >= len(game_map[0]): 
            return position
        
        tile = game_map[new_row][new_col]
        
        #Enemy detection 
        if tile == "E":
            self.start_combat((new_row, new_col))
            return position # stay in place during combat 
            #Moshe -- Does it make sense to move the player into the space the 
                #enemy was in after combat finishes assuming that the player wins?
                #it is possible for the player to lose combat.
        
        #Check if the tile is blocked 
        if tile == "#":
            return position

        #Move is valid
        return (new_row, new_col)

    def start_combat(self, enemy_pos):
        print(f"Encountered enemy at {enemy_pos}!")
        print("Combat started!")
        test = self.enemy["Enemy1"]
        
        
        enemy = Creature(test["Name"], test["Weapon"], test["HP"])
        
        self.combat_algorithim(PLAYER, enemy)
        # You can expand this later with HP and attacks)

def main():
    pass


#this comment line should replicate the error when I try to save this please

