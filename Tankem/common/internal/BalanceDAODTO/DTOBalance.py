# -*- coding: utf-8 -*-

class DTObalance():
        #####
        # Constructeur

	def __init__(self):
            self.values = {}

        # Ajouter un dictionnaire au dictionnaire
        def appendNewValue (self, key, value):
            self.values[key] = value

        # Avoir un dictionnaire
        def getValue (self, key):
            return self.values[key]

