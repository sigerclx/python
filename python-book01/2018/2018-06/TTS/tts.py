#中英文都能朗读
import win32com.client
import winsound

speak = win32com.client.Dispatch('SAPI.SPVOICE')

x = input("请输入中文：")

speak.Speak(x)

#winsound.Beep(1000, 1000)
