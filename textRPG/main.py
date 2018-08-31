import random


# Functions:
# player attacks
def attack(damage1, damage2, enemy_health):
    damage = roll_dice(damage1, damage2)
    enemy_health -= damage
    print("\nDealt " + str(damage) + " damage.")
    return enemy_health


# monster attacks
def monster_attacks(damage1, damage2, monster_health):
    damage = roll_dice(damage1, damage2)
    monster_health -= damage
    print("\nTook " + str(damage) + " damage.")
    return monster_health


# random number generator
def roll_dice(min_num, max_num):
    result = random.randint(min_num, max_num)
    return result


# random monster name
def random_name():
    monster_names = ["Evilsaur", "Badrex", "Pterodevil", "Darksaur", "Shadowrex", "Gloomsaur", "Killrex"]
    roll = roll_dice(0, len(monster_names)-1)
    return monster_names[roll]


# random monster type generator
def random_type():
    monster_types = ["Fire", "Water", "Wind", "Ground", "Evil", "Plant"]
    roll = roll_dice(0, len(monster_types))
    return monster_types[roll-1]


# random monster generator
def random_monster():
    health = roll_dice(80, 150)
    monster = [random_name(), random_type(), health, roll_dice(10, 13), roll_dice(14, 25), roll_dice(13, 20),
               roll_dice(24, 35), roll_dice(6, 8), roll_dice(10, 12), health]
    return monster


# output all monster info
def output_monsters(all_monsters):
    for monster in all_monsters:
        print("\nName: " + monster[0] + "\nType: " + monster[1] + "\nHealth: " + str(monster[2]) + "\nAttacks: \n" +
              monster[5] + "\n" + monster[8] + "\nHeal: \n" + monster[11])


# Encounter
def encounter():
    new_monster = random_monster()
    print("A wild " + new_monster[0] + " (" + new_monster[1] + ") appears!\n")

    print("Which monster do you choose?")
    output_monsters(all_my_monsters)

    player_monster = monster_picker()
    print(player_monster)
    print(player_monster[0] + " go! ")
    returned = attack_main(new_monster, player_monster)
    print(returned)
    '''if player_monster[2] <= 0:
        print("\n" + player_monster[0] + " has fainted and can't fight anymore...")
        player_monster[13] = True
        if all_my_monsters[0][13] == True and all_my_monsters[1][13] == True and all_my_monsters[2][13] == True:
            print("\nAll of your monsters have fainted. You lose.")
            return True
        player_monster = monster_picker()'''


# pick monster
def monster_picker():
    monster_pick = input("\nEnter monster\'s name to call it out: ")
    if monster_pick != "Aquarex" and monster_pick != "Inferosaur" and monster_pick != "Pterowind":
        monster_pick = input("This monster doesn\'t exist. Enter monster\'s name to call it out (Aquarex, Inferosaur, "
                             "Pterowind): ")

    if monster_pick == "Aquarex":
        player_monster = aquarex
    elif monster_pick == "Inferosaur":
        player_monster = inferosaur
    elif monster_pick == "Pterowind":
        player_monster = pterowind

    if player_monster[13] == True:
        print("\n" + player_monster[0] + " has fainted and can't fight anymore... Pick a different monster.")
        monster_picker()

    return player_monster


# fight with current monster
def attack_main(monster, player_monster):
    print("\nYour turn!")
    print("\n" + player_monster[0] + "\'s health: " + str(player_monster[2]))
    print("Which move should " + player_monster[0] + " use?")
    # list attacks
    print("\n1. " + player_monster[5] + "\n2. " + player_monster[8] + "\n3. " + player_monster[11])
    move = int(input("Input move number (1, 2 or 3): "))
    if move > 3 or move < 1:
        move = int(input("Invalid choice. Input move number (1, 2 or 3): "))

    if move == 1:
        print("\n" + player_monster[0] + " used " + player_monster[5] + ".")
        monster[2] = attack(player_monster[3], player_monster[4], monster[2])
    elif move == 2:
        print("\n" + player_monster[0] + " used " + player_monster[8] + ".")
        monster[2] = attack(player_monster[6], player_monster[7], monster[2])
    elif move == 3:
        print("\n" + player_monster[0] + " used " + player_monster[11] + ".")
        if player_monster[2] != player_monster[12]:
            health_roll = roll_dice(player_monster[9], player_monster[10])
            if player_monster[2] + health_roll < player_monster[12]:
                player_monster[2] += health_roll
                print("\n" + player_monster[0] + "\'s health: " + str(player_monster[2]))
            elif player_monster[2] + health_roll >= player_monster[12]:
                player_monster[2] = player_monster[12]
                print("\n" + player_monster[0] + " is back to full health!")
        else:
            print("\nUsed a healing move, but already at full health...")

    if monster[2] <= 0:
        print("\n" + monster[0] + " has been defeated!")
        return player_monster
    else:
        # if monster not defeated he gets another turn
        print("\n" + monster[0] + "\'s turn...")
        move = roll_dice(1, 3)
        if move == 1:
            print("\n" + monster[0] + " used a short range attack!")
            player_monster[2] = monster_attacks(monster[3], monster[4], player_monster[2])
        elif move == 2:
            print("\n" + monster[0] + " used a long range attack!")
            player_monster[2] = monster_attacks(monster[5], monster[6], player_monster[2])
        elif move == 3:
            if monster[2] == monster[9]:
                print("\n" + monster[0] + " used a healing move, but already at full health...")
            elif monster[2] != monster[9]:
                health_roll = roll_dice(monster[7], monster[8])
                if monster[2] + health_roll < monster[9]:
                    monster[2] += health_roll
                    print("\n" + monster[0] + "\'s health: " + str(monster[2]))
                elif monster[2] + health_roll >= monster[9]:
                    monster[2] = monster[9]
                    print("\n" + monster[0] + " is back to full health...")

        if player_monster[2] <= 0:
            print("\n" + player_monster[0] + " has been defeated...")
            player_monster[13] = True
            return monster
        else:
            # if player monster not defeated he gets to attack again
            attack_main(monster, player_monster)


# Monsters:
aquarex = ["Aquarex", "Water", 110, 15, 20, "Splash: 15-20 damage", 10, 28, "Wave: 10-28 damage", 11, 15,
           "Refresh: 11-15 heal", 110, False]
inferosaur = ["Inferosaur", "Fire", 90, 18, 23, "Spark: 18-23 damage", 15, 33, "Ignite: 18-30 damage", 6, 10,
              "Rest: 6-10 heal", 90, False]
pterowind = ["Pterowind", "Wind", 100, 18, 20, "Ruffle: 18-20 damage", 15, 30, "Sky Dive: 15-30 damage", 6, 12,
             "Nest: 6-12 heal", 100, False]
all_my_monsters = [aquarex, inferosaur, pterowind]

# Introduction:
print("\n    <3 <3 <3 Loading <3 <3 <3\n")
print("        ~Little Monsters~\n\n")

# Generate new encounter:
encounter()

