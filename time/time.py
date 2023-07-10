import time
import winsound   #用来发出声音

def clock():
    hour = int(input('hour：'))
    min = int(input("minute："))
    time1 = time.localtime()
    print("start")
    while True:
        now = time.localtime()
        if (now.tm_hour - time1.tm_hour == hour) and (now.tm_min - time1.tm_min == min) and (now.tm_sec == time1.tm_sec):
            break
    winsound.Beep(600,1000) #声音提醒
    print('end')

while(1):
    clock()