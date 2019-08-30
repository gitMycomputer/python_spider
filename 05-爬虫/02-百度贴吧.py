from urllib import request
import urllib
import time
header={
"User-Agent":
"Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"
}
#规律：50*(i-1)
# http://tieba.baidu.com/f?kw=python&tpl=5 #第一页
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0

# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50 #第2页

# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100 #第3页

# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=150 #第4页

# for i in range(1,5):
#     print("http://tieba.baidu.com/f?kw=python&ie=utf-8&pn="+str(50*(i-1)))# str()转字符串
def loadpage(url ,filename):
    req=request.Request(url,headers=header)
    return request.urlopen(req).read() #由于decode是将二进制转为字符串，下载是HTML文件属于二进制，因此不能用
def writepage(name ,file):
    with open(name,"wb") as f:
        f.write(file)
        print("写入文件" +name+"成功")
        print("-----------------------")
def post_bar_spider(url,begin_page,end_page):
    for i in range(begin_page,end_page+1):
        url=url+"&ie=utf-8&pn="+str((i-1)*50)
        filename="E:/spider_example/num_"+str(i)+".html"
        html_file=loadpage(url,filename)
        writepage(filename,html_file)

if __name__ == '__main__':
    try:
        newkw = input("请输入要爬取的贴吧名:\n")
        begin_pn = int(input("请输入起始页：\n"))
        end_pn = int(input("请输入终止页：\n"))
    except ValueError:
        print("请输入数字")
    else:
        newkw=urllib.parse.urlencode({"kw":newkw})# url.parse.urlencode():传递一个字典，会生成 键=值&键=值的格式
        url_header="http://tieba.baidu.com/f?"
        # url_header=url_header+"kw="+newkw不使用url.parse.urlencode()
        url_header=url_header+newkw
        post_bar_spider(url_header,begin_pn,end_pn)