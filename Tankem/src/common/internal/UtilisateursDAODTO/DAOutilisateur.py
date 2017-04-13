#-*- coding:utf-8 -*-
from DAOorigine import DAOorigine
from DTOJoueur import DTOJoueur
import cx_Oracle

class DAOutilisateur():

	def __init__(self):
		try:
			self.connection = cx_Oracle.connect('e1384492', 'C', '10.57.4.60/DECINFO.edu')
		except cx_Oracle.DatabaseError as e:
			error, = e.args
			print("Erreur de commande : " + e)
			print(error.code)
			print(error.message)
			print(error.context)
		

	def read(self, username, password):
		try:
			curRead = self.connexion.cursor()
			curRead.execute("SELECT * from joueur WHERE username = " + username)
			for result in curRead:
				print result

		except cx_Oracle.DatabaseError as e:
			error, = e.args
			print("Erreur de commande")
			print(error.code)
			print(error.message)
			print(error.context)
