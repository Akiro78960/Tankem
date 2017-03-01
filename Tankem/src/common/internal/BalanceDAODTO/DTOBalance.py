# -*- coding: utf-8 -*-

class DTObalance:
    #####
    # Constructeur

    def __init__(self):
        self.values = {}

    # Ajouter une valeur au dictionnaire
    def appendNewValue (self, key, value):
        self.values[key] = value

    # Avoir une valeur dans le dictionnaire
    def getValue (self, key):
        return self.values[key]

    def getDTO (self):
        return self.values
