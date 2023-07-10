import random
import _thread
import time


# get the position of each sentence
def getIndex():
    with open("beat.txt", 'a') as file: # if there is not file, create a new file
        pass
    with open("beat.txt", 'r', encoding='utf-8') as file:
        content = file.read()
    with open("index.txt", 'w') as file:
        file.write(str(allIndex(content)))

    return


# find all the position of a char in a string
def allIndex(content):
    indexList = []
    for i in range(0, len(content)):
        if (content[i] == "@"):
            indexList.append(i)
    return indexList

# read index.txt
def readList():
    with open("index.txt", 'r') as file:
        indexList = eval(file.read())
        return indexList


# show random sentance
def showSentence():
    ind = random.randint(0, len(indexList) - 1)

    print()
    print(ind)

    with open("beat.txt", 'rt', encoding='utf-8') as file:
        file.read(indexList[ind] + 1)
        if (ind == len(indexList) - 1):
            print(file.read())
        else:
            print(file.read(indexList[ind + 1] - indexList[ind] - 1))
    
    return

# show random sentance for certain period
def secondShow(delay):
    for i in range(10):
        showSentence()
        time.sleep(delay)
        

# change sentence if needed
def getChoice():
    while(1):
        choice = input("press [p] if want to pass:  ")
        if (choice == "p"):
            showSentence()




# indexList = readList()



# _thread.start_new_thread( secondShow, (5,) )

# while (1):

print("hello \nw", end= "")
time.sleep(3)
print("\r \b\b", end= "")
time.sleep(3)
print("\rworld", end= "")