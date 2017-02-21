# -*- coding: utf-8 -*-

class DTObject():
	def __init__(self):
		self.vitesseChar = 0
		self.vitesseRotChar = 0
		self.ptsVieChar = 0
		self.tpsMovementBlocs = 0
		self.canonVitBalle = 0
		self.canonTpsRecharge = 0
		self.mitVitBalle = 0
		self.mitTpsRecharge = 0
		self.grenVitInitballe = 0
		self.grenTpsRecharge = 0
		self.shotVitBalle = 0
		self.shotTpsRecharge = 0
		self.shotOuvFusil = 0
		self.piegeVitBalle = 0
		self.piegeTpsRecharge = 0
		self.missVitGuiBalle = 0
		self.missTpsRecharge = 0
		self.sprVitInitSaut = 0
		self.sprTpsRecharge = 0
		self.grosExplosion = 0
		self.messAccContenu = ""
		self.messAccDuree = 0
		self.messComRebDuree = 0
		self.messSigDebParContenu = ""
		self.messFinParContenu = ""

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