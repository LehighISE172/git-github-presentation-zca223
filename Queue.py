class Queue:

	def __init__(self):
		# creating list
		self.lst = []

	def pop(self):
		# removing items from given index and returing value
		return self.lst.pop(0)

	def push(self, e):
		# adding item to the list
		self.lst.append(e)

	def isEmpty(self):
		# break once list empty
		return len(self.lst) == 0