from MyBase import MyBase

def main():
	base = MyBase(fresh_start=False)
	# base.createTable("First Table")
	base.memTableLimit("First Table", 1)
	# base.putRow("First Table", 'bstocks', {'name':{'first': 'Brad', 'last': 'stocks'}})	
	# base.putRow("First Table", 'alynn', {'name':{'first': 'stacey', 'last': 'lynn'}})	
	print(base.getRow("First Table", 'alynn'))
	print(base.getColumnByRow("First Table", 'alynn', 'name', ['last']))


if __name__ == '__main__':
	main()