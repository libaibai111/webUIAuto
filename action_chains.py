from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

# 实例化
driver = webdriver.Chrome()

# 打开网页#
driver.get("http://www.jd.com")
time.sleep(2)
driver.maximize_window()  # 窗口最大化
time.sleep(2)

# 鼠标悬停
locator = driver.find_element_by_link_text("电脑")  # 定位元素
action = ActionChains(driver)  # 实例化ActionChains类
action.move_to_element(locator).perform()  # 鼠标悬停
time.sleep(2)
# driver.find_element_by_link_text("笔记本").click() # 点击笔记本
# time.sleep(2)

# 鼠标右键单击
action.context_click(locator).perform()  # 鼠标右键单击
time.sleep(2)
pyautogui.typewrite(['down','down','enter'],2)  # 选中右键菜单中第二个选项
time.sleep(5)

# 在元素上按下左键
# action.click_and_hold(locator).perform()  # 在元素上按下左键

driver.quit()