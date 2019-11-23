## 客如云商家后台自动登陆，有验证码问题
from selenium import webdriver
import pytesseract
import requests ,os,time,sys,random
from selenium.common.exceptions import NoSuchElementException
from PIL import Image
from collections import defaultdict

def download_pic(src):
    res =requests.get(src)
    res.raise_for_status()
    filename= 'yzm'+str(random.randint(100000,199999))+'.jpg'
    filename= os.path.join('yanzheng_pic',filename) #路径名加上文件名
    imageFile = open(filename,'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close() 
    return filename


def checkyzm(src):
    catIM= Image.open(src)
    w,h = catIM.size

    for j in range(1,w-1):
        for k in range(1,h-1):
            a,b,c=catIM.getpixel((j,k))
            if (a<=90 and b<=89 and c>=50):
                catIM.putpixel((j,k), (0,0,0))   # 近于蓝色涂黑色
            else:
                catIM.putpixel((j,k), (255,255,255))  # 其他颜色涂白色


    new= catIM.crop((2,2,w-5,h-2))
    #new.save(r'yanzheng_pic\yzm1.jpg')
    pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

    text = pytesseract.image_to_string(new)
    return text.replace(" ", "")

def catchYzm():
    inputElem=browser.find_element_by_id('userPassword')
    inputElem.send_keys('kry201910')
    inputElem=browser.find_element_by_class_name("form-group__captcha")
    src= (inputElem.get_attribute("src"))  #本次下载链接
    filename = download_pic(src)
    time.sleep(0.3)
    text= checkyzm(filename)
    time.sleep(0.3)
    inputElem=browser.find_element_by_id('captcha')
    inputElem.send_keys(text)
    inputElem.submit()

#browser = webdriver.Firefox()
tryYanzhengCount=20  # 验证码最多尝试次数
browser = webdriver.Chrome()
browser.get('http://sso.keruyun.com/cas/login?service=http://b.keruyun.com/cas')
dengluHandle = browser.current_window_handle
inputElem=browser.find_element_by_id('loginIdInput')
inputElem.send_keys('159304')
inputElem.submit()
inputElem=browser.find_element_by_id('userPhone')
inputElem.send_keys('18561533863')
inputElem.get_attribute
print(dengluHandle)
catchYzm()

i=0 # 尝试验证码的次数
info=True
while(info):
    try:
        info= browser.find_element_by_class_name("cas-form__error").is_displayed()  #验证码出错时，该层会显示，True
    except NoSuchElementException:
        #print ("没找到验证错误")
        break
    print ("验证码出错！")
    catchYzm()
    i=i+1
    if (i>tryYanzhengCount):
        print("多次尝试失败")
        sys.exit(0)

#点击报表，准备下载
time.sleep(5)
#print("准备打开报表")
browser.switch_to.parent_frame()
#handles = browser.current_window_handle
#browser.switch_to.window(handles[-1])
browser.maximize_window()
browser.get('http://b.keruyun.com/bui-link/#/mind/report/bizSurveyRes/index')
browser.implicitly_wait(8)
try:
    info = browser.find_elements_by_class_name("radio")
    #browser.find_elements_by_xpath("//*/input[@type="+"\"radio\""+"]")
    print("radio is get")
except NoSuchElementException:
    print ('error')
    sys.exit(0)
print("info is ",info)
for i in info: # 实现遍历点击所有的radio  
    #print ("radio= ",i.get_attribute("value"))
    #if(i.get_attribute("value")==2):
    #    print (i)
    print(i)
    time.sleep(3)
    i.click()






