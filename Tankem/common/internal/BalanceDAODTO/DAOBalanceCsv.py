# -*- coding: utf-8 -*-
from DAOBalance import DAOBalance
import csv

class DAOBalanceCsv(DAOBalance):
	def read(self,csvfile):
		DTO = DAOBalance()
		with open(csvfile) as csvfile :
			reader = csv.DictReader(csvfile,delimiter=";")
			for row in reader:
				print(row['Name'], row['Value'])
					#DTO.appendNewDictionnary(row['Name'],row['Name'],row['Value'],0,0)