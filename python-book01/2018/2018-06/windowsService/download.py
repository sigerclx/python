import winreg
import requests
import os
key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SYSTEM\CurrentControlSet\Services\PCInfo")
downloadPath =winreg.QueryValueEx(key,"ImagePath")
info = {"status": "download"}
print(downloadPath)
try:
    res =requests.get(r'http://13.112.4.16:83/PCInfoService.exe')
except Exception as err:
    print(err)

down=os.path.dirname(downloadPath[0][1:])

down=os.path.join(down,'PCInfoService.exe')


print(down)

downloadFile = open(down,'wb')
for chunk in res.iter_content(100000):
    downloadFile.write(chunk)
downloadFile.close()
