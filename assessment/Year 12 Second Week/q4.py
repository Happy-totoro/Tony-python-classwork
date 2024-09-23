matrix = [[3, 5, 1], [9, 2, 8], [4, 7, 6]]
def find_largest_in_each_row(matrix):
    length = len(matrix)
    largest_in_rows = [0]*length
    for i in range(0, length):
        row = matrix[i]
        max_in_row = row[0]
        for temp in row:
            if temp > max_in_row:
                max_in_row = temp
        largest_in_rows[i] = max_in_row
    return largest_in_rows
print(find_largest_in_each_row(matrix))