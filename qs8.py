# Check weather a character is vowel or Consonant
ch = input("Enter a single character: ")
if(len(ch) > 1 ):
    print("please enter a single character")
elif(ch.lower() == "a" or ch.lower() == "e" or ch.lower() == "i" or ch.lower() == "o" or ch.lower() == "u" ):
    print("Vowel character")
else:
    print("Consonant character")

# By using membership operator "in"
c = input("Enter a single character: ")
if(len(c) != 1 ):
    print("please enter a single character")
elif(c.lower() in "aeiou"):
    print("Vowel character")
else:
    print("Consonant character")