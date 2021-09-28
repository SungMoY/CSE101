# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Lab 5


# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!


def conversion(number_string, n):
    result = 0
    reversal = number_string[::-1]
    
    if n == 2 or n ==8:
        if n == 2:
            if "2" in number_string or "3" in number_string or "4" in number_string or "5" in number_string or "6" in number_string or "7" in number_string or "8" in number_string or "9" in number_string:
                return "illegal digit"
            else:
                for i in range(len(reversal)):
                    addvalue = int(reversal[i]) * 2**i
                    result += addvalue
                return result
        elif n == 8:
            if "8" in number_string or "9" in number_string:
                return "illegal digit"
            else:
                for i in range(len(reversal)):
                    addvalue = int(reversal[i]) * 8**i
                    result += addvalue
                return result
            return
    else:
        return "illegal base"
# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.
    print('101 in base 2 is', conversion("101", 2))
    print('112 in base 2 is', conversion("112", 2))
    print('073 in base 8 is', conversion("073", 8))
    print('821 in base 8 is', conversion("821", 8))
    print('456 in base 4 is', conversion("456", 4))

    # Write your own tests for this function here!
    print() # prints a blank line
