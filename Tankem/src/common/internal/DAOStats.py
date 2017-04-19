from DTOStats import DTOStats
from SingletonDBConnection import SingletonDBConnection


class DAOStats():

    def __init__(self):
		self.connection = SingletonDBConnection().getConnection()
		self.DTOStats = None


	def create(DTOStats):
		cur = self.connection.cursor()
		#insert les infos de la partie
		statement = "INSERT INTO partie(IdJoueur1, IdJoueur2, IdNiveau, IdGagnant) VALUES(:1, :2, :3, :4)"
		result = cur.execute(statement, (DTOStats.idJoueur1, DTOStats.idJoueur2, DTOStats.idGagnant, DTOStats.idNiveau))


		#recup l'id de la partie
		result2 = cur.execute("SELECT COUNT(Id) FROM partie")
		for i in result2:
			idPartie = i[0]

		#insert les Stats des armes
		for i in range(6):
			#StatsArmesJ1
			statement = "INSERT INTO joueur_arme_partie(IdPartie, IdJoueur, IdArme, NbFoisUtilArme) VALUES(:1, :2, :3, :4)"
			cur.execute(statement, (idPartie, DTOStats.idJoueur1, DTOStats.DTOStatsArmeJ1[i].idArme, DTOStats.DTOStatsArmeJ1[i].nbUtil))
			#StatsArmesJ2
			statement = "INSERT INTO joueur_arme_partie(IdPartie, IdJoueur, IdArme, NbFoisUtilArme) VALUES(:1, :2, :3, :4)"
			cur.execute(statement, (idPartie, DTOStats.idJoueur2, DTOStats.DTOStatsArmeJ2[i].idArme, DTOStats.DTOStatsArmeJ2[i].nbUtil))
			

