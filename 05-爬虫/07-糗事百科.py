import requests
from lxml import etree
import xlsxwriter


header={
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
lau_url="https://www.qiushibaike.com/"

response=requests.get(lau_url,headers=header).text

# <div class="recmd-right">
# <a class="recmd-content" href="/article/121138296" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">爸爸酒驾被查，女儿教育爸爸惹笑众人！开酒不喝车？捋不明白了</a>

lau_html=etree.HTML(response)
lau_result=lau_html.xpath("//div[@class='recmd-right']//a[@class='recmd-content']/@href")
workbook=xlsxwriter.Workbook("E:\\python_spider_example\\糗事百科.xlsx")
worksheet=workbook.add_worksheet()

# https://www.qiushibaike.com/article/121138296
for i in range(0,len(lau_result)):
    lau_url2="https://www.qiushibaike.com"+lau_result[i]
    response2=requests.get(lau_url2,headers=header).text

    # <div class="content">爸爸酒驾被查，女儿教育爸爸惹笑众人！开酒不喝车？捋不明白了</div>

    lau_html2=etree.HTML(response2)
    print(lau_html2)
    lau_result2=lau_html2.xpath("//div[@class='content']")
    print("第"+str(i)+"个段子："+lau_result2[0].text)
    worksheet.write("A"+str(i+1)+"",lau_result2[0].text)
workbook.close()