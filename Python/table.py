import os
from memtable import Memtable
from ystore import Ystore
from yindex import Yindex

class Table():

	def __init__(self, tableName, load=False):
		self.tableName = tableName
		self.memtable = Memtable(tableName)
		# TODO: load schema from meta
		if load:
			self._load_meta()
		else:
			self.entries = 0
		self.schema = {}
		self.ystore = Ystore(tableName)
		self.yindex = Yindex(tableName)
		self._write_meta()

	def destroy(self):
		del self.memtable
		self.yindex.close()
		del self.yindex
		del self.schema
		# TODO remove ystore
		return True

	def putRow(self, rowKey, columns):
		memFull = self.memtable.put(rowKey, columns)
		self.entries += 1
		if memFull:
			self.spill()
		self.updateSchema(columns)
		return True


	def getRow(self, rowKey):
		memFind = self.memtable.get(rowKey)
		if memFind:
			return memFind
		data = self.yindex.get(rowKey)
		if not data:
			print("Couldn't find row with key: {}".format(rowKey))
			return None
		return self.ystore.get(data[0], data[1])

	def getRows(self, startRow, endRow):
		memFind, notFound = self.memtable.getRange(startRow, endRow)
		if not notFound:
			return memFind
		rows = memFind
		for rowKey in notFound:
			data = self.yindex.get(rowKey)
			if offset:
				rows.append(self.ystore.get(data[0], data[1]))
		return rows

	def getColumnByRow(self, rowKey, fam, quals):
		# if not fam in self.schema:
		# 	print("{} not present in schema please review schema as shown".format(fam))
		# 	self.printSchema()
		# 	return None
		row = self.getRow(rowKey)
		row = row[rowKey]
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
				self.schema[fam] = set()
				for col in columns[fam]:
					self.schema[fam].add(col)


	def open(self):
		self.memtable = Memtable(self.tableName)


	def close(self):
		del self.memtable

	def printSchema(self):
		print("Schema for {}:".format(self.tableName))
		start = '['
		for fam in self.schema:
			s = '{' + "{}:\t".format(fam)
			for col in self.schema[fam]:
				s = "{}{}, ".format(s, col)
			start += s + '}, '
		start += ']'
		print(start)

	def spill(self):
		print("Spilling to disk")
		memTableContents = self.memtable.flush()
		idx_updates = self.ystore.store(memTableContents)
		self.yindex.update(idx_updates)

	def _load_meta(self):
		with open('./meta/{}.txt'.format(self.tableName), 'r') as f:
			self.entries = int(f.readline())

	def _write_meta(self):
		if not os.path.isdir("./meta"):
			os.makedirs("./meta")
		with open('./meta/{}.txt'.format(self.tableName), 'w') as f:
			f.write(str(self.entries))
