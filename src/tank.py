## -*- coding: utf-8 -*-
import inclureCheminCegep

import sys
from panda3d.bullet import *
from panda3d.core import *
from panda3d.ai import *
from direct.interval.IntervalGlobal import *
import math


class Tank():
    def __init__(self, identifiant,couleur,mondePhysique):
        #Défini les variables pour avancer et tourner
        self.speed = Vec3(0,0,0)
        self.omega = 0.0
        self.pointDeVieMax = 100
        self.pointDeVie = self.pointDeVieMax

        self.etat = "actif"
        self.hackRecuperation = False
        self.couleur = couleur

        self.debloquerTir()

        #Défini les armes de base
        self.armePrimaire = "Canon"
        self.armeSecondaire = "Aucun"

        self.identifiant = identifiant
        # On charge le modèles
        self.modele = loader.loadModel("../asset/Tank/tank")
        #On réduit sa taille un peu...
        self.modele.setScale(0.75,0.75,0.75)
        #On multiple la couleur de la texture du tank par ce facteur. Ça permet de modifier la couleur de la texture du tank
        self.modele.setColorScale(couleur.getX(),couleur.getY(),couleur.getZ(),1)

        #On ajoute une boite
        shape = BulletBoxShape(Vec3(0.6, 0.75, 0.3))
        #shape = BulletCapsuleShape(0.3, 0.75, ZUp)

        #On ajoute un contrôlleur de personnage
        self.playerNode = BulletCharacterControllerNode(shape, 0.4, 'ControlleurTank_' + str(self.identifiant))
        self.noeudPhysique = render.attachNewNode(self.playerNode)

        #Pour ne pas que le char soit entré dans le sol lors de son apparition, on le soulève un peu
        self.noeudPhysique.setZ(1.0)
        mondePhysique.attachCharacter(self.noeudPhysique.node())
        #On reparente le modele au noeud physique afin qu'il le suive
        self.modele.reparentTo(self.noeudPhysique)

        #Ajustement de la hauteur du modèle pour que la physique soit vis-à-vis le modèle
        self.modele.setZ(-0.25)

        self.noeudPhysique.setTag("EntiteTankem","Tank")
        self.noeudPhysique.setTag("IdTank",str( self.identifiant))

    def traiterCommande(self,message):
        directionHaut = Vec3(0,1,0)
        directionBas = Vec3(0,-1,0)
        directionGauche = Vec3(-1,0,0)
        directionDroite = Vec3(1,0,0)

        if(self.etat != "actif"):
            return

        if(message == "avance"):
            self.speed += directionHaut
        elif(message == "avance-stop"):
            self.speed -= directionHaut
        elif(message == "recule"):
            self.speed += directionBas
        elif(message == "recule-stop"):
            self.speed -= directionBas
        elif(message == "tourne-gauche"):
            self.speed += directionGauche
        elif(message == "tourne-gauche-stop"):
            self.speed -= directionGauche
        elif(message == "tourne-droit"):
            self.speed += directionDroite
        elif(message == "tourne-droit-stop"):
            self.speed -= directionDroite
        elif(message == "arme-primaire"):
            self.attaquer(self.armePrimaire)
        elif(message == "arme-secondaire"):
            self.attaquer(self.armeSecondaire)
        elif(message == "exploser-balle"):
            messenger.send("detonateur-explosion", [self.identifiant])

            #Todo
            #Shotgun
            #Ray
            #Passthrough

    def attaquer(self, nomArme):
        #Bloque le tir des balles
        if(self.bloquerTir):
            return

        hauteurCanon = Vec3(0,0,0.5)
        distanceCanon = 2.2

        hauteurGrenade = Vec3(0,0,0.7)
        delaiArme = 0

        distanceDerriere = 1.9

        directionQuePointeLeTank = render.getRelativeVector(self.noeudPhysique, Vec3.forward())
        directionDroite = render.getRelativeVector(self.noeudPhysique, Vec3.right())
        directionGauche = render.getRelativeVector(self.noeudPhysique, Vec3.left())

        if(nomArme == "Canon"):
            messenger.send("tirerCanon", [self.identifiant,self.noeudPhysique.getPos() + hauteurCanon + directionQuePointeLeTank * distanceCanon, directionQuePointeLeTank])
            delaiArme = 1.2
        elif(nomArme == "Grenade"):
            messenger.send("lancerGrenade", [self.identifiant,self.noeudPhysique.getPos() + hauteurGrenade, directionQuePointeLeTank])
            delaiArme = 0.8
        elif(nomArme == "Mitraillette"):
            #Tir une balle mais moins de délai pour tirer
            messenger.send("tirerMitraillette", [self.identifiant,self.noeudPhysique.getPos() + hauteurCanon + directionQuePointeLeTank * distanceCanon, directionQuePointeLeTank])
            delaiArme = 0.4
        elif(nomArme == "Piege"):
            messenger.send("deposerPiege", [self.identifiant,self.noeudPhysique.getPos() + hauteurCanon - directionQuePointeLeTank * distanceDerriere, - directionQuePointeLeTank])
            delaiArme = 0.8
        elif(nomArme == "Shotgun"):
            messenger.send("tirerShotgun", [self.identifiant,self.noeudPhysique.getPos() + hauteurCanon + directionQuePointeLeTank * distanceCanon, directionQuePointeLeTank])
            directionDroiteDiagonale = directionQuePointeLeTank + directionQuePointeLeTank + directionDroite
            directionDroiteDiagonale.normalize()
            directionGaucheDiagonale = directionQuePointeLeTank + directionQuePointeLeTank + directionGauche
            directionGaucheDiagonale.normalize()
            messenger.send("tirerShotgun", [self.identifiant,self.noeudPhysique.getPos() + hauteurCanon + directionDroiteDiagonale * distanceCanon, directionDroiteDiagonale])
            messenger.send("tirerShotgun", [self.identifiant,self.noeudPhysique.getPos() + hauteurCanon + directionGaucheDiagonale * distanceCanon, directionGaucheDiagonale])
            delaiArme = 1.8
        elif(nomArme == "AucuneArme"):
            #Ne fais rien
            pass

        #Va bloquer le tir des balles le temps de la recharge
        self.bloquerTir = True
        attendre = Wait(delaiArme)
        fonctionDebloquer = Func(self.debloquerTir)
        sequenceBlloquageTir = Sequence(attendre,fonctionDebloquer)
        sequenceBlloquageTir.start()

    def debloquerTir(self):
        self.bloquerTir = False

    def tombe(self, mondePhysique):
        self.elimineJoueur(mondePhysique)

        #On le fait tourner un peu
        self.noeudPhysiqueExplosion.node().applyTorqueImpulse(YUp * 1)

        #On le laisse tomber :-D On désactive la collision avec le plancher
        self.noeudPhysiqueExplosion.setCollideMask(BitMask32.allOff())

    def explose(self, mondePhysique):
        self.elimineJoueur(mondePhysique)
        #On lui donne une petite poussé car c'est drôle!
        self.noeudPhysiqueExplosion.node().applyImpulse(ZUp * 5,Point3(-0.5,-0.5,0))

    def elimineJoueur(self, mondePhysique):
        if(self.etat != "actif"):
            return
        self.etat = "inactif"
        self.speed = Vec3(0,0,0)
        self.omega = 0.0

        self.changerPointDeVie(0)

        #On devrait récupérer l'ancienne forme et non s'en créer une
        forme = BulletBoxShape(Vec3(0.6, 0.75, 0.3))

        #On ajoute une forme physique standard
        explosionNoeud = BulletRigidBodyNode("TankExplosion")
        explosionNoeud.addShape(forme)
        self.noeudPhysiqueExplosion = render.attachNewNode(explosionNoeud)
        self.noeudPhysiqueExplosion.node().setMass(3.0)
        self.noeudPhysiqueExplosion.setTransform(self.noeudPhysique.getTransform())
        self.noeudPhysiqueExplosion.setZ(self.noeudPhysiqueExplosion.getZ() + 1.0)
        self.modele.reparentTo(self.noeudPhysiqueExplosion)
        mondePhysique.attachRigidBody(explosionNoeud)

        mondePhysique.removeCharacter(self.playerNode)
        self.playerNode = None        

    def prendDommage(self, dommage, mondePhysique):

        #Chaque collision détectée nous fait perdre un point de vie
        self.changerPointDeVie(self.pointDeVie - dommage)

        #Vérifie si le tank explose
        if(self.pointDeVie <= 0):
            self.explose(mondePhysique)

    def changerPointDeVie(self, nouvelleValeur):
        self.pointDeVie = nouvelleValeur

        #On prévient l'interface graphique du changement
        pointDeVieSurCent = 100 * self.pointDeVie / self.pointDeVieMax
        messenger.send("changerValeurPointDeVie", [self.identifiant,pointDeVieSurCent])


    def recupereItem(self, armeId):
        #ATTENTION: pour une raison inconnue, la récupération de l'itme est détectée 2 fois...
        #On fait un beau hack...
        if(not self.hackRecuperation):
            self.hackRecuperation = True
            return

        if(self.hackRecuperation):
            self.hackRecuperation = False
            #Assigne une nouvelle arme à l'arme secondaire
            self.armeSecondaire = armeId

    def traiteMouvement(self):
        if (self.playerNode != None):

            #Si on a aucun mouvement, on ne bouge pas le tank
            if(self.speed.lengthSquared() < 0.2):
                self.playerNode.setLinearMovement(0.0, False)
                self.playerNode.setAngularMovement(0.0)
            else:
                speedCopy = Vec3(self.speed)
                speedCopy.normalize()

                vitesseAvancer = 7
                vitesseMaxTourner = 1500
                #On bouge le joueur dans la bonne direction
                #TODO: Renormalize le vecteur pour ne pas avoir un bug comme le Quake 3
                #qui nous permettrait de bouger en diagonal
                self.playerNode.setLinearMovement(speedCopy * vitesseAvancer, False)



                #Cacul un vectoriel pour tourner le tank quand on bouge
                #C'est plutôt complexe. On se base sur la théorie du pilotage
                # ("steering behavior"). Vous trouverez plein d'articles sur le sujet
                directionQuePointeLeTank = render.getRelativeVector(self.noeudPhysique, Vec3.forward())
                signeAngle = 0
                produitVectoriel = directionQuePointeLeTank.cross(speedCopy)
                angleDegre = directionQuePointeLeTank.angleDeg(speedCopy)

                #Décide de la direction de rotation
                if(produitVectoriel.getZ() > 0.01):
                    signeAngle = 1.0

                if(produitVectoriel.getZ() < -0.01):
                    signeAngle = -1.0

                #Réduire progressivement la rotation selon l'angle
                #avec une courbe en racine carrée
                angleMax = 180
                facteur = angleDegre / angleMax
                vitesseTourner = vitesseMaxTourner * math.sqrt(facteur)

                angleCritiqueIntermediaire = 5.0
                if(angleDegre < angleCritiqueIntermediaire):
                    vitesseIntermediaireTourner = vitesseMaxTourner * 0.5
                    vitesseTourner = vitesseIntermediaireTourner * facteur

                #Arrêter la rotation selon l'angle
                angleCritiqueDegre = 1.0
                if(angleDegre < angleCritiqueDegre):
                    vitesseTourner = 0.0
                    signeAngle = 0.0
                self.playerNode.setAngularMovement(signeAngle * vitesseTourner)