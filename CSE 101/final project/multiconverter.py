# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Homework 3

# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

def multiconverter(unit, value):
    if unit == "pica":
        returnlist = [value, value*12, value*16]
    elif unit == "point":
        returnlist = [value/16, value, value*(3/4)]
    elif unit == "pixel":
        returnlist = [value/16, value*(3/4), value]
    elif unit == "kelvin":
        returnlist = [value, value-273.15, value*18-459.67, value*1.8-459.67, (value-273.15)*.8]
    elif unit == "celsius":
        returnlist = [value+273.15, value, value*1.8+32, value*1.8 + 32 + 459.67, value*.8]
    elif unit == "fahrenheit":
        returnlist = [(value+459.67)/1.8, (value-32)/1.8, value, value +459.67, (value-32)/2.25]
    elif unit == "rankine":
        returnlist = [value/1.8, (value+459.67)/1.8, value-459.67, value, (value-32-459.67)/2.25]
    elif unit == "reaumur":
        returnlist = [value*1.25+273.15, value*1.25, value*2.25+32, value*2.25+32+459.67, value]
    elif unit == "feet":
        returnlist = [value, value/3.2808, value/16.5, value/6, value/5.1509]
    elif unit == "meters":
        returnlist = [value*3.2808, value, value*3.2808/16.5, value*3.2808/6, value*3.2808/5.1509]
    elif unit == "rods":
        returnlist = [value*16.5, value*16.5/3.2808, value, value*16.5/6, value*16.5/5.1509]
    elif unit == "fathoms":
        returnlist = [value*6, value*6/3.2808, value*6/16.5, value, value*6/5.1509]
    elif unit == "canas":
        returnlist = [value*5.1509, value*5.1509/3.2808, value*5.1509/16.5, value*5.1509/6, value]
    return returnlist
    
    

# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # test cases will be posted shortly

    print('multiconverter("pica", 3) =', multiconverter("pica", 3))
    print()

    print('multiconverter("pixel", 24) =', multiconverter("pixel", 24))
    print()

    print('multiconverter("point", 72) =', multiconverter("point", 72))
    print()
    
    print('multiconverter("kelvin", 451) =', multiconverter("kelvin", 451))
    print()

    print('multiconverter("celsius", 37.1) =', multiconverter("celsius", 37.1))
    print()

    print('multiconverter("fahrenheit", 212) =', multiconverter("fahrenheit", 212))
    print()

    print('multiconverter("rankine", 268) =', multiconverter("rankine", 268))
    print()

    print('multiconverter("reaumur", 17) =', multiconverter("reaumur", 17))
    print()

    print('multiconverter("feet", 25) =', multiconverter("feet", 25))
    print()

    print('multiconverter("meters", 2) =', multiconverter("meters", 2))
    print()

    print('multiconverter("rods", 14) =', multiconverter("rods", 14))
    print()

    print('multiconverter("fathoms", 10) =', multiconverter("fathoms", 10))
    print()

    print('multiconverter("canas", 20) =', multiconverter("canas", 1.0))
    print()


