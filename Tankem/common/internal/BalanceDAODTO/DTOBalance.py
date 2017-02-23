# -*- coding: utf-8 -*-

class DTObject():
	def __init__(self):
		#variable par defaut
		self.vitesseChar
		self.vitesseCharMin
		self.vitesseCharMax
		self.vitesseRotChar
		self.vitesseRotCharMin
		self.vitesseRotCharMax
		self.ptsVieChar
		self.ptsVieCharMin
		self.ptsVieCharMax
		self.tpsMovementBlocs
		self.tpsMovementBlocsMin
		self.tpsMovementBlocsMax
		self.canonVitBalle
		self.canonVitBalleMin
		self.canonVitBalleMax
		self.canonTpsRecharge
		self.canonTpsRechargeMin
		self.canonTpsRechargeMax
		self.mitVitBalle
		self.mitVitBalleMin
		self.mitVitBalleMax
		self.mitTpsRecharge
		self.mitTpsRechargeMin
		self.mitTpsRechargeMax
		self.grenVitInitballe
		self.grenVitInitballeMin
		self.grenVitInitballeMax
		self.grenTpsRecharge
		self.grenTpsRechargeMin
		self.grenTpsRechargeMax
		self.shotVitBalle
		self.shotVitBalleMin
		self.shotVitBalleMax
		self.shotTpsRecharge
		self.shotTpsRechargeMin
		self.shotTpsRechargeMax
		self.shotOuvFusil
		self.shotOuvFusilMin
		self.shotOuvFusilMax
		self.piegeVitBalle
		self.piegeVitBalleMin
		self.piegeVitBalleMax
		self.piegeTpsRecharge
		self.piegeTpsRechargeMin
		self.piegeTpsRechargeMax
		self.missVitGuiBalle
		self.missVitGuiBalleMin
		self.missVitGuiBalleMax
		self.missTpsRecharge
		self.missTpsRechargeMin
		self.missTpsRechargeMax
		self.sprVitInitSaut
		self.sprVitInitSautMin
		self.sprVitInitSautMax
		self.sprTpsRecharge
		self.sprTpsRechargeMin
		self.sprTpsRechargeMax
		self.grosExplosion
		self.grosExplosionMin
		self.grosExplosionMax
		self.messAccContenu
		self.messAccContenuMin
		self.messAccContenuMax
		self.messAccDuree
		self.messAccDureeMin
		self.messAccDureeMax
		self.messComRebDuree
		self.messComRebDureeMin
		self.messComRebDureeMax
		self.messSigDebParContenu
		self.messSigDebParContenuMin
		self.messSigDebParContenuMax
		self.messFinParContenu
		self.messFinParContenuMin
		self.messFinParContenuMax

	# Retourne true si la valeur ne respecte pas son min/max
	def isBelowMin(self, value, min):
		result = true 

		if(min <= value):
				result = false

		return result

	def isAboveMax(self, value, max):
		result = true 

		if(value <= max):
				result = false

		return result

	# Retourne true is toutes les valeurs respectent leur min/max
	def isBalanced(self):

            # self.vitesseChar 
            if(isBelowMin(self.vitesseChar ,self.vitesseCharMin):
                print "self.vitesseChar est en dessous du minimum"
            else if(isAboveMax(self.vitesseChar ,self.vitesseCharMax):
                print "self.vitesseChar est au dessus du maximum"

            # self.vitesseRotChar
            if(isBelowMin(self.vitesseRotChar,self.vitesseRotCharMin)):
                print "self.vitesseRotChar est en dessous du minimum"
            else if(isAboveMax(self.vitesseRotChar,self.vitesseRotCharMax)):
                print "self.vitesseRotChar est au dessus du maximum"



            # self.ptsVieChar
            if(isBelowMin(self.ptsVieChar,self.ptsVieCharMin)):
                print "self.ptsVieChar est en dessous du minimum"
            else if(isAboveMax(self.ptsVieChar,self.ptsVieCharMax)):
                print "self.ptsVieChar est au dessus du maximum"

            # self.tpsMovementBlocs
            if(isBelowMin(self.tpsMovementBlocs,self.tpsMovementBlocsMin)):
                print "self.tpsMovementBlocs est en dessous du minimum"
            else if(isAboveMax(self.tpsMovementBlocs,self.tpsMovementBlocsMax)):
                print "self.tpsMovementBlocs est au dessus du maximum"

            # self.canonVitBalle
            if(isBelowMin(canonVitBalle,canonVitBalleMin)):
                print "canonVitBalle est en dessous du minimum"
            else if(isAboveMax(canonVitBalle,canonVitBalleMax)):
                print "canonVitBalle est au dessus du maximum"

            # self.canonTpsRecharge
            if(isBelowMin(canonTpsRecharge,canonTpsRechargeMin)):
                print "canonTpsRecharge est en dessous du minimum"
            else if(isAboveMax(canonTpsRecharge,canonTpsRechargeMax)):
                print "canonTpsRecharge est au dessus du maximum"

            # self.mitVitBalle
            if(isBelowMin(self.mitVitBalle,self.mitVitBalleMin)):
                print "self.mitVitBalle est en dessous du minimum"
            else if(isAboveMax(self.mitVitBalle,self.mitVitBalleMax)):
                print "self.mitVitBalle est au dessus du maximum"

            # self.mitTpsRecharge
            if(isBelowMin(self.mitTpsRecharge,self.mitTpsRechargeMin)):
                print "self.mitTpsRecharge est en dessous du minimum"
            else if(isAboveMax(self.mitTpsRecharge,self.mitTpsRechargeMax)):
                print "self.mitTpsRecharge est au dessus du maximum"

            # self.grenVitInitballe
            if(isBelowMin(self.grenVitInitballe,self.grenVitInitballeMin)):
                print "self.grenVitInitballe est en dessous du minimum"
            else if(isAboveMax(self.grenVitInitballe,self.grenVitInitballeMax)):
                print "self.grenVitInitballe est au dessus du maximum"

            # self.grenTpsRecharge
            if(isBelowMin(self.grenTpsRecharge,self.grenTpsRechargeMin)):
                print "self.grenTpsRecharge est en dessous du minimum"
            else if(isAboveMax(self.grenTpsRecharge,self.grenTpsRechargeMax)):
                print "self.grenTpsRecharge est au dessus du maximum"

            # self.shotVitBalle
            if(isBelowMin(self.shotVitBalle,self.shotVitBalleMin)):
                print "self.shotVitBalle est en dessous du minimum"
            else if(isAboveMax(self.shotVitBalle,self.shotVitBalleMax)):
                print "self.shotVitBalle est au dessus du maximum"

            # self.shotTpsRecharge
            if(isBelowMin(self.shotTpsRecharge,self.shotTpsRechargeMin)):
                print "self.shotTpsRecharge est en dessous du minimum"
            else if(isAboveMax(self.shotTpsRecharge,self.shotTpsRechargeMax)):
                print "self.shotTpsRecharge est au dessus du maximum"

            # self.shotOuvFusil
            if(isBelowMin(self.shotOuvFusil,self.shotOuvFusilMin)):
                print "self.shotOuvFusil est en dessous du minimum"
            else if(isAboveMax(self.shotOuvFusil,self.shotOuvFusilMax)):
                print "self.shotOuvFusil est au dessus du maximum"

            # self.piegeVitBalle
            if(isBelowMin(self.piegeVitBalle,self.piegeVitBalleMin)):
                print "self.piegeVitBalle est en dessous du minimum"
            else if(isAboveMax(self.piegeVitBalle,self.piegeVitBalleMax)):
                print "self.piegeVitBalle est au dessus du maximum"

            # self.piegeTpsRecharge
            if(isBelowMin(self.piegeTpsRecharge,self.piegeTpsRechargeMin)):
                print "self.piegeTpsRecharge est en dessous du minimum"
            else if(isAboveMax(self.piegeTpsRecharge,self.piegeTpsRechargeMax)):
                print "self.piegeTpsRecharge est au dessus du maximum"

            # self.missVitGuiBalle
            if(isBelowMin(self.missVitGuiBalle,self.missVitGuiBalleMin)):
                print "self.missVitGuiBalle est en dessous du minimum"
            else if(isAboveMax(self.missVitGuiBalle,self.missVitGuiBalleMax)):
                print "self.missVitGuiBalle est au dessus du maximum"

            # self.missTpsRecharge
            if(isBelowMin(self.missTpsRecharge,self.missTpsRechargeMin)):
                print "self.missTpsRecharge est en dessous du minimum"
            else if(isAboveMax(self.missTpsRecharge,self.missTpsRechargeMax)):
                print "self.missTpsRecharge est au dessus du maximum"

            # self.sprVitInitSaut
            if(isBelowMin(self.sprVitInitSaut,self.sprVitInitSautMin)):
                print "self.sprVitInitSaut est en dessous du minimum"
            else if(isAboveMax(self.sprVitInitSaut,self.sprVitInitSautMax)):
                print "self.sprVitInitSaut est au dessus du maximum"

            # self.sprTpsRecharge
            if(isBelowMin(self.sprTpsRecharge,self.sprTpsRechargeMin)):
                print "self.sprTpsRecharge est en dessous du minimum"
            else if(isAboveMax(self.sprTpsRecharge,self.sprTpsRechargeMax)):
                print "self.sprTpsRecharge est au dessus du maximum"

            # self.grosExplosion
            if(isBelowMin(self.grosExplosion,self.grosExplosionMin)):
                print "self.grosExplosion est en dessous du minimum"
            else if(isAboveMax(self.grosExplosion,self.grosExplosionMax)):
                print "self.grosExplosion est au dessus du maximum"

            # self.messAccContenu
            if(isBelowMin(self.messAccContenu,self.messAccContenuMin)):
                print "self.messAccContenu est en dessous du minimum"
            else if(isAboveMax(self.messAccContenu,self.messAccContenuMax)):
                print "self.messAccContenu est au dessus du maximum"

            # self.messAccDuree
            if(isBelowMin(self.messAccDuree,self.messAccDureeMin)):
                print "self.messAccDuree est en dessous du minimum"
            else if(isAboveMax(self.messAccDuree,self.messAccDureeMax)):
                print "self.messAccDuree est au dessus du maximum"

            # self.messComRebDuree
            if(isBelowMin(self.messComRebDuree,self.messComRebDureeMin)):
                print "self.messComRebDuree est en dessous du minimum"
            else if(isAboveMax(self.messComRebDuree,self.messComRebDureeMax)):
                print "self.messComRebDuree est au dessus du maximum"

            # self.messSigDebParContenu
            if(isBelowMin(self.messSigDebParContenu,self.messSigDebParContenuMin)):
                print "self.messSigDebParContenu est en dessous du minimum"
            else if(isAboveMax(self.messSigDebParContenu,self.messSigDebParContenuMax)):
                print "self.messSigDebParContenu est au dessus du maximum"

            # self.messFinParContenu
            if(isBelowMin(self.messFinParContenu,self.messFinParContenuMin)):
                print "self.messFinParContenu est en dessous du minimum"
            else if(isAboveMax(self.messFinParContenu,self.messFinParContenuMax)):
                print "self.messFinParContenu est au dessus du maximum"

# PARTI DE CODE POUR SE CONNECTER À LA DATABSE, DÉSOLÉ

# import cx_Oracle

# def insererInfoBD():
# 	print "Début de l'insertion des données"
# 	connection()

# def executer(curseur, commande):
# 	try:
# 		curseur.execute(commande)
# 	except cx_Oracle.DatabaseError as e:
# 		error, = e.args
# 		print("Erreur d'insertion!")
# 		print(error.code)
# 		print(error.message)
# 		print(error.context)
# 	cur.close()

# def connection():
# 	con = cx_Oracle.connect('e1384492','C','10.57.4.60/DECINFO.edu')
# 	print "Connection à Oracle"
# 	con.close()
