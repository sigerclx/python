import urllib.request
#file = urllib.request.urlretrieve("https://www.mzitu.com/",filename="mm.html") #该网站不能直接下载，防爬虫，需要用下面的方式
#url ="https://blog.csdn.net/yuanziok/article/details/103166087"

url="https://www.mzitu.com/"
# headers 是用电脑浏览器打开该站，然后f12，network里再刷新该站，点击该网站，取得header，把user-agent复制出来，这样就能下载了
headers =("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
opener =urllib.request.build_opener()
opener.addheaders=[headers]
data = opener.open(url).read()
fhandle = open("mm1.html","wb")
fhandle.write(data)
fhandle.close()
