name="Parul"
length=len(name)
for i in range(length): #for number of rows
    for j in range(length-i): #for decreasing right triangle pattern to print space
        print('',end=' ')
    for j in range(i+1):  #for right triangle pattern   
        print(name[j],end=' ')
    print()