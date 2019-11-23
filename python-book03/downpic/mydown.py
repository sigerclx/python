import urllib.request
import requests
import re,time,os,random
# 从www.mzitu.com上下载图片

# 请求头设置模拟的浏览器版本,headers 是用电脑浏览器打开该站，然后f12，network里再刷新该站，点击该网站，取得header，把user-agent复制出来，这样就能下载了
# 下载图片使用
headersPIC = {'Referer':'https://www.mzitu.com','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3679.0 Safari/537.36'}


# 设置url入口
linkUrl="https://www.mzitu.com/159671/16"
# 设置正则过滤条件
# 首先过滤出含主图的部分
pat1 = '(<div class="main-image">).+(<div class="pagenavi">)'
# 过滤出图片正式地址
pat2 ='(src=).+(.jpg)'
# 过滤出下一页地址
pat3 ='(href=").+( )'

# 定制请求头，下载网页使用
headers =("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
opener =urllib.request.build_opener()
opener.addheaders=[headers]

for i in range(1,100000):

    data = opener.open(linkUrl).read()
    data= str(data)
    
    # 下载当前url的页面
    resultPage = re.search(pat1,data)   

    # 过滤出含图片和下一个url
    resultImg = re.search(pat2,resultPage.group()) 

    # 过滤出下一页要下载的url
    resultLink = re.search(pat3,resultPage.group()) 

    # 得出下页真实地址和图片地址
    linkUrl = str.split(resultLink.group(),"\"")[1]
    imgUrl =  str.split(resultImg.group(),"\"")[1]
    print (imgUrl,linkUrl)

    # 利用下载路径生成图片名称，不会重复
    linkStr=str.split(linkUrl,'/')
    nameImg = linkStr[-2]+"_"+linkStr[-1]+".jpg"  
    nameImg=os.path.join(r"D:\Python\python-book03\downpic\mm",nameImg)
    
    # 随机休息0.2-0.5秒
    time.sleep(random.randint(20,50)/100)

    # 每下载100张图片，休息几秒
    if (i%100==0):
        shui=random.randint(5,36)
        print(i,'休息：',shui,"秒")
        time.sleep(shui)
        
    #日志文件
    log=open('log.txt','a')
    #下载并写入本地文件，同时把下载地址和图片地址写入日志
    try:
        res = requests.get(imgUrl, headers=headersPIC)
        downloadFile = open(nameImg,'wb')
        for chunk in res.iter_content(100000):
            downloadFile.write(chunk)
        downloadFile.close()
        log.writelines(linkUrl+" "+imgUrl+"\n")
        #print('成功保存图片')  
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print (e.code)
        if hasattr(e,"reason"):
            print (e.reason)

log.close()


