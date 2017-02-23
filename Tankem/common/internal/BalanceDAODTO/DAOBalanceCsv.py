# -*- coding: utf-8 -*-
import DAOBalance

class DAOBalanceCsv():
	__metaclass__ = DAOBalance

	@abstractmethod
	def read(self):
		print "Yoyo"
