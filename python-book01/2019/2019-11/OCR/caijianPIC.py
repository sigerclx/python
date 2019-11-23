import os
import pytesseract
from PIL import Image
from collections import defaultdict
# 把yanzheng_pic目录里所有客如云的验证码图片解析成字符

for folder,subfolder,filename in os.walk(r'yanzheng_pic'):
    continue
    #print(filename)

for thisPicName in filename:
    #os.chdir('yanzheng_pic')
    thisFile= os.path.join('yanzheng_pic',thisPicName) #路径名加上文件名
    catIM= Image.open(thisFile)
    w,h = catIM.size

    for j in range(1,w-1):   # 过滤黑边
        for k in range(1,h-1):
            a,b,c=catIM.getpixel((j,k))
            if (a<=90 and b<=89 and c>=50):  #这几个参数是在PS中打开图片，看偏蓝色的三原色，找到的规律
                catIM.putpixel((j,k), (0,0,0))   # 近于蓝色涂黑色
            else:
                catIM.putpixel((j,k), (255,255,255))  # 其他颜色涂白色

    #catIM.save(r'yanzheng_pic\old\bn43_1.jpg')
    new= catIM.crop((2,2,w-5,h-2))  #切掉黑边
    #new.save(r'yanzheng_pic\yzm1.jpg')
    pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

    text = pytesseract.image_to_string(new)
    print(thisPicName,' = ',text.replace(" ", ""))
