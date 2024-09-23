matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def matrix_diagonal_difference(matrix):
    lengthOfMatrix = len(matrix)
    primary_diagonal = 0
    secondary_diagonal = 0
    for i in range(0, lengthOfMatrix):
        primary_diagonal += matrix[i][i]
        secondary_diagonal += matrix[i][lengthOfMatrix-i-1]
    return(abs(primary_diagonal-secondary_diagonal))
print(matrix_diagonal_difference(matrix))