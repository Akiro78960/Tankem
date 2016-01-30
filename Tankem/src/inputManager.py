## -*- coding: utf-8 -*-

import sys
from direct.showbase.ShowBase import ShowBase

class InputManager(ShowBase):
    def __init__(self, listTank):

        self.listTank = listTank
        #Contrôle de débug
        self.accept("escape", sys.exit)
        self.accept('f1', self.toggleDebogue)
        self.accept('f2', self.toggleFreeCam)

    def debuterControle(self):
        #Faisable avec une liste de dictionnaire ce qui donnera la moitié moins de ligne,
        #mais on garde ça simple. Laissé en exercise plus tard?
        CTRL_P1_AVANCE = "w"
        CTRL_P1_RECULE = "s"
        CTRL_P1_GAUCHE = "a"
        CTRL_P1_DROITE = "d"
        CTRL_P1_PRIMAIRE = "v"
        CTRL_P1_SECONDAIRE = "b"
        CTRL_P1_DETONATION = "n"

        CTRL_P2_AVANCE = "arrow_up"
        CTRL_P2_RECULE = "arrow_down"
        CTRL_P2_GAUCHE = "arrow_left"
        CTRL_P2_DROITE = "arrow_right"
        CTRL_P2_PRIMAIRE = "1"
        CTRL_P2_SECONDAIRE = "2"
        CTRL_P2_DETONATION = "3"

        #Joueur 1
        self.accept(CTRL_P1_AVANCE, self.relaiControle, [0,"avance"])
        self.accept(CTRL_P1_RECULE, self.relaiControle, [0,"recule"])
        self.accept(CTRL_P1_AVANCE + "-up", self.relaiControle, [0,"avance-stop"])
        self.accept(CTRL_P1_RECULE + "-up", self.relaiControle, [0,"recule-stop"])

        self.accept(CTRL_P1_GAUCHE, self.relaiControle, [0,"tourne-gauche"])
        self.accept(CTRL_P1_DROITE, self.relaiControle, [0,"tourne-droit"])
        self.accept(CTRL_P1_GAUCHE + "-up", self.relaiControle, [0,"tourne-gauche-stop"])
        self.accept(CTRL_P1_DROITE + "-up", self.relaiControle, [0,"tourne-droit-stop"])

        self.accept(CTRL_P1_PRIMAIRE, self.relaiControle, [0,"arme-primaire"])
        self.accept(CTRL_P1_SECONDAIRE, self.relaiControle, [0,"arme-secondaire"])
        self.accept(CTRL_P1_DETONATION, self.relaiControle, [0,"exploser-balle"])

        #Joueur 2
        self.accept(CTRL_P2_AVANCE, self.relaiControle, [1,"avance"])
        self.accept(CTRL_P2_RECULE, self.relaiControle, [1,"recule"])
        self.accept(CTRL_P2_AVANCE + "-up", self.relaiControle, [1,"avance-stop"])
        self.accept(CTRL_P2_RECULE + "-up", self.relaiControle, [1,"recule-stop"])

        self.accept(CTRL_P2_GAUCHE, self.relaiControle, [1,"tourne-gauche"])
        self.accept(CTRL_P2_DROITE, self.relaiControle, [1,"tourne-droit"])
        self.accept(CTRL_P2_GAUCHE + "-up", self.relaiControle, [1,"tourne-gauche-stop"])
        self.accept(CTRL_P2_DROITE + "-up", self.relaiControle, [1,"tourne-droit-stop"])

        self.accept(CTRL_P2_PRIMAIRE, self.relaiControle, [1,"arme-primaire"])
        self.accept(CTRL_P2_SECONDAIRE, self.relaiControle, [1,"arme-secondaire"])
        self.accept(CTRL_P2_DETONATION, self.relaiControle, [1,"exploser-balle"])

    def bloquerControle(self):
        #Joueur 1
        self.ignore(CTRL_P1_AVANCE)
        self.ignore(CTRL_P1_AVANCE)
        self.ignore(CTRL_P1_AVANCE + "-up")
        self.ignore(CTRL_P1_AVANCE + "-up")

        self.ignore(CTRL_P1_GAUCHE)
        self.ignore(CTRL_P1_DROITE)
        self.ignore(CTRL_P1_GAUCHE + "-up")
        self.ignore(CTRL_P1_DROITE + "-up")

        self.ignore(CTRL_P1_PRIMAIRE)
        self.ignore(CTRL_P1_SECONDAIRE)
        self.ignore(CTRL_P1_DETONATION)

        #Joueur 2
        self.ignore(CTRL_P2_AVANCE)
        self.ignore(CTRL_P2_AVANCE)
        self.ignore(CTRL_P2_AVANCE + "-up")
        self.ignore(CTRL_P2_AVANCE + "-up")

        self.ignore(CTRL_P2_GAUCHE)
        self.ignore(CTRL_P2_DROITE)
        self.ignore(CTRL_P2_GAUCHE + "-up")
        self.ignore(CTRL_P2_DROITE + "-up")

        self.ignore(CTRL_P2_PRIMAIRE)
        self.ignore(CTRL_P2_SECONDAIRE)
        self.ignore(CTRL_P2_DETONATION)

    def relaiControle(self, identifiant, message):
        self.listTank[identifiant].traiterCommande(message)

    def toggleDebogue(self):
        base.messenger.toggleVerbose()
        if self.debugNP.isHidden():
            self.debugNP.show()
            base.setFrameRateMeter(True)
        else:
            self.debugNP.hide()
            base.setFrameRateMeter(False)

    def toggleFreeCam(self):
        if(not self.mouseEnabled):
            self.enableMouse()
            self.mouseEnabled = True
        else:
            self.disableMouse()
            self.placerCameraInitiale()
            self.mouseEnabled = False   