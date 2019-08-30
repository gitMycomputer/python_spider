import re
import requests
from lxml import etree



# header={
# "User-Agent":
# "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
# }
# tel_url="http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20"
#
#
#
#
# req=requests.get(tel_url,headers=header)
# # req.encoding="gb2312"
# # req_text=req.text
# data=req.text
#
# pat1 = re.compile('<a href="/play/\d+" target="play" title="(.*?)"')
# pat2 = re.compile('<a href="/artist/\d+" title="(.*?)"|<a href="/artist/detail/(.*?)"')
#
# data1=pat1.findall(data)
# data2=pat2.findall(data)
#
#
# print(data1[0])
# print(len(data2))



# import json
#
# with open(r"E:\Python-爬虫\scrapy_spider\musoc.json",'rb') as f:
#     data=json.load(f)
#     print(data)

header={
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
tel_url="http://wz.sun0769.com/html/question/201907/422604.shtml"




req=requests.get(tel_url,headers=header)
print(req.encoding)
# req.encoding="gb2312"
# req_text=req.text
html=etree.HTML(req.text)
data=html.xpath('//div[@class="wzy1"]/table[2]//td[@class="txt16_3"][1]/text()')[0].encode("ISO-8859-1").decode("gbk")
# data1 = "".join([each for each in data])
print(data)






# print(data1[0])
# print(len(data2))
