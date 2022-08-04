import readline


'''
1. create/open a txt file to store missions and shedule
2. read and create dictionary from 'shedule.txt'
3. 
'''
# create/open a txt file to store missions and shedule
def getDic():
    with open('shedule.txt', 'a') as shedule:
        pass
    with open('shedule.txt', 'r') as shedule:
        txt = shedule.read()
        if (txt != ""):
            sheduleList.update(eval(txt))
            print(sheduleList)
        else:
            print("welcome to use system 'shedule'")

    # 以下为初期用 “shedule process” 整理数据的代码
    # line1 = file.readline()
    # while (line1 != ""):
    #     setDic(line1)
    #     line1 = file.readline()
    
    # return


# # read and create dictionary from 'shedule.txt'
# def setDic(lin):
#     linList = lin.split()
#     sheduleList[linList[0]] = linList[1]

#     return

# judge the input
def judgeCommand():
    while(1):
        inp = input("please enter your command:\n(\n 1. [r] for reading shedule;\n 2. [w] for changing shedule;\n 3. [d] for deleting specific shedule;\n 4. [e] for exiting;\n)\n :   " )
        if (inp == "r"):
            print(sheduleList)
        elif (inp == "w"):
            writeDic()
        elif (inp == "d"):
            delDic()
        elif (inp == "e"):
            print("goodbye!")
            break
        else:
            print("wrong command!!!")


# change shedule
def writeDic():
    inp = input("tell me your shedule tittle:  ")
    process = sheduleList.get(inp)
    if (process == None):
        print("creating a new shedule ...")
    else:
        print("the process of " + inp + " is:  " + sheduleList[inp] + "")

    process = input("tell me your process:  ")
    sheduleList[inp] = process


    return


# delete specific shedule
def delDic():
    key = input("which one do you want to delete?  ")
    if (sheduleList.get(key)):
        sheduleList.pop(key)
        print("sucessfully delete it")
    else:
        print("wrong command: there is not title named " + key + "!!!")

sheduleList = {}
getDic()
judgeCommand()
with open('shedule.txt', 'w') as shedule:
    shedule.write(str(sheduleList))
