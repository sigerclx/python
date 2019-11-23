
class bank(object):
    '''
    该类是银行账户，有存钱和花钱、转账的功能，账户余额只能初始化，后面只能存取。
    '''
    def __init__(self,account,money):
        self.__account = account
        self.__money = money
    
    def cun(self,addMoney):
        self.__money = self.__money + addMoney
        print(self.__account,'存入',addMoney,'剩余金额:',self.__money)
    
    def hua(self,reduceMoney):
        self.__money = self.__money - reduceMoney
    
    def disp(self):
        print (self.__account,"剩余金额:",self.__money)

    def zhuanzhang(self,account,money): #转账
        self.__money = self.__money - money
        account.cun(money)
        print(self.__account,"转账",money,'剩余金额:',self.__money)

