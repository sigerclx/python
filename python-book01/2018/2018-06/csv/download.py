import requests
import os


#down=os.path.dirname(downloadPath[0][1:])

#down=os.path.join(down,'PCInfoService.exe')

def downloadfile(url,filename):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
    res=''
    try:
        #res =requests.get(url,headers=headers)
        res =requests.get(url)
        res.raise_for_status()
    except Exception as err:
        print("发现错误了："+str(err))

    downloadFile = open(filename,'wb')
    for chunk in res.iter_content(100000):
        downloadFile.write(chunk)
    downloadFile.close()


