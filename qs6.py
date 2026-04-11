# Check weather a number is divided by 5 and 11

n = int(input("Enter a number: "))
if(n % 5 == 0 and n % 11 == 0):
    print(f"{n} is divided by 5 and 11")
else:
    print("It is not ") 
