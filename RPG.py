""" A RPG game that allows the player to do simple things like move, fight, and
    use an inventory
    

"""




def combat_algorithim(creature1, creature2):
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
    """
    
    c1HP = creature1.getHP
    c2HP = creature2.getHP
    
    currentturn = "c1"
    
    while c1HP > 0 or c2HP > 0:
        if currentturn == "c1":
            action = input("Please choose what action you would like to do \n Attack, Use Inventory, Defend \n")
            if action == "Attack":
                dmg = creature1.attack()
                c2HP -= dmg
            elif action == "Use Inventory":
                item = input("Please choose what item to use: \n health_potion, mega_potion, or freeze_orb")
                c1HP, enemy_frozen = inventory_algorithm(creature1.inventory(), item, c1HP)
            elif action == "Defend":
                c1armor += 1
            else:
                print("Sorry that action isn't defined, please try again")
                continue
            currentturn = "c2"
        
        if currentturn == "c2":
            if enemy_frozen:
                currentturn = "c1"
                print(f"The {creature2.name()} is frozen and loses its turn!")
                continue
            else:
                dmg = enemy_intelligence()
                c1HP-= (dmg-c1armor)
                currentturn = "c1"
            
            
        
    if c1HP > 0 and c2HP <= 0:
        print(f"{creature1.name} won the combat")
    else:
        print(f"{creature1.name} lost the combat, better luck next time")

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


def move_player(position: tuple[int, int], direction: str, game_map: 
        list[list[str]]) -> tuple[int, int]:
    """
    An algorithm that controls how the player moves around the map.

    It checks the direction the player wants to move and makes sure the move is
    valid.
    If the space is open and within the map, the player moves there. If not, 
    the player stays in the same spot.

    Args:
        position (tuple[int, int]): The player’s current location on the map.
        direction (str): The direction the player wants to move 
        ("up", "down", "left", "right").
        game_map (list[list[str]]): A grid that represents the map and 
        shows open or blocked spaces.

    Returns:
        tuple[int, int]: The updated position of the player after the move.

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

    if direction not in moves:
        raise ValueError("Invalid direction. Choose up, down, left, or right.")

    d_row, d_col = moves[direction]
    new_row = row + d_row
    new_col = col + d_col

    for r in range(len(game_map)):
        for c in range(len(game_map[0])):

            if r == new_row and c == new_col:

                
                if game_map[r][c] != "#":
                    return (r, c)

                return position

    return position


class Creature:

    def attack(self):
        return 5
    def getname(self):
        return "I am a robot beep boop bop"
    def inventory(self):
        return ["health_potion","health_potion","health_potion","health_potion"]