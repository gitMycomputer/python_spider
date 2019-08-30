from urllib import request
import re
import random

url=r"http://www.baidu.com/"


# 反爬虫机制1 限制非浏览器的访问====>伪装浏览器的userAGENT,限制同一浏览器多次访问====>多个useragent
agent1="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
agent2="Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"
agent3="Mozilla/5.0 (Linux; Android 8.1; PAR-AL00 Build/HUAWEIPAR-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044304 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070333) NetType/WIFI Language/zh_CN Process/tools"
agent4="Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"
agent5="Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
list1=[agent1,agent2,agent3,agent4,agent5]
agent=random.choice(list1)

# 创建自定义的opener
http_open=request.HTTPHandler()
opener=request.build_opener(http_open)
request.install_opener(http_open)


header={"User-Agent": agent}
rep=request.Request(url,headers=header)
response=opener.open(rep).read().decode()


pat=r"<title>(.*?)</title>"
data=re.findall(pat,response)
print(data[0])