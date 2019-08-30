import requests
import re

header={
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
# start=40&limit=20 从第四十部开始，每次显示20部
rank_url="https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"
req=requests.get(rank_url,headers=header).text
print(req)
# "score":"9.7"
# "title":"肖申克的救赎"
# "rank":1
pat1=r'"rating":\["(.*?)","\d+"\],'
pat2=r'"title":"(.*?)"'
pat3=r'"rank":(\d+),'

pattern1=re.compile(pat1,re.I)
pattern2=re.compile(pat2,re.I)
pattern3=re.compile(pat3,re.I)
data1=pattern1.findall(req)
data2=pattern2.findall(req)
data3=pattern3.findall(req)
print(data1)
print(data2)
print(data3)