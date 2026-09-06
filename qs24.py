#  Count even and odd numbers in array
ls = [2, 3, 4, 8]
countEven = 0
countOdd = 0

for i in ls:
    if(i % 2 == 0):
        countEven += 1    
    else:
        countOdd += 1

print(f"Even numbers are: {countEven}")
print(f"Odd numbers are: {countOdd}")


