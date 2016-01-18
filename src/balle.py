## -*- coding: utf-8 -*-
import inclureCheminCegep

import sys
from direct.showbase.ShowBase import ShowBase
from panda3d.bullet import *
from panda3d.core import *
from panda3d.ai import *
from direct.interval.IntervalGlobal import *
import random

class Balle(ShowBase):
    def __init__(self, identifiantLanceur,mondePhysique):
        self.mondePhysique = mondePhysique
        self.identifiantLanceur = identifiantLanceur
        # On charge le modèles
        self.modele = loader.loadModel("../asset/Balle/ball")
        self.modele.reparentTo(render)
        #On réduit sa taille un peu...
        self.modele.setScale(0.5,0.5,0.5)

        #On ajoute une sphere de physique
        forme = BulletSphereShape(0.2)
        noeud = BulletRigidBodyNode("Balle")
        noeud.addShape(forme)
        self.noeudPhysique = render.attachNewNode(noeud)
        self.noeudPhysique.node().setMass(1.0)
        self.modele.reparentTo(self.noeudPhysique)

        self.accept("declencher-explosion",self.exploser)

        self.noeudPhysique.setTag("EntiteTankem","Balle")

    def exploser(self, identifiantLanceur):
        if(identifiantLanceur == self.identifiantLanceur and self.etat == "actif"):
            self.etat = "explose"

            #Arrêt de la sequence de destruction automatique
            if hasattr(self, 'sequenceExplosionAutomatique'):
               self.sequenceExplosionAutomatique.finish()

            #On désactive le mouvement sur cette balle
            #Les collisions seront détectées mais la balle
            #ne bougera pas
            self.noeudPhysique.node().setKinematic(True)

            self.modele.setTransparency(TransparencyAttrib.MAlpha)
            intervalPhysique = LerpScaleInterval(self.noeudPhysique, 0.2, 8.0, 1.0)
            intervalCouleur = LerpColorScaleInterval(self.modele,0.3,LVecBase4(0.8,0.2,0.2,0),self.modele.getColorScale())
            fonctionDetruire = Func(self.destroy)
            self.sequenceDetruire = Sequence(intervalCouleur,fonctionDetruire)

            intervalPhysique.start()
            self.sequenceDetruire.start()

    def projetter(self, position, direction):
        self.etat = "actif"

        self.noeudPhysique.setPos(position)

        self.modele.setColorScale(0.8,0.3,0,1)
        
        self.noeudPhysique.node().setGravity(0.0)
        self.noeudPhysique.node().setLinearDamping(0.0)
        self.noeudPhysique.node().setFriction(0.0)
        self.noeudPhysique.node().setRestitution(2.0)
        vitesseBalle = 14
        self.noeudPhysique.node().applyCentralImpulse(direction * vitesseBalle)
        self.mondePhysique.attachRigidBody(self.noeudPhysique.node())

        self.intervalExplosion(1.2)

    def projetterRapide(self, position, direction):
        self.etat = "actif"

        self.noeudPhysique.setPos(position)

        self.modele.setColorScale(0.1,0.1,0,1)
        
        self.noeudPhysique.node().setGravity(0.0)
        self.noeudPhysique.node().setLinearDamping(0.0)
        self.noeudPhysique.node().setFriction(0.0)
        self.noeudPhysique.node().setRestitution(2.0)
        vitesseBalle = 16
        self.noeudPhysique.node().applyCentralImpulse(direction * vitesseBalle)
        self.mondePhysique.attachRigidBody(self.noeudPhysique.node())

        self.intervalExplosion(0.5)

    def projetterVariable(self, position, direction):
        self.etat = "actif"

        self.noeudPhysique.setPos(position)

        self.modele.setColorScale(0.9,0.9,0.9,1)
        
        self.noeudPhysique.node().setGravity(0.0)
        self.noeudPhysique.node().setLinearDamping(0.0)
        self.noeudPhysique.node().setFriction(0.0)
        self.noeudPhysique.node().setRestitution(2.0)
        vitesseBalle = random.uniform(10,16)
        self.noeudPhysique.node().applyCentralImpulse(direction * vitesseBalle)
        self.mondePhysique.attachRigidBody(self.noeudPhysique.node())

        self.intervalExplosion(0.5)

    def deposer(self, position, direction):
        self.etat = "actif"

        self.noeudPhysique.setPos(position)

        self.modele.setColorScale(0.3,0.9,0.3,1)
        
        self.noeudPhysique.node().setLinearDamping(0.7)
        self.noeudPhysique.node().setFriction(0.7)
        self.noeudPhysique.node().setRestitution(0.0)
        vitesseBalle = 1
        self.noeudPhysique.node().applyCentralImpulse(direction * vitesseBalle)
        self.mondePhysique.attachRigidBody(self.noeudPhysique.node())

        self.intervalExplosion(10)

    def destroy(self):
        self.etat = "Detruit"
        self.mondePhysique.removeRigidBody(self.noeudPhysique.node())
        self.noeudPhysique.removeNode()
        self.modele.removeNode()

    def lancer(self, position, direction):
        self.etat = "actif"

        self.modele.setColorScale(0.8,0.1,0.6,1)

        self.noeudPhysique.setPos(position)
        self.noeudPhysique.node().setMass(2.0)
        self.noeudPhysique.node().setLinearDamping(0.1)
        self.noeudPhysique.node().setAngularDamping(0.99)
        self.noeudPhysique.node().setFriction(0.9)
        self.noeudPhysique.node().setRestitution(1.0)
        vitesseBalle = 9
        #On lancera à enciron 60 degré la balle
        directionFinale = direction + Vec3(0,0,3)
        directionFinale.normalize()
        self.noeudPhysique.node().setLinearVelocity(directionFinale * vitesseBalle)
        self.mondePhysique.attachRigidBody(self.noeudPhysique.node())

        self.intervalExplosion(3.0)

    def intervalExplosion(self, delai):
        #On fait exploser la balle dans quelques secondes
        delai = Wait(delai)
        fonctionExploser = Func(self.exploser, self.identifiantLanceur)
        self.sequenceExplosionAutomatique = Sequence(delai,fonctionExploser)
        self.sequenceExplosionAutomatique.start()