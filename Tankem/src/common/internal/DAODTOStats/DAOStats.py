from DTOStats import DTOStats
from SingletonDBConnection import SingletonDBConnection


class DAOStats():

    def __init__(self):
		self.connection = SingletonDBConnection().getConnection()
		self.DTOStats= DTOStats()


