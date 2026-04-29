""" A RPG game that allows the player to do simple things like move, fight, and
        use an inventory
        

"""


class RPG:
    """ the big class for the RPG game, full runner
    """
<<<<<<< HEAD
    
    def inventory_algorithm(inventory, item_name, player_hp, enemy_frozen):
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

=======
    
>>>>>>> 1a49229eb61d7e4bf440a3140eb08a46b7e75fac

def move_player(
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
    #Check if the tile is blocked 
    if game_map[new_row][new_col] == "#": 
        return position
    
    #Move is valid
    return (new_row, new_col)