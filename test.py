# ！/user/bin/env python
# _*_ coding:utf-8  _*_
# @Filename:test1.py


from selenium import webdriver
import time

driver = webdriver.Chrome()  # 实例化driver对象
driver.get("http://www.baidu.com")  # 打开并访问百度首页
time.sleep(3)   # 停留3秒
driver.refresh()  # 浏览器刷新

driver.maximize_window()  # 窗口最大化
driver.set_window_size(480,800)  # 480，800像素点大小

driver.get("http://www.taobao.com")  # 打开并访问淘宝首页
time.sleep(3)   # 停留3秒
driver.refresh()  # 浏览器刷新

driver.get("http://www.jd.com")  # 打开并访问京东首页
time.sleep(3)   # 停留3秒
driver.back()  # 后退到上一个页面
time.sleep(3)   # 停留3秒
driver.forward()  # 前进到下一个页面
time.sleep(3)   # 停留3秒
# driver.close()  # 关闭当前窗口

driver.quit()  # 退出所有窗口并关闭浏览器驱动


# driver.maximize_window()  # 最大化浏览器
# driver.set_window_size(480,800)  # 480，800像素点大小
# driver.forward()  # 前进到下一个页面
# driver.back()  # 后退到上一个页面
# driver.quit()  # 退出所有窗口并关闭浏览器驱动

# driver.find_element_by_id("kw").send_keys("刘德华")  # 输入框输入“刘德华”
# driver.find_element_by_id("su").click()  # 点击按钮
# driver.find_element_by_name("wd")  # 定位wd输入框
# driver.find_element_by_class_name("s_ipt")  # 定位类名s_ipt
# driver.find_element_by_class_name("s_btn")  # 定位类名s_btn






