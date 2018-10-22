from table import Table
import utils

class MyBase:

	def __init__(self, distributed_mode=False, meta_file="meta.txt", fresh_start=False):
		self.tables = {}
		self.tableSessions = {}
		self.meta_file = meta_file
		if not fresh_start:
			self._load_meta()


	def createTable(self, tableName):
		# check if table already exists
		# if self.check_membership(tableName, self.tables):
		if tableName in self.tables:
			print("{} already exists".format(tableName))
			return False
		# add to table list
		self.tables[tableName] = Table(tableName)
		# initialize a user session
		self.tableSessions[tableName] = {
			'count': 1,
			'table_obj': self.tables[tableName]
			}
		# TODO: return handle (whatever that is)
		self._update_meta()
		return True

	def destroyTable(self, tableName):
		if tableName in self.tableSessions:
			print("{} is currently in use and can't be destroyed".format(tableName))
			return False
		# if not self.check_membership(tableName, self.tables):
		if not tableName in self.tables:
			print("{} doesn't exist and can't be destroyed".format(tableName))
			return False
		deleted = self.tables[tableName].destroy()
		if deleted:
			print("{} was successfully destroyed".format(tableName))
			del self.tables[tableName]
			self._update_meta()
			return True
		else:
			print("Something went wrong with the destroy operation")
			return False

	# columns: {'familyName':{'columnName1' : value1, 'columnName2': value2}, 'fam2' ...}
	def putRow(self, tableName, rowKey, columns):
		if not tableName in self.tables:
			print("{} doesn't exist".format(tableName))
			return False
		if not tableName in self.tableSessions:
			self.tableSessions[tableName] = {
				'count': 1, 
				'table_obj': self.tables[tableName]
				}
		else:
			self.tableSessions[tableName]['count'] += 1

		success = self.tableSessions[tableName]['table_obj'].putRow(rowKey, columns)
		if success:
			print("Successfully put row {}".format(rowKey))
			return True
		else:
			print("Something went wrong with put operation")
			return False

	def getRow(self, tableName, rowKey):
		if not tableName in self.tables:
			print("{} doesn't exist".format(tableName))
			return False
		if not tableName in self.tableSessions:
			self.tableSessions[tableName] = {
				'count': 1, 
				'table_obj': self.tables[tableName]
				}
		else:
			self.tableSessions[tableName]['count'] += 1

		row = self.tableSessions[tableName]['table_obj'].getRow(rowKey)
		if not row:
			print("Unable to complete get operation")
		return row

	def getRows(self, tableName, startRow, endRow):
		if not tableName in self.tables:
			print("{} doesn't exist".format(tableName))
			return False
		if not tableName in self.tableSessions:
			self.tableSessions[tableName] = {
				'count': 1, 
				'table_obj': self.tables[tableName]
				}
		else:
			self.tableSessions[tableName]['count'] += 1

		rows = self.tableSessions[tableName]['table_obj'].getRows(startRow, endRow)
		if not rows:
			print("Unable to complete get operation")
		return rows

	def getColumnByRow(self, tableName, rowKey, family, qualifiers):
		# note that only one family but multiple qualifiers are allowed
		if not tableName in self.tables:
			print("{} doesn't exist".format(tableName))
			return False
		if not tableName in self.tableSessions:
			self.tableSessions[tableName] = {
				'count': 1, 
				'table_obj': self.tables[tableName]
				}
		else:
			self.tableSessions[tableName]['count'] += 1

		data = self.tableSessions[tableName]['table_obj'].getColumnByRow(rowKey, family, qualifiers)
		if not data:
			print("Something went wrong with getColumnByRow")
		return data

	def getSchema(self, tableName):
		if not tableName in self.tables:
			print("{} doesn't exist".format(tableName))
			return False
		self.tableSessions[tableName]['table_obj'].printSchema()

	def memTableLimit(self, tableName, newLimit):
		if not tableName in self.tables:
			print("{} doesn't exist".format(tableName))
			return False
		if not tableName in self.tableSessions:
			self.tableSessions[tableName] = {
				'count': 1, 
				'table_obj': self.tables[tableName]
				}
		else:
			self.tableSessions[tableName]['count'] += 1
		success = self.tableSessions[tableName]['table_obj'].setMemTableLimit(newLimit)
		if not success:
			print("Unable to set new memtable limit for {}".format(tableName))
			return False
		else:
			print("Set memtable limit for {} to {}".format(tableName, newLimit))
			return True

	def _load_meta(self):
		with open(self.meta_file, 'r') as f:
			name = f.readline()
			self.tables[name] = Table(name, load=True)
		print("Loaded {} tables from stored meta".format(len(self.tables)))

	def check_membership(self, name, dictionary, key='name'):
		for i in dictionary:
			if name == dictionary[i][key]:
				return True
		return False

	def _update_meta(self):
		with open(self.meta_file, 'w') as f:
			for t in self.tables:
				f.write(t)
