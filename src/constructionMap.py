## -*- coding: utf-8 -*-
import inclureCheminCegep

from direct.showbase import DirectObject
from panda3d.core import *
from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletBoxShape
from panda3d.bullet import YUp
from direct.interval.IntervalGlobal import *
import random

from tank import Tank
from balle import Balle
from item import Item
from interface_jeu import interface_jeu
from mazeUtil import MazeBuilder

#Module qui sert à la création des maps
class Carte(DirectObject.DirectObject):
    def __init__(self, mondePhysique):
        #initialisation des constantes utiles
        self.map_nb_tuile_x = 10
        self.map_nb_tuile_y = 10
        self.map_grosseur_carre = 2.0
        #On veut que le monde soit centré. On calcul donc le décalage nécessaire des tuiles
        self.position_depart_x = - self.map_grosseur_carre * self.map_nb_tuile_x / 2.0
        self.position_depart_y = - self.map_grosseur_carre * self.map_nb_tuile_y / 2.0

        self.listTank = []
        self.listeItem = []
        self.listeBalle = []

        #Initialise le contenu vide la carte
        #On y mettra les id selon ce qu'on met
        self.endroitDisponible = [[True for x in range(self.map_nb_tuile_x)] for x in range(self.map_nb_tuile_y)]

        #Initialize la carte
        self.mondePhysique = mondePhysique

        #Message qui permettent la création d'objets pendant la partie
        self.accept("tirerCanon",self.tirerCanon)
        self.accept("tirerMitraillette",self.tirerMitraillette)
        self.accept("lancerGrenade",self.lancerGrenade)
        self.accept("deposerPiege",self.deposerPiege)
        self.accept("tirerShotgun",self.tirerShotgun)

    def construireUI(self):
        self.interfaceJeu = []
        self.interfaceJeu.append(interface_jeu(0,self.listTank[0].couleur))
        self.interfaceJeu.append(interface_jeu(1,self.listTank[1].couleur))

    def bloquerEndroitGrille(self,i,j,doitBloquer):
        self.endroitDisponible[i][j] = doitBloquer

    def construireMapHasard(self):
        maze = MazeBuilder(self.map_nb_tuile_x, self.map_nb_tuile_y)
        mazeArray = maze.build()
        for row in mazeArray:
            for cell in row:
                if(cell.type == 1):
                    self.creerMur(cell.row, cell.col)

        self.creerChar(6,6,0,Vec3(0.1,0.1,0.1))
        self.creerChar(3,3,1,Vec3(0.9,0.9,0.9))

        #Dans la carte par défaut, des items vont appraître constamment
        self.genererItemParInterval(4,8)

    def construireDecor(self, camera):
        modele = loader.loadModel("../asset/Skybox/skybox")
        modele.set_bin("background", 0);
        modele.set_two_sided(True);
        modele.set_depth_write(False);
        modele.set_compass();
        modele.reparentTo(camera)

    def figeObjetImmobile(self):
        self.noeudOptimisation.flattenStrong()

    def construireBase(self):
        #Optimisation... on attache les objets statiques au même noeud et on utiliser
        #la méthode flattenStrong() pour améliorer les performances.
        self.noeudOptimisation = NodePath('NoeudOptimisation')
        self.noeudOptimisation.reparentTo(render)

        #Construction du plancher
        # On charge les tuiles qui vont former le plancher
        for i in range(0,self.map_nb_tuile_x):
            for j in range(0,self.map_nb_tuile_y):
                modele = loader.loadModel("../asset/Floor/Floor")
                # Reparentage du modèle à la racine de la scène
                modele.reparentTo(self.noeudOptimisation)
                self.placerSurGrille(modele,i, j)

        #Construction du plancher si on tombe
        #Un plan devrait marche mais j'ai un bug de collision en continu...
        shape = BulletBoxShape(Vec3(50,50,5))
        node = BulletRigidBodyNode('Frontiere sol')
        node.addShape(shape)
        np = render.attachNewNode(node)
        np.setTag("EntiteTankem","LimiteJeu")
        np.setPos(Vec3(0,0,-9.0))
        self.mondePhysique.attachRigidBody(node)

        #Construction de l'aire de jeu sur laquelle on joue
        shape = BulletBoxShape(Vec3(-self.position_depart_x, -self.position_depart_y, 2))
        node = BulletRigidBodyNode('Plancher')
        node.addShape(shape)
        np = render.attachNewNode(node)
        np.setTag("EntiteTankem","Plancher")
        HACK_VALUE = 0.02 #Optimisation de collision, les masques ne marchent pas
        np.setZ(-2.00 - HACK_VALUE)
        self.mondePhysique.attachRigidBody(node)

    def postInitialisation(self):
        self.construireUI()

    def placerSurGrille(self,noeud,positionX, positionY):
        # On place l'objet en calculant sa position sur la grille
        noeud.setX(self.position_depart_x + (positionX+0.5) * self.map_grosseur_carre)
        noeud.setY(self.position_depart_y + (positionY+0.5) * self.map_grosseur_carre)

    def tirerCanon(self, identifiantLanceur, position, direction):
        #Création d'une balle de physique
        balle = Balle(identifiantLanceur,self.mondePhysique)
        self.listeBalle.append(balle)
        balle.projetter(position,direction)

    def tirerMitraillette(self, identifiantLanceur, position, direction):
        #Création d'une balle de physique
        balle = Balle(identifiantLanceur,self.mondePhysique)
        self.listeBalle.append(balle)
        balle.projetterRapide(position,direction)

    def lancerGrenade(self, identifiantLanceur, position, direction):
        #Création d'une balle de physique
        balle = Balle(identifiantLanceur, self.mondePhysique)
        self.listeBalle.append(balle)
        balle.lancer(position,direction)

    def deposerPiege(self, identifiantLanceur, position, direction):
        #Création d'une balle de physique
        balle = Balle(identifiantLanceur, self.mondePhysique)
        self.listeBalle.append(balle)
        balle.deposer(position,direction)

    def tirerShotgun(self, identifiantLanceur, position, direction):
        #Création d'une balle de physique
        balle = Balle(identifiantLanceur,self.mondePhysique)
        self.listeBalle.append(balle)
        balle.projetterVariable(position,direction)

    #####################################################
    #Création des différentes entités sur la carte
    #####################################################
    def creerMur(self,positionX, positionY):
        # On charge le modèles
        modele = loader.loadModel("../asset/Wall/Wall")
        #On fait les cubes à peine plus petits afin que rien ne collisionne
        #Les groupes de collision ne fonctionnent pas alors on fait son possible... 
        HACK_VALUE = 0.98
        formeCollision = BulletBoxShape(Vec3(HACK_VALUE, HACK_VALUE, HACK_VALUE))
        noeud = BulletRigidBodyNode('Mur' + str(positionX) + '_' + str(positionY))
        decalagePosition = TransformState.makePos(Vec3(0,0,1))
        noeud.addShape(formeCollision,decalagePosition)
        noeudPhysique = render.attachNewNode(noeud)
        modele.reparentTo(noeudPhysique)
        noeudPhysique.node().setFriction(0.5)
        noeudPhysique.node().setRestitution(0.5)
        self.mondePhysique.attachRigidBody(noeud)

        noeudPhysique.reparentTo(self.noeudOptimisation)
        #On place le bloc sur la grille
        self.placerSurGrille(noeudPhysique,positionX,positionY)
        self.bloquerEndroitGrille(positionX,positionY,True)

    def creerItem(self, positionX, positionY, armeId):
        #L'index dans le tableau d'item coincide avec son
        #itemId. Ça va éviter une recherche inutile pendant l'éxécution
        itemCourrant = Item(armeId,self.mondePhysique)
        self.listeItem.append(itemCourrant)
        #On place le tank sur la grille
        self.placerSurGrille(itemCourrant.noeudPhysique,positionX,positionY)

    def creerItemHasard(self, positionX, positionY):
        listeItem = ["Mitraillette", "Shotgun", "Piege", "Grenade"]
        itemHasard = random.choice(listeItem)
        self.creerItem(positionX, positionY,itemHasard)

    def creerItemPositionHasard(self):
        #Pas de do while en Python! Beurk...
        randomX = random.randrange(0,self.map_nb_tuile_x-1)
        randomY = random.randrange(0,self.map_nb_tuile_y-1)

        #Tant qu'on trouve pas d'endroit disponibles...
        while(not self.endroitDisponible[randomX][randomY]):
            randomX = random.randrange(0,self.map_nb_tuile_x-1)
            randomY = random.randrange(0,self.map_nb_tuile_y-1)

        #Quand c'est fait on met un item au hasard
        self.creerItemHasard(randomX,randomY)

    def genererItemParInterval(self, delaiMinimum, delaiMaximum):
        #Délai au hasard entre les bornes
        delai = random.uniform(delaiMinimum, delaiMaximum)
        intervalDelai = Wait(delai)
        intervalCreerItem = Func(self.creerItemPositionHasard)
        intervalRecommence = Func(self.genererItemParInterval,delaiMinimum,delaiMaximum)

        sequenceCreation = Sequence(intervalDelai,
                                    intervalCreerItem,
                                    intervalRecommence,
                                    name="Creation item automatique")
        #On le joue une fois et il se rappelera lui-même :-)
        sequenceCreation.start()

    def creerMurMobile(self,positionX, positionY, mouvementInverse=False):
        # On charge le modèles
        modele = loader.loadModel("../asset/Wall/Wall")
        formeCollision = BulletBoxShape(Vec3(1, 1, 1))
        noeud = BulletRigidBodyNode('Mur-Mobile' + str(positionX) + '_' + str(positionY))
        decalagePosition = TransformState.makePos(Vec3(0,0,1))
        noeud.addShape(formeCollision,decalagePosition)
        noeudPhysique = render.attachNewNode(noeud)
        modele.reparentTo(noeudPhysique)
        noeudPhysique.node().setFriction(0.5)
        noeudPhysique.node().setRestitution(0.5)
        #On va l'animer et il faut le dire au moteur de physique
        #Ça évitera que la gravité s'applique
        noeud.setKinematic(True)
        self.mondePhysique.attachRigidBody(noeud)
        noeudPhysique.reparentTo(render)
        #On place le bloc sur la grille
        self.placerSurGrille(noeudPhysique,positionX,positionY)
        self.bloquerEndroitGrille(positionX,positionY,True)

        positionActuelle = noeudPhysique.getPos()
        tempsMouvement = 0.8
        blocPosInterval1 = LerpPosInterval( noeudPhysique,
                                            tempsMouvement,
                                            positionActuelle + Vec3(0,0,-1.95),
                                            startPos=positionActuelle)
        blocPosInterval2 = LerpPosInterval( noeudPhysique,
                                            tempsMouvement,
                                            positionActuelle,
                                            positionActuelle + Vec3(0,0,-1.95))
        delai = Wait(1.2)
        # On créé une séquence pour bouger le bloc
        mouvementBloc = Sequence()
        if(not mouvementInverse):
            mouvementBloc = Sequence(   blocPosInterval1,
                                        delai,
                                        blocPosInterval2,
                                        delai,
                                        name="mouvement-bloc" + str(positionX) + '_' + str(positionY))

        else:
            mouvementBloc = Sequence(   blocPosInterval2,
                                        delai,
                                        blocPosInterval1,
                                        delai,
                                        name="mouvement-bloc-inverse" + str(positionX) + '_' + str(positionY))
        

        mouvementBloc.loop()

    def creerChar(self,positionX, positionY, identifiant, couleur):
        tank = Tank(identifiant,couleur,self.mondePhysique)
        #On place le tank sur la grille
        self.placerSurGrille(tank.noeudPhysique,positionX,positionY)

        #Ajouter le char dans la liste
        self.listTank.append(tank)

    def traiterCollision(self,node0, node1):
        #Pas très propre mais enfin...
        indiceTank = int(self.traiterCollisionTankAvecObjet(node0, node1,"Balle"))
        if(indiceTank != -1):
            tireurBalleId = int(self.trouverTag(node0, node1, "lanceurId"))
            balleId = int(self.trouverTag(node0, node1, "balleId"))
            #Prend 1 de dommage par défaut si la balle n'a pas été tirée par le tank
            self.listeBalle[balleId].exploser()
            if(tireurBalleId != indiceTank):
                self.listTank[indiceTank].prendDommage(1,self.mondePhysique)
            return
        
        indiceTank = int(self.traiterCollisionTankAvecObjet(node0, node1,"Item"))
        if(indiceTank != -1):
            itemID = int(self.trouverTag(node0, node1, "itemId"))
            if(itemID != -1):
                #Avertit l'item et le tank de la récupération
                itemCourrant = self.listeItem[itemID]
                itemCourrant.recupere()
                self.listTank[indiceTank].recupereItem(itemCourrant.armeId)
                return

        indiceTank = int(self.traiterCollisionTankAvecObjet(node0, node1,"LimiteJeu"))
        if(indiceTank != -1):
            #Un tank est tombé. mouhahahadddddddddd
            self.listTank[indiceTank].tombe(self.mondePhysique)
            return


    #Méthode qui va retourner -1 si aucune collision avec un tank
    #Ou encore l'index du tank touché si applicable
    def traiterCollisionTankAvecObjet(self,node0,node1,testEntite):
        tag0 = node0.getTag("EntiteTankem")
        tag1 = node1.getTag("EntiteTankem")
        retour = -1
        if(tag0 == "Tank" and tag1 == testEntite):
           retour = node0.getTag("IdTank")

        if(tag0 == testEntite and tag1 == "Tank"):
            retour = node1.getTag("IdTank")
        return retour

    #Trouve si un des 2 noeuds a le tag indiqué
    def trouverTag(self,node0, node1, tag):
        retour = ""
        #On trouve l'ID de l'item qui a collisionné
        if(node0.getTag(tag) != ""):
            retour = node0.getTag(tag)

        if(node1.getTag(tag) != ""):
            retour = node1.getTag(tag)

        return retour

    #On met à jour ce qui est nécessaire de mettre à jour
    def update(self):
        for tank in self.listTank:
            tank.traiteMouvement()