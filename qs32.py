#  Print inverted triangle
height = 4

for i in range( height):
    str = ""
    j = height
    while j > i:
        str += "*"
        j -= 1
    print(str)

