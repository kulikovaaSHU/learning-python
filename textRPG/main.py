import random


# Functions:
# player attacks
def attack(damage1, damage2, enemy_health):
    enemy_health -= roll_dice(damage1, damage2)
    return enemy_health


# monster attacks
def monster_attacks(damage1, damage2, monster_health):
    monster_health -= roll_dice(damage1, damage2)
    return monster_health


# random number generator
def roll_dice(min_num, max_num):
    result = random.randint(min_num-1, max_num)
    return result


# random monster name
def random_name():
    monster_names = ["Evilsaur", "Badrex", "Pterodevil", "Darksaur", "Shadowrex", "Gloomsaur", "Killrex"]
    roll = roll_dice(0, len(monster_names))
    return monster_names[roll-1]


# random monster type generator
def random_type():
    monster_types = ["Fire", "Water", "Wind", "Ground", "Evil", "Plant"]
    roll = roll_dice(0, len(monster_types))
    return monster_types[roll-1]


# random monster generator
def random_monster():
    monster = [random_name(), random_type(), roll_dice(40, 100), roll_dice(5, 18), roll_dice(8, 20), roll_dice(8, 13),
               roll_dice(20, 35), roll_dice(4, 8), roll_dice(10, 12)]
    return monster


# output all monster info
def output_monsters(all_monsters):
    for monster in all_monsters:
        print("\nName: " + monster[0] + "\nType: " + monster[1] + "\nHealth: " + str(monster[2]) + "\nAttacks: \n" +
              monster[5] + "\n" + monster[8] + "\nHeal: \n" + monster[11])


# Monsters:
aquarex = ["Aquarex", "Water", 110, 15, 20, "Splash: 15-20 damage", 10, 35, "Wave: 10-35 damage", 10, 15,
           "Refresh: 10-15 heal"]
inferosaur = ["Inferosaur", "Fire", 90, 18, 23, "Spark: 18-23 damage", 15, 38, "Ignite: 15-38 damage", 8, 12,
              "Rest: 8-12 heal"]
pterowind = ["Pterowind", "Wind", 100, 18, 20, "Ruffle: 18-20 damage", 15, 35, "Sky Dive: 15-35 damage", 10, 12,
             "Nest: 10-12 heal"]
all_my_monsters = [aquarex, inferosaur, pterowind]

# Introduction:
print("\nLoading <3 <3 <3\n")
print("         ~Little Monsters~\n\n")

new_monster = random_monster()
print("A wild " + new_monster[0] + " (" + new_monster[1] + ") appears!\n")

print("Which monster do you choose?\n")
output_monsters(all_my_monsters)

monster_pick = input("\nEnter monster's name to call it out: ")