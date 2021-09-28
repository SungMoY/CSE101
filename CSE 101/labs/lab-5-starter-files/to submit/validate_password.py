# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Lab 5


# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def validate_password(password):
    eightchr = False
    onebinary = False
    onelower = False
    oneupper = False
    onespecial = False
    if len(password) >= 8:
        eightchr = True
    else:
        return "invalid"
    if "1" in password or "0" in password:
        onebinary = True
    else:
        return "invalid"
    for i in range(97, 123):
        if chr(i) in password:
            onelower = True
    if not onelower:
        return "invalid"
    for i in range(97, 123):
        if chr(i).upper() in password:
            oneupper = True
    if not oneupper:
        return "invalid"
    if "!" in password or "@" in password or "#" in password or "$" in password or "%" in password:
        onespecial = True
    else:
        return "invalid"
    if eightchr and onebinary and onelower and oneupper and onespecial:
        return "valid"    

# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('SBCs123 is', validate_password('SBCs123'))
    print('SBcs9876 is', validate_password('SBcs9876'))
    print('CSE101!isCool is', validate_password('CSE101!isCool'))
    print('cse101!iscool is', validate_password('cse101!iscool'))
    print('CSE101@ISCOOL is', validate_password('CSE101@ISCOOL'))
    print('CSE337%usesPerl is', validate_password('"CSE337%usesPerl'))

    # Write your own tests for this function here!
    print() # prints a blank line
