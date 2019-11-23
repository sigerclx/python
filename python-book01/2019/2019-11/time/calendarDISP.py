import calendar
cal = calendar.month(2020, 2)
print (cal)
i=2010
for i in range(2010,2030,1):
    print (i,calendar.isleap(i))

print (calendar.SATURDAY(2019,12))