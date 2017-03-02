# -*- coding: utf-8 -*-
from DAOBalance import DAOBalance
from DTOBalance import DTObalance
import cx_Oracle

class DAOBalanceOracle(DAOBalance):

    def __init__(self):
        self.connection = cx_Oracle.connect('e1384492','C','10.57.4.60/DECINFO.edu')

    def read(self, table_name):
        table_name = table_name.upper()
        tmpDTO = DTObalance()
        curRead = self.connection.cursor()

        curRead = curRead.execute("SELECT column_name FROM user_tab_columns WHERE table_name = '%s'" % (table_name))
        keysList = curRead.fetchall()

        curRead.close()

        for key in keysList:
            curRead = self.connection.cursor()
            curRead.execute("SELECT %s FROM tankem_values" % (key[0]))
            value = curRead.fetchall()

            tmpDTO.setValue(key[0], value[0][0])

            curRead.close()

        return tmpDTO

    def update(self, DTO):
        tmpDict = DTO.getDictionary()
        tmpID = DTO.getValue("ID")

        for key,value in tmpDict.items():
            if(key != "ID"):
                curRead = self.connection.cursor()
                curRead.execute("UPDATE tankem_values SET %s = %s WHERE id = %s" % (key,value,tmpID))
                curRead.close()
        self.connection.commit()

