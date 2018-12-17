class picture_n(object):
	"""docstring for ClassName"""
	def __init__(self, n):
		self.n = n
	def num(self):
		page_list = []
		for i in range(self.n):
			if i < 10:
				page_list.append('0' + str(i))
			elif 10<= i <100:
				page_list.append('00' + str(i))
			elif i >= 100:
				page_list.append('000' + str(i))
			else:
				pass
		return page_list
	#只在数字前面加三个零就可以
	def num2(self):
		page_list = []
		for i in range(self.n):
			page_list.append('000' + str(i))
		return page_list


a = picture_n(10)
print(a.num2())