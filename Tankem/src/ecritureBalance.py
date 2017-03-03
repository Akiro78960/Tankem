# -*- coding:utf-8 -*-
 #programme qui prends les données du csv, les sanitize et les envoie a la base de donnée si tout est correct (+gestion messages d'erreur)

import common

DAOracle = common.internal.BalanceDAODTO.DAOBalanceOracle.DAOBalanceOracle()
DAOcsv = common.internal.BalanceDAODTO.DAOBalanceCsv.DAOBalanceCsv()

DTO = DAOcsv.read("test.csv")
DAOracle.update(DTO)
