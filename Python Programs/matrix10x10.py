matrix=[]
print("Enter elements in 10 x 10 matrix")
for i in range(10):
    a=[]
    for j in range(10):
        print(f"Element [{i},{j}]: ",end="")
        a.append(int(input()))
    matrix.append(a)
print(matrix[:])

#printing diagonal values
print("Diagonal Values in 10 x 10 matrix are: ")
for i in range(10):
    for j in range(10):
        if(i==j):
            print(matrix[i][j])
    
