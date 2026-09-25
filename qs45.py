#  Function to check palindrome 
n = "madaM"
def palindrome(text):
    lwr_text = text[::-1].lower()
    if(lwr_text == text.lower()):
        print("It is palindrome")
    else:
        print("It is not palindrome")

palindrome(n)
