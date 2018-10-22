import copy

class Memtable:

	def __init__(self, tableName, limit=25):
		self.limit = 25
		self.count = 0
		self.name = tableName
		self.entries = []

	def put(self, rowKey, columns):
		idx = self._check(rowKey)
		if idx == -1:
			self.entries.append({'key': rowKey, 'val': columns})
			self.count += 1
		else:
			self.entries[idx] = {'key': rowKey, 'val': columns}
		# TODO: sort
		if self.count > self.limit:
			return True
		return False

	def get(self, rowKey):
		idx = self._check(rowKey)
		if idx == -1:
			return None
		return self.entries[idx]


	def getRange(self, start, end):
		# TODO: determine range property for strings ie. Car -> Cat = Car, Cas, Cat ?
		r = [start, end] # temporary
		misses = []
		hits = []
		for rowKey in r:
			idx = self._check(rowKey)
			if idx == -1:
				misses.append(rowKey)
			else:
				hits.append(self.entries[idx])

		return hits, misses


	def setLimit(self, newLimit):
		self.limit = newLimit
		return True

	def flush(self):
		temp = copy.deepcopy(self.entries)
		self.entries = []
		self.count = 0
		return temp

	def _check(self, rowKey):
		for i, entry in enumerate(self.entries):
			if entry['key'] == rowKey:
				return i
		return -1