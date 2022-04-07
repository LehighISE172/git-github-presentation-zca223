class Stack:
	
	def __init__(self):
		# creating list
		self.lst = []
		
	def pop(self):
		# removing value from given list, but then also return value of altered length
		return self.lst.pop(len(self.lst)-1)

	def push(self, e):
		# adding item to the list
		self.lst.append(e)
		
	def isEmpty(self):
		# break once list empty
		return len(self.lst) == 0