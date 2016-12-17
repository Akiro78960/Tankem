## -*- coding: utf-8 -*-
from util import *
from entity import *

from direct.showbase import DirectObject
from panda3d.core import *
from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletBoxShape
from panda3d.bullet import YUp
from direct.interval.IntervalGlobal import *
import random


#Module qui sert à la création des maps
class Map(DirectObject.DirectObject):
    def __init__(self, mondePhysique):
        #On garde le monde physique en référence
        self.mondePhysique = mondePhysique

        #initialisation des constantes utiles
        self.map_nb_tuile_x = 25
        self.map_nb_tuile_y = 8
        self.map_grosseur_carre = 2.0 #dimension d'un carré
        self.map_petite_valeur_carre = 0.05 #Afin de contourner des problèmes d'affichage, on va parfois décaler les carrés/animations d'une petite valeur. Par exmeple, on ne veut pas que les cubes animés passent dans le plancher.

        #On veut que le monde soit centré. On calcul donc le décalage nécessaire des tuiles
        self.position_depart_x = - self.map_grosseur_carre * self.map_nb_tuile_x / 2.0
        self.position_depart_y = - self.map_grosseur_carre * self.map_nb_tuile_y / 2.0

        #On déclare des listes pour les tanks, les items et les balles
        self.listTank = []
        self.listeItem = []
        self.listeBalle = []

        #Dictionnaire qui contient des noeuds animés.
        #On pourra attacher les objets de notre choix à animer
        self.dictNoeudAnimation = {}
        self.creerNoeudAnimationImmobile() #Pour être consistant, on créé une animation... qui ne bouge pas
        self.creerNoeudAnimationVerticale() #Animation des blocs qui bougent verticalement
        self.creerNoeudAnimationVerticaleInverse() #Idem, mais décalé

        #Initialise le contenu vide la carte
        #On y mettra les id selon ce qu'on met
        self.endroitDisponible = [[True for x in range(self.map_nb_tuile_y)] for x in range(self.map_nb_tuile_x)]

        #Message qui permettent la création d'objets pendant la partie
        self.accept("tirerCanon",self.tirerCanon)
        self.accept("tirerMitraillette",self.tirerMitraillette)
        self.accept("lancerGrenade",self.lancerGrenade)
        self.accept("lancerGuide",self.lancerGuide)
        self.accept("deposerPiege",self.deposerPiege)
        self.accept("tirerShotgun",self.tirerShotgun)

    def libererEndroitGrille(self,i,j,doitBloquer):
        #print "bloque " + str(i) + " " + str(j)
        self.endroitDisponible[i][j] = doitBloquer

    def figeObjetImmobile(self):
        self.noeudOptimisation.flattenStrong()

    def construireMapHasard(self):
        #Utilisation du module de création au hasard
        #Le module a un x et y inversé!
        maze = mazeUtil.MazeBuilder(self.map_nb_tuile_y, self.map_nb_tuile_x)
        maze.build()
        mazeArray = maze.refine(.75)

        #Interprétation du résultat de l'algo
        for row in mazeArray:
            for cell in row:
                if(cell.type == 1):
                    typeMur = random.randint(0, 5)
                    #On créé des murs!
                    #60% du temps un mur immobile
                    #20% du temps un mur mobile
                    #20% du temps un mur mobile inverse
                    if(typeMur <= 1):
                        self.creerMur(cell.row, cell.col, "AnimationMurVerticale" if typeMur == 1 else "AnimationMurVerticaleInverse")
                    else:
                        self.creerMur(cell.row, cell.col,"AnimationMurImmobile")

        self.creerChar(6,6,0,Vec3(0.1,0.1,0.1)) #Char noir
        self.creerChar(3,3,1,Vec3(0.6,0.6,0.5)) #Char gris-jaune

        #Dans la carte par défaut, des items vont appraître constamment entre 10 et 20 secondes d'interval
        self.genererItemParInterval(0.1,0.1)

    def construireDecor(self, camera):
        modele = loader.loadModel("../asset/Skybox/skybox")
        modele.set_bin("background", 0);
        modele.set_two_sided(True);
        modele.set_depth_write(False);
        modele.set_compass();
        verticalRandomAngle = random.randint(0,45)
        modele.setHpr(0,verticalRandomAngle,-90)
        randomGrayScale = random.uniform(0.6,1.2)
        semiRandomColor = Vec4(randomGrayScale,randomGrayScale,randomGrayScale,1)
        modele.setColorScale(semiRandomColor)
        modele.setPos(0,0,0.5)
        #Et oui! Le ciel est parenté à la caméra!
        modele.reparentTo(camera)

    def construirePlancher(self):
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
        node = BulletRigidBodyNode('Frontfiere sol')
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

    def placerSurGrille(self,noeud,positionX, positionY):
        # On place l'objet en calculant sa position sur la grille
        noeud.setX(self.position_depart_x + (positionX+0.5) * self.map_grosseur_carre)
        noeud.setY(self.position_depart_y + (positionY+0.5) * self.map_grosseur_carre)

    def tirerCanon(self, identifiantLanceur, position, direction):
        #Création d'une balle de physique
        someBalle = balle.Balle(identifiantLanceur,self.mondePhysique)
        self.listeBalle.append(someBalle)
        someBalle.projetter(position,direction)

    def tirerMitraillette(self, identifiantLanceur, position, direction):
        #Création d'une balle de physique
        someBalle = balle.Balle(identifiantLanceur,self.mondePhysique)
        self.listeBalle.append(someBalle)
        someBalle.projetterRapide(position,direction)

    def lancerGrenade(self, identifiantLanceur, position, direction):
        #Création d'une balle de physique
        someBalle = balle.Balle(identifiantLanceur, self.mondePhysique)
        self.listeBalle.append(someBalle)
        someBalle.lancer(position,direction)

    def lancerGuide(self, identifiantLanceur, position, direction):
        #Création d'une balle de physique
        someBalle = balle.Balle(identifiantLanceur, self.mondePhysique)
        self.listeBalle.append(someBalle)

        #On définit la position d'arrivé de missile guidé
        noeudDestination = self.listTank[0].noeudPhysique
        if(identifiantLanceur == 0):
            noeudDestination = self.listTank[1].noeudPhysique

        someBalle.lancerGuide(position,noeudDestination)

    def deposerPiege(self, identifiantLanceur, position, direction):
        #Création d'une balle de physique
        someBalle = balle.Balle(identifiantLanceur, self.mondePhysique)
        self.listeBalle.append(someBalle)
        someBalle.deposer(position,direction)

    def tirerShotgun(self, identifiantLanceur, position, direction):
        #Création d'une balle de physique
        someBalle = balle.Balle(identifiantLanceur,self.mondePhysique)
        self.listeBalle.append(someBalle)
        someBalle.projetterVariable(position,direction)

    #####################################################
    #Création des différentes entités sur la carte
    #####################################################

    def creerItem(self, positionX, positionY, armeId):
        #L'index dans le tableau d'item coincide avec son
        #itemId. Ça va éviter une recherche inutile pendant l'éxécution
        itemCourrant = item.Item(armeId,self.mondePhysique , lambda : self.libererEndroitGrille(positionX, positionY,True))
        self.listeItem.append(itemCourrant)
        #On place le tank sur la grille
        self.placerSurGrille(itemCourrant.noeudPhysique,positionX,positionY)
        self.libererEndroitGrille(positionX, positionY,False)

    def creerItemHasard(self, positionX, positionY):
        listeItem = ["Mitraillette", "Shotgun", "Piege", "Grenade", "Guide","Spring"]
        itemHasard = random.choice(listeItem)
        self.creerItem(positionX, positionY,itemHasard)

    def creerItemPositionHasard(self):
        #Pas de do while en Python! Beurk...
        randomX = random.randrange(0,self.map_nb_tuile_x)
        randomY = random.randrange(0,self.map_nb_tuile_y)

        #Tant qu'on trouve pas d'endroit disponibles...
        while(not self.endroitDisponible[randomX][randomY]):
            randomX = random.randrange(0,self.map_nb_tuile_x)
            randomY = random.randrange(0,self.map_nb_tuile_y)

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

    def creerMur(self,positionX, positionY, strAnimation = None):
        mur = Wall(self.mondePhysique)
        #On place le bloc sur la grille
        self.placerSurGrille(mur.noeudPhysique,positionX,positionY)
        self.libererEndroitGrille(positionX,positionY,False)

        if(strAnimation):
            mur.animate(self.dictNoeudAnimation[strAnimation])

    def creerNoeudAnimationImmobile(self):
        noeudAnimationCourrant = NodePath("AnimationMurImmobile")
        self.dictNoeudAnimation["AnimationMurImmobile"] = noeudAnimationCourrant
        noeudAnimationCourrant.reparentTo(render)

    def creerNoeudAnimationVerticale(self):
        #Création d'un noeud vide
        noeudAnimationCourrant = NodePath("AnimationMurVerticale")
        tempsMouvement = 0.8
        blocPosInterval1 = LerpPosInterval( noeudAnimationCourrant,
                                            tempsMouvement,
                                            Vec3(0,0,-self.map_grosseur_carre + self.map_petite_valeur_carre),
                                            startPos=Vec3(0,0,0))
        blocPosInterval2 = LerpPosInterval( noeudAnimationCourrant,
                                            tempsMouvement,
                                            Vec3(0,0,0),
                                            startPos=Vec3(0,0,-self.map_grosseur_carre + self.map_petite_valeur_carre))
        delai = Wait(1.2)
        # On créé une séquence pour bouger le bloc
        mouvementBloc = Sequence()
        mouvementBloc = Sequence(   blocPosInterval1,
                                    delai,
                                    blocPosInterval2,
                                    delai,
                                    name="mouvement-bloc")

        mouvementBloc.loop()

        noeudAnimationCourrant.reparentTo(render)
        #Ajout dans le dicitonnaire de l'animation
        self.dictNoeudAnimation["AnimationMurVerticale"] = noeudAnimationCourrant

    def creerNoeudAnimationVerticaleInverse(self):
        #Création d'un noeud vide
        noeudAnimationCourrant = NodePath("AnimationMurVerticaleInverse")
        tempsMouvement = 0.8
        blocPosInterval1 = LerpPosInterval( noeudAnimationCourrant,
                                            tempsMouvement,
                                            Vec3(0,0,-self.map_grosseur_carre + self.map_petite_valeur_carre),
                                            startPos=Vec3(0,0,0))
        blocPosInterval2 = LerpPosInterval( noeudAnimationCourrant,
                                            tempsMouvement,
                                            Vec3(0,0,0),
                                            startPos=Vec3(0,0,-self.map_grosseur_carre + self.map_petite_valeur_carre))
        delai = Wait(1.2)
        # On créé une séquence pour bouger le bloc
        mouvementBloc = Sequence()
        mouvementBloc = Sequence(   blocPosInterval2,
                                    delai,
                                    blocPosInterval1,
                                    delai,
                                    name="mouvement-bloc-inverse")
        mouvementBloc.loop()

        noeudAnimationCourrant.reparentTo(render)
        #Ajout dans le dicitonnaire de l'animation
        self.dictNoeudAnimation["AnimationMurVerticaleInverse"] = noeudAnimationCourrant


    def creerChar(self,positionX, positionY, identifiant, couleur):
        someTank = tank.Tank(identifiant,couleur,self.mondePhysique)
        #On place le tank sur la grille
        self.placerSurGrille(someTank.noeudPhysique,positionX,positionY)

        #Ajouter le char dans la liste
        self.listTank.append(someTank)

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
    def update(self,tempsTot):
        for tank in self.listTank:
            tank.traiteMouvement(tempsTot)