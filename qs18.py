# Print Fibonacci series
num = 6
a, b = 0, 1

for _ in range(num):
    a, b = b, a + b
    print(a)

# OR
a = 0
b= 1
for _ in range(num+1):
    print(a, end = " ")
    temp = a

    a = b

    b = temp + b
    

