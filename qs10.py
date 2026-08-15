# Check whether a number is prime or not.
n = 5

if n > 1:

    for i in range(2, n):
        if (n%i == 0):
                print(f"{n} is not Prime")
                break
    else:
            print(f"{n} is Prime")          
else:
     print(f"{n} is not Prime")



