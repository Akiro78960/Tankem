# -*- coding: utf-8 -*-
from DAO import DAO
from DTOTuile import DTOtuile
from DTOSpawn import DTOspawn
from DTOMap import DTOmap
import cx_Oracle

class DAOMapOracle(DAOBalance):

    def __init__(self):
        self.connection = cx_Oracle.connect('e1384492','C','10.57.4.60/DECINFO.edu')

    def read (self):
        table_name = table_name.upper()
        DTO
        DTOmap = DTOmap()
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

        return DTOmap
