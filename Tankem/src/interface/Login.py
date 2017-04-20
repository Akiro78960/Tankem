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
import SingletonDBConnection
DAOMap = common.internal.MapDAODTO.DAOMapOracle.DAOmaporacle()
DTOlistmap = DAOMap.read()

class MenuLogin(ShowBase):
	def __init__(self, gameLogic):
		self.gameLogic = gameLogic
		self.user = common.internal.UtilisateursDAODTO.DAOutilisateur.DAOutilisateur()
		# self.joueur = self.daoJoueur.read("Test2","AAAaaa111")
		#Image d'arrière plan
		self.background=OnscreenImage(parent=render2d, image="../asset/Menu/BackgroundLogin.jpg")

		#On dit à la caméra que le dernier modèle doit s'afficher toujours en arrière
		self.baseSort = base.cam.node().getDisplayRegion(0).getSort()
		base.cam.node().getDisplayRegion(0).setSort(20)

		#Boutons
		btnScale = (0.06,0.06)
		text_scale = 0.12
		borderW = (0.02, 0.02)
		couleurBack = (0.243,0.325,0.321,1)
		separation = 1
		hauteur = -0.6
		numItemsVisible = 50
		self.player1ready = False
		self.player2ready = False
		#Titre du jeu

		self.labelplayer1 = OnscreenText(text = "Player 1",
									  pos = (-1.25,0.8,-1.67), 
									  scale = 0.15,
									  fg=(0,0,0,1),
									  align=TextNode.ACenter)
		self.username1 = DirectEntry(text = "" ,scale=.05,
									initialText="", 
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
									initialText="", 
									numLines = 1,
									focus=1,
									pos=(0,0,0.69) )
		self.labelpassword2 = OnscreenText(text = "Password",
									  pos = (0.25,0.50,-1.67), 
									  scale = 0.15,
									  fg=(0,0,0,1),
									  align=TextNode.ACenter)
		self.labelpassword2 = OnscreenText(text = "Message box ",
									  pos = (-0.3,0.2,-1.67), 
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
									initialText="Veuillez vous connecter à Tank'em", 
									numLines = 1,
									focus=0,
									pos=(-1.5,0,0.1),
									focusInCommand=self.clearText )
		self.b2 = DirectButton(text = ("Login", "Login", "Login", "disabled"),
						  text_scale=btnScale,
						  borderWidth = borderW,
						  text_bg=couleurBack,
						  frameColor=couleurBack,
						  relief=2,
						  textMayChange = 1,
						  pad = (0,0),
						  command = self.setPlayer1Ready,
						  extraArgs = [True],
						  pos = (-1.25,0,0.25))
		self.b3 = DirectButton(text = ("Login", "Login", "Login", "disabled"),
						  text_scale=btnScale,
						  borderWidth = borderW,
						  text_bg=couleurBack,
						  frameColor=couleurBack,
						  relief=2,
						  textMayChange = 1,
						  pad = (0,0),
						  command = self.setPlayer2Ready,
						  extraArgs = [True],
						  pos = (0.25,0,0.25))

		
				

		
		#Initialisation de l'effet de transition
		curtain = loader.loadTexture("../asset/Menu/load.png")

		self.transition = Transitions(loader)
		self.transition.setFadeColor(0, 0, 0)
		self.transition.setFadeModel(curtain)

		self.sound = loader.loadSfx("../asset/Menu/shotgun.mp3")

	def setPlayer1Ready(self,state):
		self.username = self.username1.get()
		self.password = self.password1.get()
		self.joueur = self.user.read(self.username,self.password)
		
		if self.joueur == 1 :
			self.setText("Mauvais nom d'utilisateur")
		elif self.joueur == 0 : 
			self.setText("Mauvais mot de passe")
		else :
			self.player1ready = state

		if self.player1ready == True and self.player2ready == True :
			self.setText("Welcome to Tank'em !")
		elif self.player1ready :
			self.setText('Player 2 must also login')
		elif self.player2ready :
			self.settext('Player 1 must also login')
		else :
			self.setText('Both players must login')

	def setPlayer2Ready(self,state):
		self.username = self.username2.get()
		self.password = self.password2.get()
		self.joueur = self.user.read(self.username,self.password)

		if self.joueur == 1 :
			self.setText("Mauvais nom d'utilisateur")
		elif self.joueur == 0 : 
			self.setText("Mauvais mot de passe")
		else :
			self.player2ready = state

		if self.player1ready == True and self.player2ready == True :
			self.setText("Welcome to Tank'em !")
		elif self.player1ready :
			self.setText('Player 2 must also login')
		elif self.player2ready :
			self.settext('Player 1 must also login')
		else :
			self.setText('Both players must login')
	#callback function to set  text 
	def setText(self,textEntered):
		self.messageBox.enterText(textEntered)
 
	#clear the text
	def clearText(self):
		self.messageBox.enterText('')
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

	def calculateName(self, joueur):
		self.statsJoueur = joueur.getStats()
		print self.statsJoueur
			