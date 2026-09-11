#  Print reverse number pattern 
height = 4

for i in range(height):
    num = ""
    j = height
    k = 1
    while j > i:
        num += str(k)
        j -= 1
        k += 1
    print(num)