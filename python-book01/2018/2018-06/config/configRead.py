#-*- coding: utf-8 -*-
import configparser


def func():
    cp = configparser.SafeConfigParser()
    cp.read('config.ini',encoding='utf-8')

    print ('Timeout =',cp.get('geturl','timeout'))
    #print ('ip',cp.get('serverip','ip'))

    ip = eval(cp.get('serverip','ip'))
    print (type(ip))
    for a in ip:
         print(a)

if __name__ == '__main__':
    func()
