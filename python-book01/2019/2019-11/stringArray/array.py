a=[]
for i in range(1,5):
    a.append(i)
print (a)

b=[]
for i in range(1,10,2):
    b.append(i)
c = tuple(b)
print (c)

b=[]
for i in range(5,50,5):
    b.append(i)
c = tuple(b)
print (c)

a=[]
for i in range(1,6):
    a.append(i)
    a.append(i)
    a.append(i)
print (a)

aa= "abc"
print (tuple(aa))
print (list(aa))
print (set(aa))

s=["a","b","\n"]
ab={}
for bb in s:
    ab[bb]=ord(bb)
print (ab)

a=65
for i in range(65,120):
    print (chr(i),end='')