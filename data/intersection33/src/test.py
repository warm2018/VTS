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
	traci.simulationStep()
	step = 0
	col = 0
	row = 0
	Step_a = 0
	Step_b = 0
	Step_c = 0
	Step_d = 0
	Step_e = 0
	Step_f = 0
	Step_g = 0
	Step_h = 0
	Step_j = 0		
	Time_clocka = 1
	Time_clockb = 1
	Time_clockc = 1
	Time_clockd = 1
	Time_clocke = 1
	Time_clockf = 1
	Time_clockg = 1
	Time_clockh = 1	
	Time_clockj = 1	
	S_a = []
	S_b = []
	S_c = []
	S_d = []
	S_e = []
	S_f = []
	S_g = []
	S_h = []
	S_j = []

	P_a = []
	P_b = []
	P_c = []
	P_d = []
	P_e = []
	P_f = []
	P_g = []
	P_h = []
	P_j = []
	Platoon_lengtha = [0,0,0,0,0,0,0,0,0,0]
	Platoon_lengthb = [0,0,0,0,0,0,0,0,0,0]
	Platoon_lengthc = [0,0,0,0,0,0,0,0,0,0]
	Platoon_lengthd = [0,0,0,0,0,0,0,0,0,0]
	Platoon_lengthe = [0,0,0,0,0,0,0,0,0,0]
	Platoon_lengthf = [0,0,0,0,0,0,0,0,0,0]
	Platoon_lengthg = [0,0,0,0,0,0,0,0,0,0]
	Platoon_lengthh = [0,0,0,0,0,0,0,0,0,0]
	Platoon_lengthj = [0,0,0,0,0,0,0,0,0,0]       
	workbook = xlsxwriter.Workbook('../output/Output-data2.xlsx')
	worksheet = workbook.add_worksheet(name="flowrate")
	worksheet2 = workbook.add_worksheet(name="speed")

	speed_index = 0
	speed = []
	while step<3000: 
		running_car1 = traci.vehicle.getIDList()
		traci.simulationStep()
		Position_list = []
		Road_list = []
		Lane_list = []
		Laneposition_list = []
		step = step + 1
#获取交叉口车辆的信息
		Id_List = traci.vehicle.getIDList()
		Idlist =  traci.vehicle.getIDList()#得到所有vehicle 的ID
		running_car2 = list(Id_List)
		numbercar = len(Id_List)
		out_car = 0

		'''
		for value in running_car1:
			if value not in running_car2:
				out_car = out_car + 1
		worksheet.write(row,col,out_car)
		worksheet.write(row,col+1,numbercar)
		'''
		
		'''
		for value in Id_List:
			worksheet2.write(row,col+1,traci.vehicle.getSpeed(value))
			row = row + 1
		'''
		for Vehicle_ID in Id_List:
			Vehicle_Lane = traci.vehicle.getLaneID(Vehicle_ID)
			Vehicle_Laneposition = traci.vehicle.getLanePosition(Vehicle_ID)                #**********get the information of every vehicle************
			Lane_list.append(Vehicle_Lane)
			Laneposition_list.append(Vehicle_Laneposition)# get the position(x,y) of every vehicle
			#**********let the information became the list
			#**********write the values in EXCEL sheet to make the data more visibl
	#******************************************************************************************
	#******************************BELOW ARE INTERSECTION A************************************************************
	#******************************************************************************************
		Single_LaneList_a = []

		Single_IdList_a = []
		for V_index  in range(len(Lane_list)):
			if Lane_list[V_index].find("a") != -1:
				Single_LaneList_a.append(Lane_list[V_index])
				Single_IdList_a.append(Id_List[V_index])
		Id_result,Position_result = get_list(Single_IdList_a,Single_LaneList_a)
		n2=Id_result[0];n1=Id_result[1];      
		e2=Id_result[2];e1=Id_result[3];
		s2=Id_result[4];s1=Id_result[5];
		w2=Id_result[6];w1=Id_result[7];

		## we can write these information to EXCEL worksheet and make the data visible
		if Time_clocka == step:
			casea = Input()
			casea = Input_Addtional(Id_result,Platoon_lengtha)
			Optimiza_result = optimize_av(casea)
		
			temp_a = Speed_Accelerator(Optimiza_result,Id_result)
			D_a=temp_a[0];V0_a=temp_a[1];Vn_a=temp_a[2];a_a=temp_a[3]
			#D=temp[0];V0=temp[1];Vn_a=temp[2];a=temp[3]
			car_accord_a=[0,0,0,0,0,0,0,0]; 
			if n2!=[]:
				car_accord_a[0]=n2[0]
			if n1!=[]:
				car_accord_a[1]=n1[0]
				
			if e2!=[]:
				car_accord_a[2]=e2[0]
			if e1!=[]:
				car_accord_a[3]=e1[0]
					
			if s2!=[]:
				car_accord_a[4]=s2[0]
			if s1!=[]:
				car_accord_a[5]=s1[0]
					
			if w2!=[]:
				car_accord_a[6]=w2[0]
			if w1!=[]:
				car_accord_a[7]=w1[0]
			#####################################################    
			#########################################################
			 
			S_a = []
			P_a = []
			Cycle_a=int(Optimiza_result.cycle)#0~cycle
			Time_clocka=Time_clocka + Cycle_a;
			for value in Optimiza_result.csta:
				S_a.append(value)
			for value in Optimiza_result.cphi:
				P_a.append(value)#八个方向的持续时间；
		if Cycle_a == 0:
			Time_clocka = Time_clocka + 1
		Step_a = Cycle_a - (Time_clocka - step)
		Binary=[0,0,0,0,0,0,0,0];
		for i in range(8):
			if(S_a[i]<=Step_a and S_a[i]+P_a[i]>Step_a):## 其实 bstep_temp 就是step 的代替，如何让现在的step成为
				Binary[i]=1
			else:
				Binary[i]=0                       
		signal_temp=0;
		for i in range(8):
			signal_temp = signal_temp+(2**(7-i))*Binary[i]             
		traci.trafficlight.setPhase("a",signal_temp) 
		
		if n2!=[]:   
			if car_accord_a[0]==n2[0] and traci.vehicle.getLanePosition(n2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_a[0], Vn_a[0])

		
				
		if n1!=[]:   
			if car_accord_a[1]==n1[0] and traci.vehicle.getLanePosition(n1[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_a[1], Vn_a[1])

				
				
						
		if e2!=[]:
			if car_accord_a[2]==e2[0] and traci.vehicle.getLanePosition(e2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_a[2], Vn_a[2])

       
				
				
		if e1!=[]:
			if car_accord_a[3]==e1[0] and traci.vehicle.getLanePosition(e1[0]) - 5.1 <120:    

				traci.vehicle.setSpeed(car_accord_a[3], Vn_a[3])



								
				
		if s2!=[]:    
			if car_accord_a[4]==s2[0] and traci.vehicle.getLanePosition(s2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_a[4], Vn_a[4])

								
				
		if s1!=[]:
			if car_accord_a[5]==s1[0] and traci.vehicle.getLanePosition(s1[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_a[5], Vn_a[5])

						
		if w2!=[]:    
			if car_accord_a[6]==w2[0] and traci.vehicle.getLanePosition(w2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_a[6], Vn_a[6])



						
				
		if w1!=[]:
			if car_accord_a[7]==w1[0] and traci.vehicle.getLanePosition(w1[0]) - 5.1 <120:

				traci.vehicle.setSpeed( car_accord_a[7], Vn_a[7])

		
		Platoon_lengtha = Platoon_Intersection(Id_result,Binary)
		Outlist_speedset(Single_IdList_a,Single_LaneList_a)


	#*************************************************************************************************************
	#*************************************************************************************************************
	#************************************************************************************************************* 
	#***********************************ABOVE IS  INTERSECTION  AAAAAAAAAA*****************************


		#I get the data in order to get the vehicle's information and located it make it easy to build Model

		Single_LaneList_b = []
		Single_IdList_b = []
		for V_index  in range(len(Lane_list)):
			if Lane_list[V_index].find("b") != -1:
				Single_LaneList_b.append(Lane_list[V_index])
				Single_IdList_b.append(Id_List[V_index])
		Id_result,Position_result = get_list(Single_IdList_b,Single_LaneList_b)
		n2=Id_result[0];n1=Id_result[1];      
		e2=Id_result[2];e1=Id_result[3];
		s2=Id_result[4];s1=Id_result[5];
		w2=Id_result[6];w1=Id_result[7];


		if Time_clockb == step:
			caseb = Input()
			caseb = Input_Addtional(Id_result,Platoon_lengthb)
			Optimiza_result=optimize_av(caseb)
			
			temp_b = Speed_Accelerator(Optimiza_result,Id_result)
			D_b = temp_b[0];V0_b = temp_b[1];Vn_b = temp_b[2];a_b = temp_b[3]
			car_accord_b = [0,0,0,0,0,0,0,0]; 
			if n2!=[]:
				car_accord_b[0] = n2[0]
			if n1!=[]:
				car_accord_b[1] = n1[0]
				
			if e2!=[]:
				car_accord_b[2] = e2[0]
			if e1!=[]:
				car_accord_b[3] = e1[0]
					
			if s2!=[]:
				car_accord_b[4] = s2[0]
			if s1!=[]:
				car_accord_b[5] = s1[0]
					
			if w2!=[]:
				car_accord_b[6] = w2[0]
			if w1!=[]:
				car_accord_b[7] = w1[0]
			#####################################################    
			#########################################################

			S_b = []
			P_b = []
			Cycle_b = int(Optimiza_result.cycle)#0~cycle
			Time_clockb=Time_clockb + Cycle_b;
			for value in Optimiza_result.csta:
				S_b.append(value)
			for value in Optimiza_result.cphi:
				P_b.append(value) #八个方向的开始时间；
		if Cycle_b == 0:
			Time_clockb = Time_clockb + 1
		Step_b = Cycle_b - (Time_clockb - step)
		Binary=[0,0,0,0,0,0,0,0];
		for i in range(8):
			if(S_b[i]<=Step_b and S_b[i]+P_b[i]>Step_b):## 其实 bstep_temp 就是step 的代替，如何让现在的step成为
				Binary[i]=1
			else:
				Binary[i]=0                        
		signal_temp=0;
		for i in range(8):
			signal_temp=signal_temp+(2**(7-i))*Binary[i]             
		traci.trafficlight.setPhase("b",signal_temp) 
		if n2!=[]:   
			if car_accord_b[0]==n2[0] and traci.vehicle.getLanePosition(n2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_b[0], Vn_b[0])

		
				
		if n1!=[]:   
			if car_accord_b[1]==n1[0] and traci.vehicle.getLanePosition(n1[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_b[1], Vn_b[1])

				
				
						
		if e2!=[]:
			if car_accord_b[2]==e2[0] and traci.vehicle.getLanePosition(e2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_b[2], Vn_b[2])

       
				
				
		if e1!=[]:
			if car_accord_b[3]==e1[0] and traci.vehicle.getLanePosition(e1[0]) - 5.1 <120:    

				traci.vehicle.setSpeed(car_accord_b[3], Vn_b[3])



								
				
		if s2!=[]:    
			if car_accord_b[4]==s2[0] and traci.vehicle.getLanePosition(s2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_b[4], Vn_b[4])

								
				
		if s1!=[]:
			if car_accord_b[5]==s1[0] and traci.vehicle.getLanePosition(s1[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_b[5], Vn_b[5])

						
		if w2!=[]:    
			if car_accord_b[6]==w2[0] and traci.vehicle.getLanePosition(w2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_b[6], Vn_b[6])



						
				
		if w1!=[]:
			if car_accord_b[7]==w1[0] and traci.vehicle.getLanePosition(w1[0]) - 5.1 <120:

				traci.vehicle.setSpeed( car_accord_b[7], Vn_b[7])

		Platoon_lengthb = Platoon_Intersection(Id_result,Binary)
		Outlist_speedset(Single_IdList_b,Single_LaneList_b)

	#*************************************************************************************************************
	#*************************************************************************************************************
	#************************************************************************************************************* 
	#***********************************ABOVE IS  INTERSECTION B************************************************


   
		#I get the data in order to get the vehicle's information and located it make it easy to build Model

		Single_LaneList_c = []
		Single_IdList_c = []
		for V_index  in range(len(Lane_list)):
			if Lane_list[V_index].find("c") != -1:
				Single_LaneList_c.append(Lane_list[V_index])
				Single_IdList_c.append(Id_List[V_index])
		Id_result,Position_result = get_list(Single_IdList_c,Single_LaneList_c)
		n2=Id_result[0];n1=Id_result[1];      
		e2=Id_result[2];e1=Id_result[3];
		s2=Id_result[4];s1=Id_result[5];
		w2=Id_result[6];w1=Id_result[7];


		## we can write these information to EXCEL worksheet and make the data visible
		if Time_clockc == step:
			casec = Input()
			casec = Input_Addtional(Id_result,Platoon_lengthc)
			Optimiza_result = optimize_av(casec)

			temp_c = Speed_Accelerator(Optimiza_result,Id_result)
			D_c= temp_c[0];V0_c = temp_c[1];Vn_c = temp_c[2];a_c = temp_c[3]
			car_accord_c=[0,0,0,0,0,0,0,0]; 
			if n2!=[]:
				car_accord_c[0]=n2[0]
			if n1!=[]:
				car_accord_c[1]=n1[0]
				
			if e2!=[]:
				car_accord_c[2]=e2[0]
			if e1!=[]:
				car_accord_c[3]=e1[0]
					
			if s2!=[]:
				car_accord_c[4]=s2[0]
			if s1!=[]:
				car_accord_c[5]=s1[0]
					
			if w2!=[]:
				car_accord_c[6]=w2[0]
			if w1!=[]:
				car_accord_c[7]=w1[0]
			#####################################################    
			#########################################################

			S_c = []
			P_c = []
			Cycle_c = int(Optimiza_result.cycle)#0~cycle
			Time_clockc=Time_clockc + Cycle_c ;
			for value in Optimiza_result.csta:
				S_c.append(value)
			for value in Optimiza_result.cphi:
				P_c.append(value) #八个方向的开始时间；
		if Cycle_c  == 0:
			Time_clockc = Time_clockc + 1
		Step_c = Cycle_c  - (Time_clockc - step)
		Binary=[0,0,0,0,0,0,0,0];
		for i in range(8):
			if(S_c[i]<=Step_c and S_c[i]+P_c[i]>Step_c):## 其实 bstep_temp 就是step 的代替，如何让现在的step成为
				Binary[i]=1
			else:
				Binary[i]=0                 
		signal_temp=0;
		for i in range(8):
			signal_temp=signal_temp+(2**(7-i))*Binary[i]             
		traci.trafficlight.setPhase("c",signal_temp) 
		if n2!=[]:   
			if car_accord_c[0]==n2[0] and traci.vehicle.getLanePosition(n2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_c[0], Vn_c[0])

		
				
		if n1!=[]:   
			if car_accord_c[1]==n1[0] and traci.vehicle.getLanePosition(n1[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_c[1], Vn_c[1])

				
				
						
		if e2!=[]:
			if car_accord_c[2]==e2[0] and traci.vehicle.getLanePosition(e2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_c[2], Vn_c[2])

       
				
				
		if e1!=[]:
			if car_accord_c[3]==e1[0] and traci.vehicle.getLanePosition(e1[0]) - 5.1 <120:    

				traci.vehicle.setSpeed(car_accord_c[3], Vn_c[3])



								
				
		if s2!=[]:    
			if car_accord_c[4]==s2[0] and traci.vehicle.getLanePosition(s2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_c[4], Vn_c[4])

								
				
		if s1!=[]:
			if car_accord_c[5]==s1[0] and traci.vehicle.getLanePosition(s1[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_c[5], Vn_c[5])

						
		if w2!=[]:    
			if car_accord_c[6]==w2[0] and traci.vehicle.getLanePosition(w2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_c[6], Vn_c[6])



						
				
		if w1!=[]:
			if car_accord_a[7]==w1[0] and traci.vehicle.getLanePosition(w1[0]) - 5.1 <120:

				traci.vehicle.setSpeed( car_accord_a[7], Vn_c[7])
		Platoon_lengthc = Platoon_Intersection(Id_result,Binary)
		Outlist_speedset(Single_IdList_c,Single_LaneList_c)


	#*************************************************************************************************************
	#*************************************************************************************************************
	#************************************************************************************************************* 
	#***********************************ABOVE IS  INTERSECTION C************************************************




   
		#I get the data in order to get the vehicle's information and located it make it easy to build Model

		Single_LaneList_d = []
		Single_IdList_d = []
		for V_index  in range(len(Lane_list)):
			if Lane_list[V_index].find("d") != -1:
				Single_LaneList_d.append(Lane_list[V_index])
				Single_IdList_d.append(Id_List[V_index])
		Id_result,Position_result = get_list(Single_IdList_d,Single_LaneList_d)
		n2=Id_result[0];n1=Id_result[1];      
		e2=Id_result[2];e1=Id_result[3];
		s2=Id_result[4];s1=Id_result[5];
		w2=Id_result[6];w1=Id_result[7];

		## we can write these information to EXCEL worksheet and make the data visible
		if Time_clockd == step:
			cased = Input()
			cased = Input_Addtional(Id_result,Platoon_lengthd)
			Optimiza_result = optimize_av(cased)
			temp_d=Speed_Accelerator(Optimiza_result,Id_result)
			D_d = temp_d[0];V0_d = temp_d[1];Vn_d = temp_d[2];a_d = temp_d[3]
			car_accord_d=[0,0,0,0,0,0,0,0]; 
			if n2!=[]:
				car_accord_d[0]=n2[0]
			if n1!=[]:
				car_accord_d[1]=n1[0]
				
			if e2!=[]:
				car_accord_d[2]=e2[0]
			if e1!=[]:
				car_accord_d[3]=e1[0]
					
			if s2!=[]:
				car_accord_d[4]=s2[0]
			if s1!=[]:
				car_accord_d[5]=s1[0]
					
			if w2!=[]:
				car_accord_d[6]=w2[0]
			if w1!=[]:
				car_accord_d[7]=w1[0]
			#####################################################    
			#########################################################

			S_d = []
			P_d = []
			Cycle_d = int(Optimiza_result.cycle)#0~cycle
			Time_clockd=Time_clockd + Cycle_d ;
			for value in Optimiza_result.csta:
				S_d.append(value)
			for value in Optimiza_result.cphi:
				P_d.append(value)
		if Cycle_d  == 0:
			Time_clockd = Time_clockd + 1
		Step_d = Cycle_d  - (Time_clockd - step)
		Binary=[0,0,0,0,0,0,0,0];
		for i in range(8):
			if(S_d[i]<=Step_d and S_d[i]+P_d[i]>Step_d):## 其实 bstep_temp 就是step 的代替，如何让现在的step成为
				Binary[i]=1
			else: 
				Binary[i]=0                        
		signal_temp=0;
		print(S_d,P_d,id(S_d),id(P_d))           
		for i in range(8):
			signal_temp=signal_temp+(2**(7-i))*Binary[i]             
		traci.trafficlight.setPhase("d",signal_temp) 
		if n2!=[]:   
			if car_accord_d[0]==n2[0] and traci.vehicle.getLanePosition(n2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_d[0], Vn_d[0])

		
				
		if n1!=[]:   
			if car_accord_d[1]==n1[0] and traci.vehicle.getLanePosition(n1[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_d[1], Vn_d[1])

				
				
						
		if e2!=[]:
			if car_accord_d[2]==e2[0] and traci.vehicle.getLanePosition(e2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_d[2], Vn_d[2])

       
				
				
		if e1!=[]:
			if car_accord_d[3]==e1[0] and traci.vehicle.getLanePosition(e1[0]) - 5.1 <120:    

				traci.vehicle.setSpeed(car_accord_d[3], Vn_d[3])



								
				
		if s2!=[]:    
			if car_accord_d[4]==s2[0] and traci.vehicle.getLanePosition(s2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_d[4], Vn_d[4])

								
				
		if s1!=[]:
			if car_accord_d[5]==s1[0] and traci.vehicle.getLanePosition(s1[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_d[5], Vn_d[5])

						
		if w2!=[]:    
			if car_accord_d[6]==w2[0] and traci.vehicle.getLanePosition(w2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_d[6], Vn_d[6])



						
				
		if w1!=[]:
			if car_accord_d[7]==w1[0] and traci.vehicle.getLanePosition(w1[0]) - 5.1 <120:

				traci.vehicle.setSpeed( car_accord_d[7], Vn_d[7])

		Platoon_lengthd = Platoon_Intersection(Id_result,Binary)
		Outlist_speedset(Single_IdList_d,Single_LaneList_d)


	#*************************************************************************************************************
	#*************************************************************************************************************
	#************************************************************************************************************* 
	#***********************************ABOVE IS  INTERSECTION D***********************************************


		Single_LaneList_e = []
		Single_IdList_e = []
		for V_index  in range(len(Lane_list)):
			if Lane_list[V_index].find("e") != -1:
				Single_LaneList_e.append(Lane_list[V_index])
				Single_IdList_e.append(Id_List[V_index])
		Id_result,Position_result = get_list(Single_IdList_e,Single_LaneList_e)
		n2=Id_result[0];n1=Id_result[1];      
		e2=Id_result[2];e1=Id_result[3];
		s2=Id_result[4];s1=Id_result[5];
		w2=Id_result[6];w1=Id_result[7];


		if Time_clocke == step:
			casee = Input()
			casee = Input_Addtional(Id_result,Platoon_lengthe)
			Optimiza_result=optimize_av(casee)
			
			temp_e = Speed_Accelerator(Optimiza_result,Id_result)
			D_e = temp_b[0];V0_e = temp_e[1];Vn_e = temp_e[2];a_e = temp_e[3]
			car_accord_e = [0,0,0,0,0,0,0,0]; 
			if n2!=[]:
				car_accord_e[0] = n2[0]
			if n1!=[]:
				car_accord_e[1] = n1[0]
				
			if e2!=[]:
				car_accord_e[2] = e2[0]
			if e1!=[]:
				car_accord_e[3] = e1[0]
					
			if s2!=[]:
				car_accord_e[4] = s2[0]
			if s1!=[]:
				car_accord_e[5] = s1[0]
					
			if w2!=[]:
				car_accord_e[6] = w2[0]
			if w1!=[]:
				car_accord_e[7] = w1[0]
			#####################################################    
			#########################################################

			S_e = []
			P_e = []
			Cycle_e = int(Optimiza_result.cycle)#0~cycle
			Time_clocke=Time_clocke + Cycle_e;
			for value in Optimiza_result.csta:
				S_e.append(value)
			for value in Optimiza_result.cphi:
				P_e.append(value) #八个方向的开始时间；
		if Cycle_e == 0:
			Time_clocke = Time_clocke + 1
		Step_e = Cycle_e - (Time_clocke - step)
		Binary=[0,0,0,0,0,0,0,0];
		for i in range(8):
			if(S_e[i]<=Step_e and S_e[i]+P_e[i]>Step_e):## 其实 bstep_temp 就是step 的代替，如何让现在的step成为
				Binary[i]=1
			else:
				Binary[i]=0                        
		signal_temp=0;
		for i in range(8):
			signal_temp=signal_temp+(2**(7-i))*Binary[i]             
		traci.trafficlight.setPhase("e",signal_temp) 

		if n2!=[]:   
			if car_accord_e[0]==n2[0] and traci.vehicle.getLanePosition(n2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_e[0], Vn_e[0])

		
				
		if n1!=[]:   
			if car_accord_e[1]==n1[0] and traci.vehicle.getLanePosition(n1[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_e[1], Vn_e[1])

				
				
						
		if e2!=[]:
			if car_accord_e[2]==e2[0] and traci.vehicle.getLanePosition(e2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_e[2], Vn_e[2])

       
				
				
		if e1!=[]:
			if car_accord_e[3]==e1[0] and traci.vehicle.getLanePosition(e1[0]) - 5.1 <120:    

				traci.vehicle.setSpeed(car_accord_e[3], Vn_e[3])



								
				
		if s2!=[]:    
			if car_accord_e[4]==s2[0] and traci.vehicle.getLanePosition(s2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_e[4], Vn_e[4])

								
				
		if s1!=[]:
			if car_accord_e[5]==s1[0] and traci.vehicle.getLanePosition(s1[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_e[5], Vn_e[5])

						
		if w2!=[]:    
			if car_accord_e[6]==w2[0] and traci.vehicle.getLanePosition(w2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_e[6], Vn_e[6])



						
				
		if w1!=[]:
			if car_accord_e[7]==w1[0] and traci.vehicle.getLanePosition(w1[0]) - 5.1 <120:

				traci.vehicle.setSpeed( car_accord_e[7], Vn_e[7])

		Platoon_lengthe = Platoon_Intersection(Id_result,Binary)
		Outlist_speedset(Single_IdList_e,Single_LaneList_e)

	#*************************************************************************************************************
	#*************************************************************************************************************
	#************************************************************************************************************* 
	#***********************************ABOVE IS  INTERSECTION E************************************************




		Single_LaneList_f = []
		Single_IdList_f = []
		for V_index  in range(len(Lane_list)):
			if Lane_list[V_index].find("f") != -1:
				Single_LaneList_f.append(Lane_list[V_index])
				Single_IdList_f.append(Id_List[V_index])
		Id_result,Position_result = get_list(Single_IdList_f,Single_LaneList_f)
		n2=Id_result[0];n1=Id_result[1];      
		e2=Id_result[2];e1=Id_result[3];
		s2=Id_result[4];s1=Id_result[5];
		w2=Id_result[6];w1=Id_result[7];


		if Time_clockf == step:
			casef = Input()
			casef = Input_Addtional(Id_result,Platoon_lengthf)
			Optimiza_result=optimize_av(casef)
			
			temp_f = Speed_Accelerator(Optimiza_result,Id_result)
			D_f = temp_b[0];V0_f = temp_f[1];Vn_f = temp_f[2];a_f = temp_f[3]
			car_accord_f = [0,0,0,0,0,0,0,0]; 
			if n2!=[]:
				car_accord_f[0] = n2[0]
			if n1!=[]:
				car_accord_f[1] = n1[0]
				
			if e2!=[]:
				car_accord_f[2] = e2[0]
			if e1!=[]:
				car_accord_f[3] = e1[0]
					
			if s2!=[]:
				car_accord_f[4] = s2[0]
			if s1!=[]:
				car_accord_f[5] = s1[0]
					
			if w2!=[]:
				car_accord_f[6] = w2[0]
			if w1!=[]:
				car_accord_f[7] = w1[0]
			#####################################################    
			#########################################################

			S_f = []
			P_f = []
			Cycle_f = int(Optimiza_result.cycle)#0~cycle
			Time_clockf=Time_clockf + Cycle_f;
			for value in Optimiza_result.csta:
				S_f.append(value)
			for value in Optimiza_result.cphi:
				P_f.append(value) #八个方向的开始时间；
		if Cycle_f == 0:
			Time_clockf = Time_clockf + 1
		Step_f = Cycle_f - (Time_clockf - step)
		Binary=[0,0,0,0,0,0,0,0];
		for i in range(8):
			if(S_f[i]<=Step_f and S_f[i]+P_f[i]>Step_f):## 其实 bstep_temp 就是step 的代替，如何让现在的step成为
				Binary[i]=1
			else:
				Binary[i]=0                        
		signal_temp=0;
		for i in range(8):
			signal_temp=signal_temp+(2**(7-i))*Binary[i]             
		traci.trafficlight.setPhase("f",signal_temp) 
		if n2!=[]:   
			if car_accord_b[0]==n2[0] and traci.vehicle.getLanePosition(n2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_f[0], Vn_f[0])

		
				
		if n1!=[]:   
			if car_accord_b[1]==n1[0] and traci.vehicle.getLanePosition(n1[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_f[1], Vn_f[1])

				
				
						
		if e2!=[]:
			if car_accord_b[2]==e2[0] and traci.vehicle.getLanePosition(e2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_f[2], Vn_f[2])

       
				
				
		if e1!=[]:
			if car_accord_b[3]==e1[0] and traci.vehicle.getLanePosition(e1[0]) - 5.1 <120:    

				traci.vehicle.setSpeed(car_accord_f[3], Vn_f[3])



								
				
		if s2!=[]:    
			if car_accord_b[4]==s2[0] and traci.vehicle.getLanePosition(s2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_f[4], Vn_f[4])

								
				
		if s1!=[]:
			if car_accord_b[5]==s1[0] and traci.vehicle.getLanePosition(s1[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_f[5], Vn_f[5])

						
		if w2!=[]:    
			if car_accord_b[6]==w2[0] and traci.vehicle.getLanePosition(w2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_f[6], Vn_f[6])



						
				
		if w1!=[]:
			if car_accord_b[7]==w1[0] and traci.vehicle.getLanePosition(w1[0]) - 5.1 <120:

				traci.vehicle.setSpeed( car_accord_f[7], Vn_f[7])

		Platoon_lengthf = Platoon_Intersection(Id_result,Binary)
		Outlist_speedset(Single_IdList_f,Single_LaneList_f)

	#*************************************************************************************************************
	#*************************************************************************************************************
	#************************************************************************************************************* 
	#***********************************ABOVE IS  INTERSECTION F************************************************




		Single_LaneList_g = []
		Single_IdList_g = []
		for V_index  in range(len(Lane_list)):
			if Lane_list[V_index].find("g") != -1:
				Single_LaneList_g.append(Lane_list[V_index])
				Single_IdList_g.append(Id_List[V_index])
		Id_result,Position_result = get_list(Single_IdList_g,Single_LaneList_g)
		n2=Id_result[0];n1=Id_result[1];      
		e2=Id_result[2];e1=Id_result[3];
		s2=Id_result[4];s1=Id_result[5];
		w2=Id_result[6];w1=Id_result[7];


		if Time_clockg == step:
			caseg = Input()
			caseg = Input_Addtional(Id_result,Platoon_lengthg)
			Optimiza_result=optimize_av(caseg)
			temp_g = Speed_Accelerator(Optimiza_result,Id_result)
			D_g = temp_g[0];V0_g = temp_g[1];Vn_g = temp_g[2];a_g = temp_g[3]
			car_accord_g = [0,0,0,0,0,0,0,0]; 
			if n2!=[]:
				car_accord_g[0] = n2[0]
			if n1!=[]:
				car_accord_g[1] = n1[0]
				
			if e2!=[]:
				car_accord_g[2] = e2[0]
			if e1!=[]:
				car_accord_g[3] = e1[0]
					
			if s2!=[]:
				car_accord_g[4] = s2[0]
			if s1!=[]:
				car_accord_g[5] = s1[0]
					
			if w2!=[]:
				car_accord_g[6] = w2[0]
			if w1!=[]:
				car_accord_g[7] = w1[0]
			#####################################################    
			#########################################################

			S_g = []
			P_g = []
			Cycle_g = int(Optimiza_result.cycle)#0~cycle
			Time_clockg=Time_clockg + Cycle_g;
			for value in Optimiza_result.csta:
				S_g.append(value)
			for value in Optimiza_result.cphi:
				P_g.append(value) #八个方向的开始时间；
		if Cycle_g == 0:
			Time_clockg = Time_clockg + 1
		Step_g = Cycle_g - (Time_clockg - step)
		Binary=[0,0,0,0,0,0,0,0];
		for i in range(8):
			if(S_g[i]<=Step_g and S_g[i]+P_g[i]>Step_g):## 其实 bstep_temp 就是step 的代替，如何让现在的step成为
				Binary[i]=1
			else:
				Binary[i]=0                        
		signal_temp=0;
		for i in range(8):
			signal_temp=signal_temp+(2**(7-i))*Binary[i]             
		traci.trafficlight.setPhase("g",signal_temp) 
		if n2!=[]:   
			if car_accord_g[0]==n2[0] and traci.vehicle.getLanePosition(n2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_g[0], Vn_g[0])

		
				
		if n1!=[]:   
			if car_accord_g[1]==n1[0] and traci.vehicle.getLanePosition(n1[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_g[1], Vn_g[1])

				
				
						
		if e2!=[]:
			if car_accord_g[2]==e2[0] and traci.vehicle.getLanePosition(e2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_g[2], Vn_g[2])

       
				
				
		if e1!=[]:
			if car_accord_g[3]==e1[0] and traci.vehicle.getLanePosition(e1[0]) - 5.1 <120:    

				traci.vehicle.setSpeed(car_accord_g[3], Vn_g[3])



								
				
		if s2!=[]:    
			if car_accord_g[4]==s2[0] and traci.vehicle.getLanePosition(s2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_g[4], Vn_g[4])

								
				
		if s1!=[]:
			if car_accord_g[5]==s1[0] and traci.vehicle.getLanePosition(s1[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_g[5], Vn_g[5])

						
		if w2!=[]:    
			if car_accord_g[6]==w2[0] and traci.vehicle.getLanePosition(w2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_g[6], Vn_g[6])



						
				
		if w1!=[]:
			if car_accord_g[7]==w1[0] and traci.vehicle.getLanePosition(w1[0]) - 5.1 <120:

				traci.vehicle.setSpeed( car_accord_g[7], Vn_g[7])

		Platoon_lengthg = Platoon_Intersection(Id_result,Binary)
		Outlist_speedset(Single_IdList_g,Single_LaneList_g)

	#*************************************************************************************************************
	#*************************************************************************************************************
	#************************************************************************************************************* 
	#***********************************ABOVE IS  INTERSECTION G************************************************


		Single_LaneList_h = []
		Single_IdList_h = []
		for V_index  in range(len(Lane_list)):
			if Lane_list[V_index].find("h") != -1:
				Single_LaneList_h.append(Lane_list[V_index])
				Single_IdList_h.append(Id_List[V_index])
		Id_result,Position_result = get_list(Single_IdList_h,Single_LaneList_h)
		n2=Id_result[0];n1=Id_result[1];      
		e2=Id_result[2];e1=Id_result[3];
		s2=Id_result[4];s1=Id_result[5];
		w2=Id_result[6];w1=Id_result[7];


		if Time_clockh == step:
			caseh = Input()
			caseh = Input_Addtional(Id_result,Platoon_lengthh)
			Optimiza_result=optimize_av(caseh)
			
			temp_h = Speed_Accelerator(Optimiza_result,Id_result)
			D_h = temp_h[0];V0_h = temp_h[1];Vn_h = temp_h[2];a_h = temp_h[3]
			car_accord_h = [0,0,0,0,0,0,0,0]; 
			if n2!=[]:
				car_accord_h[0] = n2[0]
			if n1!=[]:
				car_accord_h[1] = n1[0]
				
			if e2!=[]:
				car_accord_h[2] = e2[0]
			if e1!=[]:
				car_accord_h[3] = e1[0]
					
			if s2!=[]:
				car_accord_h[4] = s2[0]
			if s1!=[]:
				car_accord_h[5] = s1[0]
					
			if w2!=[]:
				car_accord_h[6] = w2[0]
			if w1!=[]:
				car_accord_h[7] = w1[0]
			#####################################################    
			#########################################################

			S_h = []
			P_h = []
			Cycle_h = int(Optimiza_result.cycle)#0~cycle
			Time_clockh=Time_clockh + Cycle_h;
			for value in Optimiza_result.csta:
				S_h.append(value)
			for value in Optimiza_result.cphi:
				P_h.append(value) #八个方向的开始时间；
		if Cycle_h == 0:
			Time_clockh = Time_clockh + 1
		Step_h = Cycle_h - (Time_clockh - step)
		Binary=[0,0,0,0,0,0,0,0];
		for i in range(8):
			if(S_h[i]<=Step_h and S_h[i]+P_h[i]>Step_h):## 其实 bstep_temp 就是step 的代替，如何让现在的step成为
				Binary[i]=1
			else:
				Binary[i]=0                        
		signal_temp=0;
		for i in range(8):
			signal_temp=signal_temp+(2**(7-i))*Binary[i]             
		traci.trafficlight.setPhase("h",signal_temp) 
		if n2!=[]:   
			if car_accord_h[0]==n2[0] and traci.vehicle.getLanePosition(n2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_h[0], Vn_h[0])

		
				
		if n1!=[]:   
			if car_accord_h[1]==n1[0] and traci.vehicle.getLanePosition(n1[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_h[1], Vn_h[1])

				
				
						
		if e2!=[]:
			if car_accord_h[2]==e2[0] and traci.vehicle.getLanePosition(e2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_h[2], Vn_h[2])

       
				
				
		if e1!=[]:
			if car_accord_h[3]==e1[0] and traci.vehicle.getLanePosition(e1[0]) - 5.1 <120:    

				traci.vehicle.setSpeed(car_accord_h[3], Vn_h[3])



								
				
		if s2!=[]:    
			if car_accord_h[4]==s2[0] and traci.vehicle.getLanePosition(s2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_h[4], Vn_h[4])

								
				
		if s1!=[]:
			if car_accord_h[5]==s1[0] and traci.vehicle.getLanePosition(s1[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_h[5], Vn_h[5])

						
		if w2!=[]:    
			if car_accord_h[6]==w2[0] and traci.vehicle.getLanePosition(w2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_h[6], Vn_h[6])



						
				
		if w1!=[]:
			if car_accord_h[7]==w1[0] and traci.vehicle.getLanePosition(w1[0]) - 5.1 <120:

				traci.vehicle.setSpeed( car_accord_h[7], Vn_h[7])

		Platoon_lengthh = Platoon_Intersection(Id_result,Binary)
		Outlist_speedset(Single_IdList_h,Single_LaneList_h)

	#*************************************************************************************************************
	#*************************************************************************************************************
	#************************************************************************************************************* 
	#***********************************ABOVE IS  INTERSECTION H************************************************



		Single_LaneList_j = []
		Single_IdList_j = []
		for V_index  in range(len(Lane_list)):
			if Lane_list[V_index].find("j") != -1:
				Single_LaneList_j.append(Lane_list[V_index])
				Single_IdList_j.append(Id_List[V_index])
		Id_result,Position_result = get_list(Single_IdList_j,Single_LaneList_j)
		n2=Id_result[0];n1=Id_result[1];      
		e2=Id_result[2];e1=Id_result[3];
		s2=Id_result[4];s1=Id_result[5];
		w2=Id_result[6];w1=Id_result[7];


		if Time_clockj == step:
			casej = Input()
			casej = Input_Addtional(Id_result,Platoon_lengthj)
			Optimiza_result=optimize_av(casej)
			temp_j = Speed_Accelerator(Optimiza_result,Id_result)
			D_j = temp_j[0];V0_j = temp_j[1];Vn_j = temp_j[2];a_j = temp_j[3]
			car_accord_j = [0,0,0,0,0,0,0,0]; 
			if n2!=[]:
				car_accord_j[0] = n2[0]
			if n1!=[]:
				car_accord_j[1] = n1[0]
				
			if e2!=[]:
				car_accord_j[2] = e2[0]
			if e1!=[]:
				car_accord_j[3] = e1[0]
					
			if s2!=[]:
				car_accord_j[4] = s2[0]
			if s1!=[]:
				car_accord_j[5] = s1[0]
					
			if w2!=[]:
				car_accord_j[6] = w2[0]
			if w1!=[]:
				car_accord_j[7] = w1[0]
			#####################################################    
			#########################################################

			S_j = []
			P_j = []
			Cycle_j = int(Optimiza_result.cycle)#0~cycle
			Time_clockj=Time_clockj + Cycle_j;
			for value in Optimiza_result.csta:
				S_j.append(value)
			for value in Optimiza_result.cphi:
				P_j.append(value) #八个方向的开始时间；
		if Cycle_j == 0:
			Time_clockj = Time_clockj + 1
		Step_j = Cycle_j - (Time_clockj - step)
		Binary=[0,0,0,0,0,0,0,0];
		for i in range(8):
			if(S_j[i]<=Step_j and S_j[i]+P_j[i]>Step_j):## 其实 bstep_temp 就是step 的代替，如何让现在的step成为
				Binary[i]=1
			else:
				Binary[i]=0                        
		signal_temp=0;
		for i in range(8):
			signal_temp=signal_temp+(2**(7-i))*Binary[i]             
		traci.trafficlight.setPhase("j",signal_temp) 

		if n2!=[]:   
			if car_accord_j[0]==n2[0] and traci.vehicle.getLanePosition(n2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_j[0], Vn_j[0])

		
				
		if n1!=[]:   
			if car_accord_j[1]==n1[0] and traci.vehicle.getLanePosition(n1[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_j[1], Vn_j[1])

				
				
						
		if e2!=[]:
			if car_accord_j[2]==e2[0] and traci.vehicle.getLanePosition(e2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_j[2], Vn_j[2])

       
				
				
		if e1!=[]:
			if car_accord_j[3]==e1[0] and traci.vehicle.getLanePosition(e1[0]) - 5.1 <120:    

				traci.vehicle.setSpeed(car_accord_j[3], Vn_j[3])



								
				
		if s2!=[]:    
			if car_accord_j[4]==s2[0] and traci.vehicle.getLanePosition(s2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_j[4], Vn_j[4])

								
				
		if s1!=[]:
			if car_accord_j[5]==s1[0] and traci.vehicle.getLanePosition(s1[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_j[5], Vn_j[5])

						
		if w2!=[]:    
			if car_accord_j[6]==w2[0] and traci.vehicle.getLanePosition(w2[0]) - 5.1 <120:

				traci.vehicle.setSpeed(car_accord_j[6], Vn_j[6])



						
				
		if w1!=[]:
			if car_accord_j[7]==w1[0] and traci.vehicle.getLanePosition(w1[0]) - 5.1 <120:

				traci.vehicle.setSpeed( car_accord_j[7], Vn_j[7])

		Platoon_lengthj = Platoon_Intersection(Id_result,Binary)
		Outlist_speedset(Single_IdList_j,Single_LaneList_j)

	#*************************************************************************************************************
	#*************************************************************************************************************
	#************************************************************************************************************* 
	#***********************************ABOVE IS  INTERSECTION I************************************************

	workbook.close()  
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
	traci.start([sumoBinary, "-c", "../cfg/intersection.sumocfg",
							 "--tripinfo-output", "../output/tripinfo.xml",
							 "--queue-output","../output/queue.xml",
							 "--time-to-teleport","100",
							 "--collision.mingap-factor","0"])
	run()