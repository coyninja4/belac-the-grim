import random
import os

def initialize():
    global roles 
    global rules
    global selected 
    roles = ["King", "Knight", "Assasin", "Sellsword", "Hunter", "Bodyguard", "Necromancer",
              "Twins", "Seer", "Villageidiot", "Glasscannon", "Warlord",
                "Maskedman", "Chaos", "Doppleganger"]
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
            try:
                roles.remove(i)
            except:
                pass
    return ruled

#display choices for maskedman (implement)
# if i == "Maskedman":
#     print(f"\nChoose new role:")
#     for j in roles:
#         print(j)

#main function
def role_randomize(num_players, exclusions=None):
    initialize()
    #handle exclusions
    try:
        for i in exclusions:
            #capitalize input list
            i = i.capitalize()
            if i in rules:
                param = rules[i].split()
                for j in param:
                    roles.remove(j)
            roles.remove(i)
    except:
        pass
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
    return selected