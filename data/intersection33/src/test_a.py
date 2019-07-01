from __future__ import print_function
from __future__ import absolute_import
from GET_LIST import get_list
from CINPUT import Input
from INPUT_ADDITIONAL import Input_Addtional
from PLATOON_INTERSECTION import Platoon_Intersection
from SPEED_ACCERATOR import Speed_Accelerator
from optimiza_function import optimize_av
from generator_route_123 import generator
from gurobipy import *
from PLATOON_INTERSECTION import Outlist_speedset

import os
import sys
import optparse
import subprocess
import random

import xlsxwriter
import traci

import time 

#generator(1)

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

def run():
	step = 0
	steplength = 1
	while step < 3600:
		traci.simulationStep()
		step += steplength


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
	traci.start([sumoBinary, "-c", "../cfg/intersection_a.sumocfg",
							 "--tripinfo-output", "../output/tripinfo.xml",
							 "--queue-output","../output/queue.xml",
							 "--time-to-teleport","100",
							 "--collision.mingap-factor","0",
							 "--tls.actuated.show-detectors"])
	run()