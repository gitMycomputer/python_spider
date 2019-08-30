import urllib
from urllib import request,parse

url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

keyword="暗示"
header={
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
formdata={
    'i':keyword,
    "from":"AUTO",
    'to':' AUTO',
    'smartresult':' dict',
    'client':' fanyideskweb',
    'salt':' 15642020042473',
    'sign':' 4fe3bc3d050cfd31fc7ab252bd72df5f',
    'ts':' 1564202004247',
    'bv':' d6c3cd962e29b66abe48fcb8f4dd7f7d',
    'doctype':'json',
    'version':'2.1',
    ' keyfrom':'fanyi.web',
    'action':' FY_BY_REALTlME',
    "typoResult":"false"
}

newdata=parse.urlencode(formdata).encode(encoding="UTF-8")

req=request.Request(url,data=newdata,headers=header)
response=request.urlopen(req).read().decode()
print(response)
