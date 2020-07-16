from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 实例化
driver = webdriver.Chrome()

# 打开网页#
driver.get("http://www.jd.com")
time.sleep(2)
driver.maximize_window()  # 窗口最大化
time.sleep(2)

# 搜索‘鞋’
driver.find_element_by_css_selector('#key').send_keys('鞋')  # 定位输入框输入‘鞋’
time.sleep(2)
driver.find_element_by_css_selector('.button').click()  # 定位按钮并点击
time.sleep(3)

# 点击第二个商品，加入购物车
driver.find_element_by_xpath('//div[@id="J_goodsList"]/ul/li[2]/div/div[1]/a/img').click()
time.sleep(3)
handles = driver.window_handles  # 获取当前浏览器所有windows的句柄
driver.switch_to.window(handles[-1])  # 切换至最新打开的窗口
time.sleep(3)
# 搜索店内商品
driver.find_element_by_css_selector('form input:nth-child(1)').send_keys('衣服')  # 定位输入框输入‘衣服’
time.sleep(3)
driver.find_element_by_css_selector('form input:nth-of-type(2)').click()  # 定位搜索按钮并点击
time.sleep(3)

# 返回至初始窗口搜索‘小米手机’
driver.switch_to.window(handles[0])  # 切换至初始窗口
time.sleep(3)
driver.find_element(By.ID,"key").clear()  # 清除输入框内容
time.sleep(3)
driver.find_element(By.ID,"key").send_keys("小米手机")  # 定位输入框输入‘小米手机’
time.sleep(3)
driver.find_element(By.XPATH,'//button[@class="button cw-icon"]').click()  # 定位搜索按钮并点击
time.sleep(3)

driver.quit()  # 退出浏览器