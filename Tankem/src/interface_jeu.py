## -*- coding: utf-8 -*-
import inclureCheminCegep

from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText 
from direct.gui.DirectGui import *
from panda3d.core import *
from direct.interval.LerpInterval import *
from direct.interval.IntervalGlobal import *
 
class interface_jeu(ShowBase):
	def __init__(self, identificateurTank, couleurBarre):
		self.identificateurTank = identificateurTank

		#On doit créer une couleur avec 4 composantes sinon ça crash... beurk
		couleurBarreAlpha = Vec4(couleurBarre.getX(),couleurBarre.getY(),couleurBarre.getZ(),1)

		positionBarreVie = Vec3(-1.1,0,0.85) #tank 0
		if(identificateurTank == 1): #tank 1
			positionBarreVie.setX(1.1)

		self.barreVie = DirectWaitBar(barColor = couleurBarreAlpha, text = "", value = 100, pos = positionBarreVie, scale=0.5)

		couleurChargeAlpha = couleurBarreAlpha * 0.8
		positionBarreCharge = Vec3(-1.4,0,0.75) #tank 0
		if(identificateurTank == 1): #tank 1
			positionBarreCharge.setX(1.4)
		self.barCharge = DirectWaitBar(barColor = couleurChargeAlpha, text = "", value = 100, pos = positionBarreCharge, scale=0.2)

		self.accept("effetPointDeVie",self.effetPointDeVie)
		self.accept("effetRecharge",self.effetRecharge)
		self.accept("tankElimine",self.displayGameOver)

		#À mettre dans game logic
		self.displayCountDown(3)

	def effetPointDeVie(self,identificateurTank,nouvelleValeur):
		if(self.identificateurTank == identificateurTank):
			self.changerValeurPointDeVie(nouvelleValeur)


	def effetRecharge(self,identificateurTank,duree):
		if(self.identificateurTank == identificateurTank):
			effetRecharge = LerpFunc(self.changerValeurCharge,fromData=0,toData=100, duration=duree, blendType='easeOut')
			effetRecharge.start()

	def changerValeurPointDeVie(self,nouvelleValeur):
			self.barreVie['value'] = nouvelleValeur

	def changerValeurCharge(self,nouvelleValeur):
			self.barCharge['value'] = nouvelleValeur

	def displayCountDown(self, nombre):

		message = str(nombre)
		startScale = 0.4

		text = TextNode('Compte à rebour')
		text.setText(message)
		textNodePath = aspect2d.attachNewNode(text)
		textNodePath.setScale(startScale)
		text.setShadow(0.05, 0.05)
		text.setShadowColor(0, 0, 0, 1)
		text.setTextColor(0.5, 0.5, 1, 1)
		text.setAlign(TextNode.ACenter)

		effetScale = LerpScaleInterval(textNodePath, 1.0, 0.05, startScale)
		effetFadeOut = LerpColorScaleInterval(textNodePath, 1.0, LVecBase4(1,1,1,0), LVecBase4(1,1,1,1))
		effetFadeOut.start()

		recursion = Func(self.displayCountDown,nombre-1)

		#Le prochain tour, on affiche la message de début de partie
		if(nombre == 1):
			recursion = Func(self.displayStartGame)

		sequence = Sequence(effetScale,recursion)
		sequence.start()

	def displayStartGame(self):
		message = "Tankem!"
		startScale = 0.4

		text = TextNode('Début de la partie')
		text.setText(message)
		textNodePath = aspect2d.attachNewNode(text)
		textNodePath.setScale(startScale)
		text.setShadow(0.05, 0.05)
		text.setShadowColor(0, 0, 0, 1)
		text.setTextColor(0.5, 0.5, 1, 1)
		text.setAlign(TextNode.ACenter)

		delai = Wait(0.3)
		effetFadeOut = LerpColorScaleInterval(textNodePath, 0.15, LVecBase4(1,1,1,0), LVecBase4(1,1,1,1), blendType = 'easeIn')

		sequence = Sequence(delai,effetFadeOut)
		sequence.start()
		
		#Emphase
		#text.setFrameColor(0, 0, 1, 1)
		#text.setFrameAsMargin(0.2, 0.2, 0.1, 0.1)
		#text.setCardColor(1, 1, 0.5, 1)
		#text.setCardAsMargin(0, 0, 0, 0)
		#text.setCardDecal(True)

	def displayGameOver(self, idPerdant):

		joueurGagnant = 1
		if(idPerdant == 1):
			joueurGagnant = 2

		message = "Kaboom! \n Joueur "+ str(joueurGagnant) + " a gagné!"
		startScale = 0.3

		text = TextNode('Fin de partie')
		text.setText(message)
		textNodePath = aspect2d.attachNewNode(text)
		textNodePath.setScale(startScale)
		text.setShadow(0.05, 0.05)
		text.setShadowColor(0, 0, 0, 1)
		text.setTextColor(0.5, 0.5, 1, 1)
		text.setAlign(TextNode.ACenter)

		delai = Wait(1.0)
		effetFadeIn = LerpColorScaleInterval(textNodePath, 1, LVecBase4(1,1,1,1), LVecBase4(1,1,1,0), blendType = 'easeIn')

		sequence = Sequence(delai,effetFadeIn)
		sequence.start()
