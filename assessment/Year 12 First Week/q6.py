my_array = [8, 1, -6, 9, -15, 7, 2]
print(max(my_array))
my_array.sort()
print(my_array[-1:])

#without using max() and sort()
highest_value = my_array[0]

for i in my_array:
    if i>highest_value:
        highest_value = i
print(highest_value)

#change it into function
def find_highest_value(a):
    highest_value2 = a[0]
    
    for i in a:
        if i>highest_value2:
            highest_value2 = i
    return highest_value2

answ = find_highest_value(my_array)
print(answ)
    