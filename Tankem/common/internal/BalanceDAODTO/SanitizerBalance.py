# -*- coding: utf-8 -*-

class Sanitizer():
    #####
    # Constructeur

    def __init__(self):

    #####
    # Verifie si les valeurs respectent les min/max

    def isBelowMin(value, min):
        result = true 

        if(min <= value):
            result = false

        return result

    def isAboveMax(value, max):
        result = true 

        if(value <= max):
            result = false

        return result

    def dicIsBalanced(dictionary):
        result = true

        if(isBelowMin( dictionary['value'], dictionary['min']):
            result = false
            print dictionary['name'] + " est sous le minimum requis"
        else if(isAboveMax( dictionary['value'], dictionary['max']):
            result = false
            print dictionary['name'] + " est au dessus du maximum requis"

        return result

    def allIsBalanced(self):
        result = true

        for key, dic in self.dictionarInception:
            if(!dicIsBalanced(dic)):
                result = false

        return result
