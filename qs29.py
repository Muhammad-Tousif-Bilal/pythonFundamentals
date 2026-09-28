# Find transpose of matrix 
matrix = [
    [1, 2, 3],
    [4, 5, 6]
] 
 
tanspose = [[], []]
i = 0
while i < 2:
    tanspose[i][i] = matrix[i][i]
    i += 1

print(matrix)
print(tanspose)
