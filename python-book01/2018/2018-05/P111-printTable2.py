#! python3
# P111 页练习，打印表格
data =[['apples','oranges','cherries','banana'],
       ['Alice','Bob','Carol','David'],
       ['dogs','cats','moose','goose']
       ]

str1=[[],[],[],[]]

#把data的行和列颠倒过来
for list in data:
    for i in range(len(list)):
        str1[i].append(list[i])


for list in str1:
    for value in list:
        print(value.ljust(10),end='')
    print('\n')
