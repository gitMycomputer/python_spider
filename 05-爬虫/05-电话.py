import re
import requests


#<td width="20%" height="25">[\s\S?]
#   <a target="_blank" href="http://www.00cha.com/p119.html">119</a>
# [\s\S?]</td>[\s\S?]
# <td width="33%">火警电话　</td>
header={
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
tel_url="http://www.00cha.com/tel.htm"

#--------------------首先通过网页源代码查看网页编码格式

# req=requests.get(tel_url,headers=header).content.decode(encoding="utf-8")
req=requests.get(tel_url,headers=header)
req.encoding="gb2312"
req_text=req.text
pat1='<td width="20%" height="25"><a target=_blank href=http://www.00cha.com/p\d+.html>(\d+)</a>'
pat2='</td>[\s\S]*?<td width="33%">(.*?)　</td>'
# pat1='<td width="20%" height="25">[\s\S]*?<a target="_blank" href="http://www.00cha.com/p119.html">119</a>[\s\S?]</td>[\s\S?]<td width="33%">火警电话　</td>'
pattern1=re.compile(pat1)
pattern2=re.compile(pat2)

data1=pattern1.findall(req_text)
data2=pattern2.findall(req_text)
print(len(data1))
print(len(data2))

# num_list=[]
# for i in range(0,len(data1)-1):
#     num_list.append(data2[i]+":"+data1[i])
# print(len(num_list))