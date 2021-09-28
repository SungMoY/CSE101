# Your name: Sung Mo Yang
# Your SBU ID number: 112801117
# Your Stony Brook NetID: sungyang
# CSE 101, Fall 2019
# Final Project

# In this part of the file it is very important that you ONLY write code inside
# the function below! If you write code anywhere else, then the grading system
# will not be able to read your code and grade your work!

import random
from createLibrary import createLibrary

def buildPlayList(library, genres, length):
    ngreaterlist = []
    genrelist = []
    nonegenre = False
    tuplelist = []
    for key in library:
        for item in library[key]:
            ngreaterlist.append(item[1])
        if key in genres:
            genrelist.append(key)
        else:
            nonegenre = True
    if nonegenre and len(genrelist) == 0:
        return []
    if length > len(ngreaterlist):
        return ngreaterlist
    for x in genrelist:
        for y in library[x]:
            tuplelist.append((y[0],y[1]))
    returnlist = random.sample(tuplelist, length)
    return returnlist

def buildPlayListByLength(library, genres, length):
    indexer = 0
    testtime = 0
    totaltime = 0
    nestedsonglist = []
    ngreaterlist = []
    genrelist = []
    nonegenre = False
    tuplelist = []
    for key in library:
        for item in library[key]:
            ngreaterlist.append(item[1])
        if key in genres:
            genrelist.append(key)
        else:
            nonegenre = True
    if nonegenre and len(genrelist) == 0:
        return []
    for x in genrelist:
        for y in library[x]:
            nestedsonglist.append(y)
    for p in nestedsonglist:
        testtime += p[2]
        testtime += 2
    if testtime-2 < length:
        return []
    addedsong = random.sample(nestedsonglist, len(nestedsonglist))
    while totaltime < length:
        tuplelist.append((addedsong[indexer][0], addedsong[indexer][1]))
        totaltime += addedsong[indexer][2]
        totaltime += 2
        indexer += 1
    return tuplelist

def buildPlayListByRating(library, genres, rating):
    ngreaterlist = []
    genrelist = []
    nonegenre = False
    tuplelist = []
    nestedsonglist = []
    newnestedsonglist = []
    newnewnestedsonglist = []
    for key in library:
        for item in library[key]:
            ngreaterlist.append(item[1])
        if key in genres:
            genrelist.append(key)
        else:
            nonegenre = True
    if nonegenre and len(genrelist) == 0:
        return []
    for x in genrelist:
        for y in library[x]:
            nestedsonglist.append(y)
    for item in nestedsonglist:
        if int(item[-1]) >= rating:
            newnestedsonglist.append(item)
    if len(newnestedsonglist) == 0:
        return []
    else:
        newnewnestedsonglist = random.sample(newnestedsonglist, len(newnestedsonglist))
    for p in newnewnestedsonglist:
        tuplelist.append((p[0], p[1]))
    return tuplelist

# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    print('createLibrary("library1.txt") returns the dictionary:')
    print()
    lib_1 = createLibrary("library1.txt")
    print(lib_1)
    print()
    print()

    print('createLibrary("library2.txt") returns the dictionary:')
    print()
    lib_2 = createLibrary("library2.txt")
    print(lib_2)
    print()
    print()

    print('createLibrary("library3.txt") returns the dictionary:')
    print()
    lib_3 = createLibrary("library3.txt")
    print(lib_3)
    print()
    print()

    print('createLibrary("library4.txt") returns the dictionary:')
    print()
    lib_4 = createLibrary("library4.txt")
    print(lib_4)
    print()
    print()

    print('createLibrary("library5.txt") returns the dictionary:')
    print()
    lib_5 = createLibrary("library5.txt")
    print(lib_5)
    print()
    print()

    print('createLibrary("library6.txt") returns the dictionary:')
    print()
    lib_6 = createLibrary("library6.txt")
    print(lib_6)
    print()
    print()

    print('buildPlayList() based on "library2.txt" using the genres ["electronic","rock"] and a length of 12 returns:')
    print(buildPlayList(createLibrary("library2.txt"),["electronic","rock"],12))
    print()

    print('buildPlayList() based on "library4.txt" using the genres ["electronic","rock"] and a length of 4 returns:')
    print(buildPlayList(createLibrary("library4.txt"),["electronic","rock"],4))
    print()

    print('buildPlayListByLength() based on "library4.txt" using the genres ["electronic","rock"] and a time of 800 returns:')
    print(buildPlayListByLength(createLibrary("library4.txt"),["electronic","rock"],800))
    print()

    print('buildPlayListByLength() based on "library2.txt" using the genres ["jazz"] and a time of 2000 returns:')
    print(buildPlayListByLength(createLibrary("library2.txt"),["jazz"],2000))
    print()

    print('buildPlayListByLength() based on "library2.txt" using the genres ["jazz","classical"] and a time of 1000 returns:')
    print(buildPlayListByLength(createLibrary("library2.txt"),["jazz","classical"],1000))
    print()

    print('buildPlayListByRating() based on "library1.txt" using the genres ["blues","kpop"] and a rating of 4 returns:')
    print(buildPlayListByRating(createLibrary("library1.txt"),["blues","kpop"],4))
    print()

    print('buildPlayListByRating() based on "library1.txt" using the genres ["blues","kpop"] and a rating of 2 returns:')
    print(buildPlayListByRating(createLibrary("library1.txt"),["blues","kpop"],2))
    print()



