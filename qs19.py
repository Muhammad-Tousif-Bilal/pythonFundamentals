# Find GCD of two numbers (a = bq + r)
a = 14
b = 6

print(f"GCD of {a},{b} is", end=" ")

while b:
    a, b = b, a % b
    
print(f"{a}")


