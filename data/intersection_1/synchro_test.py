#zone2
from __future__ import absolute_import
from __future__ import print_function
from gurobipy import *
from CCAR import CAR_L
from CINPUT import Input
from optimiza_function import optimize_av
from GetDelay import Get_Delay
from CRESULT import Result
from GET_LIST import get_list
from PLATOON_INTERSECTION import Platoon_Intersection

import simpla
import xlsxwriter
import os
import sys
import optparse
import subprocess
import random
import traci

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
	row = 0
	row1 = 0
	col = 0
	workbook = xlsxwriter.Workbook('Output-data.xlsx')
	worksheet = workbook.add_worksheet()
	workbook2 = xlsxwriter.Workbook('Speed-fixed.xlsx')
	worksheet2 = workbook2.add_worksheet()
	step = 0
	cycle_a =  60
	cycle_b = 90
	cycle_c = 90
	cycle_d = 90
	Qrate = 0
	start_a = [40,30,10,0,40,30,10,0] #60
	duration_a = [20,10,20,10,20,10,20,10]

	#start_a = [35,35,15,20,50,55,0,0] #70
	#duration_a = [20,15,20,15,20,15,20,15]

	#start_a = [33,33,12,0,45,97,0,0] 
	#duration_a = [32,33,32,33,32,33,32,33]

	#start_a = [65,97,33,32,65,97,0,0]
	#duration_a = [32,33,32,33,32,33,32,33]

	#start_a = [40,30,10,0,40,30,10,0]
	#duration_a = [20,10,20,10,20,10,20,10]
	
	#start_a = [65,97,33,32,65,97,0,0]
	#duration_a = [32,33,32,33,32,33,32,33]

	#start_a = [65,97,33,32,65,97,0,0]
	#duration_a = [32,33,32,33,32,33,32,33]

	#start_a = [65,97,33,32,65,97,0,0]
	#duration_a = [32,33,32,33,32,33,32,33]

	"""
	cycle_a = 100
	aphase1_length = 20; aphase1_order = 136 #南北直行
	aphase2_length = 30; aphase2_order = 68 # 南北左转
	aphase3_length = 30; aphase3_order = 17 # 东西左转
	aphase4_length = 20; aphase4_order = 34 # 东西直行，下同

	cycle_b = 100
	bphase1_length = 20; bphase1_order = 136
	bphase2_length = 30; bphase2_order = 68
	bphase3_length = 30; bphase3_order = 17
	bphase4_length = 20; bphase4_order = 34

	cycle_c = 100
	cphase1_length = 20; cphase1_order = 136
	cphase2_length = 30; cphase2_order = 68
	cphase3_length = 30; cphase3_order = 17
	cphase4_length = 20; cphase4_order = 34

	cycle_d = 100
	dphase1_length = 20; dphase1_order = 136
	dphase2_length = 30; dphase2_order = 68
	dphase3_length = 30; dphase3_order = 17
	dphase4_length = 20; dphase4_order = 34

	while step < 3600:
			if step % cycle_a < aphase1_length:
				traci.trafficlight.setPhase("a",aphase1_order) ## 相位为在net文件中信号灯设置的第68个配时方案
			
			if step % cycle_a > aphase1_length and step % cycle_a < aphase1_length + aphase2_length:
				traci.trafficlight.setPhase("a",aphase2_order)
	
			if step % cycle_a > aphase1_length + aphase2_length and step % cycle_a < aphase1_length + aphase2_length + aphase3_length:
				traci.trafficlight.setPhase("a",aphase3_order)

			if step % cycle_a > aphase1_length + aphase2_length + aphase3_length and step % cycle_a < aphase1_length + aphase2_length + aphase3_length + aphase4_length:
				traci.trafficlight.setPhase("a",aphase4_order)
	#**************************************************a*********************************************************
			if step % cycle_b < bphase1_length:
				traci.trafficlight.setPhase("b",bphase1_order) ## 相位为在net文件中信号灯设置的第68个配时方案
			
			if step % cycle_b > bphase1_length and step % cycle_b < bphase1_length + bphase2_length:
				traci.trafficlight.setPhase("b",bphase2_order)
	
			if step % cycle_b > bphase1_length + bphase2_length and step % cycle_b < bphase1_length + bphase2_length + bphase3_length:
				traci.trafficlight.setPhase("b",bphase3_order)

			if step % cycle_b > bphase1_length + bphase2_length + bphase3_length and step % cycle_b < bphase1_length + bphase2_length + bphase3_length + bphase4_length:
				traci.trafficlight.setPhase("b",bphase4_order)
#**************************************************b*********************************************************
			if step % cycle_c < cphase1_length:
				traci.trafficlight.setPhase("c",cphase1_order) ## 相位为在net文件中信号灯设置的第68个配时方案
			
			if step % cycle_c > cphase1_length and step % cycle_c < cphase1_length + cphase2_length:
				traci.trafficlight.setPhase("c",cphase2_order)
	
			if step % cycle_c > cphase1_length + cphase2_length and step % cycle_c < cphase1_length + cphase2_length + cphase3_length:
				traci.trafficlight.setPhase("c",cphase3_order)

			if step % cycle_c > cphase1_length + cphase2_length + cphase3_length and step % cycle_c < cphase1_length + cphase2_length + cphase3_length + cphase4_length:
				traci.trafficlight.setPhase("c",cphase4_order)
#**************************************************c*********************************************************                
			if step % cycle_d < dphase1_length:
				traci.trafficlight.setPhase("d",dphase1_order) ## 相位为在net文件中信号灯设置的第68个配时方案
			if step % cycle_d > dphase1_length and step % cycle_d < dphase1_length + dphase2_length:
				traci.trafficlight.setPhase("d",dphase2_order)
	
			if step % cycle_d > dphase1_length + dphase2_length and step % cycle_d < dphase1_length + dphase2_length + dphase3_length:
				traci.trafficlight.setPhase("d",dphase3_order)

			if step % cycle_d > dphase1_length + dphase2_length + dphase3_length and step % cycle_d < dphase1_length + dphase2_length + dphase3_length + dphase4_length:
				traci.trafficlight.setPhase("d",dphase4_order)
	#**************************************************d*********************************************************
#********************************* INTERSECTION ********C*************************************
			"""
	while step < 3600:

		step_a = step % cycle_a
		step_b = step % cycle_b
		step_c = step % cycle_c
		step_d = step % cycle_d

		#*******************对A的信号灯进行设置
		Binary=[0,0,0,0,0,0,0,0];signal_temp = 0;
		for i in range(8):
			if(start_a[i] <= step_a and start_a[i]+duration_a[i] > step_a):## 其实 bstep_temp 就是step 的代替，如何让现在的step成为
				Binary[i]=1
			else:
				Binary[i]=0
		for i in range(8):
			signal_temp = signal_temp+(2**(7-i))*Binary[i]             
		traci.trafficlight.setPhase("a",signal_temp)
		'''
		#*******************对B的信号灯进行设置
		Binary=[0,0,0,0,0,0,0,0];signal_temp = 0;
		for i in range(8):
			if(start_b[i] <= step_b and start_b[i]+duration_b[i] > step_b):## 其实 bstep_temp 就是step 的代替，如何让现在的step成为
				Binary[i]=1
			else:
				Binary[i]=0
		for i in range(8):
			signal_temp = signal_temp+(2**(7-i))*Binary[i]             
		traci.trafficlight.setPhase("b",signal_temp)

		#*******************对C的信号灯进行设置
		Binary=[0,0,0,0,0,0,0,0];signal_temp = 0;
		for i in range(8):
			if(start_c[i] <= step_c and start_c[i]+duration_c[i] > step_c):## 其实 bstep_temp 就是step 的代替，如何让现在的step成为
				Binary[i]=1
			else:
				Binary[i]=0
		for i in range(8):
			signal_temp = signal_temp+(2**(7-i))*Binary[i]             
		traci.trafficlight.setPhase("c",signal_temp) 

		#*******************对D的信号灯进行设置
		Binary=[0,0,0,0,0,0,0,0];signal_temp = 0;
		for i in range(8):
			if(start_d[i] <= step_d and start_d[i]+duration_d[i] > step_d):## 其实 bstep_temp 就是step 的代替，如何让现在的step成为
				Binary[i]=1
			else:
				Binary[i]=0
		for i in range(8):
			signal_temp = signal_temp+(2**(7-i))*Binary[i]             
		traci.trafficlight.setPhase("d",signal_temp) 
		'''
		Id_list =  traci.vehicle.getIDList()#得到所有vehicle 的ID
		running_car1 = Id_list
		worksheet.write(row,col,len(running_car1))
		row = row + 1
		traci.simulationStep()
		Id_list =  traci.vehicle.getIDList()#得到所有vehicle 的ID

		'''
		for value in Id_list:
			if traci.vehicle.getLaneID(value).find(':') == -1:
				worksheet2.write(row1,col,traci.vehicle.getSpeed(value))
				row1 = row1 +1
		
		
		for value in Id_list:
			worksheet2.write(row1,col,traci.vehicle.getSpeed(value))
			row1 = row1 + 1
		'''
		''' #用来写入速度的代码
		running_car2 = list(Id_list)
		print(type(running_car2))
		out_car = 0
		numbercar = len(running_car1)

		'''
		'''
		for value in running_car1:
			if value not in running_car2:
				out_car = out_car + 1
		worksheet.write(row,col,out_car)
		worksheet.write(row,col+1,numbercar)
		'''
		step = step + 1
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
	traci.start([sumoBinary, "-c", "intersection.sumocfg",
							 "--tripinfo-output", "tripinfo.xml",
							 "--queue-output","queue.xml"])
	run()
	delay=Get_Delay()
	print("delay")
	print(delay)