""" A RPG game that allows the player to do simple things like move, fight, and
        use an inventory
        

"""


class RPG:
    """ the big class for the RPG game, full runner
    """
    
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

