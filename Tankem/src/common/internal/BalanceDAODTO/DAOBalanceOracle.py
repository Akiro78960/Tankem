# -*- coding: utf-8 -*-
from DAOBalance import DAOBalance
from DTOBalance import DTObalance
import cx_Oracle

class DAOBalanceOracle(DAOBalance):

    def __init__(self):
        try:
            self.connection = cx_Oracle.connect('e1384492','C','10.57.4.60/DECINFO.edu')
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Erreur de commande")
            print(error.code)
            print(error.message)
            print(error.context)

    def read(self, table_name):
        table_name = table_name.upper()
        tmpDTO = DTObalance()
        try:
            curRead = self.connection.cursor()

            curRead = curRead.execute("SELECT column_name FROM user_tab_columns WHERE table_name = '%s'" % (table_name))
            keysList = curRead.fetchall()

            curRead.close()

            for key in keysList:
                curRead = self.connection.cursor()
                curRead.execute("SELECT %s FROM %s" % (key[0],table_name))
                value = curRead.fetchall()

                tmpDTO.setValue(key[0], value[0][0])

                curRead.close()

            tmpDTO.setValue("TABLE_NAME", table_name)
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Erreur de commande")
            print(error.code)
            print(error.message)
            print(error.context)

        return tmpDTO

    def update(self, DTO):
        try:
            tmpDict = DTO.getDictionary()
            tmpID = DTO.getValue("ID")
            table_name = DTO.getValue("TABLE_NAME")

            for key,value in tmpDict.items():
                if(key != "ID" and key != "TABLE_NAME"):
                    curRead = self.connection.cursor()
                    curRead.execute("UPDATE %s SET %s = %s WHERE id = %s" % (table_name,key,value,tmpID))
                    curRead.close()
            self.connection.commit()
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Erreur de commande")
            print(error.code)
            print(error.message)
            print(error.context)


