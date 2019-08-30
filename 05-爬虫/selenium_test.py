from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from lxml import etree
import re
import time

brower=webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
brower.get("https://space.bilibili.com/10462362/channel/detail?cid=17263")
brower.maximize_window()
page=brower.page_source

# print(brower.page_source)
'''


<ul class="be-pager" style="">
    <span class="be-pager-options-elevator">
    <input type="text">
  </span>
  </span></ul>
  <span class="be-pager-total">共 7 页，</span>
'''

'''
<li title="2" class="be-pager-item be-pager-item-active"><a>2</a></li>

'''

# pat1=re.compile('<li title=".*?" class="be-pager-item be-pager-item-active"><a>(.*?)</a></li>')
# result=pat1.findall(page)
# print(str(result[0]).strip())

# pat1=re.compile('<span class="be-pager-total">共(.*?)页，</span>')
# result=pat1.findall(page)
# print(str(result[0]).strip())

input=brower.find_element_by_xpath('//ul[@class="be-pager"]/span[@class="be-pager-options-elevator"]/input')
print(input)
time.sleep(5)
brower.execute_script("window.scrollTo(0,1000)")
time.sleep(5)
input.send_keys("5")
time.sleep(5)
input.send_keys(Keys.ENTER)
action=ActionChains(brower)
action.send_keys(Keys.ENTER).perform()
page2=brower.page_source

print(page==page2)


# pat1 = re.compile('<a href="(.*?)" target="_blank" title="(.*?)" class="title">')
# result1=pat1.findall(page)
# print(type(result1))
# tem=[]
# for i in result1:
#     a=[]
#     a.append(i[0])
#     a.append(i[1])
#     tem.append(a)
#
# for i in a:
#     print(type(i))

'''
<div class="meta">
'''

# html=etree.HTML(page)
# # print(html)
# # result=html.xpath('normalize-space(//div[@class="meta"]/span[@class="play"]/text())')
# result2=html.xpath('//div[@class="meta"]/span[@class="play"]/text()')
# print(type(result2))
# tem=list()
# for i in range(0,len(result2)):
#     a=str(result2[i]).replace("\n","").strip()
#     tem.append(a)
# print(type(tem))
#
# for i in range(0,len(result1)):
#     # print(str(result1[i])+tem[i])
#     # print(type(result1[i]))
#     # print(result1[i]+eval(tem[i]))
#     # print(list(result1[i]))
#     # print(type(result1[i]))
#     print(result1[i][0]+result1[i][1]+tem[i])

