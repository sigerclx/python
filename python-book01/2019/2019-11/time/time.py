import time
def calcProd(num):

    for i in range(1,num):
        pro= i+i*(i+1)
    return pro
num=2000000
startTime = time.time()
prod = calcProd(num)
endTime = time.time()
print ("数字"+str(num)+"运行的时间周期："+str(endTime-startTime))
print (prod)
# 四舍五入
print (str(round(4.1234345,2)))


