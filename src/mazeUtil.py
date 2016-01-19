import random

class MazeBuilder:    

	def __init__(self, colCount, rowCount):
		self.colCount = colCount
		self.rowCount = rowCount	

	def build(self):
		if (self.colCount >= 4 and self.rowCount >= 4):
			self.cells = []
			
			# ================================================
			# Initialization
			for line in range(0,self.rowCount):
				self.cells.append([])
				for row in range(0,self.colCount):
					self.cells[line].append(Cell(line, row))

			# ================================================
			# Carving into walls
			initRow = (int)(random.random() * len(self.cells))
			initCol = (int)(random.random() * len(self.cells[0]))
			cell = self.cells[initRow][initCol]
			cell.type = 0
			mustContinue = True

			while (mustContinue):
				while (not cell.hasVisitedAllDir()):
					direction = cell.getDirection()

					if direction == 0 and cell.row - 1 >= 0:
						targetCell = self.cells[cell.row - 1][cell.col]
						cell = self.carve(direction, cell, targetCell)
					elif direction == 1 and cell.col + 1 < self.colCount:
						targetCell = self.cells[cell.row][cell.col + 1]
						cell = self.carve(direction, cell, targetCell)
						
					elif direction == 2 and cell.row + 1 < self.rowCount:
						targetCell = self.cells[cell.row + 1][cell.col]
						cell = self.carve(direction, cell, targetCell)
					elif direction == 3 and cell.col - 1 >= 0:
						targetCell = self.cells[cell.row][cell.col - 1]
						cell = self.carve(direction, cell, targetCell)

				if (cell.parent == None):
					mustContinue = False
				else:
					cell = cell.parent

		else:
			self.cells = []
		

		return self.cells

	def carve(self, direction, cell, targetCell):
		if (not targetCell.wasVisited() and cell.parent != targetCell):
			if (direction == 0 or direction == 2):
				if (cell.col - 1 >= 0 and not self.cells[cell.row][cell.col - 1].wasVisited()):
					self.cells[cell.row][cell.col - 1].forceWall()

				if (cell.col + 1 < self.colCount and not self.cells[cell.row][cell.col + 1].wasVisited()):
					self.cells[cell.row][cell.col + 1].forceWall()
			if (direction == 1 or direction == 3):
				if (cell.row - 1 >= 0 and not self.cells[cell.row - 1][cell.col].wasVisited()):
					self.cells[cell.row - 1][cell.col].forceWall()

				if (cell.row + 1 < self.rowCount and not self.cells[cell.row + 1][cell.col].wasVisited()):
					self.cells[cell.row + 1][cell.col].forceWall()

			targetCell.type = 0
			targetCell.parent = cell
			cell = targetCell

		return cell

	def toString(self, currentCell = None):
		for row in self.cells:
			for col in row:
				if (currentCell is None or currentCell != col):
					print(col.type, )
				else:
					print("*", )
				print(" ", )
			print("")

		print("")


class Cell:
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.toVisit = [0, 1, 2, 3] # up, right, bottom, left
		self.type = 1
		self.parent = None

	def wasVisited(self):
		return len(self.toVisit) != 4

	def forceWall(self):
		self.toVisit[:] = []

	def getDirection(self):
		idx = (int)(random.random() * len(self.toVisit))
		dir = self.toVisit[idx]
		del self.toVisit[idx]
		return dir

	def hasVisitedAllDir(self):
		return len(self.toVisit) == 0
