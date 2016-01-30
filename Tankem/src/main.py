## -*- coding: utf-8 -*-
#Ajout des chemins vers les librarires
from util import inclureCheminCegep
import sys
print(sys.path)


#Importe la configuration de notre jeu
from panda3d.core import loadPrcFile
loadPrcFile("config/ConfigTankem.prc")



#Module de Panda3D
from direct.showbase.ShowBase import ShowBase

#Modules internes
from gameLogic import *
 
class Tankem(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.demarrer()

    def demarrer(self):
        self.gameLogic = GameLogic(self)
        self.gameLogic.startGame()


#Main de l'application.. assez simple!
app = Tankem()
app.run()