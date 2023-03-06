import math as mtn
import time as tm

def KvadratWithDelay(num, time):
    tm.sleep(time/1000)
    return mtn.sqrt(num)

num = int(input())
time = int(input())
print(KvadratWithDelay(num, time))
