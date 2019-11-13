import time,threading
print ("Start thread")
def takeMyapp():
    for i in range(1,1000):
        time.sleep(0.1)
        print (i)

    print ("Wake up")

threadObj = threading.Thread(target=takeMyapp)
threadObj.start()

for i in range(10000,20000):
    time.sleep(0.2)
    print (i)


print ("end thread")
