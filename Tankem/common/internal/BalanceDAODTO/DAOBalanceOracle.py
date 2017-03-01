# -*- coding: utf-8 -*-
import DAOBalance
import cx_Oracle

class DAOBalanceOrdre():
    __metaclass__ = DAOBalance

    def __init__(self):
        self.dto = DTOBalance()
        self.connection = cx_Oracle.connect('1338283','A','10.57.4.60/DECINFO.edu')

    def read(self):
        curRead = con.cursor()
        listeDB = curRead.execute("SELECT * FROM tankem_values")
        curRead.close()

        for value in listeDB:
            self.dto.appendNewDictionary()

    def update(self):

