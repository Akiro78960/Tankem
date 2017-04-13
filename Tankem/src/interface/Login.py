## -*- coding: utf-8 -*-

from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText 
from direct.gui.DirectGui import *
from panda3d.core import *
from pandac.PandaModules import *
from direct.interval.LerpInterval import *
from direct.interval.IntervalGlobal import *
from direct.showbase.Transitions import Transitions

import sys
import common
import settings

DAOMap = common.internal.MapDAODTO.DAOMapOracle.DAOmaporacle()
DTOlistmap = DAOMap.read()

class MenuLogin(ShowBase):
	def __init__(self, gameLogic):
		self.gameLogic = gameLogic
		#Image d'arrière plan
		self.background=OnscreenImage(parent=render2d, image="../asset/Menu/BackgroundLogin.jpg")

		#On dit à la caméra que le dernier modèle doit s'afficher toujours en arrière
		self.baseSort = base.cam.node().getDisplayRegion(0).getSort()
		base.cam.node().getDisplayRegion(0).setSort(20)

		

		#Boutons
		btnScale = (0.18,0.18)
		text_scale = 0.12
		borderW = (0.04, 0.04)
		couleurBack = (0.243,0.325,0.121,1)
		separation = 1
		hauteur = -0.6
		numItemsVisible = 50
		#Titre du jeu

		self.labelplayer1 = OnscreenText(text = "Player 1",
									  pos = (-1.25,0.8,-1.67), 
									  scale = 0.15,
									  fg=(0,0,0,1),
									  align=TextNode.ACenter)
		self.username1 = DirectEntry(text = "" ,scale=.05,
									initialText="Enter username", 
									numLines = 1,
									focus=1,
									pos=(-1.50,0,0.69) )
		self.password1 = DirectEntry(text = "" ,scale=.05,
									initialText="", 
									numLines = 1,
									focus=1,
									pos=(-1.50,0,0.39),
									obscured=1 )
		self.labelpassword1 = OnscreenText(text = "Password",
									  pos = (-1.25,0.50,-1.67), 
									  scale = 0.15,
									  fg=(0,0,0,1),
									  align=TextNode.ACenter)

		self.Player2 = OnscreenText(text = "Player 2",
									  pos = (0.25,0.8,-1.67), 
									  scale = 0.15,
									  fg=(0,0,0,1),
									  align=TextNode.ACenter)
		
		self.username2 = DirectEntry(text = "" ,scale=.05,
									initialText="Enter username", 
									numLines = 1,
									focus=1,
									pos=(0,0,0.69) )
		self.labelpassword2 = OnscreenText(text = "Password",
									  pos = (0.25,0.50,-1.67), 
									  scale = 0.15,
									  fg=(0,0,0,1),
									  align=TextNode.ACenter)
		self.labelpassword2 = OnscreenText(text = "Message box ",
									  pos = (-0.1,0.2,-1.67), 
									  scale = 0.15,
									  fg=(0,0,0,1),
									  align=TextNode.ACenter)
		self.password2 = DirectEntry(text = "" ,scale=.05,
									initialText="", 
									numLines = 1,
									focus=1,
									pos=(0,0,0.39),
									obscured=1 )
		self.messageBox = DirectEntry(text = "" ,scale=.05,
									width =55,
									initialText="", 
									numLines = 1,
									focus=1,
									pos=(-1.5,0,0.1) )
		

		
		#Initialisation de l'effet de transition
		curtain = loader.loadTexture("../asset/Menu/load.png")

		self.transition = Transitions(loader)
		self.transition.setFadeColor(0, 0, 0)
		self.transition.setFadeModel(curtain)

		self.sound = loader.loadSfx("../asset/Menu/shotgun.mp3")

	# def cacher(self):
	# 		#Est esssentiellement un code de "loading"

	# 		#On remet la caméra comme avant
	# 		base.cam.node().getDisplayRegion(0).setSort(self.baseSort)
	# 		#On cache les menus
	# 		self.background.hide()
	# 		self.b1.hide()
	# 		self.b2.hide()
	# 		self.scrollList.hide()
	# 		self.textTitre.hide()

	# def setNiveauChoisi(self,idNiveau):
	# 		self.gameLogic.setIdNiveau(idNiveau)
	# 		self.chargeJeu()

	# def chargeJeu(self):
	# 		#On démarre!
	# 		Sequence(Func(lambda : self.transition.irisOut(0.2)),
	# 				 SoundInterval(self.sound),
	# 				 Func(self.cacher),
	# 				 Func(lambda : messenger.send("DemarrerPartie")),
	# 				 Wait(0.2), #Bug étrange quand on met pas ça. L'effet de transition doit lagger
	# 				 Func(lambda : self.transition.irisIn(0.2))
	# 		).start()
			