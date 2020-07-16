# 打开淘宝并访问
# 定位输入框输入“鞋”
# 定位搜索按钮并点击

# 引入
from selenium import webdriver
import time

# 实例化
driver = webdriver.Chrome()

# 打开网页#
driver.get("http://www.taobao.com")
time.sleep(2)
# 窗口最大化
driver.maximize_window()
# driver.set_window_size(800,600)
time.sleep(2)

# 定位输入框输入“鞋”
driver.find_element_by_xpath('//input[@id="q"]').send_keys('鞋')
time.sleep(3)
# 定位按钮并点击
driver.find_element_by_xpath('//form[@id="J_TSearchForm"]/div[1]/button').click()
time.sleep(3)

driver.quit()