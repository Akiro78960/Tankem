from DTOStats import DTOStats
from SingletonDBConnection import SingletonDBConnection
import cx_Oracle


class DAOStats():

	def __init__(self):
		self.connection = SingletonDBConnection().getConnection()

	def create(self, DTOStats):
		cur = self.connection.cursor()
		#insert les infos de la partie
		statement = "INSERT INTO partie(IdJoueur1, IdJoueur2, IdNiveau, IdGagnant) VALUES(:1, :2, :3, :4)"
		result = cur.execute(statement, (DTOStats.idJoueur1, DTOStats.idJoueur2, DTOStats.idNiveau, DTOStats.idGagnant))
		self.connection.commit()
		print("insert into partie done!")

		#recup l'id de la partie
		result2 = cur.execute("SELECT MAX(Id) FROM partie")
		for i in result2:
			idPartie = i[0]

		try:
			#insert les Stats des armes
			for i in range(6):
				#StatsArmesJ1
				print("idPartie: "+str(idPartie)+"   idJoueur1: "+str(DTOStats.idJoueur1)+"   idArme: "+str(DTOStats.DTOStatsArmeJ1[i].idArme)+"   nbUtil: "+str(DTOStats.DTOStatsArmeJ1[i].nbUtil))
				statement = "INSERT INTO joueur_arme_partie(IdPartie, IdJoueur, IdArme, NbFoisUtilArme) VALUES(:1, :2, :3, :4)"
				cur.execute(statement, (idPartie, DTOStats.idJoueur1, DTOStats.DTOStatsArmeJ1[i].idArme, DTOStats.DTOStatsArmeJ1[i].nbUtil))
				#StatsArmesJ2
				statement = "INSERT INTO joueur_arme_partie(IdPartie, IdJoueur, IdArme, NbFoisUtilArme) VALUES(:1, :2, :3, :4)"
				cur.execute(statement, (idPartie, DTOStats.idJoueur2, DTOStats.DTOStatsArmeJ2[i].idArme, DTOStats.DTOStatsArmeJ2[i].nbUtil))
			self.connection.commit()
		except cx_Oracle.DatabaseError as e:
			error, = e.args
			print("Erreur d'insert")
			print(error.code)
			print(error.message)
			print(error.context)
			

