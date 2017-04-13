from DTOStats import DTOStats


class DAOStats():

    def __init__(self):
		try:
			self.connection = cx_Oracle.connect('e1384492', 'C',
											'10.57.4.60/DECINFO.edu')
		except cx_Oracle.DatabaseError as e:
			error, = e.args
			print("Erreur de commande")
			print(error.code)
			print(error.message)
			print(error.context)

		self.DTOStats= DTOStats()


