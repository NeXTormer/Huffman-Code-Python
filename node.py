class Node:
	def __init__(self, id, key, value):
		global idcounter
		self.left = None
		self.right = None
		self.id = id
		self.value = value
		self.key = key
		self.parent = None