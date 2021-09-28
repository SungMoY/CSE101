# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Homework 2

# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

# IMPORTANT: You must complete Part I (the createLibrary() function) before you
# can test your work for this part of the assignment.

def getSongsByArtist(library, artist):
    returnlist = []
    for key in library:
        for entry in library[key]:
            if entry[1] == artist:
                returnlist.append(entry[0])
    return returnlist

# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    from createLibrary import createLibrary

    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    library_1 = createLibrary("library1.txt")

    print("Searching Library 1 for songs by Etta James:")
    print("Result:", getSongsByArtist(library_1, "Etta James"))
    print()

    print("Searching Library 1 for songs by Metallica:")
    print("Result:", getSongsByArtist(library_1, "Metallica"))
    print()


    # Write your own tests for this function here!
    print() # prints a blank line

