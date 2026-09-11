# Print number pattern
height = 4

for i in range(2, height+2):
    num = ""
    j = 1
    while j < i:
        num += str(j)
        j += 1
    print(num)