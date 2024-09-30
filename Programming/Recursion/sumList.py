numbers = [3, 6, 2, 8, 1]
def iterTotal(arr) ->int:
    sum = 0
    for i in range(len(arr)):
        sum += numbers[i]
    return sum
print(iterTotal(numbers))

def recurTotal(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0]+recurTotal(arr[1:])
print(recurTotal(numbers))