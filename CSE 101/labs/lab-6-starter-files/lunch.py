# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Lab 6


# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def lunch(adjustments):
    total = adjustments[0]
    adjustments = adjustments[1::]
    for adj in adjustments:
        if adj[0] == "tip":
            total *= (adj[1]/100 + 1)
        elif adj[0] == "extra":
            total += adj[1]
        elif adj[0] == "coupon":
            total -= adj[1]
        elif adj[0] == "discount":
            total *= (1 - (adj[1]/100))
    if total <= 0:
        total = 0
    return total
    
        
# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('lunch([29.77, ["tip", 1]]) produces a final bill of:', lunch([29.77, ["tip", 1]]))
    print()
    print('lunch([40.32]) produces a final bill of:', lunch([40.32]))
    print()
    print('lunch([40.41, ["extra", 9.55], ["discount", 15]]) produces a final bill of:', lunch([40.41, ["extra", 9.55], ["discount", 15]]))
    print()
    print('lunch([19.34, ["discount", 69], ["tip", 62], ["extra", 2.53], ["coupon", 5.34], ["extra", 3.25]]) produces a final bill of:', lunch([19.34, ["discount", 69], ["tip", 62], ["extra", 2.53], ["coupon", 5.34], ["extra", 3.25]]))
    print()
    print('lunch([4.55, ["discount", 11], ["coupon", 5.63], ["coupon", 6.28], ["discount", 61], ["extra", 2.42], ["tip", 65], ["discount", 40], ["tip", 6]]) produces a final bill of:', lunch([4.55, ["discount", 11], ["coupon", 5.63], ["coupon", 6.28], ["discount", 61], ["extra", 2.42], ["tip", 65], ["discount", 40], ["tip", 6]]))
    print()

    # Write your own tests for this function here!
    print() # prints a blank line
