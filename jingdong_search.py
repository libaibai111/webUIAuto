# 打开并访问京东首页
# 定位输入框输入“小米手机”
# 点击搜索按钮
# 点击结果中第一个商品
# 切换窗口
# 获取价格
# 加入购物车

# 引入webdriver、time、By
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 实例化
driver = webdriver.Chrome()
# 打开网页
driver.get("http://www.jd.com")
time.sleep(2)

# 窗口最大化
driver.maximize_window()
time.sleep(2)

# 打印当前页面url
# url = driver.current_url
# print(url)

# 定位输入框输入“小米手机”
driver.find_element(By.ID,"key").send_keys("小米手机")
time.sleep(3)
# 获取标签class属性并打印
# text = driver.find_element(By.ID,"key").get_attribute("class")
# print(text)

# 定位按钮并点击按钮
driver.find_element(By.CLASS_NAME,"button").click()
time.sleep(3)
# 获取标签class属性并打印
# button = driver.find_element(By.CLASS_NAME,"button").get_attribute("class")
# print(button)

# 定位第一个结果并点击打开新窗口
driver.find_element(By.CSS_SELECTOR,"div[class='p-img'] > a > img").click()
time.sleep(3)
# 切换窗口
handles = driver.window_handles
print(handles)
driver.switch_to.window(handles[-1])

# 定位价格并获取价格
# price = driver.find_element(By.CLASS_NAME,'price.J-p-100009082466').text
# print(price)

# 点击【加入购物车】
driver.find_element(By.XPATH,"//a[@id='InitCartUrl']").click()
time.sleep(3)

driver.quit()
