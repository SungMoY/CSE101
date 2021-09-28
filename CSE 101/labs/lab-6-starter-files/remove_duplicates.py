# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Lab 6


# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def remove_duplicates(original):
    chrhold = ""
    for i in range(len(original)):
        if original[i] not in chrhold:
            chrhold += (original[i])
    return chrhold

# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('remove_duplicates("aaaaaaaah") produces', remove_duplicates("aaaaaaaah"))
    print()
    print('remove_duplicates("abcd") produces', remove_duplicates("abcd"))
    print()
    print('remove_duplicates("csee101") produces', remove_duplicates("csee101"))
    print()
    print('remove_duplicates("byyyyeeeeeseeeyouuulaterrrrr")', remove_duplicates("byyyyeeeeeseeeyouuulaterrrrr"))
    print()

    # Write your own tests for this function here!
    print() # prints a blank line
