# -*- coding: utf-8 -*-

class DTObject():
	def __init__(self):
		#variable par defaut
		self.vitesseChar = 7.0
		self.vitesseRotChar = 1500.0
		self.ptsVieChar = 200.0
		self.tpsMovementBlocs = 0.8
		self.canonVitBalle = 14.0
		self.canonTpsRecharge = 1.2
		self.mitVitBalle = 18.0
		self.mitTpsRecharge = 0.4
		self.grenVitInitballe = 16.0
		self.grenTpsRecharge = 0.8
		self.shotVitBalle = 13.0
		self.shotTpsRecharge = 1.8
		self.shotOuvFusil = 0.4
		self.piegeVitBalle = 1.0
		self.piegeTpsRecharge = 0.8
		self.missVitGuiBalle = 30.0
		self.missTpsRecharge = 3.0
		self.sprVitInitSaut = 10.0
		self.sprTpsRecharge = 0.5
		self.grosExplosion = 9.0
		self.messAccContenu = "Yolo"
		self.messAccDuree = 3.0
		self.messComRebDuree = 3.0
		self.messSigDebParContenu = "Sw4g"
		self.messFinParContenu = "K1ll M3"

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
		if(self.isNotInRange(self.vitesseChar, 4.0, 12.0)):
			print "La vitesse des chars ne respecte pas le min/max"

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