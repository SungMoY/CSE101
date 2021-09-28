# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Lab 1

# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def retirement(current_age, retirement_age, current_year):
    diff_age = retirement_age - current_age
    current_year += diff_age
    return current_year

# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('retirement(25, 65, 2019) returns', retirement(25, 65, 2019))
    print()
    print('retirement(55, 62, 2022) returns', retirement(55, 62, 2022))
    print()
    print('retirement(30, 78, 2014) returns', retirement(30, 78, 2014))
    print()
    # Write your own tests for this function here!
    print() # prints a blank line

