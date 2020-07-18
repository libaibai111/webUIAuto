from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# 实例化
driver = webdriver.Chrome()

# 打开网页#
driver.get("http://www.jd.com")
time.sleep(2)
driver.maximize_window()  # 窗口最大化
time.sleep(2)

# 键盘事件
driver.find_element_by_xpath('//input[@id="key"]').clear()  # 清除输入框内容
time.sleep(2)
driver.find_element_by_xpath('//input[@id="key"]').send_keys("海尔冰箱")  # 输入框输入海尔冰箱
time.sleep(3)
driver.find_element_by_xpath('//input[@id="key"]').send_keys(Keys.ENTER)  # 回车键
time.sleep(3)

driver.quit()