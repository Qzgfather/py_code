for i in range(156):
		n_2 = '{:04}'.format(i)
		f = open('html_data.txt','a')
		f.write('<div align="center"><img src="36\\'+n_2+'.jpg"></div>'+'\n')


f = open("mh36.html",'w')
f_html_r = open("html_data.txt",'r')
f_html_r = f_html_r.read()
message = """
<html lang="zh-cn"><head>
    <meta name="viewport" content="width=device-width,initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
    <title>恶女皇后漫画_第36话 快到本宫这里来</title>
<body>
	<div class="comicpage">
    """+ f_html_r +"""
</body>
</html>
"""
f.write(message)
f.close()
