#  Print right triangle star pattern 
height = int(input("Height: "))


for i in range(1, height + 1):
    str = ""
    j = 0
    while j < i:
        str += "*"
        j += 1
    print(str)
