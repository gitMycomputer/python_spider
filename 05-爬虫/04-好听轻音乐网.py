#第一页
#http://www.htqyy.com/top/hot
#http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20

#第2页
#http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20

#第3页
#http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20

# 音乐
# http://www.htqyy.com/play/33

#播放
# http://f2.htqyy.com/play7/62/mp3/7
# http://f2.htqyy.com/play7/55/mp3/7

import re
import requests
header={
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
pat1=r'title="(.*?)" sid='
pat2=' sid="(.*?)"'
song_name=[]
song_id=[]
def writeData(name,id):
    for i in range(len(name)):
        tem_http="http://f2.htqyy.com/play7/"+str(id[i])+"/mp3/7"
        tem_bin=requests.get(tem_http).content #获取二进制文件
        print("正在下载第{}首".format(i+1))
        with open("E:\\python_spider_example\\{}.mp3".format(name[i]),"wb") as f:
            f.write(tem_bin)
            print("下载成功---------------------")

if __name__ == '__main__':
    try:
        begin_page=int(input("请输入下载的开始页码:\n"))
        end_page=int(input("请输入下载的结束页码:\n"))
    except TypeError:
        print("请输入数字")
    else:
        for i in range(begin_page-1,end_page):
            url="http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"&pageSize=20"
            response=requests.get(url,headers=header)
            # print(response.text)
            #<a href="/play/56" target="play" title="夜的钢琴曲五" sid="56">
            #E:\python - spider_example
            song_name=re.findall(pat1,response.text)
            song_id=re.findall(pat2,response.text)
        writeData(song_name,song_id)

