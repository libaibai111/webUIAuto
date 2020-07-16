# 1、打开后台页面
# 2、登录
#    输入用户名
#    输入密码
#    点击【进入管理中心】
# 3、点击【会员管理】
# 4、点击【会员列表】
# 5、点击【添加会员】
#    输入会员名称
#    输入邮件地址
#    输入登录密码
#    输入确认密码
#    点击【确定】
# 6、点击编辑图标
#    清空邮件地址
#    输入邮件地址
#    点击【确定】
# 7、点击收货地址图标
#    回退上一页面
# 8、点击查看订单图标
#    回退上一页面
# 9、点击查看账目明细图标
#    回退上一页面
# 10、点击移除图标
#    点击【确定】
# 11、点击退出

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 1、打开后台页面
driver = webdriver.Chrome()
url = 'http://localhost/upload/admin/privilege.php?act=login'
driver.get(url)
time.sleep(1)
driver.maximize_window()
time.sleep(1)

# 2、登录
#    输入用户名
driver.find_element(By.NAME,"username").send_keys("李白")
time.sleep(1)
#    输入密码
driver.find_element(By.NAME,"password").send_keys("aaa535889071")
time.sleep(1)
#    点击【进入管理中心】
driver.find_element(By.CLASS_NAME,"button").click()
time.sleep(2)

# 3、点击【会员管理】
driver.switch_to.frame("menu-frame")  # 进入左侧的menu-frame
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[7]').click()
time.sleep(2)

# 4、点击【会员列表】
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[7]/ul/li[1]/a').click()
time.sleep(2)

# 5、点击【添加会员】
driver.switch_to.parent_frame()  # 跳到上一层
driver.switch_to.frame("main-frame")  # 进入右侧的main-frame
driver.find_element(By.XPATH,'/html/body/h1/span[1]/a').click()
time.sleep(2)
#    输入会员名称
driver.find_element(By.NAME,'username').send_keys("李白白白")
time.sleep(1)
#    输入邮件地址
driver.find_element(By.NAME,'email').send_keys("1234567@qq.com")
time.sleep(1)
#    输入登录密码
driver.find_element(By.NAME,'password').send_keys("123456")
time.sleep(1)
#    输入确认密码
driver.find_element(By.NAME,'confirm_password').send_keys("123456")
time.sleep(1)
#    点击【确定】
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[14]/td/input[1]').click()
time.sleep(5)

# 6、点击编辑图标
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[3]/td[10]/a[1]/img').click()
time.sleep(2)
#    清空邮件地址
driver.find_element(By.NAME,'email').clear()
time.sleep(2)
#    输入邮件地址
driver.find_element(By.NAME,'email').send_keys("12345678@qq.com")
time.sleep(1)
#    点击【确定】
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[18]/td/input[1]').click()
time.sleep(5)

# 7、点击收货地址图标
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[3]/td[10]/a[2]/img').click()
time.sleep(2)
#    回退上一页面
driver.back()
time.sleep(2)

# 8、点击查看订单图标
driver.switch_to.parent_frame()  # 跳到上一层
driver.switch_to.frame("main-frame")  # 进入右侧的main-frame
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[3]/td[10]/a[3]/img').click()
time.sleep(2)
#    回退上一页面
driver.back()
time.sleep(2)

# 9、点击查看账目明细图标
driver.switch_to.parent_frame()  # 跳到上一层
driver.switch_to.frame("main-frame")  # 进入右侧的main-frame
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[3]/td[10]/a[4]/img').click()
time.sleep(2)
#    回退上一页面
driver.back()
time.sleep(2)

# 10、点击移除图标
driver.switch_to.parent_frame()  # 跳到上一层
driver.switch_to.frame("main-frame")  # 进入右侧的main-frame
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[3]/td[10]/a[5]/img').click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(5)

# 11、点击退出
driver.switch_to.default_content()  # 跳出最外层
driver.switch_to.frame("header-frame")  # 进入顶部的header-frame
driver.find_element(By.XPATH,'//div[@id="submenu-div"]/ul/li[1]/a/img').click()
time.sleep(2)

driver.quit()

