# Reverse a number
num = 6784
reverseNum = 0

while num > 0:
    lastDigit = num % 10

    reverseNum = (reverseNum * 10) + lastDigit

    num = num // 10

print("Reversed number is:", reverseNum)
