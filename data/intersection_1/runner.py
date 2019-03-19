from __future__ import absolute_import
from __future__ import print_function
from gurobipy import *
from CCAR import CAR_L
from CINPUT import Input
from optimiza_function import optimize_av
from GetDelay import Get_Delay
from GET_LIST import get_list
from GET_LIST_II import get_list_II
from generator_route_123 import generator
from CRESULT import Result
from INPUT_ADDITIONAL import Input_Addtional
from SPEED_JUNCTION import Speed_Junction
from SPEED_ACCERATOR import Speed_Accelerator
from PLATOON_INTERSECTION import Platoon_Intersection
#from PLATOON_INTERSECTION_DIS_SPEED import Platoon_Intersection_dis_speed
import os
import sys
import optparse
import subprocess
import random
# we need to import python modules from the $SUMO_HOME/tools directory
try:
    sys.path.append(os.path.join(os.path.dirname(
        __file__), '..', '..', '..', '..', "tools"))  # tutorial in tests
    sys.path.append(os.path.join(os.environ.get("SUMO_HOME", os.path.join(
        os.path.dirname(__file__), "..", "..", "..")), "tools"))  # tutorial in docs
    from sumolib import checkBinary  # noqa\

    
except ImportError:
    sys.exit(
        "please declare environment variable 'SUMO_HOME' as the root directory of your sumo installation (it should contain folders 'bin', 'tools' and 'docs')")

import traci

def run():	
    #generator(2);
    step=0;
    length=215;
    v_max=20;#m/s
    debugs=0
    t0=0;
    tn=0;
    ncar=0;
    x=list();
    for i in range(19):#初始化交叉口;  
        traci.trafficlight.setPhase("0",0)
        traci.simulationStep()
        step=step+1
    while step<1000:
        for i in range(1):           
            traci.trafficlight.setPhase("0",0)
            traci.simulationStep()
            step=step+1
    #获取交叉口车辆的信息
            IDList =  #得到所有vehicle 的ID
            Platoon_Intersection(IDList) 
#输入部分
        case0 = Input()
        IDList = traci.vehicle.getIDList() 
        case0 = Input_Addtional(IDList)
        
        IDList_result=get_list(IDList)
        n2=IDList_result[0];n1=IDList_result[1];      
        e2=IDList_result[2];e1=IDList_result[3];
        s2=IDList_result[4];s1=IDList_result[5];
        w2=IDList_result[6];w1=IDList_result[7];
        print("step-%i"%step)
        print("case0.n")
        print(case0.n)
        print("case0.v")
        print(case0.v)
        print("case0.d")
        print(case0.d)        
      
      
        optimize_result=optimize_av(case0)
        print("cycle")
        print(optimize_result.cycle)
        print("csta")
        print(optimize_result.csta)
        print("cphi")
        print(optimize_result.cphi)        
        
#得到距离D、初速度V0、末速度Vn、加速度a;        
        temp=Speed_Accelerator(optimize_result,IDList)
        D=temp[0];V0=temp[1];Vn=temp[2];a=temp[3]
        car_accord=[0,0,0,0,0,0,0,0]; 
        if n2!=[]:
            car_accord[0]=n2[0]
        if n1!=[]:
            car_accord[1]=n1[0]
            
        if e2!=[]:
            car_accord[2]=e2[0]
        if e1!=[]:
            car_accord[3]=e1[0]
                
        if s2!=[]:
            car_accord[4]=s2[0]
        if s1!=[]:
            car_accord[5]=s1[0]
                
        if w2!=[]:
            car_accord[6]=w2[0]
        if w1!=[]:
            car_accord[7]=w1[0]
#####################################################
        Cycle=int(optimize_result.cycle)#0~Cycle
        S=optimize_result.csta #八个方向的开始时间；
        P=optimize_result.cphi#八个方向的持续时间；
        for tt in range(Cycle):
            Binary=[0,0,0,0,0,0,0,0];
            for i in range(8):
                if(S[i]<=tt and S[i]+P[i]>tt):
                    Binary[i]=1
                else:
                    Binary[i]=0                        
            signal_temp=0;
            for i in range(8):
                signal_temp=signal_temp+(2**(7-i))*Binary[i]             
            traci.trafficlight.setPhase("0",signal_temp)  
            if n2!=[]:   
                if car_accord[0]==n2[0] and traci.vehicle.getDistance(n2[0])<185:
                    traci.vehicle.setSpeed(n2[0], Vn[0])   
                    traci.vehicle.setAccel(n2[0], a[0])
                    traci.vehicle.setDecel(n2[0], a[0])   
                if car_accord[0]==n2[0] and traci.vehicle.getDistance(n2[0])>=185:
                    traci.vehicle.setSpeed(n2[0], 20)   
                    traci.vehicle.setAccel(n2[0], 5)
                    traci.vehicle.setDecel(n2[0], 5)
            
            		
            if n1!=[]:   
                if car_accord[1]==n1[0] and traci.vehicle.getDistance(n1[0])<185:
                    traci.vehicle.setSpeed(n1[0], Vn[1])   
                    traci.vehicle.setAccel(n1[0], a[1])
                    traci.vehicle.setDecel(n1[0], a[1]) 
                if car_accord[1]==n1[0] and traci.vehicle.getDistance(n1[0])>=185:
                    traci.vehicle.setSpeed(n1[0], 20)   
                    traci.vehicle.setAccel(n1[0], 5)
                    traci.vehicle.setDecel(n1[0], 5)		
            		
            		
            				
            if e2!=[]:
                if car_accord[2]==e2[0] and traci.vehicle.getDistance(e2[0])<185:
                    traci.vehicle.setSpeed(e2[0], Vn[2])   
                    traci.vehicle.setAccel(e2[0], a[2])
                    traci.vehicle.setDecel(e2[0], a[2]) 
                if car_accord[2]==e2[0] and traci.vehicle.getDistance(e2[0])>=185:
                    traci.vehicle.setSpeed(e2[0], 20)   
                    traci.vehicle.setAccel(e2[0], 5)
                    traci.vehicle.setDecel(e2[0], 5)		
            		
            		
            if e1!=[]:
                if car_accord[3]==e1[0] and traci.vehicle.getDistance(e1[0])<185:    
                    traci.vehicle.setSpeed(e1[0], Vn[3])   
                    traci.vehicle.setAccel(e1[0], a[3])
                    traci.vehicle.setDecel(e1[0], a[3]) 
                if car_accord[3]==e1[0] and traci.vehicle.getDistance(e1[0])>=185:    
                    traci.vehicle.setSpeed(e1[0], 20)   
                    traci.vehicle.setAccel(e1[0], 5)
                    traci.vehicle.setDecel(e1[0], 5)		
            						
            		
            if s2!=[]:    
                if car_accord[4]==s2[0] and traci.vehicle.getDistance(s2[0])<185:
                    traci.vehicle.setSpeed(s2[0], Vn[4])   
                    traci.vehicle.setAccel(s2[0], a[4])
                    traci.vehicle.setDecel(s2[0], a[4]) 
                if car_accord[4]==s2[0] and traci.vehicle.getDistance(s2[0])>=185:
                    traci.vehicle.setSpeed(s2[0], 20)   
                    traci.vehicle.setAccel(s2[0], 5)
                    traci.vehicle.setDecel(s2[0], 5)		
            						
            		
            if s1!=[]:
                if car_accord[5]==s1[0] and traci.vehicle.getDistance(s1[0])<185:
                    traci.vehicle.setSpeed(s1[0], Vn[5])   
                    traci.vehicle.setAccel(s1[0], a[5])
                    traci.vehicle.setDecel(s1[0], a[5]) 
                if car_accord[5]==s1[0] and traci.vehicle.getDistance(s1[0])>=185:
                    traci.vehicle.setSpeed(s1[0], 20)   
                    traci.vehicle.setAccel(s1[0], 5)
                    traci.vehicle.setDecel(s1[0], 5) 		
            		
            				
            if w2!=[]:    
                if car_accord[6]==w2[0] and traci.vehicle.getDistance(w2[0])<185:
                    traci.vehicle.setSpeed(w2[0], Vn[6])   
                    traci.vehicle.setAccel(w2[0], a[6])
                    traci.vehicle.setDecel(w2[0], a[6]) 
                if car_accord[6]==w2[0] and traci.vehicle.getDistance(w2[0])>=185:
                    traci.vehicle.setSpeed(w2[0], 20)   
                    traci.vehicle.setAccel(w2[0], 5)
                    traci.vehicle.setDecel(w2[0], 5)		
            				
            		
            if w1!=[]:
                if car_accord[7]==w1[0] and traci.vehicle.getDistance(w1[0])<185:
                    traci.vehicle.setSpeed(w1[0], Vn[7])   
                    traci.vehicle.setAccel(w1[0], a[7])
                    traci.vehicle.setDecel(w1[0], a[7])
                if car_accord[7]==w1[0] and traci.vehicle.getDistance(w1[0])>=185:
                    traci.vehicle.setSpeed(w1[0], 20)   
                    traci.vehicle.setAccel(w1[0], 5)
                    traci.vehicle.setDecel(w1[0], 5)				  
#            if n2!=[]:   
#                if car_accord[0]==n2[0] and traci.vehicle.getDistance(n2[0])<300:
#                    traci.vehicle.setSpeed(n2[0], Vn[0])   
#                    traci.vehicle.setAccel(n2[0], a[0])
#                    traci.vehicle.setDecel(n2[0], a[0])                       
#            if n1!=[]:   
#                if car_accord[1]==n1[0] and traci.vehicle.getDistance(n1[0])<300:
#                    traci.vehicle.setSpeed(n1[0], Vn[1])   
#                    traci.vehicle.setAccel(n1[0], a[1])
#                    traci.vehicle.setDecel(n1[0], a[1]) 
#            if e2!=[]:
#                if car_accord[2]==e2[0] and traci.vehicle.getDistance(e2[0])<300:
#                    traci.vehicle.setSpeed(e2[0], Vn[2])   
#                    traci.vehicle.setAccel(e2[0], a[2])
#                    traci.vehicle.setDecel(e2[0], a[2]) 
#            if e1!=[]:
#                if car_accord[3]==e1[0] and traci.vehicle.getDistance(e1[0])<300:    
#                    traci.vehicle.setSpeed(e1[0], Vn[3])   
#                    traci.vehicle.setAccel(e1[0], a[3])
#                    traci.vehicle.setDecel(e1[0], a[3]) 
#            if s2!=[]:    
#                if car_accord[4]==s2[0] and traci.vehicle.getDistance(s2[0])<300:
#                    traci.vehicle.setSpeed(s2[0], Vn[4])   
#                    traci.vehicle.setAccel(s2[0], a[4])
#                    traci.vehicle.setDecel(s2[0], a[4]) 
#            if s1!=[]:
#                if car_accord[5]==s1[0] and traci.vehicle.getDistance(s1[0])<300:
#                    traci.vehicle.setSpeed(s1[0], Vn[5])   
#                    traci.vehicle.setAccel(s1[0], a[5])
#                    traci.vehicle.setDecel(s1[0], a[5]) 
#            if w2!=[]:    
#                if car_accord[6]==w2[0] and traci.vehicle.getDistance(w2[0])<300:
#                    traci.vehicle.setSpeed(w2[0], Vn[6])   
#                    traci.vehicle.setAccel(w2[0], a[6])
#                    traci.vehicle.setDecel(w2[0], a[6]) 
#            if w1!=[]:
#                if car_accord[7]==w1[0] and traci.vehicle.getDistance(w1[0])<300:
#                    traci.vehicle.setSpeed(w1[0], Vn[7])   
#                    traci.vehicle.setAccel(w1[0], a[7])
#                    traci.vehicle.setDecel(w1[0], a[7])                                                     

            

            Platoon_Intersection(IDList)            
            IDList = traci.vehicle.getIDList()
            
            
            IDList_result=get_list_II(IDList)            
            n2=IDList_result[0];n1=IDList_result[1];      
            e2=IDList_result[2];e1=IDList_result[3];
            s2=IDList_result[4];s1=IDList_result[5];
            w2=IDList_result[6];w1=IDList_result[7];
            
            #Platoon_Intersection(IDList)
            
            #IDList_result=get_list(IDList)        
#            IDList = traci.vehicle.getIDList()
#            Speed_Junction(IDList)                      
    traci.close()
    sys.stdout.flush()
def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options
# this is the main entry point of this script
if __name__ == "__main__":
    options = get_options()

    # this script has been called from the command line. It will start sumo as a
    # server, then connect and run
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')
    # this is the normal way of using traci. sumo is started as a
    # subprocess and then the python script connects and runs
    traci.start([sumoBinary, "-c", "data/intersection/intersection.sumocfg",
                             "--tripinfo-output", "tripinfo.xml"])
    run()
    delay=Get_Delay()
    print("delay")
    print(delay)