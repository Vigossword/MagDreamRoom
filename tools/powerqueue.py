# 这个对象很强大（我预想是这样的）
# 1. 它可以按先进先出的方式存取数据
# 2. 它保证数据被从内存中删除之前， 已经正确存入数据库了
# 3. 它会缓存最近的 m 个数据， 用来查询使用
############################################


class PowerQueue:

	def __init__(self,m=100):
		pass

	def push(self,data):
		pass

	def pop(self,data):
		pass

	#查找数据在缓存中的位置
	def findInCache(self,data):
		pass


