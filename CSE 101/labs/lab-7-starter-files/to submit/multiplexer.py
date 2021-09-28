# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Lab 7


# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def multiplexer(filename):
    dictionary = {}
    lst = []
    twolst = []
    joiner = " "
    newline = ""
    testline = ""
    for line in open(filename):
        lst = line.split()
        twolst = lst[1::]
        twolst.append("")
        newline = joiner.join(twolst)
        if int(lst[0]) not in dictionary:
            dictionary[int(lst[0])] = newline
        else:
            testline = dictionary[int(lst[0])]
            testline += newline
            dictionary[int(lst[0])] = testline
    return dictionary

# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('multiplexer("test-file-1.txt") produces:')
    print(multiplexer("test-file-1.txt"))
    print()
    print()
    print('multiplexer("test-file-2.txt") produces:')
    print(multiplexer("test-file-2.txt"))
    print()
    print()
    print('multiplexer("test-file-3.txt") produces:')
    print(multiplexer("test-file-3.txt"))
    print()
    print()
    
    # Write your own tests for this function here!
    print() # prints a blank line
