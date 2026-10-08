# Find transpose of matrix 
matrix = [
    [1, 2, 3],
    [4, 5, 6]
] 
 
tanspose = [[0,0], [0,0], [0,0]] # set the initial vale to 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        tanspose[j][i] = matrix[i][j]
        
        

print("Origninal", matrix)
print("Transpose", tanspose)
