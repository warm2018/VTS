#zone2
from __future__ import absolute_import
from __future__ import print_function

from gurobipy import *
from CCAR import CAR_L
from CINPUT import Input
from optimiza_function import optimize_av
from CRESULT import Result
from CIDLIST import IDlist
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
    
#    t0=0;
#    tn=0;
#    ncar=0;
#    x=list();
    t0=[0,0,0,0,0,0,0,0];
    tn=[0,0,0,0,0,0,0,0];
    ncar=[0,0,0,0,0,0,0,0];
    x=[[],[],[],[],[],[],[],[]];
    while step<1000:
        #traci.trafficlight.setPhase("0",0)
        traci.simulationStep()
        traci.trafficlight.setPhase("0",1)
        step=step+1
#        IDList = traci.vehicle.getIDList()
#        n1=list();
#        n2=list();
#        e1=list();
#        e2=list();	
#        s1=list();
#        s2=list();
#        w1=list();
#        w2=list();        
#        for i in range(len(IDList)):
#            if IDList[i].find("n1") != -1:
#                n1.append(IDList[i])
#            elif IDList[i].find("n2") != -1:
#                n2.append(IDList[i])
#            elif IDList[i].find("e1") != -1:
#                e1.append(IDList[i])
#            elif IDList[i].find("e2") != -1:
#                e2.append(IDList[i])
#            elif IDList[i].find("s1") != -1:
#                s1.append(IDList[i])
#            elif IDList[i].find("s2") != -1:
#                s2.append(IDList[i])
#            elif IDList[i].find("w1") != -1:
#                w1.append(IDList[i])
#            else:
#                w2.append(IDList[i])
#        error=8.5
#        Rlength=length-error
#        if len(n1)>0:
#            for i in range(len(n1)):
#                if traci.vehicle.getDistance(n1[i])>200-error:
#                    n1[i]=0					
#        if len(n2)>0:
#            for i in range(len(n2)):
#                if traci.vehicle.getDistance(n2[i])>200-error:
#                    n2[i]=0
#	
#        if len(e1)>0:
#            for i in range(len(e1)):
#                if traci.vehicle.getDistance(e1[i])>200-error:
#                    e1[i]=0	
#        if len(e2)>0:
#            for i in range(len(e2)):
#                if traci.vehicle.getDistance(e2[i])>200-error:
#                    e2[i]=0	
#
#        if len(s1)>0:
#            for i in range(len(s1)):
#                if traci.vehicle.getDistance(s1[i])>200-error:
#                    s1[i]=0	
#        if len(s2)>0:
#            for i in range(len(s2)):
#                if traci.vehicle.getDistance(s2[i])>200-error:
#                    s2[i]=0						
#	
#        if len(w1)>0:
#            for i in range(len(w1)):
#                if traci.vehicle.getDistance(w1[i])>200-error:
#                    w1[i]=0	
#        if len(w2)>0:
#            for i in range(len(w2)):
#                if traci.vehicle.getDistance(w2[i])>200-error:
#                    w2[i]=0		
#
#        for i in range(len(n1)-1,-1,-1):
#            if(n1[i]==0):
#                del n1[i]
#				
#        for i in range(len(n2)-1,-1,-1):
#            if n2[i]==0:
#                del n2[i]
#				
#        for i in range(len(e1)-1,-1,-1):
#            if e1[i]==0:
#                del e1[i]		
#        for i in range(len(e2)-1,-1,-1):
#            if e2[i]==0:
#                del e2[i]
#				
#        for i in range(len(s1)-1,-1,-1):
#            if s1[i]==0:
#                del s1[i]		
#        for i in range(len(s2)-1,-1,-1):
#            if s2[i]==0:
#                del s2[i]	
#				
#        for i in range(len(w1)-1,-1,-1):
#            if w1[i]==0:
#                del w1[i]		
#        for i in range(len(w2)-1,-1,-1):
#            if w2[i]==0:
#                del w2[i]		       
#        #去除数组中的重复元素;
#        n1=sorted(n1,key=lambda x:int(x[3:]))
#        n2=sorted(n2,key=lambda x:int(x[3:]))
#        e1=sorted(e1,key=lambda x:int(x[3:]))
#        e2=sorted(e2,key=lambda x:int(x[3:]))
#        s1=sorted(s1,key=lambda x:int(x[3:]))
#        s2=sorted(s2,key=lambda x:int(x[3:]))
#        w1=sorted(w1,key=lambda x:int(x[3:]))
#        w2=sorted(w2,key=lambda x:int(x[3:]))
#        
##        if len(s2)>0 and s2[-1] not in x and step<500:
##            t0=t0+step
##            x.append(s2[-1])
##            ncar=ncar+1
##        if len(x)>0:
##            if traci.vehicle.getDistance(x[0])>300:
##                tn=tn+step;
##                x.remove(x[0])
#        if len(s2)>0 and s2[-1] not in x[4] and step<500:
#            t0[4]=t0[4]+step
#            x[4].append(s2[-1])
#            ncar[4]=ncar[4]+1
#        if len(x[4])>0:
#            if traci.vehicle.getDistance(x[4][0])>300:
#                tn[4]=tn[4]+step;
#                x[4].remove(x[4][0])         
#        #arm1-1[s1]~5
#        if len(s1)>0 and s1[-1] not in x[5] and step<500:
#            t0[5]=t0[5]+step
#            x[5].append(s1[-1])
#            ncar[5]=ncar[5]+1
#        if len(x[5])>0:
#            if traci.vehicle.getDistance(x[5][0])>300:
#                tn[5]=tn[5]+step;
#                x[5].remove(x[5][0])
#        		
#        #arm2-1[w1]~7
#        if len(w1)>0 and w1[-1] not in x[7] and step<500:
#            t0[7]=t0[7]+step
#            x[7].append(w1[-1])
#            ncar[7]=ncar[7]+1
#        if len(x[7])>0:
#            if traci.vehicle.getDistance(x[7][0])>300:
#                tn[7]=tn[7]+step;
#                x[7].remove(x[7][0])		
#        		
#        #arm2-2[w2]~6
#        if len(w2)>0 and w2[-1] not in x[6] and step<500:
#            t0[6]=t0[6]+step
#            x[6].append(w2[-1])
#            ncar[6]=ncar[6]+1
#        if len(x[6])>0:
#            if traci.vehicle.getDistance(x[6][0])>300:
#                tn[6]=tn[6]+step;
#                x[6].remove(x[6][0])		
#        
#        #arm3-1[n1]~1
#        if len(n1)>0 and n1[-1] not in x[1] and step<500:
#            t0[1]=t0[1]+step
#            x[1].append(n1[-1])
#            ncar[1]=ncar[1]+1
#        if len(x[1])>0:
#            if traci.vehicle.getDistance(x[1][0])>300:
#                tn[1]=tn[1]+step;
#                x[1].remove(x[1][0])
#        
#        #arm3-2[n2]~0
#        if len(n2)>0 and n2[-1] not in x[0] and step<500:
#            t0[0]=t0[0]+step
#            x[0].append(n2[-1])
#            ncar[0]=ncar[0]+1
#        if len(x[0])>0:
#            if traci.vehicle.getDistance(x[0][0])>300:
#                tn[0]=tn[0]+step;
#                x[0].remove(x[0][0])
#        
#        
#        #arm4-1[s1]~3
#        if len(s1)>0 and s1[-1] not in x[3] and step<500:
#            t0[3]=t0[3]+step
#            x[3].append(s1[-1])
#            ncar[3]=ncar[3]+1
#        if len(x[3])>0:
#            if traci.vehicle.getDistance(x[3][0])>300:
#                tn[3]=tn[3]+step;
#                x[3].remove(x[3][0])
#        
#        
#        #arm4-2[s2]~2
#        if len(s2)>0 and s2[-1] not in x[2] and step<500:
#            t0[2]=t0[2]+step
#            x[2].append(s2[-1])
#            ncar[2]=ncar[2]+1
#        if len(x[2])>0:
#            if traci.vehicle.getDistance(x[2][0])>300:
#                tn[2]=tn[2]+step;
#                x[2].remove(x[2][0])           
#        
#        print("t0=%i"%t0)
#        print("tn=%i"%tn)
#        print("n=%i"%ncar)   
          
        traci.simulationStep()
        traci.trafficlight.setPhase("0",1)
        step=step+1
        #traci.trafficlight.setPhase("0",0)
    for i in range(8):
        print((tn[i]-t0[i])/ncar[i]-15)
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
