#交叉口处控制车辆的速度、加速度
import traci
from GET_LIST_II import get_list_II
def Speed_Junction(IDList):  
    IDList_result=get_list_II(IDList)
    n2=IDList_result[0];n1=IDList_result[1];      
    e2=IDList_result[2];e1=IDList_result[3];
    s2=IDList_result[4];s1=IDList_result[5];
    w2=IDList_result[6];w1=IDList_result[7];
    max_speed=20# m/s
    max_accel=5 #m/s^2  
    Stop_Line=200 
    if len(s1)>0:
        if traci.vehicle.getDistance(s1[0])>=Stop_Line:
            traci.vehicle.setSpeed(s1[0],max_speed)
            traci.vehicle.setAccel(s1[0],max_accel)        
    		# 如果车辆没有到达范围内，则将其速度和加速度和设定为最大值，下同
            
    if len(s2)>0:
        if traci.vehicle.getDistance(s2[0])>=Stop_Line:
            traci.vehicle.setSpeed(s2[0],max_speed)
            traci.vehicle.setAccel(s2[0],max_accel)
    		
    if len(w1)>0:
        if traci.vehicle.getDistance(w1[0])>=Stop_Line:
            traci.vehicle.setSpeed(w1[0],max_speed)
            traci.vehicle.setAccel(w1[0],max_accel)
    		
    if len(w2)>0:
        if traci.vehicle.getDistance(w2[0])>=Stop_Line:
            traci.vehicle.setSpeed(w2[0],max_speed)
            traci.vehicle.setAccel(w2[0],max_accel)
    		
    if len(n1)>0:
        if traci.vehicle.getDistance(n1[0])>=Stop_Line:
            traci.vehicle.setSpeed(n1[0],max_speed)
            traci.vehicle.setAccel(n1[0],max_accel)
    		
    if len(n2)>0:
        if traci.vehicle.getDistance(n2[0])>=Stop_Line:
            traci.vehicle.setSpeed(n2[0],max_speed)
            traci.vehicle.setAccel(n2[0],max_accel)	
    		
    if len(e1)>0:
        if traci.vehicle.getDistance(e1[0])>=Stop_Line:
            traci.vehicle.setSpeed(e1[0],max_speed)
            traci.vehicle.setAccel(e1[0],max_accel)	
    
    if len(e2)>0:
        if traci.vehicle.getDistance(e2[0])>=Stop_Line:
            traci.vehicle.setSpeed(e2[0],max_speed)
            traci.vehicle.setAccel(e2[0],max_accel)	