import winreg

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SYSTEM\CurrentControlSet\Services\PCInfo") 
#print(winreg.EnumValue(key,2))
print(winreg.QueryValueEx(key,"ImagePath"))

print()
aa =winreg.QueryValueEx(key,"ImagePath")
print(aa[0])




