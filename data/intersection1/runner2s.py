#zone2
from __future__ import absolute_import
from __future__ import print_function

from gurobipy import *
from CCAR import CAR_L
from CINPUT import Input
from optimiza_function import optimize_av
from CRESULT import Result
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
    from sumolib import checkBinary  # noqa
except ImportError:
    sys.exit(
        "please declare environment variable 'SUMO_HOME' as the root directory of your sumo installation (it should contain folders 'bin', 'tools' and 'docs')")

import traci
def run():	
    step=0;
    length=200;
    v_max=20;#m/s
    debugs=0
    #while traci.simulation.getMinExpectedNumber() > 0:
    for i in range(19):      
        traci.trafficlight.setPhase("0",0)
        traci.simulationStep()
        step=step+1
    while step<1000:
        traci.simulationStep()
        step=step+1
#        traci.trafficlight.setPhase("0",1)
####################################################################
###################################################################
        IDList = traci.vehicle.getIDList()
        n1=list();
        n2=list();
        e1=list();
        e2=list();	
        s1=list();
        s2=list();
        w1=list();
        w2=list();        
        for i in range(len(IDList)):
            if IDList[i].find("n1") != -1:
                n1.append(IDList[i])
            elif IDList[i].find("n2") != -1:
                n2.append(IDList[i])
            elif IDList[i].find("e1") != -1:
                e1.append(IDList[i])
            elif IDList[i].find("e2") != -1:
                e2.append(IDList[i])
            elif IDList[i].find("s1") != -1:
                s1.append(IDList[i])
            elif IDList[i].find("s2") != -1:
                s2.append(IDList[i])
            elif IDList[i].find("w1") != -1:
                w1.append(IDList[i])
            else:
                w2.append(IDList[i])# 获取每个进口道的车辆ID
        error=8.5
        Rlength=length-error
        if len(n1)>0:
            for i in range(len(n1)):
                if traci.vehicle.getDistance(n1[i])>200-error:
                    n1[i]=0
        if len(n2)>0:
            for i in range(len(n2)):
                if traci.vehicle.getDistance(n2[i])>200-error:
                    n2[i]=0
	
        if len(e1)>0:
            for i in range(len(e1)):
                if traci.vehicle.getDistance(e1[i])>200-error:
                    e1[i]=0	
        if len(e2)>0:
            for i in range(len(e2)):
                if traci.vehicle.getDistance(e2[i])>200-error:
                    e2[i]=0	

        if len(s1)>0:
            for i in range(len(s1)):
                if traci.vehicle.getDistance(s1[i])>200-error:
                    s1[i]=0	
        if len(s2)>0:
            for i in range(len(s2)):
                if traci.vehicle.getDistance(s2[i])>200-error:
                    s2[i]=0						
	
        if len(w1)>0:
            for i in range(len(w1)):
                if traci.vehicle.getDistance(w1[i])>200-error:
                    w1[i]=0	
        if len(w2)>0:
            for i in range(len(w2)):
                if traci.vehicle.getDistance(w2[i])>200-error:
                    w2[i]=0		

        for i in range(len(n1)-1,-1,-1):
            if(n1[i]==0):
                del n1[i]
				
        for i in range(len(n2)-1,-1,-1):
            if n2[i]==0:
                del n2[i]
				
        for i in range(len(e1)-1,-1,-1):
            if e1[i]==0:
                del e1[i]		
        for i in range(len(e2)-1,-1,-1):
            if e2[i]==0:
                del e2[i]
				
        for i in range(len(s1)-1,-1,-1):
            if s1[i]==0:
                del s1[i]		
        for i in range(len(s2)-1,-1,-1):
            if s2[i]==0:
                del s2[i]	
				
        for i in range(len(w1)-1,-1,-1):
            if w1[i]==0:
                del w1[i]		
        for i in range(len(w2)-1,-1,-1):
            if w2[i]==0:
                del w2[i]		       
        #去除数组中的重复元素;
        n1=sorted(set(n1),key=n1.index)
        n2=sorted(set(n2),key=n2.index)
        
        e1=sorted(set(e1),key=e1.index)
        e2=sorted(set(e2),key=e2.index)
        
        s1=sorted(set(s1),key=s1.index)
        s2=sorted(set(s2),key=s2.index)
        
        w1=sorted(set(w1),key=w1.index)
        w2=sorted(set(w2),key=w2.index)
###################################################################
###################################################################            
        dis_n1=list()
        dis_n2=list()
        dis_e1=list()
        dis_e2=list()
        dis_s1=list()
        dis_s2=list()
        dis_w1=list()
        dis_w2=list()
        for i in range(len(n1)):
            dis_n1.append(int(traci.vehicle.getDistance(n1[i]))	)
        #print(dis_n1)
        for i in range(len(n2)):
            dis_n2.append(int(traci.vehicle.getDistance(n2[i])))
        for i in range(len(e1)):
            dis_e1.append(int(traci.vehicle.getDistance(e1[i])))
        for i in range(len(e2)):
            dis_e2.append(int(traci.vehicle.getDistance(e2[i])))
        for i in range(len(s1)):
            dis_s1.append(int(traci.vehicle.getDistance(s1[i])))
        for i in range(len(s2)):
            dis_s2.append(int(traci.vehicle.getDistance(s2[i])))
        for i in range(len(w1)):
            dis_w1.append(int(traci.vehicle.getDistance(w1[i])))
        for i in range(len(w2)):
            dis_w2.append(int(traci.vehicle.getDistance(w2[i]))	)			

################################################################################
################################################################################
#____________________________________________1输入部分___________________________
        case0=Input()
        case0.d=[ [0,0],[0,0],[0,0],[0,0] ]
        case0.v=[ [0,0],[0,0],[0,0],[0,0] ]
        case0.n=  [ [0,0],[0,0],[0,0],[0,0] ]
        case0.dis=[ [0,0],[0,0],[0,0],[0,0] ]
#——————————判断各方向是否有车—————————————
###########################s1
        if s1==[]:
            case0.n[0][0]=0;
        else:
            case0.n[0][0]=traci.vehicle.getLength(s1[0])/5;
            case0.d[0][0]=int(200-traci.vehicle.getDistance(s1[0]))
            case0.v[0][0]=int(traci.vehicle.getSpeed(s1[0]))
            if case0.v[0][0]==0:
                case0.v[0][0]=1
###########################s2
        if s2==[]:
            case0.n[0][1]=0;
        else:
            case0.n[0][1]=traci.vehicle.getLength(s2[0])/5;
            case0.d[0][1]=200-int(traci.vehicle.getDistance(s2[0]))
            case0.v[0][1]=int(traci.vehicle.getSpeed(s2[0]))
            if case0.v[0][1]==0:
                case0.v[0][1]=1
###########################w1
        if w1==[]:
            case0.n[1][0]=0;
        else:
            case0.n[1][0]=traci.vehicle.getLength(w1[0])/5;
            case0.d[1][0]=200-int(traci.vehicle.getDistance(w1[0]))
            case0.v[1][0]=int(traci.vehicle.getSpeed(w1[0]))
            if case0.v[1][0]==0:
                case0.v[1][0]=1
###########################w2
        if w2==[]:
            case0.n[1][1]=0;
        else:
            case0.n[1][1]=traci.vehicle.getLength(w2[0])/5;
            case0.d[1][1]=200-int(traci.vehicle.getDistance(w2[0]))
            case0.v[1][1]=int(traci.vehicle.getSpeed(w2[0]))
            if case0.v[1][1]==0:
                case0.v[1][1]=1
        ###########################n1
        if n1==[]:
            case0.n[2][0]=0;
        else:
            case0.n[2][0]=traci.vehicle.getLength(n1[0])/5;
            case0.d[2][0]=200-int(traci.vehicle.getDistance(n1[0]))
            case0.v[2][0]=int(traci.vehicle.getSpeed(n1[0]))
            if case0.v[2][0]==0:
                case0.v[2][0]=1
        ###########################n2
        if n2==[]:
            case0.n[2][1]=0;
        else:
            case0.n[2][1]=traci.vehicle.getLength(n2[0])/5;
            case0.d[2][1]=200-int(traci.vehicle.getDistance(n2[0]))
            case0.v[2][1]=int(traci.vehicle.getSpeed(n2[0]))
            if case0.v[2][1]==0:
                case0.v[2][1]=1
        ###########################e1
        if e1==[]:
            case0.n[3][0]=0;
        else:
            case0.n[3][0]=traci.vehicle.getLength(e1[0])/5;
            case0.d[3][0]=200-int(traci.vehicle.getDistance(e1[0]))
            case0.v[3][0]=int(traci.vehicle.getSpeed(e1[0]))
            if case0.v[3][0]==0:
                case0.v[3][0]=1
        ###########################e2   
        if e2==[]:
            case0.n[3][1]=0;
        else:
            case0.n[3][1]=traci.vehicle.getLength(e2[0])/5;
            case0.d[3][1]=200-int(traci.vehicle.getDistance(e2[0]))
            case0.v[3][1]=int(traci.vehicle.getSpeed(e2[0]))     
            if case0.v[3][1]==0:
                case0.v[3][1]=1
        
        optimize_result=optimize_av(case0)
        debugs=debugs+1
        
#        #____________________________________________2输出部分___________________________        
#        #—————————信号控制；
        
        S=optimize_result.csta #八个方向的开始时间；
        P=optimize_result.cphi#八个方向的持续时间；    
        #控制信号灯；setPhase()
        #每个step进行一次的信号设置；
        #————————————控制车辆；
        dlen=[len(n2),len(n1),len(e2),len(e1),len(s2),len(s1),len(w2),len(w1)];
        D=[0,0,0,0,0,0,0,0];
        V0=[0,0,0,0,0,0,0,0];
        Vn=[0,0,0,0,0,0,0,0];
        a=[0,0,0,0,0,0,0,0];
        Rlength=215
        if n2!=[]:
            D[0]=Rlength-traci.vehicle.getDistance(n2[0])
        if n1!=[]:
            D[1]=Rlength-traci.vehicle.getDistance(n1[0])
        if e2!=[]:
            D[2]=Rlength-traci.vehicle.getDistance(e2[0])
        if e1!=[]:
            D[3]=Rlength-traci.vehicle.getDistance(e1[0])
            
        if s2!=[]:
            D[4]=Rlength-traci.vehicle.getDistance(s2[0])
        if s1!=[]:
            D[5]=Rlength-traci.vehicle.getDistance(s1[0])
            
        if w2!=[]:
            D[6]=Rlength-traci.vehicle.getDistance(w2[0])
        if w1!=[]:
            D[7]=Rlength-traci.vehicle.getDistance(w1[0])
            
        if n2!=[]:
            V0[0]=traci.vehicle.getSpeed(n2[0])
        if n1!=[]:
            V0[1]=traci.vehicle.getSpeed(n1[0])            
        if e2!=[]:
            V0[2]=traci.vehicle.getSpeed(e2[0])
        if e1!=[]:
            V0[3]=traci.vehicle.getSpeed(e1[0])
        if s2!=[]:
            V0[4]=traci.vehicle.getSpeed(s2[0])
        if s1!=[]:
            V0[5]=traci.vehicle.getSpeed(s1[0])
        if w2!=[]:
            V0[6]=traci.vehicle.getSpeed(w2[0])
        if w1!=[]:
            V0[7]=traci.vehicle.getSpeed(w1[0])
        daita=S
        for i in range(8):
            if dlen[i]>0 and S[i]>0:
                Vn[i]=2*float(D[i])/float(S[i])-V0[i]
                a[i]=abs(float((Vn[i]-V0[i]))/float(S[i]))

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
        
        print("step0")
        print(step)

#####################################################
        Cycle=int(optimize_result.cycle)#0~Cycle
        print(Cycle)
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
                if car_accord[0]==n2[0] and traci.vehicle.getDistance(n2[0])<300:
                    traci.vehicle.setSpeed(n2[0], Vn[0])   
                    traci.vehicle.setAccel(n2[0], a[0])
                    traci.vehicle.setDecel(n2[0], a[0]) 
            if n1!=[]:   
                if car_accord[1]==n1[0] and traci.vehicle.getDistance(n1[0])<300:
                    traci.vehicle.setSpeed(n1[0], Vn[1])   
                    traci.vehicle.setAccel(n1[0], a[1])
                    traci.vehicle.setDecel(n1[0], a[1]) 
            if e2!=[]:
                if car_accord[2]==e2[0] and traci.vehicle.getDistance(e2[0])<300:
                    traci.vehicle.setSpeed(e2[0], Vn[2])   
                    traci.vehicle.setAccel(e2[0], a[2])
                    traci.vehicle.setDecel(e2[0], a[2]) 
            if e1!=[]:
                if car_accord[3]==e1[0] and traci.vehicle.getDistance(e1[0])<300:    
                    traci.vehicle.setSpeed(e1[0], Vn[3])   
                    traci.vehicle.setAccel(e1[0], a[3])
                    traci.vehicle.setDecel(e1[0], a[3]) 
            if s2!=[]:    
                if car_accord[4]==s2[0] and traci.vehicle.getDistance(s2[0])<300:
                    traci.vehicle.setSpeed(s2[0], Vn[4])   
                    traci.vehicle.setAccel(s2[0], a[4])
                    traci.vehicle.setDecel(s2[0], a[4]) 
            if s1!=[]:
                if car_accord[5]==s1[0] and traci.vehicle.getDistance(s1[0])<300:
                    traci.vehicle.setSpeed(s1[0], Vn[5])   
                    traci.vehicle.setAccel(s1[0], a[5])
                    traci.vehicle.setDecel(s1[0], a[5]) 
            if w2!=[]:    
                if car_accord[6]==w2[0] and traci.vehicle.getDistance(w2[0])<300:
                    traci.vehicle.setSpeed(w2[0], Vn[6])   
                    traci.vehicle.setAccel(w2[0], a[6])
                    traci.vehicle.setDecel(w2[0], a[6]) 
            if w1!=[]:
                if car_accord[7]==w1[0] and traci.vehicle.getDistance(w1[0])<300:
                    traci.vehicle.setSpeed(w1[0], Vn[7])   
                    traci.vehicle.setAccel(w1[0], a[7])
                    traci.vehicle.setDecel(w1[0], a[7])                 
                                    
            tt=tt+1
            traci.simulationStep()       
            step=step+1;
####################################################################
###################################################################
            IDList = traci.vehicle.getIDList()
            n1=list();
            n2=list();
            e1=list();
            e2=list();	
            s1=list();
            s2=list();
            w1=list();
            w2=list();        
            for i in range(len(IDList)):
                if IDList[i].find("n1") != -1:
                    n1.append(IDList[i])
                elif IDList[i].find("n2") != -1:
                    n2.append(IDList[i])
                elif IDList[i].find("e1") != -1:
                    e1.append(IDList[i])
                elif IDList[i].find("e2") != -1:
                    e2.append(IDList[i])
                elif IDList[i].find("s1") != -1:
                    s1.append(IDList[i])
                elif IDList[i].find("s2") != -1:
                    s2.append(IDList[i])
                elif IDList[i].find("w1") != -1:
                    w1.append(IDList[i])
                else:
                    w2.append(IDList[i])
            error=8.5
            Rlength=length-error
            if len(n1)>0:
                for i in range(len(n1)):
                    if traci.vehicle.getDistance(n1[i])>200-error:
                        n1[i]=0					
            if len(n2)>0:
                for i in range(len(n2)):
                    if traci.vehicle.getDistance(n2[i])>200-error:
                        n2[i]=0
    	
            if len(e1)>0:
                for i in range(len(e1)):
                    if traci.vehicle.getDistance(e1[i])>200-error:
                        e1[i]=0	
            if len(e2)>0:
                for i in range(len(e2)):
                    if traci.vehicle.getDistance(e2[i])>200-error:
                        e2[i]=0	
    
            if len(s1)>0:
                for i in range(len(s1)):
                    if traci.vehicle.getDistance(s1[i])>200-error:
                        s1[i]=0	
            if len(s2)>0:
                for i in range(len(s2)):
                    if traci.vehicle.getDistance(s2[i])>200-error:
                        s2[i]=0						
    	
            if len(w1)>0:
                for i in range(len(w1)):
                    if traci.vehicle.getDistance(w1[i])>200-error:
                        w1[i]=0	
            if len(w2)>0:
                for i in range(len(w2)):
                    if traci.vehicle.getDistance(w2[i])>200-error:
                        w2[i]=0		
    
            for i in range(len(n1)-1,-1,-1):
                if(n1[i]==0):
                    del n1[i]
    				
            for i in range(len(n2)-1,-1,-1):
                if n2[i]==0:
                    del n2[i]
    				
            for i in range(len(e1)-1,-1,-1):
                if e1[i]==0:
                    del e1[i]		
            for i in range(len(e2)-1,-1,-1):
                if e2[i]==0:
                    del e2[i]
    				
            for i in range(len(s1)-1,-1,-1):
                if s1[i]==0:
                    del s1[i]		
            for i in range(len(s2)-1,-1,-1):
                if s2[i]==0:
                    del s2[i]	
    				
            for i in range(len(w1)-1,-1,-1):
                if w1[i]==0:
                    del w1[i]		
            for i in range(len(w2)-1,-1,-1):
                if w2[i]==0:
                    del w2[i]		       
            #去除数组中的重复元素;
            n1=sorted(set(n1),key=n1.index)
            n2=sorted(set(n2),key=n2.index)
            
            e1=sorted(set(e1),key=e1.index)
            e2=sorted(set(e2),key=e2.index)
            
            s1=sorted(set(s1),key=s1.index)
            s2=sorted(set(s2),key=s2.index)
            
            w1=sorted(set(w1),key=w1.index)
            w2=sorted(set(w2),key=w2.index)             
#        if debugs>=2:        
#            exit();
###################################################################
###################################################################                                     
            #continue
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
    traci.start([sumoBinary, "-c", "data/cross.sumocfg",
                             "--tripinfo-output", "tripinfo.xml"])
    run()
