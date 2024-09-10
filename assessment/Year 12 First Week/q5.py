num_list = []
while True:
    num = int(input(""))
    if num < 0:
        break
    num_list.append(num)
    total = sum(num_list)
    counts = len(num_list)
print(total/counts)