# 1、打开首页并访问
# 2、点击注册
# 3、输入用户名
#    输入email
#    输入密码
#    输入确认密码
#    输入MSN
#    输入QQ
#    输入办公电话
#    输入家庭电话
#    输入手机
# 4、选择密码提示问题
# 5、输入密码问题答案
# 6、勾选协议
# 7、点击会员注册
#
# 8、点击首页
# 9、选择商品
# 10、点击【立即购买】
# 11、点击【确定】
# 12、点击【结算中心】
# 13、输入收货人信息
# 14、点击【配送至这个地址】
# 15、选择配送方式
# 16、选择支付方式
# 17、点击【提交订单】
# 18、点击退出

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# 1、打开首页并访问
driver = webdriver.Chrome()
url = "http://localhost/upload/index.php"
driver.get(url)
time.sleep(1)
driver.maximize_window()
time.sleep(1)

# 2、点击注册
driver.find_element_by_xpath('//font[@id="ECS_MEMBERZONE"]/a[2]').click()
time.sleep(1)
# handles = driver.window_handles  # 获取当前浏览器所有windows的句柄
# print(handles)
# driver.switch_to.window(handles[-1])  # 切换至最新打开的窗口

# 3、输入框输入值
driver.find_element_by_id("username").send_keys("李白白")
time.sleep(1)
driver.find_element_by_id('email').send_keys("123456@qq.com")
time.sleep(1)
driver.find_element_by_id('password1').send_keys("123456")
time.sleep(1)
driver.find_element_by_id('conform_password').send_keys("123456")
time.sleep(1)
driver.find_element_by_name('extend_field1').send_keys("123456@qq.com")
time.sleep(1)
driver.find_element_by_name('extend_field2').send_keys("123456")
time.sleep(1)
driver.find_element_by_name('extend_field3').send_keys("123456")
time.sleep(1)
driver.find_element_by_name('extend_field4').send_keys("123456")
time.sleep(1)
driver.find_element_by_name('extend_field5').send_keys("123456")
time.sleep(1)

# 4、选择密码提示问题
element = driver.find_element(By.NAME,"sel_question")
element.click()
time.sleep(2)
Select(element).select_by_index(2)
time.sleep(1)

# 5、输入密码问题答案
driver.find_element(By.NAME,"passwd_answer").send_keys("花花")
time.sleep(2)

# 6、勾选协议
radios = driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/form/table/tbody/tr[13]/td[2]/label")
try:
    radios.is_selected()
    print('协议默认已勾选')
except Exception as e:
    print('协议未勾选')
    radios.click()
time.sleep(2)

# 7、点击会员注册
driver.find_element(By.NAME,"Submit").click()
time.sleep(5)

# 8、点击首页
driver.find_element_by_xpath('/html/body/div[4]/div/div/a[1]').click()
time.sleep(2)

# 9、选择商品
driver.find_element_by_xpath('/html/body/div[9]/div[3]/div[1]/div/ul[1]/li[1]/a/img').click()
time.sleep(2)

# 10、点击【立即购买】
driver.find_element_by_xpath('//form[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img').click()
time.sleep(2)

# 11、点击【确定】
driver.switch_to.alert.accept()
time.sleep(2)

# 12、点击【结算中心】
driver.find_element_by_xpath('/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a/img').click()
time.sleep(2)

# 13、输入收货人信息
# 选择国家
element = driver.find_element(By.ID,'selCountries_0')
element.click()
time.sleep(2)
Select(element).select_by_index(1)
time.sleep(2)
# 选择省份
element = driver.find_element(By.ID,'selProvinces_0')
element.click()
time.sleep(2)
Select(element).select_by_index(1)
time.sleep(2)
# 选择城市
element = driver.find_element(By.ID,'selCities_0')
element.click()
time.sleep(2)
Select(element).select_by_index(1)
time.sleep(2)
# 选择区域
element = driver.find_element(By.ID,'selDistricts_0')
element.click()
time.sleep(2)
Select(element).select_by_index(1)
time.sleep(2)
# 输入收货人姓名
driver.find_element(By.ID,'consignee_0').send_keys('李白白')
time.sleep(2)
# 输入详细地址
driver.find_element(By.ID,'address_0').send_keys('天安门')
time.sleep(2)
# 输入电话
driver.find_element(By.ID,'tel_0').send_keys('123456')
time.sleep(2)

# 14、点击【配送至这个地址】
driver.find_element(By.NAME,'Submit').click()
time.sleep(2)

# 15、选择配送方式
driver.find_element(By.XPATH,'//table[@id="shippingTable"]/tbody/tr[2]/td[1]/input').click()
time.sleep(2)

# 16、选择支付方式
driver.find_element(By.XPATH,'//table[@id="paymentTable"]/tbody/tr[2]/td[1]/input').click()
time.sleep(2)

# 17、点击【提交订单】
driver.find_element(By.XPATH,'//form[@id="theForm"]/div[15]/div[2]/input[1]').click()
time.sleep(2)

# 18、点击退出
driver.find_element(By.XPATH,'//font[@id="ECS_MEMBERZONE"]/a[2]').click()
time.sleep(2)

driver.quit()