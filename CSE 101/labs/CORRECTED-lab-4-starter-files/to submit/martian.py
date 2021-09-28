# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Lab 4

# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def martian(left, right):
    leftOddCounter = 0
    if left % 2 == 1:
        leftOddCounter += 1
    while left != 1:
        left //= 2
        if left % 2 == 1:
            leftOddCounter += 1
    return leftOddCounter

# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('martian(22, 4) is', martian(22,4))
    print()
    print('martian(15, 2) is', martian(15,2))
    print()
    print('martian(103, 5) is', martian(103,5))
    print()

    print('martian(768, 21) is', martian(768,21))
    print()
    # Write your own tests for this function here!
    print() # prints a blank line

