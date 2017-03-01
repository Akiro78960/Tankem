# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class DAOBalance:
	__metaclass__ = ABCMeta

	@abstractmethod
	def __init__ (self):
		pass

	def create(self):
		pass

	def read(self):
		pass

	def update(self):
		pass

	def delete(self):
		pass