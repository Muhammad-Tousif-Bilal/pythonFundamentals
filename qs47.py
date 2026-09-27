#  Function to swap two numbers (call by value)
a = 4
b = 5

def swap(x, y):
    tmp = x
    x = y
    y = tmp
    print(f"After a = {x}, b = {y}")

print(f"Before a = {a}, b = {b}")
swap(a, b)

