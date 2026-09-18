# function to calculate factorial
num = 7

def factorial(n):
    fat = 1
    for i in range(1, n+1):
        fat *=  i
    print("factorial is ", fat)

factorial(num)
