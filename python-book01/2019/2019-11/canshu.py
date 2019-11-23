#不确定参数的函数，一个* 代表元组，**代表字典
def w_sum(x1,x2,*y):
    sum=0
    size=len(y)
    weight = 0.3/size
    for i in y:
        sum = sum +weight*i
    sum = sum + 0.4*x1 + 0.3 *2
    return sum

print (w_sum(1,2,3,4,5,6,7,8,9)) # 这个函数参数可以多加任意个，最少3个
print (w_sum(1,2,3))

# 匿名函数
Lfun= [lambda x:x**2,
        lambda x:x**3,
        lambda y:y**4+1]
for p in Lfun:
    print (p(2))

#数值交换
a=1
b=2
a,b=b,a
print(a,b)

#map函数
#def ji(num):
#    return num**2
ji = [lambda x:x**2]
disp=map(Lfun,[1,2,3])
print (disp)