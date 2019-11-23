from selenium import webdriver
from time import sleep
# 打开百度文库，切换radio按钮 
browser = webdriver.Chrome()


handles = browser.window_handles
browser.switch_to.window(handles[0])
browser.maximize_window()
#browser.get("http://wenku.baidu.com")
browser.implicitly_wait(8)
 #"//*/input[@type='radio']"
#for i in driver.find_elements_by_xpath("//*/input[@type="+"\"radio\""+"]"): # 实现遍历点击所有的radio  
for i in browser.find_elements_by_class_name("radio"): # 实现遍历点击所有的radio  
    print(i)
    sleep(3)
    i.click()
  
