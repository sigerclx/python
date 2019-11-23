
def cha(y):
    y=y-1
    return y


ji = [lambda x:x**2]

r=map(cha,[1,2,3])
print (list(r))



from collections import Counter
 
friends = [{"sex":"male","id":1},{"sex":"female","id":2},{"sex":"female","id":2}]
print(friends[0]["sex"])
print (Counter(["a","b","c","d"]).items())
print (Counter(["a","b","c","d"]))
a = list(map(lambda x:x["sex"],friends[:]))
b = map(lambda x:x["sex"],friends[:])
c = map(lambda x:x[1],Counter(list(a)).items())
d = list(map(lambda x:x[1],Counter(a).items()))
 
print(type(a))
print(a)
print(type(b))
print(b)
print(type(c))
print(c)
print(type(d))
print(d)
 
 
count = len(a)
print(count)
