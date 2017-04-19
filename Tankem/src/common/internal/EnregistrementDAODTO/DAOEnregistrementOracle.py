# -*- coding: utf-8 -*-
import cx_Oracle

class DAOenregistrementOracle():

    def __init__(self):
        # Connection
        try:
            self.connection = cx_Oracle.connect('e1384492', 'C','10.57.4.60/DECINFO.edu')

        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Erreur de commande")
            print(error.code)
            print(error.message)
            print(error.context)

    def create(self, DTOpartie):
        # Creation de la partie dans la BD
        cur = self.connection.cursor()
        statement = "INSERT INTO ENREGISTREMENT_PARTIE(CREATION_DATE) VALUES(:2)"
        cur.execute(statement,(DTOpartie.getDate()))
        cur.close()
        self.connection.commit()

        # Avoir le ID de la partie cree
        curReadId = self.connection.cursor()
        curReadId = curReadId.execute("SELECT MAX(ID) FROM ENREGISTREMENT_PARTIE")
        idPartie = curReadId.fetchall()
        idPartie = idPartie[0]
        curReadId.close()

        # Insertion du joueur 1
        arrayJoueur1 = DTOpartie.getArrayJoueur1()
        for dtoJoueur in arrayJoueur1:
            curJoueur = self.connection.cursor()
            statement = "INSERT INTO ENREGISTREMENT_JOUEUR(NO_JOUEUR, ID_PARTIE, TIME_SEC, POS_X, POS_Y) VALUES(:1,:2,:3,:4,:5)"
            curJoueur.execute(statement,(1,idPartie,dtoJoueur.getTime(),dtoJoueur.getX(),dtoJoueur.getY()))
            curJoueur.close()

        # Insertion du joueur 2
        arrayJoueur2 = DTOpartie.getArrayJoueur2()
        for dtoJoueur in arrayJoueur2:
            curJoueur = self.connection.cursor()
            statement = "INSERT INTO ENREGISTREMENT_JOUEUR(NO_JOUEUR, ID_PARTIE, TIME_SEC, POS_X, POS_Y) VALUES(:1,:2,:3,:4,:5)"
            curJoueur.execute(statement,(2,idPartie,dtoJoueur.getTime(),dtoJoueur.getX(),dtoJoueur.getY()))
            curJoueur.close()

        # Insertion arme
        arrayArme = DTOpartie.getArrayArme()
        for dtoArme in arrayArme:
            curArme = self.connection.cursor()
            statement = "INSERT INTO ENREGISTREMENT_ARME(TYPE_ARME, ID_PARTIE, TIME_SEC, POS_X, POS_Y) VALUES(:1,:2,:3,:4,:5)"
            curArme.execute(statement,(dtoArme.getType(),idPartie,dtoArme.getTime(),dtoArme.getX(),dtoArme.getY()))
            curArme.close()

        # Insertion projectile
        arrayProjectile = DTOpartie.getArrayProjectile()
        for dtoProjectile in arrayProjectile:
            curProjectile = self.connection.cursor()
            statement = "INSERT INTO ENREGISTREMENT_PROJECTILE(ID_PARTIE, TIME_SEC, POS_X, POS_Y, POS_Z, EN_MOUVEMENT) VALUES(:1,:2,:3,:4,:5,:6)"
            curProjectile.execute(statement,(idPartie,dtoProjectile.getTime(),dtoProjectile.getX(),dtoProjectile.getY(),dtoProjectile.getZ(),dtoProjectile.getEnMouvement()))
            curProjectile.close()

        # Commit
        self.connection.commit()

        # ----------------------------------------------------------------------
        # Verification qu'il n'y a que 5 parties dans la BD

        # Avoir le nombre de parties
        curReadNb = self.connection.cursor()
        curReadNb = curReadNb.execute("SELECT COUNT(ID) FROM ENREGISTREMENT_PARTIE")
        nbParties = curReadNb.fetchall()
        nbParties = nbParties[0]

        if(nbParties > 5):
            # Avoir le id de la plus petite partie
            curReadId = self.connection.cursor()
            curReadId = curReadId.execute("SELECT MIN(ID) FROM ENREGISTREMENT_PARTIE")
            idPartie = curReadId.fetchall()
            idPartie = idPartie[0]
            curReadId.close()

            self.delete(idPartie)

    def delete(self, idPartie):
        # Delete Joueurs
        cur = self.connection.cursor()
        statement = 'DELETE FROM ENREGISTREMENT_JOUEUR WHERE ID_PARTIE = :ID'
        cur.execute(statement, {'ID':idPartie})
        cur.close()

        # Delete Arme
        cur = self.connection.cursor()
        statement = 'DELETE FROM ENREGISTREMENT_ARME WHERE ID_PARTIE = :ID'
        cur.execute(statement, {'ID':idPartie})
        cur.close()

        # Delete Projectile
        cur = self.connection.cursor()
        statement = 'DELETE FROM ENREGISTREMENT_PROJECTILE WHERE ID_PARTIE = :ID'
        cur.execute(statement, {'ID':idPartie})
        cur.close()

        # Delete Partie
        cur = self.connection.cursor()
        statement = 'DELETE FROM ENREGISTREMENT_PARTIE WHERE ID = :ID'
        cur.execute(statement, {'ID':idPartie})
        cur.close()

        # Commit
        self.connection.commit()
