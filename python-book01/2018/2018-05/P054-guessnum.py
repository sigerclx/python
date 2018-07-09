import random
myNumber = random.randint(1,100)
num=1000
line=1
print ("    猜数游戏 v1.00 版\n")
print ("  第  1  次 请猜想一个数字(1-100):",end='')
while myNumber!=num:
    num=int(input())
    line=line+1
    if myNumber<num:
        
        if myNumber<(num-40):
             print ("你第 ",line," 次猜的数字", num ," 大了好多",end='')
             continue
        else:
             print ("你第 ",line," 次猜的数字", num ," 大了一点",end='')
        
    else:
        if myNumber>(num+40):
             print ("你第 ",line," 次猜的数字", num ," 小了好多",end='')
             continue
        else:
             print ("你第 ",line," 次猜的数字", num ," 小了一点",end='')

    
print ("恭喜，你猜到 ",myNumber, " 一共用了 ",line," 次！")




                
