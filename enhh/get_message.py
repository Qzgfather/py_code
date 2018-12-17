import requests
import re
url = 'https://www.tohomh.com/envhuanghou/'
res = requests.get(url,timeout=5).text
# re_res = re.findall('<ul\sclass="view-win-list\sdetail-list-select"\sid="detail-list-select-1">(.*?)</ul>', res, re.S)
# print(re_res)
re_res_2 = re.findall('<li><a\shref=".*?"\starget="_blank"\srel="nofollow">(.*?)</a></li>',res, re.S)
print(re_res_2)