# -*- coding: utf-8 -*-
from DAO import DAO
from DTOTuile import DTOtuile
from DTOSpawn import DTOspawn
from DTOMap import DTOmap
from DTOListmap import DTOlistmap
import cx_Oracle


class DAOmaporacle():

    # Connection
    def __init__(self):
        self.connection = cx_Oracle.connect('e1384492', 'C',
                                            '10.57.4.60/DECINFO.edu')

        self.DTOlistmap = DTOlistmap()

    def read(self):
        # Get array maps
        curRead = self.connection.cursor()
        curRead = curRead.execute("SELECT * FROM %s " % ("EDITOR_NIVEAU"))
        arrayMapTmp = curRead.fetchall()
        curRead.close()

        nbMaps = arrayMapTmp.length()

        # Append each map to DTOlistmap
        for i in range(0, nbMaps):
            DTOmapTmp = DTOmap()

            # Get tuiles of map
            curRead = self.connection.cursor()
            curRead.execute("SELECT * FROM EDITOR_TUILE WHERE id_niveau='%s'"
                            % (i))

            arrayTuilesTmp = curRead.fetchall()
            curRead.close()

            # Get tuiles of map
            curRead = self.connection.cursor()
            curRead.execute("SELECT * FROM EDITOR_SPAWN WHERE id_niveau='%s'"
                            % (i))

            arraySpawnTmp = curRead.fetchall()
            curRead.close()

        return self.DTOlistmap
