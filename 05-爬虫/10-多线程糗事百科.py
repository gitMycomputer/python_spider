import requests
import time
from lxml import etree
import threading
import queue
header={
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
lau_url="https://www.qiushibaike.com/"
falg1=False
falg2=False
data_queue = queue.Queue()

class loadThread(threading.Thread):
    def __init__(self,thread_name,page_queue,data_queue):
        threading.Thread.__init__(self)
        self.thread_name=thread_name
        self.page_queue=page_queue
        self.data_queue=data_queue
        self.headers=header

    def run(self):
        print("启动线程==>"+self.thread_name)
        while not falg1:
        # while not self.page_queue.empty():
            try:
                # https://www.qiushibaike.com/8hr/page/1/
                data=self.page_queue.get()
                # print(type(data))
                tem_url="https://www.qiushibaike.com/8hr/page/"+str(data)+"/"
                response=requests.get(tem_url,headers=self.headers).text
                # print(response)
                # time.sleep(0.5)#线程睡眠0.5s
                self.data_queue.put(response)
            except Exception as e:
                print("ERROR002")
                print(e)
        print("结束线程==>"+self.thread_name)
        global data_queue
        data_queue=self.data_queue

class explainThread(threading.Thread):
    def __init__(self, thread_name,data_queue,filename):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.filename = filename
        self.data_queue = data_queue

    def run(self):
        print("启动线程==>"+self.thread_name)
        while not falg2:
        # while not self.data_queue.empty():
            try:
                #<a class="recmd-content" href="/article/121167993"
                # target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">
                # </a>

                data=self.data_queue.get()
                lau_html = etree.HTML(data)
                lau_result = lau_html.xpath("//div[@class='recmd-right']//a[@class='recmd-content']/@href")

                # print(len(lau_result))
                for i in range(0,len(lau_result)):
                    lau_url2 = "https://www.qiushibaike.com" + lau_result[i]
                    print(lau_url2)
                    response2 = requests.get(lau_url2, headers=header).text
                    # response2.encode(encoding="gb2312")
                    lau_html2 = etree.HTML(response2)
                    # <div class="content"></div>
                    lau_result2 = lau_html2.xpath("//div[@class='content']")
                    # print(lau_result2[0].text)
                    print("第" + str(i+1) + "个段子写入中")
                    self.filename.write(lau_result2[0].text+"\n")# 写入文件中
            except Exception as e:
                # print("ERROR003:")
                # print(e)
                pass
        print("结束线程==>"+self.thread_name)

def main(begin_num,end_num):
    page_queue=queue.Queue(end_num-begin_num+1)
    for i in range(begin_num,end_num+1):
        page_queue.put(i)
    # filename=open(r"E:\\python_spider_example\\qiushibaike_"+str(time.time())+".txt","a")# "a"以append追加的方式输入
    filename=open(r"E:\\python_spider_example\\qiushibaike.txt","a")# "a"以append追加的方式输入

    t1=loadThread("加载链接",page_queue,data_queue)
    t1.start()
    t2=explainThread("解析链接",data_queue,filename)
    t2.start()

    while not page_queue.empty():
        pass
    global falg1# 声明全局变量
    falg1=True

    while not data_queue.empty():
        pass
    global falg2# 声明全局变量
    falg2=True

    t1.join()
    t2.join()

    filename.close()#必须要关闭

    print("录入完成")

if __name__ == '__main__':
    try:
        begin_page = int(input("请输入起始页：\n"))
        end_page = int(input("请输入结束页：\n"))
    except Exception as e:
        print("ERROR001")
        print(e)
    else:
        main(begin_page,end_page)
