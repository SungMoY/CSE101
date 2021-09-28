# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Lab 8


# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def index(filename):
    dictionary = {}
    length = 0
    for line in open(filename):
        wordlist = line.split()
        for i in range(len(wordlist)):
            if wordlist[i] in dictionary:
                dictionary[wordlist[i]].append(i + length)
            else:
                dictionary[wordlist[i]] = [i+length]
        length += len(wordlist)
        
    return dictionary



# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('Testing index("sample1.txt"):', index("sample1.txt"))
    print()

    print('Testing index("sample2.txt"):', index("sample2.txt"))
    print()

    print('Testing index("sample3.txt"):', index("sample3.txt"))
    print()

    # Write your own tests for this function here!
    print() # prints a blank line
