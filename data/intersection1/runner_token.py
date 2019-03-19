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
    length=215;
    v_max=20;#m/s
    debugs=0
    t0=[0,0,0,0,0,0,0,0];
    tn=[0,0,0,0,0,0,0,0];
    ncar=[0,0,0,0,0,0,0,0];
    x=[[],[],[],[],[],[],[],[]];   
    while step<1000:
        traci.simulationStep()
        step=step+1
#########————————————获取交叉口车辆的信息———————————######################
        IDList = traci.vehicle.getIDList()
        n1=list();
        n2=list();
        e1=list();
        e2=list();	
        s1=list();
        s2=list();
        w1=list();
        w2=list();        
        for i in range(len(IDList)):#对所有的车辆ID进行遍历
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
        #find the number of the vehicles in every lane

        error=8.5
        if len(n1)>0:
            for i in range(len(n1)):
                if traci.vehicle.getDistance(n1[i])>200-error:
                    n1[i]=0	#if the vehicle is too far from the intersection  ,it will be deleted 				
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
###########################################
        for i in range(len(n1)-1,-1,-1):
            if(n1[i]==0):
                del n1[i]
#delete the 0 element  found in above step  inn the list 
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
        n1=sorted(n1,key=lambda x:int(x[3:]))
        n2=sorted(n2,key=lambda x:int(x[3:]))
        e1=sorted(e1,key=lambda x:int(x[3:]))
        e2=sorted(e2,key=lambda x:int(x[3:]))
        s1=sorted(s1,key=lambda x:int(x[3:]))
        s2=sorted(s2,key=lambda x:int(x[3:]))
        w1=sorted(w1,key=lambda x:int(x[3:]))
        w2=sorted(w2,key=lambda x:int(x[3:]))
        #lambda function is used to describe the rules to operate list or turtle
###################################
        ##############################
#arm1-2[s2]~4
        if len(s2)>0 and s2[-1] not in x[4] and step<500:
            t0[4]=t0[4]+step#t0 is to describe the 
            x[4].append(s2[-1])##the last vehicle list at every step 
            ncar[4]=ncar[4]+1#如果某个车道的车辆数大于0，且最后一辆车不在x[4]这个；列表里面，则可以进信不过操作
        if len(x[4])>0:
            if traci.vehicle.getDistance(x[4][0])>300:
                tn[4]=tn[4]+step;
                x[4].remove(x[4][0])    
            #每一个step更新一次;如果车辆的距离大于300m，则将其从列表中
     #arm1-1[s1]~5
        if len(s1)>0 and s1[-1] not in x[5] and step<500:
            t0[5]=t0[5]+step
            x[5].append(s1[-1])
            ncar[5]=ncar[5]+1
        if len(x[5])>0:
            if traci.vehicle.getDistance(x[5][0])>300:
                tn[5]=tn[5]+step;
                x[5].remove(x[5][0])
        		
        #arm2-1[w1]~7
        if len(w1)>0 and w1[-1] not in x[7] and step<500:
            t0[7]=t0[7]+step
            x[7].append(w1[-1])
            ncar[7]=ncar[7]+1
        if len(x[7])>0:
            if traci.vehicle.getDistance(x[7][0])>300:
                tn[7]=tn[7]+step;
                x[7].remove(x[7][0])		
        		
        #arm2-2[w2]~6
        if len(w2)>0 and w2[-1] not in x[6] and step<500:
            t0[6]=t0[6]+step
            x[6].append(w2[-1])
            ncar[6]=ncar[6]+1
        if len(x[6])>0:
            if traci.vehicle.getDistance(x[6][0])>300:
                tn[6]=tn[6]+step;
                x[6].remove(x[6][0])		
        
        #arm3-1[n1]~1
        if len(n1)>0 and n1[-1] not in x[1] and step<500:
            t0[1]=t0[1]+step
            x[1].append(n1[-1])
            ncar[1]=ncar[1]+1
        if len(x[1])>0:
            if traci.vehicle.getDistance(x[1][0])>300:
                tn[1]=tn[1]+step;
                x[1].remove(x[1][0])
        
        #arm3-2[n2]~0
        if len(n2)>0 and n2[-1] not in x[0] and step<500:
            t0[0]=t0[0]+step
            x[0].append(n2[-1])
            ncar[0]=ncar[0]+1
        if len(x[0])>0:
            for i in range(len(x[0])):
                if traci.vehicle.getDistance(x[0][i])>300:
                    tn[0]=tn[0]+step;
                    x[0].remove(x[0][i])

        #arm4-1[s1]~3
        if len(s1)>0 and s1[-1] not in x[3] and step<500:
            t0[3]=t0[3]+step
            x[3].append(s1[-1])
            ncar[3]=ncar[3]+1
        if len(x[3])>0:
            if traci.vehicle.getDistance(x[3][0])>300:
                tn[3]=tn[3]+step;
                x[3].remove(x[3][0])
        
        
        #arm4-2[s2]~2
        if len(s2)>0 and s2[-1] not in x[2] and step<500:
            t0[2]=t0[2]+step
            x[2].append(s2[-1])
            ncar[2]=ncar[2]+1
        if len(x[2])>0:
            if traci.vehicle.getDistance(x[2][0])>300:
                tn[2]=tn[2]+step;
                x[2].remove(x[2][0])        
        
        ###############################
###################################        
        
        
        
        
#____________________________________________1输入部分___________________________
        case0=Input()
        case0.d=[ [0,0],[0,0],[0,0],[0,0] ]
        case0.v=[ [0,0],[0,0],[0,0],[0,0] ]
        case0.n=  [ [0,0],[0,0],[0,0],[0,0] ]
        case0.dis=[ [0,0],[0,0],[0,0],[0,0] ]
#——————————判断各方向是否有车—————————————
###########################s1
        ex=10        
        if s1==[]:
            case0.n[0][0]=0;
        else:
            case0.n[0][0]=int(traci.vehicle.getLength(s1[0])/10)+2;
            case0.d[0][0]=length-traci.vehicle.getDistance(s1[0])-traci.vehicle.getLength(s1[0])+ex
            case0.v[0][0]=traci.vehicle.getSpeed(s1[0])
            if case0.v[0][0]<=1:
                case0.v[0][0]=1
###########################s2
        if s2==[]:
            case0.n[0][1]=0;
        else:
            case0.n[0][1]=int(traci.vehicle.getLength(s2[0])/10)+2;
            case0.d[0][1]=length-traci.vehicle.getDistance(s2[0])-traci.vehicle.getLength(s2[0])
            case0.v[0][1]=traci.vehicle.getSpeed(s2[0])
            if case0.v[0][1]<=1:
                case0.v[0][1]=1
###########################w1
        if w1==[]:
            case0.n[1][0]=0;
        else:
            case0.n[1][0]=int(traci.vehicle.getLength(w1[0])/15)+2;
            case0.d[1][0]=length-traci.vehicle.getDistance(w1[0])-traci.vehicle.getLength(w1[0])
            case0.v[1][0]=traci.vehicle.getSpeed(w1[0])
            if case0.v[1][0]<=1:
                case0.v[1][0]=1
###########################w2
        if w2==[]:
            case0.n[1][1]=0;
        else:
            case0.n[1][1]=int(traci.vehicle.getLength(w2[0])/15)+2;
            case0.d[1][1]=length-traci.vehicle.getDistance(w2[0])-traci.vehicle.getLength(w2[0])
            case0.v[1][1]=traci.vehicle.getSpeed(w2[0])
            if case0.v[1][1]<=1:
                case0.v[1][1]=1
        ###########################n1
        if n1==[]:
            case0.n[2][0]=0;
        else:
            case0.n[2][0]=int(traci.vehicle.getLength(n1[0])/15)+2;
            case0.d[2][0]=length-traci.vehicle.getDistance(n1[0])-traci.vehicle.getLength(n1[0])
            case0.v[2][0]=traci.vehicle.getSpeed(n1[0])
            if case0.v[2][0]<=1:
                case0.v[2][0]=1
        ###########################n2
        if n2==[]:
            case0.n[2][1]=0;
        else:
            case0.n[2][1]=int(traci.vehicle.getLength(n2[0])/15)+2;
            case0.d[2][1]=length-traci.vehicle.getDistance(n2[0])-traci.vehicle.getLength(n2[0])
            case0.v[2][1]=traci.vehicle.getSpeed(n2[0])
            if case0.v[2][1]<=1:
                case0.v[2][1]=1
        ###########################e1
        if e1==[]:
            case0.n[3][0]=0;
        else:
            case0.n[3][0]=int(traci.vehicle.getLength(e1[0])/15)+2;
            case0.d[3][0]=length-traci.vehicle.getDistance(e1[0])-traci.vehicle.getLength(e1[0])
            case0.v[3][0]=traci.vehicle.getSpeed(e1[0])
            if case0.v[3][0]<=1:
                case0.v[3][0]=1
        ###########################e2   
        if e2==[]:
            case0.n[3][1]=0;
        else:
            case0.n[3][1]=int(traci.vehicle.getLength(e2[0])/15)+2;
            case0.d[3][1]=length-traci.vehicle.getDistance(e2[0])-traci.vehicle.getLength(e2[0])
            case0.v[3][1]=traci.vehicle.getSpeed(e2[0])  
            if case0.v[3][1]<=1:
                case0.v[3][1]=1
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #s2[0][1]        
        temp_s2=0
        if len(s2)>=2:
            len_s2=len(s2);
            temp_s2=0;
            for i in range(len_s2-1):
                if (traci.vehicle.getDistance(s2[i])-traci.vehicle.getDistance(s2[i+1])-traci.vehicle.getLength(s2[i+1]))<=15:
                    temp_s2=temp_s2+1;
        case0.n[0][1]=case0.n[0][1]+temp_s2       
        #s1[0][0] 
        temp_s1=0
        if len(s1)>=2:
            len_s1=len(s1);
            temp_s1=0;
            for i in range(len_s1-1):
                if (traci.vehicle.getDistance(s1[i])-traci.vehicle.getDistance(s1[i+1])-traci.vehicle.getLength(s1[i+1]))<=15:
                    temp_s1=temp_s1+1;
        case0.n[0][0]=case0.n[0][0]+temp_s1
        #w1[1][0]
        temp_w1=0
        if len(w1)>=2:
            len_w1=len(w1);
            temp_w1=0;
            for i in range(len_w1-1):
                if (traci.vehicle.getDistance(w1[i])-traci.vehicle.getDistance(w1[i+1])-traci.vehicle.getLength(w1[i+1]))<=15:
                    temp_w1=temp_w1+1;
        case0.n[1][0]=case0.n[1][0]+temp_w1
        #w2[1][1]
        temp_w2=0
        if len(w2)>=2:
            len_w2=len(w2);
            temp_w2=0;
            for i in range(len_w2-1):
                if (traci.vehicle.getDistance(w2[i])-traci.vehicle.getDistance(w2[i+1])-traci.vehicle.getLength(w2[i+1]))<=15:
                    temp_w2=temp_w2+1;
        case0.n[1][1]=case0.n[1][1]+temp_w2        
        #n1[2][0]
        temp_n1=0
        if len(n1)>=2:
            len_n1=len(n1);
            temp_n1=0;
            for i in range(len_n1-1):
                if (traci.vehicle.getDistance(n1[i])-traci.vehicle.getDistance(n1[i+1])-traci.vehicle.getLength(n1[i+1]))<=15:
                    temp_n1=temp_n1+1;
        case0.n[2][0]=case0.n[2][0]+temp_n1
        #n2[2][1]
        temp_n2=0
        if len(n2)>=2:
            len_n2=len(n2);
            temp_n2=0;
            for i in range(len_n2-1):
                if (traci.vehicle.getDistance(n2[i])-traci.vehicle.getDistance(n2[i+1])-traci.vehicle.getLength(n2[i+1]))<=15:
                    temp_n2=temp_n2+1;
        case0.n[2][1]=case0.n[2][1]+temp_n2
        #e1[3][0]
        temp_e1=0
        if len(e1)>=2:
            len_e1=len(e1);
            temp_e1=0;
            for i in range(len_e1-1):
                if (traci.vehicle.getDistance(e1[i])-traci.vehicle.getDistance(e1[i+1])-traci.vehicle.getLength(e1[i+1]))<=15:
                    temp_e1=temp_e1+1;
        case0.n[3][0]=case0.n[3][0]+temp_e1
        #e2[3][1]
        temp_e2=0
        if len(e2)>=2:
            len_e2=len(e2);
            temp_e2=0;
            for i in range(len_e2-1):
                if (traci.vehicle.getDistance(e2[i])-traci.vehicle.getDistance(e2[i+1])-traci.vehicle.getLength(e2[i+1]))<=15:
                    temp_e2=temp_e2+1;
        case0.n[3][1]=case0.n[3][1]+temp_e2
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        optimize_result=optimize_av(case0)
#        debugs=debugs+1
        ##every step optimiazation ??????
#        #____________________________________________2输出部分___________________________        
#        #—————————信号控制；
        ex=10
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
        if n2!=[]:   # the distance - length   why? 头车的距离减去头车的长度
            D[0]=length-traci.vehicle.getDistance(n2[0])-traci.vehicle.getLength(n2[0])+ex
        if n1!=[]:
            D[1]=length-traci.vehicle.getDistance(n1[0])-traci.vehicle.getLength(n1[0])+ex
        if e2!=[]:
            D[2]=length-traci.vehicle.getDistance(e2[0])-traci.vehicle.getLength(e2[0])+ex
        if e1!=[]:
            D[3]=length-traci.vehicle.getDistance(e1[0])-traci.vehicle.getLength(e1[0])+ex
            
        if s2!=[]:
            D[4]=length-traci.vehicle.getDistance(s2[0])-traci.vehicle.getLength(s2[0])+ex-15
        if s1!=[]:
            D[5]=length-traci.vehicle.getDistance(s1[0])-traci.vehicle.getLength(s1[0])+ex 
        if w2!=[]:
            D[6]=length-traci.vehicle.getDistance(w2[0])-traci.vehicle.getLength(w2[0])+ex
        if w1!=[]:
            D[7]=length-traci.vehicle.getDistance(w1[0])-traci.vehicle.getLength(w1[0])+ex
    ##
        if n2!=[]:
            V0[0]=traci.vehicle.getSpeed(n2[0]) #n2表示北进口的直行，0
        if n1!=[]:
            V0[1]=traci.vehicle.getSpeed(n1[0]) #n1表示北进口的左转
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
        daita=S###绿灯开始时间
        for i in range(8):
            if dlen[i]>0 and S[i]>0:
                Vn[i]=2*float(D[i])/float(S[i])-V0[i]
                a[i]=abs(float((Vn[i]-V0[i]))/float(S[i]))##

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
            if len(s2)>0 and s2[-1] not in x[4] and step<500:
                t0[4]=t0[4]+step
                x[4].append(s2[-1])
                ncar[4]=ncar[4]+1
            if len(x[4])>0:
                if traci.vehicle.getDistance(x[4][0])>300:
                    tn[4]=tn[4]+step;
                    x[4].remove(x[4][0])         
            #arm1-1[s1]~5
            if len(s1)>0 and s1[-1] not in x[5] and step<500:
                t0[5]=t0[5]+step
                x[5].append(s1[-1])
                ncar[5]=ncar[5]+1
            if len(x[5])>0:
                if traci.vehicle.getDistance(x[5][0])>300:
                    tn[5]=tn[5]+step;
                    x[5].remove(x[5][0])
            		
            #arm2-1[w1]~7
            if len(w1)>0 and w1[-1] not in x[7] and step<500:
                t0[7]=t0[7]+step
                x[7].append(w1[-1])
                ncar[7]=ncar[7]+1
            if len(x[7])>0:
                if traci.vehicle.getDistance(x[7][0])>300:
                    tn[7]=tn[7]+step;
                    x[7].remove(x[7][0])		
            		
            #arm2-2[w2]~6
            if len(w2)>0 and w2[-1] not in x[6] and step<500:
                t0[6]=t0[6]+step
                x[6].append(w2[-1])
                ncar[6]=ncar[6]+1
            if len(x[6])>0:
                if traci.vehicle.getDistance(x[6][0])>300:
                    tn[6]=tn[6]+step;
                    x[6].remove(x[6][0])		
            
            #arm3-1[n1]~1
            if len(n1)>0 and n1[-1] not in x[1] and step<500:
                t0[1]=t0[1]+step
                x[1].append(n1[-1])
                ncar[1]=ncar[1]+1
            if len(x[1])>0:
                if traci.vehicle.getDistance(x[1][0])>300:
                    tn[1]=tn[1]+step;
                    x[1].remove(x[1][0])
            
            #arm3-2[n2]~0
            if len(n2)>0 and n2[-1] not in x[0] and step<500:
                t0[0]=t0[0]+step
                x[0].append(n2[-1])
                ncar[0]=ncar[0]+1
            if len(x[0])>0:
                print("len(x[0])")
                print(len(x[0]))
                for i in range(len(x[0])):
                    print("i=%i"%i)
                    if traci.vehicle.getDistance(x[0][i])>300:
                        tn[0]=tn[0]+step;
                        x[0].remove(x[0][i])          
            #arm4-1[s1]~3
            if len(s1)>0 and s1[-1] not in x[3] and step<500:
                t0[3]=t0[3]+step
                x[3].append(s1[-1])
                ncar[3]=ncar[3]+1
            if len(x[3])>0:
                if traci.vehicle.getDistance(x[3][0])>300:
                    tn[3]=tn[3]+step;
                    x[3].remove(x[3][0])
            
            
            #arm4-2[s2]~2
            if len(s2)>0 and s2[-1] not in x[2] and step<500:
                t0[2]=t0[2]+step
                x[2].append(s2[-1])
                ncar[2]=ncar[2]+1
            if len(x[2])>0:
                if traci.vehicle.getDistance(x[2][0])>300:
                    tn[2]=tn[2]+step;
                    x[2].remove(x[2][0])            

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