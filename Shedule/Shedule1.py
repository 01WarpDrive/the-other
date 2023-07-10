import readline
import sys 
import win32gui
import win32api
import win32con
import win32clipboard   #剪切板操作

sheduleList = {}

'''
1. create/open a txt file to store missions and shedule
2. read and create dictionary from 'shedule.txt'
3. 
'''
# create/open a txt file to store missions and shedule
def getDic():
    """获取字典数据"""
    with open('shedule.txt', 'a') as shedule: # if there is not "shedule.txt", create a new txt file
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
    """指令执行"""
    while(1):
        inp = input("please enter your command:\n(\n 1. [s] for showing shedule;\n 2. [w] for changing shedule;\n 3. [d] for deleting specific shedule;\n 4. [e] for exiting;\n)\n :   " )
        if (inp == "s"):
            showShedule()
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
    """字典编辑"""
    inp = input("tell me your shedule tittle:  ")
    process = sheduleList.get(inp)
    if (process == None):
        print("creating a new shedule ...")
    else:
        print("the process of " + inp + " is:  " + sheduleList[inp] + "")

    process = input("tell me your process:  ")
    try:
        num = int(process)
        if (num >= 0 and num <= 100):
            sheduleList[inp] = num
        else:
            print("ERROR: you should input number between 0 and 100")
    except:
        print("ERROR: you should enter number")
    


    return


# delete specific shedule
def delDic():
    key = input("which one do you want to delete?  ")
    if (sheduleList.get(key)):
        sheduleList.pop(key)
        print("sucessfully delete it")
    else:
        print("wrong command: there is not title named " + key + "!!!")


# show the shedule, if there is a process reaching 100, show it
def showShedule():
    i = 1
    listCopy = dict(sheduleList)
    for ele in listCopy:
        text = "「{}」".format(ele)
        print("{}. {:<15}: {}%".format(i, text, sheduleList[ele]))
        i += 1
        if (listCopy[ele] == 100):
            sheduleList.pop(ele)
            print("Congratulate! you have finish 「{}」!".format(ele))


def start():
    getDic()
    judgeCommand()
    with open('shedule.txt', 'w') as shedule:
        shedule.write(str(sheduleList))

start()
