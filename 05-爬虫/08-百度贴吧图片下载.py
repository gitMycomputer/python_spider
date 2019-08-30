import requests
from lxml import etree

# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100

header={
"User-Agent":
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
}
IMG_NUM=0 #定义常量
def post_content(result):
    tem_list=[]
    print("<链接载入中>")
    for i in result:
        post_url2="http://tieba.baidu.com"+i
        post_response2=requests.get(post_url2,headers=header).text
        post_html2=etree.HTML(post_response2)
        # < img class ="BDE_Image"
        # pic_type="0" width="560" height="469"
        # src="http://imgsrc.baidu.com/forum/w%3D580/sign=94a1c6c7c1fc1e17fdbf8c397a91f67c/e706d2160924ab18402390e63bfae6cd7a890b8e.jpg"
        # style="cursor: url(&quot;http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;" >

        post_result2=post_html2.xpath("//img[@class='BDE_Image']/@src")
        if  len(post_result2)>=1:
            for i in range(0, len(post_result2)):
                tem_list.append(post_result2[i])
        else :
            continue
    print("<准备下载>")
    loadImg(tem_list)

def loadImg(list):
    global IMG_NUM
    for i in range(0,len(list)):
        tem=requests.get(list[i]).content
        with open("E:\\python_spider_example\\img_{}.jpg".format(IMG_NUM),"wb") as f:
            print("--正在下载第"+str(i+1)+"幅图片--")
            f.write(tem)
            IMG_NUM += 1

    print("下载完成,---------------共下载了"+str(len(list))+"幅图片-------------------")
if __name__ == '__main__':
    try:
        post_bar_name = input("请输入贴吧名：\n")
        begin_page = int(input("请输入起始页：\n"))
        end_page = int(input("请输入结束页：\n"))
    except TypeError:
        print("ERROR")
    else:
        print("<开始获取图片链接>")
        for i in range(begin_page,end_page+1):
            post_url1="http://tieba.baidu.com/f?kw=python&ie=utf-8&pn="+str((i-1)*50)
            post_response1=requests.get(post_url1,headers=header).text
            # print(post_response1)
            post_html1=etree.HTML(post_response1)
        #  < div class ="threadlist_title pull_left j_th_tit " >
        #    <a rel="noreferrer" href="/p/6207281002"
            #    title="求哪个大神教我解答一下这个题"
            #    target="_blank" class="j_th_tit ">求哪个大神教我解答一下这个题</a>
        # < / div >
            post_result1=post_html1.xpath("//a[@class='j_th_tit ']/@href")
        # http://tieba.baidu.com/p/6206894425
            print("<第"+str(i)+"页图片链接获取成功--->")
            post_content(post_result1)
