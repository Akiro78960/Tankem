# -*- coding: utf-8 -*-
from DAOBalance import DAOBalance
from DTOBalance import DTObalance
import cx_Oracle

class DAOBalanceOracle(DAOBalance):

    def __init__(self):
        self.dto = DTObalance()
        self.connection = cx_Oracle.connect('e1384492','C','10.57.4.60/DECINFO.edu')

    def read(self):
        curRead = self.connection.cursor()

        curRead = curRead.execute("SELECT column_name FROM user_tab_columns WHERE table_name = 'TANKEM_VALUES'")
        keysList = curRead.fetchall()

        curRead.close()

        for key in keysList:
            curRead = self.connection.cursor()
            curRead.execute("SELECT %s FROM tankem_values" % (key[0]))
            value = curRead.fetchall()

            self.dto.appendNewValue(key[0], value[0][0])

            curRead.close()

        return self.dto

    def update(self):
        pass
