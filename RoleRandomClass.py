import random
import json

class role_distri:
    def __init__(self, roles_config, exclusions=None):
        with open('games-config.json', 'r') as f:
            self.JSON = json.load(f)
        self.roles_list = self.JSON["games"][roles_config]
        self.roles = list()
        self.rules = {}
        for i in self.roles_list:
            self.roles.append(i['name'])
            if i['rules'] != "None":
                self.rules[i['name']] = i['rules']
        self.selected = []
        