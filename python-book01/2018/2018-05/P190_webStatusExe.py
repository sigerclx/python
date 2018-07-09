#! python3
# 自动检测各站点状态,需要读取webUrl

import logging
import requests


logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)   # 加这句话，就是log全部禁止，不加，就可以log打印了
logging.debug('Start of program'.center(30,'-'))

urlDict={
      "聚银彩":
	[
		["后台","ht.sc1000.com","svip.sc1000.com","47.75.5.72:81"],
		["API","api.jyc888.vip","api.sc1000.com","api.xiankuaiji.com","47.75.5.121:82","47.75.5.72:82","sapi.sc1000.com"],
		["Web","jyc.sc1000.com","vip.sc1000.com:89","jyc.sc1000.com:89","www.yuer567.com","999.jyc888.vip:89","888.jyc888.vip:89","www.31cv.com","47.75.5.121:83","47.75.5.72:83"]],
		
     "亚太":
	 [
		["后台","ht.9003895.com","svip.ftdz3.com","47.75.2.206:81","47.75.89.51:81"],
		["API","api.yt111b.com","api.9003895.com","api.banbanrong.com","47.75.2.206:82","47.75.89.51:82","sapi.ftdz3.com"],
		["Web","vip1.9003895.com","www.87608081.com","www.9003895.com","vip1.87608081.com","vip2.9003895.com","vip2.87608081.com","vip3.9003895.com","vip3.87608081.com","47.75.2.206:83","47.75.89.51:83"]],
		
     "NBA":
	 [
		["后台","ht.nba886.net","13.112.4.16:81","13.115.140.18:81"],
		["API","api.nba886.net","api.nbayule.com","13.112.4.16:82","13.115.140.18:82"],
		["Web","www.nba886.vip","www.nba8.co",
		"www.nba886.net","www.nbayule1.net","www.nbayule8.vip",
		"www.nbayule.com","www.nbayule.net","www.nbayule.co",
		"www.nba8.vip","www.nba789.net","www.nbayule.vip",
		"www.nba6.vip","www.nba6.co","www.nba123.co","www.nba888.co","13.112.4.16:83","13.115.140.18:83"]],
		
     "老虎机":
	 [
		["API","api.play-games.tw","47.74.44.7:81"],
		["Web","game.play-games.tw"]
	 ],

      "引流":
         [
                ["Web","www.tx5f.com"],
         ]
    }



def getUrl(url): #检测url给出状态反馈
        try:
            res=requests.get(url)
        except Exception as err:
            print(url.ljust(30,' ')+' status :  无法访问')
            return

        print(url.ljust(30,' ')+' status =',res.status_code,' time =',round(res.elapsed.total_seconds(),2))
        try:
            res.raise_for_status()
        except Exception as exc:
            #print('网站不可用：%s' %(exc))
            return

sites=list(urlDict.keys())
logging.debug(sites)


for i in range(len(sites)):
    
    print(sites[i])
    for j in range(len(urlDict[sites[i]])):
        print(urlDict[sites[i]][j][0]+':')
        for k in range(1,len(urlDict[sites[i]][j])):
            logging.debug(urlDict[sites[i]][j][k])
            url = r'http://'+urlDict[sites[i]][j][k]
            getUrl(url)

    print()        
        
print('Web health detection v0.1 按回车键结束') 
input()

logging.debug('End   of program'.center(30,'-'))
