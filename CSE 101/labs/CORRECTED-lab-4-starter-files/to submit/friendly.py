# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Lab 4

# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def friendly(number, digits):
    boolv = None
    number = str(number)
    for i in range(digits):
        if int(number[i]) % (i+1) == 0:
            boolv = True
        else:
            boolv = False
            exit
    return boolv
            

# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('friendly(42325,5) is', friendly(42325,5))
    print()
    print('friendly(82736451,8) is', friendly(82736451,8))
    print()
    print('friendly(18,2) is', friendly(18,2))
    print()
    print('friendly(497,3) is', friendly(497,3))
    print()
    # Write your own tests for this function here!
    print() # prints a blank line

