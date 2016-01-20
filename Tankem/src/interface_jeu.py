## -*- coding: utf-8 -*-
import inclureCheminCegep

from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText 
from direct.gui.DirectGui import *
from panda3d.core import *
 
class interface_jeu(ShowBase):
	def __init__(self, identificateurTank, couleurBarre):
		self.identificateurTank = identificateurTank

		#On doit créer une couleur avec 4 composantes sinon ça crash... beurk
		couleurBarreAlpha = Vec4(couleurBarre.getX(),couleurBarre.getY(),couleurBarre.getZ(),1)

		positionBarreVie = Vec3(-1.1,0,0.85) #tank 0
		if(identificateurTank == 1): #tank 1
			positionBarreVie.setX(1.1)

		self.barreVie = DirectWaitBar(barColor = couleurBarreAlpha, text = "", value = 100, pos = positionBarreVie, scale=0.5)

		#couleurChargeAlpha = couleurBarreAlpha * 0.8
		#positionBarreCharge = Vec3(-1.1,0,0.75) #tank 0
		#if(identificateurTank == 1): #tank 1
		#	positionBarreCharge.setX(1.1)
		#self.barCharge = DirectWaitBar(barColor = couleurChargeAlpha, text = "", value = 100, pos = positionBarreCharge, scale=0.5)

		self.accept("changerValeurPointDeVie",self.changerValeurPointDeVie)
		#self.accept("changerValeurCharge",self.changerValeurCharge)

	def changerValeurPointDeVie(self,identificateurTank,nouvelleValeur):
		if(self.identificateurTank == identificateurTank):
			self.barreVie['value'] = nouvelleValeur

	#Incomplet
	#def changerValeurCharge(self,identificateurTank,nouvelleValeur):
	#	if(self.identificateurTank == identificateurTank):
	#		self.barCharge['value'] = nouvelleValeur