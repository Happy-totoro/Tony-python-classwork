import time
def fib_recursive(n):
    if n<=1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

def fib_iteration(n):
    if n<=1:
        return n
    a = 0
    b = 1
    #temp = 0
    for i in range(2, n+1):
        a, b = b, a+b
        #temp = a
        #a = b
        #b = temp+b
    return b

startTime1 = time.time()
[fib_recursive(i) for i in range(10)]
endTime1 = time.time()
print("Recursive Fibonacci time for 10:", float(endTime1 - startTime1), "seconds")

startTime1 = time.time()
[fib_recursive(i) for i in range(20)]
endTime1 = time.time()
print("Recursive Fibonacci time for 20:", float(endTime1 - startTime1), "seconds")

startTime1 = time.time()
[fib_iteration(i) for i in range(10)]
endTime1 = time.time()
print("Iteration Fibonacci time for 10:", float(endTime1 - startTime1), "seconds")

startTime1 = time.time()
[fib_iteration(i) for i in range(20)]
endTime1 = time.time()
print("Iteration Fibonacci time for 20:", float(endTime1 - startTime1), "seconds")