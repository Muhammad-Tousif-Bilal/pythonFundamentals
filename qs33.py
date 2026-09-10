# Print pyramid pattern
height = 4
space = height - 1
star = 1
 # by string multiplication 
for i in range(1, height+1):
    line =  (" " * space) + ("*" * star)
    print(line)
    space -=1
    star += 2

# Or by traditional way

h = 10
x = h - 1
y = 1

for i in range(1, h + 1):
    line = ""
    
    # 1. Inner loop to add spaces
    for j in range(x):
        line += " "
        
    # 2. Inner loop to add stars
    for k in range(y):
        line += "*"
        
    print(line)
    
    # Update counts for the next row
    x -= 1
    y += 2