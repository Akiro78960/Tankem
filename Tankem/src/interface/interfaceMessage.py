## -*- coding: utf-8 -*-
from util import *

from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText 
from direct.gui.DirectGui import *
from panda3d.core import *
from direct.interval.LerpInterval import *
from direct.interval.IntervalGlobal import *
 
class InterfaceMessage(ShowBase):
    def __init__(self):
        self.accept("tankElimine",self.displayGameOver)
        self.callBackFunction = None

    def effectCountDownStart(self,nombre,callbackFunction):
        self.callBackFunction = callbackFunction
        self.displayCountDown(nombre)
        
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

        sequence = Sequence(delai,effetFadeOut,Func(self.callBackFunction))
        sequence.start()

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
