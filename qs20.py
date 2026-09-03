#  Check whether a number is Armstrong 
num = 153 
count = len(str(num))

armStrong = 0
eachNum = 0
num2 = num
while num2 > 0:
    eachNum = num2 % 10
    num2 = num2 // 10
    armStrong += eachNum**count

if(armStrong == num):
    print("Its ArmStrong")
else:
    print("Not ArmStrong")

# OR by Using a Generator Expression
"""
num = 153
power = len(str(num))

# sum() adds up the powers of each digit in a single line

armstrong_sum = sum(int(digit) ** power for digit in str(num))

if armstrong_sum == num:
    print("Its ArmStrong")
else:
    print("Not ArmStrong")
"""


