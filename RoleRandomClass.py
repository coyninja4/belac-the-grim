import random
import json

class role_distri:
    def __init__(self, roles_config, queue):
        with open('games-config.json', 'r') as f:
            self.JSON = json.load(f)
        self.roles_list = self.JSON["games"][roles_config]
        self.roles = list()
        self.rules = {}
        self.queue = queue
        for i in self.roles_list:
            self.roles.append(i['name'])
            if i['rules'] != "None":
                self.rules[i['name']] = i['rules']
        self.selected = []
        self.roles_dict = {r["name"]: r for r in self.roles_list}

    def apply_rules(self, role):
        #list for removing roles if to many are added
        ruled = []
        command = None
        if role in self.rules:
            param = self.rules[role].split()
            for i in param:
                if i == "add":
                    command = "add"
                    continue
                if i == "option":
                    command = "option"
                    continue
                else:
                    if command == "add":
                        self.selected.append(i)
                        ruled.append(i)
                        try:
                            self.roles.remove(i)
                        except:
                            continue
                    if command == "option":
                        if len(self.roles) < i:
                            self.roles.remove(role)
                        option = None
        return ruled
    
    def role_randomize(self, *exclusions):
    #handle exclusions
        try:
            for i in exclusions:
                #capitalize input list
                i = i.capitalize()
                if i in self.rules:
                    param = self.rules[i].split()
                    for j in param:
                        self.roles.remove(j)
                self.roles.remove(i)
        except:
            pass
        if len(self.queue) > len(self.roles):
            print("Too many exclusions try again")
            return
        #adding roles up to number of players
        for j in self.queue:
            x = random.randint(1, len(self.roles)) - 1
            added = self.roles[x]
            self.selected.append(added)
            ruled = self.apply_rules(added)
            random.shuffle(self.selected)
            #if rules goes over number players remove
            if len(self.selected) > len(self.queue):
                self.selected.remove(added)
                for i in ruled:
                    self.selected.remove(i)
            self.roles.remove(added)
        random.shuffle(self.selected)
        distrib_dict = {k:v for (k,v) in zip(self.queue, self.selected)}
        for i in distrib_dict:
            distrib_dict[i] = f"{distrib_dict[i]}: {self.roles_dict[distrib_dict[i]]["power"]}\nWincondition:{self.roles_dict[distrib_dict[i]]["Wincon"]}"
        return distrib_dict
    
    #def start_game(self, *exclusions):    