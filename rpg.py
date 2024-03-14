import random

class tiger:
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense

class Monster:
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense

def battle(tiger, monster):
    print(f"A {monster.name} appears!")
    while tiger.health > 0 and monster.health > 0:
        tiger_attack = random.randint(1, tiger.strength)
        monster_attack = random.randint(1, monster.strength)
        tiger_defense = random.randint(1, tiger.defense)
        monster_defense = random.randint(1, monster.defense)

        tiger_damage = max(0, tiger_attack - monster_defense)
        monster_damage = max(0, monster_attack - tiger_defense)

        tiger.health -= monster_damage
        monster.health -= tiger_damage

        print(f"{tiger.name} attacks {monster.name} for {tiger_damage} damage!")
        print(f"{monster.name} attacks {tiger.name} for {monster_damage} damage!")
        print(f"{tiger.name} has {tiger.health} health remaining!")
        print(f"{monster.name} has {monster.health} health remaining!")

    if tiger.health > 0:
        print(f"{tiger.name} defeats {monster.name}!")
    else:
        print(f"{tiger.name} has been defeated by {monster.name}.")

# Create the player and monster
tiger = tiger("Hero", 100, 10, 5)
monster = Monster("Goblin", 50, 5, 2)

# Start the battle
battle(tiger, monster)
