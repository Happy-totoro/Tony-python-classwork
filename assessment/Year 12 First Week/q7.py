my_2d_array = [[0, 1, 2], [3, 5, 10], [6, 7, 8]]

def find_highest_value(a):
    highest_value = a[0]
    for i in a:
        if i>highest_value:
            highest_value = i
    return highest_value

def find_highest_value_2d(b):
    overall_highest_value = find_highest_value(b[0])
    for n in b:
        row_highest_value = find_highest_value(n)
        if row_highest_value>overall_highest_value:
            overall_highest_value = row_highest_value
    return overall_highest_value

answ = find_highest_value_2d(my_2d_array)
print(answ)