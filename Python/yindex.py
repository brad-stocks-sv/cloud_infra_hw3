import os
import sqlite3 as sql

class Yindex:
	
	def __init__(self, tableName, directory="./yindex/"):
		self.name = tableName
		self.dir = directory
		if not os.path.isdir(self.dir):
			os.makedirs(self.dir)
		self.path = "{}{}.db".format(self.dir, self.name)
		self.conn = sql.connect(self.path)
		self.c = self.conn.cursor()
		if not os.path.exists(self.path):
			self.c.execute('''CREATE TABLE yindex (key text, offset integer, size integer)''')
			self.c.commit()

	def get(self, rowKey):
		t = (rowKey,)
		self.c.execute("SELECT offset, size FROM yindex WHERE key=?", t)
		row = self.c.fetchone()
		return row

	# idxs = [{key: '', offset: 123, size: 123}]
	def update(self, idxs):
		for i in idxs:
			query_string = "INSERT OR IGNORE INTO yindex (key, offset, size) VALUES('{}', {}, {}) ".format(i['key'], i['offset'], i['size'])
			self.c.execute(query_string)
			query_string = "UPDATE yindex SET offset={}, size={} ".format(i['offset'], i['size'])
			query_string += "WHERE key='{}'".format(i['key'])
			self.c.execute(query_string)
			self.conn.commit()
			# self.conn.execute("UPDATE yindex SET offset={} size={} ".format(i['offset'], i['size']) +
  	# 			"WHERE key='{}'".format(i['key']))

	# TODO: remove all files and artifacts on destroy
	def destroy(self):
		self.conn.close()


