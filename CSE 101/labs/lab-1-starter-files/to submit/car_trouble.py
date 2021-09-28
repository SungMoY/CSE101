
# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Lab 1

# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def car_trouble(is_silent, corroded_or_clicking, fails_to_start, starts_but_dies):
    if is_silent == "Y":
        if corroded_or_clicking == "Y":
            return("clean terminals")
        else:
            return("replace cables")
    else:
        if corroded_or_clicking == "Y":
            return("replace battery")
        else:
            if fails_to_start =="Y":
                return("check spark plugs")
            else:
                if starts_but_dies == "Y":
                    return("ensure choke is opening and closing")
                else:
                    return("bring it in for service")


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('car_trouble("Y", "Y", "N", "Y") returns', car_trouble("Y", "Y", "N", "Y"))
    print()
    print('car_trouble("Y", "N", "Y", "Y") returns', car_trouble("Y", "N", "Y", "Y"))
    print()
    print('car_trouble("N", "Y", "N", "N") returns', car_trouble("N", "Y", "N", "N"))
    print()
    print('car_trouble("N", "N", "N", "N") returns', car_trouble("N", "N", "N", "N"))
    print()
    print('car_trouble("N", "N", "N", "Y") returns', car_trouble("N", "N", "N", "Y"))
    print()
    # Write your own tests for this function here!
    print() # prints a blank line

