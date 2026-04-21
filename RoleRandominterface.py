import random
import json

with open('games-config.json', 'r') as f:
    JSON = json.load(f)

def start_game(queue, roles_config, exclusions=None):
    try:
        global roles
        global rules
        global selected 
        roles_list = JSON["games"][roles_config]
        roles = list()
        for i in roles_list:
            roles.append(i['name'])
        rules = {}
        selected = []
    except KeyError:
        print(KeyError)
    except NameError:
        print(NameError)
    except Exception as e:
        print(e)
    role_randomize(len(queue), exclusions)

start_game(5, "commander-roles")

#adding secondary roles
#change this function to account for command style entries in the rules section of the json structure(ex.maskedman)
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

def distribute(selected):


#display choices for maskedman (implement)
# if i == "Maskedman":
#     print(f"\nChoose new role:")
#     for j in roles:
#         print(j)

#main function
def role_randomize(num_players, exclusions):
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