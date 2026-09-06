#  Find largest and smallest element in an array
ls = [ 3, -5, 105, 2, 8]
smallest = ls[0]
largest = ls[0]
for i in  ls:
    if(i < smallest):
        smallest = i
    if(i > largest):
        largest = i

print("Smalles number is", smallest)
print("Largest number is", largest)
    