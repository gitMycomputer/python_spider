from selenium import webdriver
import time
import re
import xlsxwriter

driver = webdriver.Chrome(
            executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get("https://movie.douban.com/tag/#/")
driver.minimize_window()
# html = driver.page_source
'''<div data-v-3e982be2>
<a data-v-3e982be2="" href="javascript:;" class="more">加载更多</a>
'''
time.sleep(2)
writebook = xlsxwriter.Workbook("E:\\python_spider_example\\douban_film.xlsx")
writesheet = writebook.add_worksheet()
writesheet.set_column("A:A", 80)
writesheet.set_column("B:B", 25)
writesheet.set_column("C:C", 10)

def getinfro():
    html = driver.page_source
    pat1 = re.compile(r'<span data-v-2c455d87="" class="title">(.*?)</span>')
    pat2 = re.compile(r'<img data-v-2c455d87="" src=(.*?) alt=.*? x="movie:cover_x" y="\d{2,}">')
    pat3 = re.compile(r'<span data-v-2c455d87="" class="rate">(.*?)</span>')

    result1 = pat1.findall(html)
    result2 = pat2.findall(html)
    result3 = pat3.findall(html)
    for i in range(0, len(result1)):
        writesheet.write("A1", "电影名称")
        writesheet.write("B1", "电影链接")
        writesheet.write("C1", "评分")
        writesheet.write("A" + str(i + 2)+"", result1[i])
        writesheet.write("B" + str(i + 2)+"", result2[i])
        writesheet.write("C" + str(i + 2)+"", result3[i])
    writebook.close()


def scrollpage():
    time.sleep(2)
    more_btn = driver.find_element_by_xpath('//div[@id="app"]//div[@class="article"]/a[@class="more"]')
    more_btn.click()


scrollpage()
scrollpage()
getinfro()

driver.close()
'''
<a data-v-2c455d87="" data-v-3e982be2="" target="_blank" href="https://movie.douban.com/subject/1292052/" class="item">
<div data-v-2c455d87="" data-id="1292052" class="cover-wp">
<span data-v-2c455d87="" class="pic">
<img data-v-2c455d87="" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg" alt="肖申克的救赎" x="movie:cover_x" y="2963"></span>
</div> <p data-v-2c455d87=""><span data-v-2c455d87="" class="title">肖申克的救赎</span>
<span data-v-2c455d87="" class="rate">9.7</span></p></a>
'''
# print(html)
# <img data-v-2c455d87="" src="" alt="肖申克的救赎" x="movie:cover_x" y="2963">
