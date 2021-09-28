# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Lab 7


# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def long_words(text,threshold):
    newtext = []
    dictionary = {}
    text = text.split(" ")
    for word in text:
        if len(word) >= threshold:
            newtext.append(word)
    for word in newtext:
        if word not in dictionary:
            dictionary[word] = 1
        elif word in dictionary:
            dictionary[word] +=1 
    return dictionary


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('long_words("to be or not to be", 2) produces the dictionary:')
    print(long_words("to be or not to be", 2))
    print()
    print()
    print('long_words("to be or not to be", 5) produces the dictionary:')
    print(long_words("to be or not to be", 5))
    print()
    print()
    print('long_words("i am the very model of a modern major general i\'ve information vegetable animal and mineral i know the kings of england and i quote the fights historical from marathon to waterloo in order categorical i\'m very good at integral and differential calculus i know the scientific names of beings animalculous in short in matters vegetable animal and mineral i am the very model of a modern major general",5) produces the dictionary:')
    print(long_words("i am the very model of a modern major general i've information vegetable animal and mineral i know the kings of england and i quote the fights historical from marathon to waterloo in order categorical i'm very good at integral and differential calculus i know the scientific names of beings animalculous in short in matters vegetable animal and mineral i am the very model of a modern major general",5))
    print()
    print()
    print('long_words("Man: well what\'ve you got waitress: well there\'s egg and bacon egg sausage and bacon egg and spam egg bacon and spam egg bacon sausage and spam spam bacon sausage and spam spam egg spam spam bacon and spam spam sausage spam spam bacon spam tomato and spam vikings: spam spam spam spam waitress: spam spam spam egg and spam spam spam spam spam spam spam baked beans spam spam spam vikings: spam lovely spam lovely spam waitress: or lobster thermidor au crevette with a mornay sauce served in a provencale manner with shallots and aubergines garnished with truffle pate brandy and with a fried egg on top and spam", 4) produces the dictionary:')
    print(long_words("Man: well what've you got waitress: well there's egg and bacon egg sausage and bacon egg and spam egg bacon and spam egg bacon sausage and spam spam bacon sausage and spam spam egg spam spam bacon and spam spam sausage spam spam bacon spam tomato and spam vikings: spam spam spam spam waitress: spam spam spam egg and spam spam spam spam spam spam spam baked beans spam spam spam vikings: spam lovely spam lovely spam waitress: or lobster thermidor au crevette with a mornay sauce served in a provencale manner with shallots and aubergines garnished with truffle pate brandy and with a fried egg on top and spam", 4))
    print()
    
    # Write your own tests for this function here!
    print() # prints a blank line
