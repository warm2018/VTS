from __future__ import absolute_import
from __future__ import print_function

from gurobipy import *
from CCAR import CAR_L
from CINPUT import Input
from optimiza_function import optimize_av
from GetDelay import Get_Delay
from GET_LIST import get_list
from CRESULT import Result
from CIDLIST import IDlist
from GetDelay import Get_Delay
from PLATOON_INTERSECTION import Platoon_Intersection
from SPEED_JUNCTION import Speed_Junction
from GET_LIST_II import get_list_II
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
    slength=20
    error=200
    while step<1000:
        #traci.trafficlight.setPhase("0",0)
        traci.simulationStep()            
        step=step+1 
        IDList = traci.vehicle.getIDList()   
        Platoon_Intersection(IDList)
        IDList_result=get_list(IDList)
        n2=IDList_result[0];n1=IDList_result[1];      
        e2=IDList_result[2];e1=IDList_result[3];
        s2=IDList_result[4];s1=IDList_result[5];
        w2=IDList_result[6];w1=IDList_result[7];
        Speed_Junction(IDList)
                
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
    delay=Get_Delay()
    print("delay")
    print(delay)