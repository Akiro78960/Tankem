# -*- coding: utf-8 -*-

# Le DTO consiste d'un dictionnaire de plusieurs dictionnaires.
# Les dictionnaires contiennent le nom lisible, la valeur utilisée et le min/max 
# de chaque options du jeux.

class DTObject():
        #####
        # Constructeur

	def __init__(self):
            self.dictionarInception = {}

        # Ajouter un dictionnaire au dictionnaire

        def appendNewDictionary (self, key, name, value, min, max):
            tmp = {}
            tmp['name'] = name
            tmp['value'] = value
            tmp['min'] = min
            tmp['max'] = max

            self.dictionarInception[key] = tmp

        # Avoir un dictionnaire

        def getDic (self, key):
            return self.dictionarInception[key]

