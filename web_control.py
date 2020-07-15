"""
浏览器控制
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()  # 实例化driver对象
driver.get("http://www.baidu.com")  # 打开并访问百度首页
time.sleep(3)   # 停留3秒

driver.refresh()  # 浏览器刷新
time.sleep(3)   # 停留3秒

js = 'window.open("https://www.taobao.com");'
driver.execute_script(js)  # 打开新窗口（原也窗口不变）

driver.maximize_window()  # 窗口最大化
time.sleep(3)
# driver.set_window_size(480,800)  # 480，800像素点大小

driver.get("http://www.taobao.com")  # 打开并访问淘宝首页
time.sleep(3)   # 停留3秒
driver.refresh()  # 浏览器刷新
time.sleep(3)   # 停留3秒

driver.get("http://www.jd.com")  # 打开并访问京东首页
time.sleep(3)   # 停留3秒
driver.back()  # 后退到上一个页面
time.sleep(3)   # 停留3秒
driver.forward()  # 前进到下一个页面
time.sleep(3)   # 停留3秒

# driver.close()  # 关闭当前窗口
driver.quit()  # 退出所有窗口并关闭浏览器驱动





