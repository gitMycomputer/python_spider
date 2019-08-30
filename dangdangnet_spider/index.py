from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import etree
import time
import xlsxwriter
import re

# http://www.dangdang.com/
# http://search.dangdang.com/?key=Python&act=input&page_index=1
# http://search.dangdang.com/?key=Python&act=input&page_index=2
# http://search.dangdang.com/?key=python&act=input


driver = webdriver.Chrome(
            executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get("http://www.dangdang.com/")
driver.maximize_window()
write_page = xlsxwriter.Workbook("E:\\python_spider_example\\dangdangnet.xlsx")
write_sheet = write_page.add_worksheet()
now_line = 1


def get_con(page):
    html = etree.HTML(page)
    result1 = html.xpath(r'//div[@id="search_nature_rg"]/ul[@class="bigimg"]/li/a/@title')
    result2 = html.xpath(r'//div[@id="search_nature_rg"]/ul[@class="bigimg"]/li/a/@href')
    result3=(re.compile('<span class="search_now_price">(.*?)</span>')).findall(page)
    # result3 = html.xpath(r'//div[@id="search_nature_rg"]/ul[@class="bigimg"]/li'
    #                      r'/p[@class="price"]/span[@class="search_now_price"]/text()')
    print(len(result1))
    print(len(result2))
    print(len(result3))
    for i in range(1, len(result2)+1):
        global now_line
        write_sheet.write("A" + str(now_line) + "", result1[i-1])
        write_sheet.write("B" + str(now_line) + "", result2[i-1])
        write_sheet.write("C" + str(now_line) + "", result3[i-1])
        now_line += 1


def to_next(driver):
    driver.execute_script("window.scrollTo(0,14500)")
    next_page = driver.find_element_by_xpath('//div[@name="m1559565_pid0_t12835"]'
                                             '/div[@name="m1559565_pid0_t12836"]'
                                             '/div[@class="paging"]'
                                             '/ul/li[@class="next"]/a')
    time.sleep(2)
    next_page.click()
    time.sleep(2)
    get_con(driver.page_source)


input_text = driver.find_element_by_id("key_S")
time.sleep(1)
input_text.send_keys("python")
input_text.send_keys(Keys.ENTER)
time.sleep(1)

get_con(driver.page_source)
for i in range(0,11):
    to_next(driver)
write_page.close()
time.sleep(5)
driver.close()
