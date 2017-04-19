# -*- coding: utf-8 -*-
import cx_Oracle

class DAOenregistrementOracle():

	# Connection
	def __init__(self):
		try:
			self.connection = cx_Oracle.connect('e1384492', 'C','10.57.4.60/DECINFO.edu')
		except cx_Oracle.DatabaseError as e:
			error, = e.args
			print("Erreur de commande")
			print(error.code)
			print(error.message)
			print(error.context)

        def create(self, DTOpartie):
            curReadId = self.connection.cursor()
