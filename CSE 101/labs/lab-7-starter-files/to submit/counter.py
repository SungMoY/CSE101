# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Lab 7


# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def counter(filename, target):
    total = 0
    for line in open(filename):
        if line[0] == "#":
            total += 0
        else:
            for i in range(len(line)):
                if line[i] == target:
                    total += 1
    return total
            


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('counter("no-comments.txt", "e") returns the quantity', counter("no-comments.txt", "e"))
    print()
    print()
    print('counter("some-comments.txt", "s") returns the quantity', counter("some-comments.txt", "s"))
    print()
    print()
    print('counter("no-letter-found.txt", "X") returns the quantity', counter("no-letter-found.txt", "X"))
    print()
    
    # Write your own tests for this function here!
    print() # prints a blank line
