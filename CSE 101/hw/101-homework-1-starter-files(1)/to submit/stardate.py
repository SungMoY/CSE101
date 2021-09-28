# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Homework 1

# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def stardate(month, day, year):
    b = 2323
    n = 365
    month_number = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    new_month_number = month_number[month-1]
    new_date = (1000*(year-b))+((1000/n)*(new_month_number + day -1))
    return new_date

# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('stardate(2,21,2365) returns', stardate(2,21,2365))
    print()
    print('stardate(11,29,2401) returns', stardate(11,29,2401))
    print()
    print('stardate(5,4,2390) returns', stardate(5,4,2390))
    # Write your own tests for this function here!
    print() # prints a blank line

