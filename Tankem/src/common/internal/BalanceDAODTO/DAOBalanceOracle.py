# -*- coding: utf-8 -*-
from DAOBalance import DAOBalance
import cx_Oracle

class DAOBalanceOracle(DAOBalance):

    def __init__(self):
        self.connection = cx_Oracle.connect('1338283','A','10.57.4.60/DECINFO.edu')

    def read(self):
        DTO = DTObalance()
        curRead = self.connection.cursor()

        keysList = curRead.execute("SELECT column_name FROM user_tab_columns WHERE table_name = 'table_nametankem_values'")

        curRead.close()

        for key in keysList:
            curRead = self.connection.cursor()
            value = curRead.execute("SELECT %s FROM tankem_values" % (key))

            DTO.appendNewDictionary(key, value)

            curRead.close()

        return DTO

    def update(DTO):
        tmpDict = DTO

        curRead = self.connection.cursor()
        for key,value in tmpDict.items():
            curRead.execure("UPDATE tankem_values SET %s = %s" % (key,value))

        curRead.close()
