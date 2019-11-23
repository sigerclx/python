import sys
import os
from selenium import webdriver
#from selenium import chromedriver
from selenium.webdriver.common.keys import Keys
#browser = webdriver.Firefox()
browser = webdriver.Chrome()
browser.get('https://play2048.co/')
htmlElem = browser.find_element_by_tag_name('html')

for j in range(330):   ## 330是一共玩330次
    for i in range(90):     ### 90 是一次游戏中移动多少次，上下左右算一次
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)
        htmlElem.send_keys(Keys.RIGHT)
        try:
            info = browser.find_element_by_class_name("lower").is_displayed()
            if(info):
                htmlElem = browser.find_element_by_link_text('New Game')
                htmlElem.click()
                htmlElem = browser.find_element_by_tag_name('html')
        except Exception as err:
            continue
    htmlElem = browser.find_element_by_link_text('New Game')
    htmlElem.click()
    htmlElem = browser.find_element_by_tag_name('html')
