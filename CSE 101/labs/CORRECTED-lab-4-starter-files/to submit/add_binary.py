# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Lab 4

# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def add_binary(first, second):
    sum = ""
    carry = "0"
    for i in range(len(first)):
        if first[i] == "0" and second[i] == "0" and carry[i] == "0":
            sum += "0"
        elif first[i] == "1" and second[i] == "1" and carry == "0":
            carry = "1"
            sum += "0"
        elif first[i] == "0" and second[i] == "1" and carry == "0":
            sum += "1"
        elif first[i] == "1" and second[i] == "0" and carry == "0":
            sum += "1"
            
        elif first[i] == "0" and second[i] == "0" and carry[i] == "1":
            sum += "1"
        elif first[i] == "1" and second[i] == "1" and carry == "1":
            carry = "1"
            sum += "1"
        elif first[i] == "0" and second[i] == "1" and carry == "1":
            sum += "0"
        elif first[i] == "1" and second[i] == "0" and carry == "1":
            sum += "0"
    if carry == "1":
        sum += "1"
    
    return sum[::-1]
            
            


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('add_binary("011", "001") is', add_binary("011", "001")) # 6 + 4
    print()
    print('add_binary("1101", "0111") is', add_binary("1101", "0111")) # 11 + 14
    print()
    print('add_binary("100", "011") is', add_binary("100", "011")) # 1 + 6
    print()
    print('add_binary("1100111", "0111101") is', add_binary("1100111", "0111101")) # 115 + 94
    print()
    # Write your own tests for this function here!
    print() # prints a blank line

