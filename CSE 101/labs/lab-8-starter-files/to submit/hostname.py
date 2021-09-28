# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Lab 8


# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def hostname(url):
    slashchecker = True
    dotchecker = True
    index = url.rfind("://")
    indexurl = url[index+3::]
    while  slashchecker:
        if indexurl.rfind("/") != -1:
            indexurl = indexurl[0:indexurl.rfind("/")]
        else:
            slashchecker = False
    indexurl = indexurl[:indexurl.rfind(".")]
    indexurl = indexurl[indexurl.rfind(".")+1:]
    return indexurl    

# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('hostname("irc://foo.com/") returns:', hostname("irc://foo.com/"))
    print()

    print('hostname("http://i.am.a.hostname.edu/blah/blah/") returns:', hostname("http://i.am.a.hostname.edu/blah/blah/"))
    print()

    print('hostname("ftp://some-like.it-hot.net/something/filename.pdf") returns:', hostname("ftp://some-like.it-hot.net/something/filename.pdf"))
    print()

    # Write your own tests for this function here!
    print() # prints a blank line
