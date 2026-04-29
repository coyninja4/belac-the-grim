import random
import json

with open('games-config.json', 'r') as f:
    JSON = json.load(f)

def start_game(queue, roles_config, exclusions=None):
    try:
        global roles
        global rules
        global selected
        global roles_list
        roles_list = JSON["games"][roles_config]
        roles = list()
        rules = {}
        for i in roles_list:
            roles.append(i['name'])
            if i['rules'] != "None":
                rules[i['name']] = i['rules']
            selected = []
    except KeyError:
        print(KeyError)
    except NameError:
        print(NameError)
    except Exception as e:
        print(e) 
    roles_dict = {r["name"]: r for r in roles_list}
    message_comp(role_randomize(queue, exclusions))


#adding rules from game-config
#change this function to account for command style entries in the rules section of the json structure(ex.maskedman)
def apply_rules(role):
    #list for removing roles if to many are added
    ruled = []
    command = None
    if role in rules:
        param = rules[role].split()
        for i in param:
            if i == "add":
                command = "add"
                pass
            if i == "option":
                command = "option"
                pass
            else:
                if command == "add":
                    selected.append(i)
                    ruled.append(i)
                    try:
                        roles.remove(i)
                    except:
                        pass
                if command == "option":
                    if len(roles) < i:
                        roles.remove(role)
    return ruled

def message_comp(distrib_dict):
    global roles_list
    for j in distrib_dict.values():
        pass

#main function
def role_randomize(queue, exclusions):
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
    if len(queue) > len(roles):
        print("Too many exclusions try again")
        return
    #adding roles up to number of players
    for j in queue:
        x = random.randint(1, len(roles)) - 1
        added = roles[x]
        selected.append(added)
        ruled = apply_rules(added)
        random.shuffle(selected)
        #if rules goes over number players remove
        if len(selected) > len(queue):
            selected.remove(added)
            for i in ruled:
                selected.remove(i)
        roles.remove(added)
    random.shuffle(selected)
    distrib_dict = {k:v for (k,v) in zip(queue, selected)}
    return distrib_dict

start_game(set([1573, 6849, 3285, 7041, 5928]), "commander-roles")