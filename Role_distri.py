import random
import json

class Role_distri:
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
                elif i == "option":
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
                        i = int(i)
                        if len(self.roles) < i:
                            self.roles.remove(role)
        return ruled
    
    def role_randomize(self, exclusions):
        #handle exclusions
        exclusions = [e.strip() for e in exclusions.split(",") if e.strip()]
        self.excluded = set(exclusions)

        # excluding a role also excludes the roles it adds
        for name in list(self.excluded):
            self.excluded.update(w for w in self.rules.get(name, "").split() if w in self.roles_dict)

        # excluding a role also excludes any role that would add it
        for name, rule in self.rules.items():
            if any(w in self.excluded for w in rule.split() if w in self.roles_dict):
                self.excluded.add(name)

        self.roles = [r for r in self.roles if r not in self.excluded]
        print("Excluded:", self.excluded, "| Pool:", self.roles)

        if len(self.queue) > len(self.roles):
            print("Too many exclusions try again")
            return
        #adding roles up to number of players
        while len(self.selected) < len(self.queue) and self.roles:
            added = random.choice(self.roles)
            roles_backup = self.roles.copy()

            self.selected.append(added)
            ruled = self.apply_rules(added)

            if len(self.selected) > len(self.queue):
                self.selected.remove(added)
                for r in ruled:
                    self.selected.remove(r)
                self.roles = roles_backup
                self.roles.remove(added)
                continue

            if added in self.roles:
                self.roles.remove(added)
        random.shuffle(self.selected)
        distrib_dict = {k: v for (k, v) in zip(self.queue, self.selected)}

        # who holds each role (needed for roles with counterparts)
        twins = [uid for uid, role in distrib_dict.items() if role == "twin"]

        for uid, role in distrib_dict.items():
            info = self.roles_dict[role]
            text = (f"{role}: {info['status']} role\n{info['power']}\n"
                    f"Wincondition: {info['Wincon']}")

            if role == "twin":
                others = [t for t in twins if t != uid]
                if others:
                    text += "\n\nYour twin is " + ", ".join(f"<@{t}>" for t in others)

            if role == "maskedman":
                options = [r for r in self.roles_dict
                        if r not in self.selected
                        and r not in self.excluded
                        and r != "maskedman"]
                text += "\n\nRoles you can choose from: " + ", ".join(options)

            distrib_dict[uid] = text
        return distrib_dict, self.selected