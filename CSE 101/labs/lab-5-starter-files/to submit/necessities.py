# Your Name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Lab 5


# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!


def necessities(train, town):
    returnValue = 0
    if "conductor" not in train:
        return "Warning: no conductor"
    for i in range(len(town)):
        if town[i] in train:
            train.remove(town[i])
            returnValue += 1
    return returnValue


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.


if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.
    print('necessities(["conductor", "flowers", "grain"], ["pots", "flowers", "wood"]) result:', necessities(["conductor", "flowers", "grain"], ["pots", "flowers", "wood"])) # ans = 1
    print()
    print('necessities(["conductor", "clay", "ceramic", "silver", "copper"], ["pots", "wool"]) result:', necessities(["conductor", "clay", "ceramic", "silver", "copper"], ["pots", "wool"])) # ans = 0
    print()
    print('necessities(["flowers", "diamonds"], ["pots", "flowers", "wood", "iron"]) result:', necessities(["flowers", "diamonds"], ["pots", "flowers", "wood", "iron"])) # Warning: no conductor
    print()
    print('necessities(["flowers", "conductor", "diamonds", "diamonds", "flowers"], ["pots", "diamonds", "wood", "iron", "diamonds"]) result:', necessities(["flowers", "conductor", "diamonds", "diamonds", "flowers"], ["pots", "diamonds", "wood", "iron", "diamonds"])) # ans = 2
    print()
    print('necessities(["conductor", "grain", "silver", "steel", "grain", "flowers", "grain"], ["grain", "bricks", "grain", "grain", "gold", "grain", "wood", "grain", "grain"]) result:', necessities(["conductor", "grain", "silver", "steel", "grain", "flowers", "grain"], ["grain", "bricks", "grain", "grain", "gold", "grain", "wood", "grain", "grain"])) # ans = 3

    # Write your own tests for this function here!

    print() # prints a blank line
