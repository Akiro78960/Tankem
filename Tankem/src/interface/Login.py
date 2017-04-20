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
	def __init__(self, gameLogic,mapID,mapName):
		self.gameLogic = gameLogic
		self.mapID = mapID
		self.mapName = mapName
		self.user = common.internal.UtilisateursDAODTO.DAOutilisateur.DAOutilisateur()

		#Image d'arrière plan
		self.background=OnscreenImage(parent=render2d, image="../asset/Menu/BackgroundLogin.jpg")

		#On dit à la caméra que le dernier modèle doit s'afficher toujours en arrière
		self.baseSort = base.cam.node().getDisplayRegion(0).getSort()
		base.cam.node().getDisplayRegion(0).setSort(20)

		#Boutons
		btnScale = (0.06,0.06)
		text_scale = 0.12
		borderW = (0.02, 0.02)
		separation = 1
		hauteur = -0.6
		numItemsVisible = 50
		self.couleurBack = (0.243,0.325,0.321,1)
		self.player1ready = False
		self.player2ready = False
		self.couleurDisabled = (0.343,0.325,0.321,1)
		self.couleurBGLabel = (255,255,255,0.3)
		self.couleurShadow = (200,200,200,0.8)
		self.couleurFG = (0,0,0,1)
		#Titre du jeu

		self.username1 = DirectEntry(text = "" ,scale=.05,
									initialText="", 
									numLines = 1,
									focus=1,
									pos=(-1,0,0.82) )
		self.username2 = DirectEntry(text = "" ,scale=.05,
									initialText="", 
									numLines = 1,
									focus=1,
									pos=(0.4,0,0.82) )
		self.password1 = DirectEntry(text = "" ,scale=.05,
									initialText="", 
									numLines = 1,
									focus=1,
									pos=(-1,0,0.59),
									obscured=1 )
		self.password2 = DirectEntry(text = "" ,scale=.05,
									initialText="", 
									numLines = 1,
									focus=1,
									pos=(0.4,0,0.59),
									obscured=1 )
		self.messageBox = DirectEntry(text = "" ,scale=.05,
									width =55,
									initialText="Veuillez vous connecter à Tank'em", 
									numLines = 1,
									focus=0,
									pos=(-1.35,0,0.3),
									focusInCommand=self.clearText )
		self.labelplayer1 = OnscreenText(text = "Player 1",
									  pos = (-0.75,0.9,-1.67), 
									  scale = 0.10,
									  fg=self.couleurFG,
									  bg = self.couleurBGLabel,
									  shadow=self.couleurShadow,
									  align=TextNode.ACenter)
		self.labelpassword1 = OnscreenText(text = "Password",
									  pos = (-0.75,0.70,-1.67), 
									  scale = 0.10,
									  fg=self.couleurFG,
									  bg = self.couleurBGLabel,
									  shadow=self.couleurShadow,
									  align=TextNode.ACenter)

		self.labelPlayer2 = OnscreenText(text = "Player 2",
									  pos = (0.65,0.9,-1.67), 
									  scale = 0.10,
									  fg=self.couleurFG,
									  bg = self.couleurBGLabel,
									  shadow=self.couleurShadow,
									  align=TextNode.ACenter)
		
		self.labelpassword2 = OnscreenText(text = "Password",
									  pos = (0.65,0.70,-1.67), 
									  scale = 0.10,
									  fg=self.couleurFG,
									  bg = self.couleurBGLabel,
									  shadow=self.couleurShadow,
									  align=TextNode.ACenter)
		self.labelMessageBox = OnscreenText(text = "Message box ",
									  pos = (-0.05,0.4,-1.67), 
									  scale = 0.10,
									  fg=self.couleurFG,
									  bg = self.couleurBGLabel,
									  shadow=self.couleurShadow,
									  align=TextNode.ACenter)
		
		self.b2 = DirectButton(text = ("Login", "Login", "Login", "Login"),
						  text_scale=btnScale,
						  borderWidth = borderW,
						  text_bg=self.couleurBack,
						  frameColor=self.couleurBack,
						  relief=2,
						  textMayChange = 1,
						  pad = (0,0),
						  command = self.setPlayer1Ready,
						  extraArgs = [True],
						  pos = (-0.75,0,0.45))
		self.b3 = DirectButton(text = ("Login", "Login", "Login", "Login"),
						  text_scale=btnScale,
						  borderWidth = borderW,
						  text_bg=self.couleurBack,
						  frameColor=self.couleurBack,
						  relief=2,
						  textMayChange = 1,
						  pad = (0,0),
						  command = self.setPlayer2Ready,
						  extraArgs = [True],
						  pos = (0.65,0,0.45))
		self.b4 = DirectButton(text = ("Play", "Play", "Play", "Play"),
						  text_scale=btnScale,
						  borderWidth = borderW,
						  text_bg=self.couleurDisabled,
						  frameColor=self.couleurDisabled,
						  relief=2,
						  textMayChange = 1,
						  pad = (0,0),
						  state = DGG.DISABLED,
						  command = self.setNiveauChoisi,
						  extraArgs = [self.mapID],
						  pos = (-0.05,0.4,0.67))

		
				

		
		#Initialisation de l'effet de transition
		curtain = loader.loadTexture("../asset/Menu/load.png")

		self.transition = Transitions(loader)
		self.transition.setFadeColor(0, 0, 0)
		self.transition.setFadeModel(curtain)

		self.sound = loader.loadSfx("../asset/Menu/shotgun.mp3")

	def setPlayer1Ready(self,state):
		self.username1 = self.username1.get()
		self.password1 = self.password1.get()
		self.joueur1 = self.user.read(self.username1,self.password1)

		if self.joueur1 == 1 :
			self.setText("Mauvais nom d'utilisateur")
		elif self.joueur1 == 0 : 
			self.setText("Mauvais mot de passe")
		else :
			self.player1ready = state
			self.b2['state'] = DGG.DISABLED
			self.b2['frameColor'] = self.couleurDisabled
			self.b2['text_bg'] = self.couleurDisabled
			if self.player1ready == True and self.player2ready == True :
				self.setText("Welcome to Tank'em !")
				self.b4['state'] = DGG.NORMAL
				self.b4['frameColor'] = self.couleurBack
				self.b4['text_bg'] = self.couleurBack
			elif self.player1ready :
				self.setText('Player 2 must also login')
			elif self.player2ready :
				self.settext('Player 1 must also login')
			else :
				self.setText('Both players must login')

	def setPlayer2Ready(self,state):
		self.username2 = self.username1.get()
		self.password2 = self.password1.get()
		self.joueur2 = self.user.read(self.username2,self.password2)

		if self.joueur2 == 1 :
			self.setText("Mauvais nom d'utilisateur")
		elif self.joueur2 == 0 : 
			self.setText("Mauvais mot de passe")
		else :
			self.player2ready = state
			self.b3['state'] = DGG.DISABLED
			self.b3['frameColor'] = self.couleurDisabled
			self.b3['text_bg'] = self.couleurDisabled
			if self.player1ready == True and self.player2ready == True :
				self.setText("Welcome to Tank'em !")
				self.b4['state'] = DGG.NORMAL
				self.b4['frameColor'] = self.couleurBack
				self.b4['text_bg'] = self.couleurBack
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
	def cacher(self):
			#Est esssentiellement un code de "loading"
			#On remet la caméra comme avant
			base.cam.node().getDisplayRegion(0).setSort(self.baseSort)
			#On cache les menus
			self.background.hide()
			self.b2.hide()
			self.b3.hide()
			self.b4.hide()
			self.username1.hide()
			self.username2.hide()
			self.password1.hide()
			self.password2.hide()
			self.messageBox.hide()
			self.labelplayer1.hide()
			self.labelpassword1.hide()
			self.labelPlayer2.hide()
			self.labelpassword2.hide()
			self.labelMessageBox.hide()

	def setNiveauChoisi(self,idNiveau):
			self.gameLogic.setIdNiveau(idNiveau)
			self.chargeJeu()

	def chargeJeu(self):
			#On démarre!
			Sequence(Func(lambda : self.transition.irisOut(0.2)),
					 SoundInterval(self.sound),
					 Func(self.cacher),
					 Func(lambda : messenger.send("DemarrerPartie")),
					 Wait(0.2), #Bug étrange quand on met pas ça. L'effet de transition doit lagger
					 Func(lambda : self.transition.irisIn(0.2))
			).start()

	def calculateName(self, joueur):
		self.statsJoueur = joueur.getStats()
		print self.statsJoueur
			