import time
import os

import playsound
playsound.playsound('good.mp3', True)


""" #方法一
file='good.mp3' #文件名是完整路径名
pygame.mixer.init() #初始化音频
track = pygame.mixer.music.load(file)#载入音乐文件
pygame.mixer.music.play()#开始播放
time.sleep(20)#播放10秒
pygame.mixer.music.stop()#停止播放 """

""" 
#方法二 调用系统播放器
file='good.mp3' #文件名是完整路径名
os.system('good.mp3')""" 

""" import IPython.display as ipd
ipd.Audio(filename='path/to/file.mp3') """