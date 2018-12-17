import requests 
import os
try:
	os.mkdir('D:\\envhuanghou')
except:
	print('目录已存在，正在写入。。。')
# url = 'https://mh1.ahjsny.com/upload/envhuanghou/2199251/'
#url = 'https://mh1.ahjsny.com/upload/envhuanghou/6091493/'
url = 'https://mh2.ahjsny.com/upload/envhuanghou/6333861/'



def num(n):
	page_list = []
	for i in range(n):
		if i < 10:
			page_list.append('0' + str(i))
		elif 10<= i <100:
			page_list.append('00' + str(i))
		elif i >= 100:
			page_list.append('000' + str(i))
		else:
			pass
	return page_list


def download(url,num):
	response = requests.get(url)
	try:
		with open('D:\\envhuanghou\\'+num+'.jpg', 'wb') as f:
			f.write(response.content)
			f.close()
	except:
		print('未知错误')

def main():
	n = 0
	for i in num(116):
		n_2 = '{:04}'.format(n)
		f = open('html_data.txt','a')
		f.write('<div align="center"><img src="59\\'+n_2+'.jpg"></div>'+'\n')
		download(url+i+'.jpg',n_2)
		n += 1
		print('正在下载'+str(int(i)+1)+'页...')



f = open("demo_1.html",'w')
f_html_r = open("html_data.txt",'r')
f_html_r = f_html_r.read()
message = """
<html lang="zh-cn"><head>
    <meta name="viewport" content="width=device-width,initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
    <title>恶女皇后漫画_第59话 等一不归人</title>
<body>
	<div class="comicpage">
    """+ f_html_r +"""
</body>
</html>
"""
f.write(message)
f.close()
main()
