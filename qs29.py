# Find transpose of matrix 
matrix = [
    [1, 2, 3],
    [4, 5, 6]
] 
 
tanspose = [[], [], []]
for i in matrix:
    j = 0
    k = 0
    while j < 2:
        tanspose[k][j] = matrix[i][j]
        j += 1
        k += 1
        

print(matrix)
print(tanspose)
