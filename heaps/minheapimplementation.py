class MinHeap:
	def __init__(self):
		self.heap =[]
	def insert(self,val):
		self.heap.append(val)
		self.__percolateUp(len(self.heap)-1)

	def getMin(self):
		


		