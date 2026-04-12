# Calculate grade of student based on marks
marks = int(input("Enter your marks: "))
if(marks > 100 or marks < 0):
    print("Please Enter correct marks")
elif(marks >= 90 ):
    print("His grade is A")
elif(marks >= 80 ):
    print("His grade is B")
elif(marks >= 70 ):
    print("His grade is C")
elif(marks >= 40):
    print("His grade is D")
else:
    print("His grade is F")