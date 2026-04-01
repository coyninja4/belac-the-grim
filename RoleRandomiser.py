import random
import os

def initialize():
    global roles 
    global rules
    global selected 
    roles = ["King", "Sellsword", "Hunter", "Bodyguard", "Necromancer", "Twins", "Seer", "Villageidiot", "Glasscannon", "Warlord", "Maskedman", "Chaos", "Doppleganger"]
    rules = {"King":"Knight Assasin", "Twins":"Twin2"}
    selected = []

#adding secondary roles
def apply_rules(role):
    #list for removing roles if to many are added
    ruled = []
    if role in rules:
        param = rules[role].split()
        for i in param:
            selected.append(i)
            ruled.append(i)
    return ruled

#output function
def printing(selected):
    for i in selected:
        input("Player role is:")
        print(i)
        #display choices for maskedman
        if i == "Maskedman":
            print(f"\nChoose new role:")
            for j in roles:
                print(j)
        input("Press enter and pass...")
        os.system('cls' if os.name == 'nt' else 'clear')
    random.shuffle(selected)
    print(selected)

#main function
def role_randomize(num_players, exclusions):
    initialize()
    #handle exclusions
    for i in exclusions:
        #capitalize input list
        i = i.capitalize()
        roles.remove(i)
    #guarantee multiple roles for maskedman 
    if num_players + 2 >= len(roles):
        try:
            roles.remove("Maskedman")
        except:
            pass
    if num_players > len(roles):
        print("Too many exclusions try again")
        return
    #adding roles up to number of players
    while len(selected) < num_players:
        x = random.randint(1, len(roles)) - 1
        added = roles[x]
        selected.append(added)
        ruled = apply_rules(added)
        random.shuffle(selected)
        #if rules goes over number players remove
        if len(selected) > num_players:
            selected.remove(added)
            for i in ruled:
                selected.remove(i)
        roles.remove(added)
    random.shuffle(selected)
    printing(selected)