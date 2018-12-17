import requests 
import os

h_num = eval(input("请输入下载的话数，只能输入一个：")) 
    
try:
	os.mkdir('.\\mh\\'+ h_num)
except:
	print('目录已存在，正在写入。。。')
# 先让我想想 怎么获取URL
url = 'https://mh1.ahjsny.com/upload/envhuanghou/34/' 
page_num = eval(input("请输入页码:"))
# 用来 对请求的图片地址-->https://mh1.ahjsny.com/upload/envhuanghou/34/xxxxx.jpg
# xxxx格式不一样 处理那个xxxxx的 定位图片的URL
class picture_n(object):
	def __init__(self, n):
		self.n = n
	def num(self):
		page_list = []
	# 几位数前面加几个零
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
	# 要有其他类型，老子再写


# 用来下载图片的函数
def download(url,num):
	response = requests.get(url)
	try:
		with open('.\\mh\\' + h_num + num + '.jpg', 'wb') as f:
			f.write(response.content)
			f.close()
	except:
		print('未知错误')


# 先用函数写一个生成 图片链接的文档 
def main():
	global page_num
	sl_n = a = picture_n(page_num)
	for i in sl_n.num2(page_num):
		# 为了让文件名好看
		n_2 = '{:04}'.format(n)
		# 写入数据
		f = open('html_data.txt', 'a', encoding="utf-8")
		f.write('<div align="center"><img src="' + h_num + '\\'+n_2+'.jpg"></div>'+'\n')
		download(url+i+'.jpg',n_2)
		n += 1
		print('正在下载'+str(int(i)+1)+'页...')
	# 打开文档 读取内容 把body 填充起来
	f = open("mh37.html",'w',encoding="utf-8")
	# 读取文件里的信息
	f_html_r = open("html_data.txt",'r')
	f_html_r = f_html_r.read()
	message = """
	<html lang="zh-cn">
	<head>
    	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> 
    	<title >恶女皇后漫画_第""" + h_num + """话 </title>
    	<div align="center"><p>恶女皇后漫画_第""" + h_num + """话 </p></div>
    </head>
	<body>
	<div class="comicpage">
		"""+ f_html_r +"""
	</div>
	</body>
	</html>
	"""
	f.write(message)
	f.close()


main()
