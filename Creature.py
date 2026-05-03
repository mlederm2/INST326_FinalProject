class Creature:
    """
    A default creature that can be used for both the player and enemies for the game
    
    Attributes:
            name (str): the name of the creature
            primeWeapon (dict): a dictionary containing the stats for a weapon, including name and damage
            HP (int): the HP of the creature
            inventory (list): a list of items that the creature has in their inventory

    """

    def __init__(self, name, pweapon, maxHP):
        """_summary_

        Args:
            name (str): the name of the creature
            pweapon (dict): a dictionary containing the stats for a weapon, including name and damage
            maxHP (int): the maximum HP of the creature
            inventory (list): a list of items that the creature has in their inventory
        
        Side Effects:
            Creates a new creature object
        """
        self.name = name
        self.primeWeapon = pweapon
        self.HP = maxHP
        self.inventory = []
        
    def attack(self):
        
        weapon = self.primeWeapon
        """
        Use the primary weapon of the creature to deal damage equal to the weapon's damage stat
        """
        damage = weapon["Damage"]
        return damage
    
    def pickUp (self, object):
        """
        Add new items to the inventory of the character
        """
        self.inventory.append(object)