#! python3
# P111 页练习，打印表格
data =[['apples','oranges','cherries','banana'],
       ['Alice','Bob','Carol','David'],
       ['dogs','cats','moose','goose']
       ]

for i in range(4):
    print (data[0][i].rjust(10)+'  '+data[1][i].ljust(10)+data[2][i].ljust(10))

    

