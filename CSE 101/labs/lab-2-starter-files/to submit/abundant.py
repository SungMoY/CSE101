# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Lab 2

# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def abundant(n):
    test = 0
    for i in range(n):
        if i+1 < n and n%(i+1) == 0:
            test += (i+1)
    if test >  n:
        return True
    else:
        return False
    


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('abundant(12) is', abundant(12))
    print()
    print('abundant(14) is', abundant(14))
    print()
    print('abundant(28) is', abundant(28))
    print()
    print('abundant(40) is', abundant(40))
    print()
    # Write your own tests for this function here!
    print() # prints a blank line

