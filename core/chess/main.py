import time

class Player(object):
    hp = 100
    att = 100
    inventory = ['', '']
    weapon = "Empty"
    armor = "Empty"

enemies = [
    {
        "name": "skeleton",
        "hp": 50,
        "att": 10,
        "curse": None,
    },
    {
        "name": "goblin",
        "hp": 20,
        "att": 10,
        "curse": None,
    },
    {
        "name": "cursed sword",
        "hp": 30,
        "att": 30,
        "curse": "venom",
    },
]

print("Welcome to the dungeon...")
username = input("Name your warrior...")
userClass = input("Choose your class... (Warrior, Mage, Bloodknight, Thief)")
player = Player
if userClass == "Warrior":
    player.hp = 120
    player.att = 50
    player.inventory = ['Butterscotch Pie', 'Strength Potion']
    player.weapon = "Greatsword"
    player.armor = "Steel Chestplate"

elif userClass == "Mage":
    player.hp = 100
    player.att = 20
    player.inventory = ['Flame Potion', 'Mana Potion']
    player.weapon = "Water Staff"
    player.armor = "Magic Robe"

elif userClass == "Bloodknight":
    player.hp = 150
    player.att = 30
    player.inventory = ['Dragon Blood', 'Soulstone']
    player.weapon = "Chopping Axe"
    player.armor = "Black Cape"

elif userClass == "Thief":
    player.hp = 80
    player.att = 20
    player.inventory = ['Throwing Knife', 'Lockpick']
    player.weapon = "Iron Dagger"
    player.armor = "Leather Armor"

print("Your adventure begins...")
time.sleep(5)
