#  Recursive function for Fibonacci series
n = 10

def fibnoacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
   
    return fibnoacci(n - 1) + fibnoacci(n - 2)
for i in range(n + 1):
    print(fibnoacci(i), end=" ")



