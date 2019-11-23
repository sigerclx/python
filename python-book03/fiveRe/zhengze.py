import re
string = "ipython-is it nice?"
patten = ".python."
result1 =  re.match(patten,string) #需要从开头匹配
result2 = re.search(patten,string).span()
print (result1)
print (result2)