'''
百度搜索
1、访问页面
2、找到输入框,输入关键词
3、点击【百度一下】按钮
'''
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

# 1、访问页面
driver.get("http://www.baidu.com")

# 2、找到输入框
# driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_name("wd").send_keys("python")
time.sleep(2)

# 3、点击【百度一下】按钮
# driver.find_element_by_id("su").click()
driver.find_element_by_class_name("s_btn").click()
time.sleep(2)

# 4、点击结果
# driver.find_element_by_link_text("python教程-【免费】教程").click()
driver.find_element_by_partial_link_text("python教程-【免费】教程").click()

time.sleep(2)
driver.quit()