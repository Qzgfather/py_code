f = open("mh37.html",'w',encoding="utf-8")
f_html_r = open("html_data.txt",'r')
f_html_r = f_html_r.read()
message = """
<html lang="zh-cn"><head>
    <meta name="viewport" content="width=device-width,initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> 
    <title>恶女皇后漫画_第37话 威胁</title>
    <p>恶女皇后漫画_第37话 威胁</p>

<body>
	<div class="comicpage">
    """+ f_html_r +"""
</body>
</html>
"""
f.write(message)
f.close()