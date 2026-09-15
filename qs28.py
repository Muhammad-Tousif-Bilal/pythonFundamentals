# Add two 2D matrices 

matrix1 = [ 
    [1, 2, 3],  
    [4, 5, 6]   
]

matrix2 = [
            [1, 2, 3],   
            [1, 1, 1]    
]
TwoD = []

for i in range(len(matrix1)):
    add = []
    for j in range(len(matrix2[i])):
        sum = matrix1[i][j] + matrix2[i][j]
        add.append(sum)
    TwoD.append(add)

print(TwoD)

    
