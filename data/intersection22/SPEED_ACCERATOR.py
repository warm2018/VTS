"""
控制函数
"""
from GET_LIST import get_list
import traci
length=150;
def Speed_Accelerator(optimize_result,IDList_result):
    n2=IDList_result[0];n1=IDList_result[1];      
    e2=IDList_result[2];e1=IDList_result[3];
    s2=IDList_result[4];s1=IDList_result[5];
    w2=IDList_result[6];w1=IDList_result[7];
    ex=10
    S = []
    P = []
    for value in optimize_result.csta: 
        S.append(value)
    for value in optimize_result.cphi:
        P.append(value)#八个方向的开始时间
    #控制信号灯；setPhase()
    #每个step进行一次的信号设置；
    #————————————控制车辆；
    dlen=[len(n2),len(n1),len(e2),len(e1),len(s2),len(s1),len(w2),len(w1)];
    D=[0,0,0,0,0,0,0,0];##         D为头车到停车线的距离
    V0=[0,0,0,0,0,0,0,0];######    头车的速度
    Vn=[0,0,0,0,0,0,0,0];## 
    a=[0,0,0,0,0,0,0,0]; #####
    if n2!=[]:
        D[0]=length-traci.vehicle.getLanePosition(n2[0]) + traci.vehicle.getLength(n2[0]) - traci.vehicle.getLength(n2[0])+ex
    if n1!=[]:
        D[1]=length-traci.vehicle.getLanePosition(n1[0]) + traci.vehicle.getLength(n1[0]) - traci.vehicle.getLength(n1[0])+ex
    if e2!=[]:
        D[2]=length-traci.vehicle.getLanePosition(e2[0]) + traci.vehicle.getLength(e2[0]) - traci.vehicle.getLength(e2[0])+ex
    if e1!=[]:
        D[3]=length-traci.vehicle.getLanePosition(e1[0]) + traci.vehicle.getLength(e1[0]) - traci.vehicle.getLength(e1[0])+ex
        
    if s2!=[]:
        D[4]=length-traci.vehicle.getLanePosition(s2[0]) + traci.vehicle.getLength(s2[0]) - traci.vehicle.getLength(s2[0])+ex
    if s1!=[]:
        D[5]=length-traci.vehicle.getLanePosition(s1[0]) + traci.vehicle.getLength(s1[0]) - traci.vehicle.getLength(s1[0])+ex
        
    if w2!=[]:
        D[6]=length-traci.vehicle.getLanePosition(w2[0]) + traci.vehicle.getLength(w2[0]) - traci.vehicle.getLength(w2[0])+ex
    if w1!=[]:
        D[7]=length-traci.vehicle.getLanePosition(w1[0]) + traci.vehicle.getLength(w1[0]) - traci.vehicle.getLength(w1[0])+ex
        
    if n2!=[]:
        V0[0]=traci.vehicle.getSpeed(n2[0])
    if n1!=[]:
        V0[1]=traci.vehicle.getSpeed(n1[0])            
    if e2!=[]:
        V0[2]=traci.vehicle.getSpeed(e2[0])####得到头车的速度和离停车线的距离
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
    daita[0]=daita[0]-2
    daita[1]=daita[1]
    daita[4]=daita[4]-2
    daita[6]=daita[6]
    daita[6]=daita[6]
    for i in range(8):
        if dlen[i]>0 and S[i]>0:###dlen 表示每个车道上的车辆数
            Vn[i]=float(D[i])/float(S[i])
            a[i]=abs(float((Vn[i]-V0[i]))/float(daita[i]))

            
    
#
#    car_accord=[0,0,0,0,0,0,0,0]; 
#    if n2!=[]:
#        car_accord[0]=n2[0]
#    if n1!=[]:
#        car_accord[1]=n1[0]
#        
#    if e2!=[]:
#        car_accord[2]=e2[0]
#    if e1!=[]:
#        car_accord[3]=e1[0]
#            
#    if s2!=[]:
#        car_accord[4]=s2[0]
#    if s1!=[]:
#        car_accord[5]=s1[0]
#            
#    if w2!=[]:
#        car_accord[6]=w2[0]
#    if w1!=[]:
#        car_accord[7]=w1[0]
    result=[D,V0,Vn,a]
    return result