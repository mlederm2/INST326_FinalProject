import random

def enemy_reaction(enemy_name, current_hp, max_hp, incoming_damage, is_transformed):
    """
    Handles the enemy's combative response when attacked.
    
    Args:
        enemy_name (str): The name of the monster.
        current_hp (int): The monster's HP before the hit.
        max_hp (int): The monster's starting HP.
        incoming_damage (int): The damage the player is trying to deal.
        is_transformed (bool): Whether the monster has already mutated.
        
    Returns:
        tuple: (actual_damage_taken, updated_transform_status)
    """
    
    if random.random() < 0.20:
        print(f"The {enemy_name} dodged your attack! 0 damage dealt.")
        return 0, is_transformed

   
    projected_hp = current_hp - incoming_damage
    if projected_hp <= (max_hp * 0.3) and not is_transformed and projected_hp > 0:
        print(f"\n--- WARNING: {enemy_name} is evolving! ---")
        print(f"The monster glows with a dark aura and hardens its skin.")
        is_transformed = True
        incoming_damage = incoming_damage // 2 
        
    return incoming_damage, is_transformed