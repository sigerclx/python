from selenium import webdriver
from time import sleep
# 打开百度文库，切换radio按钮 
driver = webdriver.Chrome()
driver.maximize_window()
 
driver.get("http://wenku.baidu.com")
driver.implicitly_wait(8)
 #"//*/input[@type='radio']"
#for i in driver.find_elements_by_xpath("//*/input[@type="+"\"radio\""+"]"): # 实现遍历点击所有的radio  
for i in driver.find_elements_by_class_name("type-check"): # 实现遍历点击所有的radio  
 print(i)
 sleep(3)
 i.click()
  
sleep(3)