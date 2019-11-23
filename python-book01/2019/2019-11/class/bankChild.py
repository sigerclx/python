from bankClass import bank as bk
class bank(bk):
    '''
    该类是银行账户的继承，添加信用额度和检查是否超额使用。余额不足会扣减信用额度。
    '''
    def __init__(self,account,money,xinyong):
        bk.__init__(self,account,money)
        self.__xinyong = xinyong
        self.__touzhi = xinyong
    

    def xinyong (self,money):
        self.__xinyong =money
    
    def disp_xinyong(self):
        print (self.__account,"可透支金额：",self.__touzhi)

    def hua(self,money):
        if (money>(self.__money)):
            print (self.__account,"需要消费",money," 账户余额不足")
            if(self.__touzhi>(money-self.__money)):
                print (self.__account,"正在透支信用额度,剩余可用额度：",self.__touzhi-(money-self.__money))
                self.__touzhi=self.__touzhi-(money-self.__money)
                self.__money = 0
                print(self.__account,"消费",money,"账户余额:",self.__money)
            else:
                print(self.__account,"信用额度不足:",self.__touzhi,'无法消费')
        else:
            print (self.__account,"消费：",money,'剩余金额:',self.__money)
            self.__money = self.__money - money

mybank = bank('jacky',50,1000)
yourbank = bank('tom',50,500)
mybank.hua(5)
mybank.__money=89  # 这句话不会报错，但是无效，__双下划线的意思就是private内部保护变量  
mybank.zhuanzhang(yourbank,15)
yourbank.cun(4.5)
mybank.hua(35)
mybank.disp_xinyong()
mybank.hua(50)