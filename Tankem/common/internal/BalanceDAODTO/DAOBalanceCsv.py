# -*- coding: utf-8 -*-
from DAOBalance import DAOBalance
import csv

class DAOBalanceCsv(DAOBalance):
	def read(self,csvfile):
		with open(csvfile,"wb") as csvfile :
        csvwriter = csv.writer(csvfile,delimiter=";")
		for row in readerCSV:
        	for cell in row:
          		print cell.decode("windows-1252")
