## -*- coding: utf-8 -*-
import inclureCheminCegep

#Importe la configuration de notre jeu
from panda3d.core import loadPrcFile
loadPrcFile("config/ConfigTankem.prc")

import sys

#Ajout des chemins vers les librarires
import inclureCheminCegep
print(sys.path)

#Module de Panda3D
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from panda3d.bullet import BulletWorld
from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletDebugNode
from panda3d.ai import *


#Modules internes
from constructionMap import Carte
from tank import Tank
from item import Item
 
class Tankem(ShowBase):
    def __init__(self):

        ShowBase.__init__(self)

    def preparer(self):
        self.initialiserBulletPhysics()

        self.initialiserCamera()
        self.carte = Carte(self.mondePhysique)
        self.carte.construireDecor(self.camera)
        self.carte.construireBase()
        self.initialiserControle()

        #Lumière du skybox
        plight = PointLight('plight')
        plight.setColor(VBase4(1,1,1,1))
        plnp = render.attachNewNode(plight)
        plnp.setPos(0,0,0)
        self.camera.setLight(plnp)

        #Simule le soleil
        dlight = DirectionalLight('dlight')
        dlight.setColor(VBase4(0.8, 0.8, 0.6, 1))
        dlight.get_lens().set_fov(75);
        dlight.get_lens().set_near_far(0.1, 60);
        dlight.get_lens().set_film_size(30,30);
        dlnp = render.attachNewNode(dlight)
        dlnp.setPos(Vec3(-2,-2,7))
        dlnp.lookAt(render)
        render.setLight(dlnp)
        #dlight.show_frustum()

        #Lumière ambiante
        alight = AmbientLight('alight')
        alight.setColor(VBase4(0.25, 0.25, 0.25, 1))
        alnp  = render.attachNewNode(alight)
        render.setLight(alnp)

        dlight.setShadowCaster(True, 1024,1024)
        # Enable the shader generator for the receiving nodes
        render.setShaderAuto()

        #Création d'une carte de base
        self.creerCarteParDefaut()

        #Fonction qui sert à optimiser
        #Doit être appelée après la création de la carte
        #Ça va prendre les objets qui ne bougent pas et en faire un seul gros
        self.carte.figeObjetImmobile()

    def creerCarteParDefaut(self):
        self.carte.creerMur(4,5)
        self.carte.creerMur(5,4)

        self.carte.creerMur(8,2)
        self.carte.creerMur(9,9)
        self.carte.creerMur(8,3)
        self.carte.creerMur(8,4)

        self.carte.creerMur(2,8)
        self.carte.creerMur(3,8)
        self.carte.creerMur(4,8)

        self.carte.creerMur(1,2)
        self.carte.creerMur(1,1)
        self.carte.creerMur(2,1)
        self.carte.creerMurMobile(1,3)
        self.carte.creerMurMobile(3,1)

        self.carte.creerItem(6,7,"Shotgun")

        #self.carte.creerItemPositionHasard()

        self.carte.creerChar(6,6,0,Vec3(0.4,0.6,0))
        self.carte.creerChar(3,3,1,Vec3(0.6,0.4,0.9))

        #Dans la carte par défaut, des items vont appraître constamment
        self.carte.genererItemParInterval(5,10)

    def initialiserCamera(self):
        #On doit désactiver le contrôle par défaut de la caméra autrement on ne peut pas la positionner et l'orienter
        self.disableMouse()

        #Le flag pour savoir si la souris est activée ou non n'est pas accessible
        #Petit fail de Panda3D
        self.mouseEnabled = False
        self.placerCameraInitiale()
        self.taskMgr.add(self.updateCamera, "updateCamera")

    def placerCameraInitiale(self):
        #Défini la position et l'orientation de la caméra
        self.positionBaseCamera = Vec3(0,-18,32)
        self.camera.setPos(self.positionBaseCamera)
        #On dit à la caméra de regarder l'origine (point 0,0,0)
        self.camera.lookAt(self.render)

    def initialiserBulletPhysics(self):
        debugNode = BulletDebugNode('Debug')
        debugNode.showWireframe(True)
        debugNode.showConstraints(True)
        debugNode.showBoundingBoxes(False)
        debugNode.showNormals(False)
        self.debugNP = render.attachNewNode(debugNode)

        self.mondePhysique = BulletWorld()
        self.mondePhysique.setGravity(Vec3(0, 0, -9.81))
        self.mondePhysique.setDebugNode(self.debugNP.node())
        self.taskMgr.add(self.updatePhysics, "updatePhysics")

        self.taskMgr.add(self.updateCarte, "updateCarte")

    #Mise à jour du moteur de physique
    def updateCamera(self,task):
        #On ne touche pas à la caméra si on est en mode debug
        if(self.mouseEnabled):
            return task.cont

        vecTotal = Vec3(0,0,0)
        distanceRatio = 1.0
        if (len(self.carte.listTank) != 0):
            for tank in self.carte.listTank:
                vecTotal += tank.noeudPhysique.getPos()
            vecTotal = vecTotal/len(self.carte.listTank)

        vecTotal.setZ(0)
        self.camera.setPos(vecTotal + self.positionBaseCamera)
        return task.cont

    #Mise à jour du moteur de physique
    def updatePhysics(self,task):
        dt = globalClock.getDt()
        self.mondePhysique.doPhysics(dt)
        #print(len(self.mondePhysique.getManifolds()))

        #Analyse de toutes les collisions
        for entrelacement in self.mondePhysique.getManifolds():
            node0 = entrelacement.getNode0()
            node1 = entrelacement.getNode1()
            self.carte.traiterCollision(node0, node1)
        return task.cont

    def updateCarte(self,task):
        self.carte.update()
        return task.cont

    def initialiserControle(self):
        #Informations pour débugger
        self.accept("escape", sys.exit)
        self.accept('f1', self.toggleDebogue)
        self.accept('f2', self.toggleFreeCam)

        #Joueur 1
        self.accept("w", self.relaiControle, [0,"avance"])
        self.accept("s", self.relaiControle, [0,"recule"])
        self.accept("w-up", self.relaiControle, [0,"avance-stop"])
        self.accept("s-up", self.relaiControle, [0,"recule-stop"])

        self.accept("a", self.relaiControle, [0,"tourne-gauche"])
        self.accept("d", self.relaiControle, [0,"tourne-droit"])
        self.accept("a-up", self.relaiControle, [0,"tourne-gauche-stop"])
        self.accept("d-up", self.relaiControle, [0,"tourne-droit-stop"])

        self.accept("v", self.relaiControle, [0,"arme-primaire"])
        self.accept("b", self.relaiControle, [0,"arme-secondaire"])
        self.accept("n", self.relaiControle, [0,"exploser-balle"])

        #Joueur 2
        self.accept("arrow_up", self.relaiControle, [1,"avance"])
        self.accept("arrow_down", self.relaiControle, [1,"recule"])
        self.accept("arrow_up-up", self.relaiControle, [1,"avance-stop"])
        self.accept("arrow_down-up", self.relaiControle, [1,"recule-stop"])

        self.accept("arrow_left", self.relaiControle, [1,"tourne-gauche"])
        self.accept("arrow_right", self.relaiControle, [1,"tourne-droit"])
        self.accept("arrow_left-up", self.relaiControle, [1,"tourne-gauche-stop"])
        self.accept("arrow_right-up", self.relaiControle, [1,"tourne-droit-stop"])

        self.accept("1", self.relaiControle, [1,"arme-primaire"])
        self.accept("2", self.relaiControle, [1,"arme-secondaire"])
        self.accept("3", self.relaiControle, [1,"exploser-balle"])

    def relaiControle(self, identifiant, message):
        self.carte.listTank[identifiant].traiterCommande(message)

    def toggleDebogue(self):
        base.messenger.toggleVerbose()
        if self.debugNP.isHidden():
            self.debugNP.show()
            base.setFrameRateMeter(True)
        else:
            self.debugNP.hide()
            base.setFrameRateMeter(False)

    def toggleFreeCam(self):
        if(not self.mouseEnabled):
            self.enableMouse()
            self.mouseEnabled = True
        else:
            self.disableMouse()
            self.placerCameraInitiale()
            self.mouseEnabled = False

#Main de l'application.. assez simple!
app = Tankem()
app.preparer()
#app.toggleDebogue()
app.run()