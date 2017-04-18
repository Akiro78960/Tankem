#-*- coding: utf-8 -*-
class DTOenregistrementPartie:
    def __init__(self, id_partie, creation_date):
        self.id_partie = id_partie
        self.creation_date = creation_date
        self.array_joueur1 = []
        self.array_joueur2 = []
        self.array_arme = []
        self.array_projectile = []

    def appendJoueur1(self,DTOenregistrementJoueur):
        self.array_tuiles.append(DTOenregistrementJoueur)

    def appendJoueur2(self,DTOenregistrementJoueur):
        self.array_tuiles.append(DTOenregistrementJoueur)

    def appendArme(self,DTOenregistrementArme):
        self.array_arme.append(DTOenregistrementArme)

    def appendProjectile(self, DTOenregistrementProjectile):
        self.array_projectile.append(DTOenregistrementProjectile)
