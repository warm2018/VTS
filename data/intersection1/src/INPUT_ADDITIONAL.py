from CINPUT import Input
from GET_LIST import get_list
import traci


def Input_Addtional(IDList_result,Platoon_length):
    length=150;
    n2=IDList_result[0];n1=IDList_result[1];      
    e2=IDList_result[2];e1=IDList_result[3];
    s2=IDList_result[4];s1=IDList_result[5];
    w2=IDList_result[6];w1=IDList_result[7];
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
        case0.n[0][0]=int(float(Platoon_length[5])/5);
        case0.d[0][0]=length-traci.vehicle.getLanePosition(s1[0])-traci.vehicle.getLength(s1[0])+ex
        case0.v[0][0]=traci.vehicle.getSpeed(s1[0])
        if case0.v[0][0] <= 1:
            case0.v[0][0] = 1
        if case0.d[0][0] < 1:
            case0.d[0][0] = 1
###########################s2
    if s2==[]:
        case0.n[0][1]=0;
    else:
        case0.n[0][1]=int(float(Platoon_length[4])/5);
        case0.d[0][1]=length-traci.vehicle.getLanePosition(s2[0])-traci.vehicle.getLength(s2[0])
        case0.v[0][1]=traci.vehicle.getSpeed(s2[0])
        if case0.v[0][1]<=1:
            case0.v[0][1]=1
        if case0.d[0][1]<1:
            case0.d[0][1]=1
###########################w1
    if w1==[]:
        case0.n[1][0]=0;
    else:
        case0.n[1][0]=int(float(Platoon_length[7])/5);
        case0.d[1][0]=length-traci.vehicle.getLanePosition(w1[0])-traci.vehicle.getLength(w1[0])
        case0.v[1][0]=traci.vehicle.getSpeed(w1[0])
        if case0.v[1][0]<=1:
            case0.v[1][0]=1
        if case0.d[1][0]<1:
            case0.d[1][0]=1
###########################w2
    if w2==[]:
        case0.n[1][1]=0;
    else:
        case0.n[1][1]=int(float(Platoon_length[6])/5);
        case0.d[1][1]=length-traci.vehicle.getLanePosition(w2[0])-traci.vehicle.getLength(w2[0])
        case0.v[1][1]=traci.vehicle.getSpeed(w2[0])
        if case0.v[1][1]<=1:
            case0.v[1][1]=1
        if case0.d[1][1]<1:
            case0.d[1][1]=1
        ###########################n1
    if n1==[]:
        case0.n[2][0]=0;
    else:
        case0.n[2][0]=int(float(Platoon_length[1])/5);
        case0.d[2][0]=length-traci.vehicle.getLanePosition(n1[0])-traci.vehicle.getLength(n1[0])
        case0.v[2][0]=traci.vehicle.getSpeed(n1[0])
        if case0.v[2][0]<=1:
            case0.v[2][0]=1
        if case0.d[2][0]<1:
            case0.d[2][0]=1
        ###########################n2
    if n2==[]:
        case0.n[2][1]=0;
    else:
        case0.n[2][1]=int(float(Platoon_length[0])/5);
        case0.d[2][1]=length-traci.vehicle.getLanePosition(n2[0])-traci.vehicle.getLength(n2[0])
        case0.v[2][1]=traci.vehicle.getSpeed(n2[0])
        if case0.v[2][1]<=1:
            case0.v[2][1]=1
        if case0.d[2][1]<1:
            case0.d[2][1]=1
        ###########################e1
    if e1==[]:
        case0.n[3][0]=0;
    else:
        case0.n[3][0]=int(float(Platoon_length[3])/5);
        case0.d[3][0]=length-traci.vehicle.getLanePosition(e1[0])-traci.vehicle.getLength(e1[0])
        case0.v[3][0]=traci.vehicle.getSpeed(e1[0])
        if case0.v[3][0]<=1:
            case0.v[3][0]=1
        if case0.d[3][0]<1:
            case0.d[3][0]=1
        ###########################e2   
    if e2==[]:
        case0.n[3][1]=0;
    else:
        case0.n[3][1]=int(float(Platoon_length[2])/5);
        case0.d[3][1]=length-traci.vehicle.getLanePosition(e2[0])-traci.vehicle.getLength(e2[0])
        case0.v[3][1]=traci.vehicle.getSpeed(e2[0])  
        if case0.v[3][1]<=1:
            case0.v[3][1]=1
        if case0.d[3][1]<1:
            case0.d[3][1]=1

    return case0
