from MyBase import MyBase

def main():
	base = MyBase(fresh_start=False)
	# base.createTable("Second Table")
	base.openTable("Second Table")
	base.memTableLimit("Second Table", 1)
	base.putRow("Second Table", 'bstocks', {'name':{'first': 'Brad', 'last': 'stocks'}})	
	base.putRow("Second Table", 'dzhang', {'name':{'first': 'dave', 'last': 'zhang'}})	
	base.putRow("Second Table", 'alynn', {'name':{'first': 'stacey', 'last': 'lynn'}})	
	print(base.getRows("Second Table", 'a', 'c'))
	# print(base.getColumnByRow("First Table", 'alynn', 'name', ['last']))
	base.closeTable("Second Table")


if __name__ == '__main__':
	main()