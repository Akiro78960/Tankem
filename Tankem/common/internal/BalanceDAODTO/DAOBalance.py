# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class DAOBalance(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def __init__ (self):
		pass

	def read(self):
		pass

	def update(self):
		pass