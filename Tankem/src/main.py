## -*- coding: utf-8 -*-
#Ajout des chemins vers les librarires
from util import inclureCheminCegep
import sys

#Importe la configuration de notre jeu
from panda3d.core import loadPrcFile
loadPrcFile("config/ConfigTankem.prc")

#Module de Panda3DappendObject
from direct.showbase.ShowBase import ShowBase

#Modules internes
from gameLogic import GameLogic
from interface import InterfaceMenuPrincipal
 
class Tankem(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.demarrer()

    def demarrer(self):
        self.gameLogic = GameLogic(self)
        #Commenter/décommenter la ligne de votre choix pour démarrer le jeu
        #Démarre dans le menu
        #self.menuPrincipal = InterfaceMenuPrincipal()
        #Démarre directement dans le jeu
        messenger.send("DemarrerPartie")

#Main de l'application.. assez simple!
app = Tankem()
app.run()