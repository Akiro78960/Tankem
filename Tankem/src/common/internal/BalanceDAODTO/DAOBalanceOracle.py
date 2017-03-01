# -*- coding: utf-8 -*-
from DAOBalance import DAOBalance
import cx_Oracle

class DAOBalanceOracle(DAOBalance):
    __metaclass__ = DAOBalance

    def __init__(self):
        self.dto = DTOBalance()
        self.connection = cx_Oracle.connect('1338283','A','10.57.4.60/DECINFO.edu')

    def read(self):
        curRead = con.cursor()

        keysList = curRead.execute("SELECT column_name FROM user_tab_columns WHERE table_name = 'table_nametankem_values'")

        curRead.close()

        for key in keysList:
            curRead = con.cursor()
            value = curRead.execute("SELECT %s FROM tankem_values" % (key))

            self.dto.appendNewDictionary(key, value)

            curRead.close()

        return self.dto

    def update(self):
        pass
