# -*- coding:utf-8 -*-
class DTOJoueur:
	def __init__(self, idJoueur, username, name, surname, couleurTank,
				 password, email, niveau, experience, vie, force, agilite,
				 dexterite, partieJoue, partieGagne):
		self.idJoueur = idJoueur
		self.username = username
		self.name = name
		self.surname = surname
		self.couleurTank = couleurTank
		self.password = password
		self.email = email
		self.niveau = niveau
		self.experience = experience
		self.vie = vie
		self.force = force
		self.agilite = agilite
		self.dexterite = dexterite
		self.partieJoue = partieJoue
		self.partiegagne = partiGegne

	def getId(self):
		return self.idJoueur

	def getUsername(self):
		return self.username