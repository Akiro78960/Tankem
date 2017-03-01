# -*- coding: utf-8 -*-

class Sanitize:
    #####
    # Constructeur

    def __init__(self, dtoValues):
        self.keysList = self.initKeyList()

        self.dtoValues = dtoValues
        self.dtoMin
        self.dtoMax

    #####
    # Init Hardcoded shizzles

    # KeysList
    def initKeysList():
        tmpList = []

        tmpList.append(vitesse_char)
	tmpList.append(vitesse_rotation)
	tmpList.append(vie)
	tmpList.append(temps_mouvement_blocs)
	tmpList.append(canon_vitesse_balle)
	tmpList.append(canon_reload)
	tmpList.append(mitraillette_vitesse_balle)
	tmpList.append(mitraillette_reload)
	tmpList.append(grenade_vitesse_balle)
	tmpList.append(grenade_reload)
	tmpList.append(shotgun_vitesse_balle)
	tmpList.append(shotgun_reload)
	tmpList.append(shotgun_spread)
	tmpList.append(piege_vitesse_balle)
	tmpList.append(piege_reload)
	tmpList.append(missile_vitesse_balle)
	tmpList.append(missile_reload)
	tmpList.append(spring_vitesse_saut)
	tmpList.append(spring_reload)
	tmpList.append(rayon_explosion)
	tmpList.append(message_acceuil_duree)
	tmpList.append(message_countdown_duree)

        return tmpList

    # DTO Min
    def initDtoMin(self):
        tmpDTO = DTObalance()
        minList = []

        # initMinList
        4# vitesse_char
	1000# vitesse_rotation
	100# vie
	0.2# temps_mouvement_blocs
	4# canon_vitesse_balle
	0.2# canon_reload
	4# mitraillette_vitesse_balle
	0.2# mitraillette_reload
	10# grenade_vitesse_balle
	0.2# grenade_reload
	4# shotgun_vitesse_balle
	0.2# shotgun_reload
	0.1# shotgun_spread
	0.2# piege_vitesse_balle
	0.2# piege_reload
	20# missile_vitesse_balle
	0.2# missile_reload
	6# spring_vitesse_saut
	0.2# spring_reload
	1# rayon_explosion
	1# message_acceuil_duree
	0# message_countdown_duree

        return tmpDTO.getDTO()

    # DTO Max
        vitesse_char
	vitesse_rotation
	vie
	temps_mouvement_blocs
	canon_vitesse_balle
	canon_reload
	mitraillette_vitesse_balle
	mitraillette_reload
	grenade_vitesse_balle
	grenade_reload
	shotgun_vitesse_balle
	shotgun_reload
	shotgun_spread
	piege_vitesse_balle
	piege_reload
	missile_vitesse_balle
	missile_reload
	spring_vitesse_saut
	spring_reload
	rayon_explosion
	message_acceuil_duree
	message_countdown_duree
    
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
