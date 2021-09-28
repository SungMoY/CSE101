# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Lab 8


# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def multisplit(source, delimiters, includeDelimiters):
    finallist = []
    index = 0
    while index < len(source):
        splitsource = ""
        while index < len(source) and source[index] not in delimiters:
            splitsource += source[index]
            index += 1
        finallist.append(splitsource)
        splitsource = ""
        while index < len(source) and source[index] in delimiters:
            if includeDelimiters:
                splitsource += source[index]
            index += 1
        if includeDelimiters and splitsource != "":
            finallist.append(splitsource)
    return finallist

# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('Testing multisplit("repetition", [], False):', multisplit("repetition", [], False)) # no delims
    print()

    print('Testing multisplit("repetition", ["e"], False):', multisplit("repetition", ["e"], False)) # 1 delim, present
    print()

    print('Testing multisplit("i am the very model of a modern major-general", ["p"], False):', multisplit("i am the very model of a modern major-general", ["p"], False)) # 1 delim, not present
    print()

    print('Testing multisplit("why is the sun yellow and not blue", ["m", "x", "z"], False):', multisplit("why is the sun yellow and not blue", ["m", "x", "z"], False)) # multiple delims, none present
    print()

    print('Testing multisplit("vampires and werewolves are mainly nocturnal creatures", ["a", "m", "n", "x", "z"], False):', multisplit("vampires and werewolves are mainly nocturnal creatures", ["a", "m", "n", "x", "z"], False)) # multiple delims, some present
    print()

    print('Testing multisplit("repetition", [], True):', multisplit("repetition", [], True)) # no delims
    print()

    print('Testing multisplit("repetition", ["e"], True):', multisplit("repetition", ["e"], True)) # 1 delim, present
    print()

    print('Testing multisplit("i am the very model of a modern major-general", ["p"], True):', multisplit("i am the very model of a modern major-general", ["p"], True)) # 1 delim, not present
    print()

    print('Testing multisplit("why is the sun yellow and not blue", ["m", "x", "z"], True):', multisplit("why is the sun yellow and not blue", ["m", "x", "z"], True)) # multiple delims, none present
    print()

    print('Testing multisplit("vampires and werewolves are mainly nocturnal creatures", ["a", "m", "n", "x", "z"], True):', multisplit("vampires and werewolves are mainly nocturnal creatures", ["a", "m", "n", "x", "z"], True)) # multiple delims, some present
    print()

    # Write your own tests for this function here!
    print() # prints a blank line
