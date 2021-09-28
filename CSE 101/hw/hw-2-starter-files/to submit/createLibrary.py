# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Homework 2

# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!


def createLibrary(filename):
    x = []
    insertlist = [0,0,0,0,0]
    dictionary = {}
    for line in open(filename):
        entry = line.split("|")
        if "\n" in entry[-1]:
            entry[-1] = entry[-1][0]
        minute = entry[3].split(":")
        insertminute = (int(minute[0]) * 60) + int(minute[1])
        insertlist[0] = entry[0]
        insertlist[1] = entry[1]
        insertlist[2] = entry[2]
        insertlist[3] = insertminute
        insertlist[4] = entry[4]
        tobeinsert = insertlist[1::]
        genre = insertlist[0]
        if genre in dictionary:
            dictionary[genre].append(tobeinsert)
        else:
            dictionary[genre] = [tobeinsert]
    return dictionary
    

# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('createLibrary("library1.txt") returns the dictionary:')
    print()
    lib_1 = createLibrary("library1.txt")
    print(lib_1)
    print()
    print()

    print('createLibrary("library2.txt") returns the dictionary:')
    print()
    lib_2 = createLibrary("library2.txt")
    print(lib_2)
    print()
    print()

    print('createLibrary("library3.txt") returns the dictionary:')
    print()
    lib_3 = createLibrary("library3.txt")
    print(lib_3)
    print()
    print()

    print('createLibrary("library4.txt") returns the dictionary:')
    print()
    lib_4 = createLibrary("library4.txt")
    print(lib_4)
    print()
    print()

    # Write your own tests for this function here!
    print() # prints a blank line

