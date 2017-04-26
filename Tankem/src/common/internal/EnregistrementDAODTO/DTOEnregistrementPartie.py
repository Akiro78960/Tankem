#-*- coding: utf-8 -*-
class DTOenregistrementPartie:
    def __init__(self,idMap, creation_date):
        self.idMap = idMap
        self.creation_date = creation_date
        self.array_joueur1 = []
        self.array_joueur2 = []
        self.array_arme = []
        self.array_projectile = []

    def appendJoueur1(self,DTOenregistrementJoueur):
        self.array_joueur1.append(DTOenregistrementJoueur)

    def appendJoueur2(self,DTOenregistrementJoueur):
        self.array_joueur2.append(DTOenregistrementJoueur)

    def appendArme(self,DTOenregistrementArme):
        self.array_arme.append(DTOenregistrementArme)

    def appendProjectile(self, DTOenregistrementProjectile):
        self.array_projectile.append(DTOenregistrementProjectile)

    def getDate(self):
        return self.creation_date

    def getArrayJoueur1(self):
        return self.array_joueur1

    def getArrayJoueur2(self):
        return self.array_joueur2

    def getArrayArme(self):
        return self.array_arme

    def getArrayProjectile(self):
        return self.array_projectile
