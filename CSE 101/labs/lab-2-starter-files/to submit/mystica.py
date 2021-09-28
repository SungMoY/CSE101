# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Lab 2

# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def mystica(bowl_1, bowl_2, bowl_3, transfer):
    if bowl_1 + bowl_2 + bowl_3 != 12:
        return -1
    else: 
        if transfer < 0 and bowl_3 > 0:
            bowl_3 -= transfer
            bowl_1 += (transfer * -1)
        elif transfer < 0 and bowl_3 == 0:
            None
        elif transfer > 0 and bowl_3 == 12:
            None
        elif transfer > 0 and bowl_3 != 12 and bowl_1 > 0:
            bowl_2 += bowl_1
            bowl_1 = 0
        elif transfer > 0 and bowl_3 != 12 and bowl_1 == 0:
            bowl_3 += bowl_2
            bowl_2 = 0
        elif transfer > 0 and bowl_1 == 0 and bowl_2 == 0:
            None
    return bowl_1




# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('mystica(2, 3, 7, 4) returns', mystica(2, 3, 7, 4))
    print()
    print('mystica(3, 4, 5, -3) returns', mystica(3, 4, 5, -3))
    print()
    print('mystica(0, 1, 11, -10) returns', mystica(0, 1, 11, -10))
    print()
    print('mystica(3, 6, 2, 1) returns', mystica(3, 6, 2, 1))
    print()
    # Write your own tests for this function here!
    print() # prints a blank line

