# Qs: Check whether a number is Armstrong 
num = 153 
count = len(str(num))

armStrong = 0
digit = 0
temp = num
while temp > 0:
    digit = temp % 10
    temp = temp // 10
    armStrong += digit**count

if(armStrong == num):
    print("Its ArmStrong")
else:
    print("Not ArmStrong")

# OR by Using a Generator Expression
num = 153
power = len(str(num))

armstrong_sum = sum(int(digit) ** power for digit in str(num))

if armstrong_sum == num:
    print("Its ArmStrong")
else:
    print("Not ArmStrong")



