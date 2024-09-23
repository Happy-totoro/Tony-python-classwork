matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def sum_rows(matrix):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range(0, 3):
        sum1 += matrix[0][i]
    for k in range(0, 3):
        sum2 += matrix[1][k]
    for j in range(0,3):
        sum3 += matrix[2][j]
    new_matrix = [sum1, sum2, sum3]
    return(new_matrix)
print(sum_rows(matrix))