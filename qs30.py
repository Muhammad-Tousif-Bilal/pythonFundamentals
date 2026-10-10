#  Find sum of each row and column of matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [4, 5, 6]
]
# add rows
for i in range(len(matrix)):
    sum = 0
    for j in range(len(matrix[0])):
        sum += matrix[i][j]
    print(f"sum row{i} is ", sum)
# add column
for i in range(len(matrix[0])):
    sum = 0
    for j in range(len(matrix)):
        sum += matrix[j][i]
    print(f"sum of column{i} is", sum)