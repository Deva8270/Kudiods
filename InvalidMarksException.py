##WAP which will ask user to enter the marks and raise the custom exception "InvalidMarksException"
##if user enters the marks greater 100 or less than 0 

class InvalidMarksException(Exception):
    "Raised when the input value is less than 0 or Greater than 100"
    pass
try:
    marks = int(input("Enter a Marks: "))
    if marks > 100 or marks <= 0:
        raise InvalidMarksException
    else:
        print("You Got ",marks)     
except InvalidMarksException:
    print("Exception occurred: Invalid Marks")














