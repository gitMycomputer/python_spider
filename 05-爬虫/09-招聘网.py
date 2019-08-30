import requests
from bs4 import BeautifulSoup
# from selenium import webdriver

# https://careers.tencent.com/search.html?index=1
# https://careers.tencent.com/search.html?index=2
# https://careers.tencent.com/search.html?index=3

# https://www.so.com/zt/jobs/index.html#filter=city:%E4%B8%8A%E6%B5%B7%E5%B8%82&page=1
# https://www.so.com/zt/jobs/index.html#filter=city:%E4%B8%8A%E6%B5%B7%E5%B8%82&page=2

# https://jobs.51job.com/beijing/p1/
# https://jobs.51job.com/beijing/p2/
header={
    "User-Agent":
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
}
def list_content(list):
    for i in range(0,len(list)):
        post_url2=list[i].get("href")
        post_html=requests.get(post_url2,headers=header).text
        post_soup2=BeautifulSoup(post_html,"lxml")

        # div class="bmsg job_msg inbox"
        post_result2=post_soup2.select('div[class="bmsg job_msg inbox"]')
        print(post_result2)
        print("___________________________")
if __name__ == '__main__':

    try:
        begin_page = int(input("请输入查询起始页：\n"))
        end_page = int(input("请输入查询结束页：\n"))
    except TypeError:
        print("ERROR")
    else:
        for i in range(begin_page,end_page+1):
            post_url1="https://jobs.51job.com/beijing/p"+str(i)+"/"
            # print(post_url1)
            post_html=requests.get(post_url1,headers=header).text
            # post_html.encode(encoding="gb2312")
            # print(post_html)
            post_soup1=BeautifulSoup(post_html,"lxml")


            post_result1=post_soup1.select('span[class="title"] a')# css选择器
            list_content(post_result1)