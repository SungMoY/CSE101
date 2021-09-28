# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Lab 6


# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def shopping(inventory, wanted):
    total = 0
    bought = []
    for item in wanted:
        for avail in inventory:
            if item[0] == avail[0]:
                bought.append([item[0], (int(item[1])*int(avail[1]))])
                break
    for cost in bought:
        total += cost[1]
    if len(bought) != len(wanted):
        return "invalid purchase"
    else:
        return total
        
                


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('shopping([["phone", 800], ["laptop", 1000], ["earphone", 200], ["watch", 500]], [["phone", 2], ["laptop", 1]]) returns', shopping([["phone", 800], ["laptop", 1000], ["earphone", 200], ["watch", 500]], [["phone", 2], ["laptop", 1]]))
    print()
    print('shopping([["phone", 800], ["laptop", 1000], ["earphone", 200], ["watch", 500]], [["phone", 2], ["charger", 1]]) returns', shopping([['phone', 800], ['laptop', 1000], ['earphone', 200], ['watch', 500]], [['phone', 2], ['charger', 1]]))
    print()

    # Write your own tests for this function here!
    print() # prints a blank line
