# -*- coding: utf-8 -*-

class Sanitizer():
    #####
    # Constructeur

    def __init__(self):

    #####
    # Verifie si les valeurs respectent les min/max

    def isBelowMin(value, min):
        return value < min

    def isAboveMax(value, max):
        return value > max

    def dicIsBalanced(dictionary):
        result = true

        if(isBelowMin( dictionary['value'], dictionary['min']):
            result = false
            print dictionary['name'] + " est sous le minimum requis"
        else if(isAboveMax( dictionary['value'], dictionary['max']):
            result = false
            print dictionary['name'] + " est au dessus du maximum requis"

        return result

    #####
    # Main, retourne true si tout est beaux

    def sanitizeDTO(self,dictionarInception):
        result = true

        for dic in dictionarInception:
            if(!dicIsBalanced(dic)):
                result = false
                break

        return result
