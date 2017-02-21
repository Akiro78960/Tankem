# -*- coding: utf-8 -*-
import cx_Oracle

def insererInfoBD():
	print "Début de l'insertion des données"
	connection()

def executer(curseur, commande):
	try:
		curseur.execute(commande)
	except cx_Oracle.DatabaseError as e:
		error, = e.args
		print("Erreur d'insertion!")
		print(error.code)
		print(error.message)
		print(error.context)
	cur.close()

def connection():
	con = cx_Oracle.connect('e1384492','C','10.57.4.60/DECINFO.edu')
	print "Connection à Oracle"
	con.close()