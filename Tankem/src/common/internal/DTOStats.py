from DTOStatsArme import DTOStatsArme

class DTOStats():
    def __init__(self, idPartie, idJoueur1, idJoueur2, idGagnant, idNiveau):
        self.idPartie = idPartie
        self.idJoueur1 = idJoueur1
        self.idJoueur2 = idJoueur2
        self.idGagnant = idGagnant
        self.idNiveau = idNiveau
        self.DTOStatsArmeJ1 = []
        self.DTOStatsArmeJ2 = []

    def addDTOStatsArme(self, DTOStatsArme1, DTOStatsArme2):
        self­.DTOStatsArmeJ1.append(DTOStatsArme1)
        self.DTOStatsArmeJ2.append(DTOStatsArme2)