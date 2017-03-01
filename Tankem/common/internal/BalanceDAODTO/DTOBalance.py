# -*- coding: utf-8 -*-

class DTObalance():
        #####
        # Constructeur

	def __init__(self):
            self.values = {}

        # Ajouter un dictionnaire au dictionnaire
<<<<<<< HEAD
        def appendNewValue (self, key, value):
            self.values[key] = value
=======

        def appendNewDictionary (self, key, name, value, min, max):# key: nom, name: nom détaillé
            tmp = {}
            tmp['name'] = name
            tmp['value'] = value
            tmp['min'] = min
            tmp['max'] = max

            self.dictionarInception[key] = tmp
>>>>>>> 7f9319474ed7112690f27baf201f2cc231c5df40

        # Avoir un dictionnaire
        def getValue (self, key):
            return self.values[key]

