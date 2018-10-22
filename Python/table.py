from memtable import Memtable
from ystore import Ystore
from yindex import Yindex

class Table():

	def __init__(self, tableName):
		self.tableName = tableName
		self.memtable = Memtable(tableName)
		self.ystore = Ystore(tableName)
		self.yindex = Yindex(tableName)
		self.schema = {}
		self.entries = 0

	def destroy(self):
		del self.memtable
		del self.yindex
		del self.schema
		# TODO remove ystore
		return True

	def putRow(self, rowKey, columns):
		memFull = self.memtable.put(rowKey)
		self.entries += 1
		if memFull:
			self.spill()
		self.updateSchema(columns)
		return True


	def getRow(self, rowKey):
		memFind = self.memtable.get(rowKey)
		if memFind:
			return memFind
		offset = self.yindex.get(rowKey)
		if not offset:
			print("Couldn't find row with key: {}".format(rowKey))
			return None
		return self.ystore.get(offset)

	def getRows(self, startRow, endRow):
		memFind, notFound = self.memtable.getRange(startRow, endRow)
		if not notFound:
			return memFind
		rows = memFind
		for rowKey in notFound:
			offset = self.yindex.get(rowKey)
			if offset:
				rows.append(self.ystore.get(offset))
		return rows

	def getColumnByRow(self, rowKey, fam, quals):
		if not fam in self.schema:
			print("{} not present in schema please review schema as shown".format(fam))
			self.printSchema()
			return None
		row = self.getRow(rowKey)
		data = {fam:{}}
		for q in quals:
			if not q in row[fam]:
				print("{} not present in schema please review schema as shown".format(q))
				self.printSchema()
				return None
			data[fam][q] = row[fam][q]
		return data


	def setMemTableLimit(self, newLimit):
		return self.memtable.setLimit(newLimit)


	def updateSchema(self, columns):
		for fam in columns:
			if fam in self.schema:
				for col in columns[fam]:
					if not col in self.schema[fam]:
						self.schema[fam].add(col)
			else:
				self.schema[fam] = {}
				for col in columns[fam]:
					self.schema[fam].add(col)


	def open(self):
		self.memtable = Memtable(self.tableName)


	def close(self):
		del self.memtable

	def printSchema(self):
		for fam in self.schema:
			s = "{}:\t".format(fam)
			for col in self.schema[fam]:
				s = "{}{}, ".format(s, col)
			print(s)

	def spill(self):
		memTableContents = self.memtable.flush()
		idx_updates = self.Ystore.store(memTableContents)
		self.yindex.update(idx_updates)