# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Homework 1

# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def bill (orders):
    A_Price = 2
    B_Price = 2
    C_Price = 2
    current_sales_total = 0
    for i in orders:
        if i == 'A':
            if A_Price == 6:
                A_Price = 2
                current_sales_total += A_Price
                A_Price += 1
            else:
                current_sales_total += A_Price
                A_Price += 1
        elif i == 'B':
            if B_Price == 6:
                B_Price = 2
                current_sales_total += B_Price
                B_Price += 1
            else:
                current_sales_total += B_Price
                B_Price += 1
        else:
            if C_Price == 6:
                C_Price = 2
                current_sales_total += C_Price
                C_Price += 1
            else:
                current_sales_total += C_Price
                C_Price += 1
    return current_sales_total


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('bill("AACBBAA") returns', bill("AACBBAA"))
    print()
    print('bill("BC") returns', bill("BC"))
    print()
    print('bill("ABCABCAB") returns', bill("ABCABCAB"))
    print()
    print('bill("CCCC") returns', bill("CCCC"))
    print()
    print('bill("BBBBBBBBBB") returns', bill("BBBBBBBBBB"))
    print()
    # Write your own tests for this function here!
    print() # prints a blank line

