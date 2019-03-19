# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 09:10:34 2018

@author: shengyu
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:45:35 2017

@author: zz-mac
"""

from gurobipy import *
from CRESULT import Result
def optimize_av(x):
    # Create a new model
    m = Model("AV")
    gmin=0;
    gmax=40;
    gap=2;
    c=100;
    M=1000;
    arm=[1,2,3,4]
    direction=[1,2]
    h=3;
            
                                
    
    movement,d,v,n,dis=multidict({(1,1):[x.d[0][0],  x.v[0][0],  x.n[0][0],  x.dis[0][0]],
                                  (1,2):[x.d[0][1],  x.v[0][1],  x.n[0][1],  x.dis[0][1]],                                                               
                                  (2,1):[x.d[1][0],  x.v[1][0],  x.n[1][0],  x.dis[1][0]],
                                  (2,2):[x.d[1][1],  x.v[1][1],  x.n[1][1],  x.dis[1][1]],
                                  (3,1):[x.d[2][0],  x.v[2][0],  x.n[2][0],  x.dis[2][0]],
                                  (3,2):[x.d[2][1],  x.v[2][1],  x.n[2][1],  x.dis[2][1]],
                                  (4,1):[x.d[3][0],  x.v[3][0],  x.n[3][0],  x.dis[3][0]],
                                  (4,2):[x.d[3][1],  x.v[3][1],  x.n[3][1],  x.dis[3][1]]})
                              
    
        # give every movement's head vehice four  motion  parameters  
       # x.d[2][0],  x.v[2][0],  x.n[2][0],  x.dis[2][0]
    
    
    
    
    
    conflict,value=multidict({(1,1,2,1):1,(1,1,2,2):1,(1,1,3,2):1,(1,1,4,1):1,
                              (1,2,2,2):1,(1,2,3,1):1,(1,2,4,1):1,(1,2,4,2):1,
                              (2,1,3,1):1,(2,1,3,2):1,(2,1,4,2):1,(2,1,1,1):1,
                              (2,2,3,2):1,(2,2,4,1):1,(2,2,1,1):1,(2,2,1,2):1,
                              (3,1,1,2):1,(3,1,2,1):1,(3,1,4,1):1,(3,1,4,2):1,
                              (3,2,4,2):1,(3,2,1,1):1,(3,2,2,1):1,(3,2,2,2):1,
                              (4,1,3,1):1,(4,1,2,2):1,(4,1,1,1):1,(4,1,1,2):1,
                              (4,2,1,2):1,(4,2,2,1):1,(4,2,3,1):1,(4,2,3,2):1})  
    #above are the variables for step 1
    #below are the variables for step 2
    dmax=200;
    vmax=20;
    dec=-5; #meter/second2
    acc=5;
#    distance=[50,35,70,25,55,10,80,40]    #distance to the intersection stop line
#    speed=[40,30,55,20,40,10,55,35]    #speed at the moment
#    vehicles=[5,3,6,4,5,6,3,5]            #number of vehicles for platoos at each movement    
    sta={}# the start time of the phase
    phi={}# the during time of a phase 
    for i,i1 in movement:# every movement add to the constriants 
            sta[i,i1] = m.addVar(lb=0.0,ub=c,vtype=GRB.INTEGER, name='sta%s_%s_'%(i,i1))# add the constraints varibles and denote the lower and upper bound
            phi[i,i1] = m.addVar(lb=gmin,ub=gmax,vtype=GRB.INTEGER, name='phi%s_%s'%(i,i1)) #add the during time to every phase and denote the lower and upper bound               
    omg={}#denote the {0,1} varibles to conflict phase.
    for i,i1,i2,i3 in conflict: # find the conflict
            omg[i,i1,i2,i3]= m.addVar(vtype=GRB.BINARY, name='omg%s_%s_%s_%s'%(i,i1,i2,i3))
    for i,i1,i2,i3 in conflict:
        m.addConstr(omg[i,i1,i2,i3]+omg[i2,i3,i,i1]==1)
        m.addConstr(sta[i2,i3]+omg[i,i1,i2,i3]*M>=sta[i,i1]+phi[i,i1]+gap)
        # above are the constraints for step1
        # below are the constraints for step 2
    a={}
    vs={}
    t={}  # the actual travel time to the stop line
    t0={}  # the time to slow down to the stop line
    tmin={} # the shortest time to the stop line
    tn={}  # the time to the stop line if no speed change
    crosstime={}
    for i,i1 in movement:
            t[i,i1] = m.addVar(lb=0.0,ub=c,vtype=GRB.CONTINUOUS, name='t%s_%s_'%(i,i1))   # the start time of every direction
            a[i,i1] = m.addVar(lb=dec,ub=acc,vtype=GRB.INTEGER, name='a%s_%s_'%(i,i1))   #  the acceleration
            vs[i,i1] = m.addVar(lb=0,ub=vmax,vtype=GRB.CONTINUOUS, name='vs%s_%s_'%(i,i1))  # the speed of platoon at the stop line
            t0[i,i1] = m.addVar(lb=0.0,vtype=GRB.CONTINUOUS, name='t0%s_%s_'%(i,i1)) #the time to stop
            crosstime[i,i1]= m.addVar(lb=0.0,vtype=GRB.CONTINUOUS, name='crosstime%s_%s_'%(i,i1))
            tmin[i,i1]= m.addVar(lb=0.0,vtype=GRB.CONTINUOUS, name='tmin%s_%s_'%(i,i1))
            tn[i,i1]= m.addVar(lb=0.0,vtype=GRB.CONTINUOUS, name='tn%s_%s_'%(i,i1))            
    #add varibles to the optimization Model 
    #below are the equation constriants to various parameters
    for i,i1 in movement:
        m.addQConstr(v[i,i1]*0.5*t0[i,i1]==d[i,i1]) # the longest travel time 
        m.addQConstr(v[i,i1]*tn[i,i1]==d[i,i1])   # the normal travel time
        m.addQConstr((v[i,i1]+vmax)*0.5*tmin[i,i1]==d[i,i1])      # the shortest travel time  
        #m.addConstr(crosstime[i,i1]==(dis[i,i1]/5+h)*n[i,i1])
        m.addConstr(crosstime[i,i1]==n[i,i1]*h) # the cross time of a platoon in a direction.
        m.addConstr(phi[i,i1]==crosstime[i,i1]) # the during time of a phase equal to the cross time of a direction.  
        m.addConstr(sta[i,i1]>=tmin[i,i1])      # the start time of a phase  should >= 
        #m.addConstr(sta[i,i1]<=t0[i,i1])
        #the shortest time dipicts that the vehicle will accelerate to vmax at the stop line 
        #the longst time dipicts that the vehicle will decelerate to the stop line 
        #the normal time dipicts that the vehicle will keep a constant speed to the stop line
#above constriants is to calculate the optimzation 
    m.update()    
#    m.setObjective(quicksum(t[i,i1]+(sta[i,i1]-t[i,i1])*n[i,i1]+
#                            (dis[i,i1]/5+h)*n[i,i1]for (i,i1) in movement), GRB.MINIMIZE)
    m.setObjective(quicksum((sta[i,i1]*n[i,i1]) for (i,i1) in movement), GRB.MINIMIZE)
        
    m.optimize()
    
    back_temp=Result()
    back_temp_castle=Result() 
    #随机数
    back_temp_castle.csta=[0,5,10,15,0,5,10,15]
    back_temp_castle.cphi=[5,5,5,5,5,5,5,5]
    back_temp_castle.cycle=20
    
    
    S=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]  #initialize the S Matrix
    P=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]  #initialize the P Matrix

    if m.status!=GRB.status.INFEASIBLE:       
        for i in range(1,5):
            for j in range(1,3):
                S[i][j]=int(sta[i,j].x)
                P[i][j]=int(phi[i,j].x)       
        for i in range(1,5):
            for j in range(1,3): 
                if P[i][j]==0:                              
                    S[i][j]=0 
        for i in range(1,5):
            for j in range(1,3):                    
                back_temp.temp_c[i][j]= S[i][j] + P[i][j]
        back_temp.cycle=max(back_temp.temp_c);
        back_temp.csta[0]=S[3][2];
        back_temp.csta[1]=S[3][1];
        back_temp.csta[2]=S[4][2];
        back_temp.csta[3]=S[4][1];
        back_temp.csta[4]=S[1][2];
        back_temp.csta[5]=S[1][1];
        back_temp.csta[6]=S[2][2];
        back_temp.csta[7]=S[2][1];
         
        back_temp.cphi[0]=int(phi[3,2].x);
        back_temp.cphi[1]=int(phi[3,1].x);
        back_temp.cphi[2]=int(phi[4,2].x);
        back_temp.cphi[3]=int(phi[4,1].x);
        back_temp.cphi[4]=int(phi[1,2].x);
        back_temp.cphi[5]=int(phi[1,1].x);
        back_temp.cphi[6]=int(phi[2,2].x);
        back_temp.cphi[7]=int(phi[2,1].x);
        back_temp.cycle=max(max(back_temp.temp_c));
        return back_temp
    else:        
        return back_temp_castle
    
    
    
    
    
    ## this function will calculate the start time and the during time of the phase and calculate th1
    
    
    
    
    
    
    
    
    
    
    
    
           