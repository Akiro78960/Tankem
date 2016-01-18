## -*- coding: utf-8 -*-
import inclureCheminCegep

import sys
from panda3d.bullet import *
from panda3d.core import *
from panda3d.ai import *
from direct.interval.IntervalGlobal import *


class Tank():
    def __init__(self, identifiant,couleur,mondePhysique):
        #Défini les variables pour avancer et tourner
        self.speed = Vec3(0,0,0)
        self.omega = 0.0

        self.etat = "actif"
        self.hackRecuperation = False

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

        vitesseAvancer = Vec3(0,6,0)
        vitesseReculer = Vec3(0,-4,0)
        vitesseTourner = 200

        if(self.etat != "actif"):
            return

        if(message == "avance"):
            self.speed += vitesseAvancer
        elif(message == "avance-stop"):
            self.speed -= vitesseAvancer
        elif(message == "recule"):
            self.speed += vitesseReculer
        elif(message == "recule-stop"):
            self.speed -= vitesseReculer
        elif(message == "tourne-gauche"):
            self.omega += vitesseTourner
        elif(message == "tourne-gauche-stop"):
            self.omega -= vitesseTourner
        elif(message == "tourne-droit"):
            self.omega -= vitesseTourner
        elif(message == "tourne-droit-stop"):
            self.omega += vitesseTourner
        elif(message == "arme-primaire"):
            self.attaquer(self.armePrimaire)
        elif(message == "arme-secondaire"):
            self.attaquer(self.armeSecondaire)
        elif(message == "exploser-balle"):
            messenger.send("declencher-explosion", [self.identifiant])

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

    def explose(self, mondePhysique):
        if(self.etat != "actif"):
            return
        self.etat = "inactif"
        self.speed = 0.0
        self.omega = 0.0

        #On devrait récupérer l'ancienne forme et non s'en créer une
        forme = BulletBoxShape(Vec3(0.6, 0.75, 0.3))

        #On ajoute une forme physique standard
        explosionNoeud = BulletRigidBodyNode("TankExplosion")
        explosionNoeud.addShape(forme)
        self.noeudPhysiqueExplosion = render.attachNewNode(explosionNoeud)
        self.noeudPhysiqueExplosion.node().setMass(3.0)
        self.noeudPhysiqueExplosion.setTransform(self.noeudPhysique.getTransform())
        self.noeudPhysiqueExplosion.setZ(1.0)
        self.modele.reparentTo(self.noeudPhysiqueExplosion)
        mondePhysique.attachRigidBody(explosionNoeud)
        self.noeudPhysiqueExplosion.node().applyImpulse(ZUp * 5,Point3(-0.5,-0.5,0))

        mondePhysique.removeCharacter(self.playerNode)
        self.playerNode = None


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
            self.playerNode.setLinearMovement(self.speed, True)
            self.playerNode.setAngularMovement(self.omega)
