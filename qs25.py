# Search an element (linear search) 
elements = [10, 23, 45, 70, 11, 15]
find = 231
b = False

for i in elements:
    if(find == i):
        print("Found")
        b = True
        break

if (b == False):
    print("Not Found")

