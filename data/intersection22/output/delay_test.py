#!/usr/bin/python
#-*- coding: UTF-8 -*-

# this fie is used to calculate the output value  suach as Delay,quene length
import re   
Sum_waittime = 0
Sum_waitcount = 0
Sum_stoptime = 0
Sum_timeloss = 0
temp = 0
Number_car = 0

with open ("tripinfo.xml","r") as routes:
    for line in routes:
        if line != ' ' and len(line) > 90:
            temp = temp + 1
            if temp > 100:
                Wait_time = float(line.split(' ')[17].split('"')[1])
                Wait_count = float(line.split(' ')[18].split('"')[1])
                Stop_time =  float(line.split(' ')[19].split('"')[1])
                Time_loss =  float(line.split(' ')[20].split('"')[1])
                Sum_waittime = Sum_waittime + Wait_time
                Sum_waitcount = Sum_waitcount + Wait_count
                Sum_stoptime = Sum_stoptime + Stop_time
                Sum_timeloss = Sum_timeloss + Time_loss
                Number_car = Number_car + 1
Avar_waittime = float(Sum_waittime / Number_car)
Avar_waitcount = float(Sum_waitcount / Number_car)
Avar_stoptime = float(Sum_stoptime / Number_car)
Avar_timeloss = float(Sum_timeloss / Number_car)

temp = 0
Number_car = 0
Sum_queuetime = 0
Sum_queuelength = 0
with open ("queue.xml","r") as routes:
    for line in routes:
        if line != ' ' and len(line) > 90:
            temp = temp + 1
            if temp > 100:
                Queue_time = float(line.split(' ')[14].split('"')[1])
                Queue_length = float(line.split(' ')[16].split('"')[1])
                Sum_queuetime = Sum_queuetime + Queue_time
                Sum_queuelength = Sum_queuelength + Queue_length
                Number_car = Number_car + 1
Avar_queuetime = float(Sum_queuetime / Number_car)
Avar_queuelength = float(Sum_queuelength / Number_car)

print("**************************trip statistic******************************")
print("AVARAGE-waitTIME%.2fs\n AVARAGE_waitCOUNT:%0.2f time \n trip_delay:%.2fs\n" % (Avar_waittime,Avar_waitcount,Avar_timeloss))
print("*************************queue statistic*****************************")
print("AVARAGE_queueLENGTH:%0.2f M \n" % (Avar_queuelength))
