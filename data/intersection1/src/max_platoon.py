from GET_LIST import get_list
import traci

def Platoon_Intersection(IDLlist):
    IDList = traci.vehicle.getIDList()  
    IDList_result=get_list(IDList)
    n2=IDList_result[0];n1=IDList_result[1];      
    e2=IDList_result[2];e1=IDList_result[3];
    s2=IDList_result[4];s1=IDList_result[5];
    w2=IDList_result[6];w1=IDList_result[7];    
    if len(s1)>=2:
    	if traci.vehicle.getLength(s1[0])<40:        
    	    if traci.vehicle.getDistance(s1[0])-traci.vehicle.getDistance(s1[1])<=20+traci.vehicle.getLength(s1[0]) and traci.vehicle.getSpeed(s1[0])<=5 and traci.vehicle.getDistance(s1[0])>100:
              temp_length=traci.vehicle.getLength(s1[0])+traci.vehicle.getLength(s1[1])+5                                                                                                 
    		    traci.vehicle.remove(s1[1])
    		    traci.vehicle.setLength(s1[0],temp_length)     
    	else:
    	    if traci.vehicle.getDistance(s1[0])-traci.vehicle.getDistance(s1[1])<=20+traci.vehicle.getLength(s1[0]) and traci.vehicle.getSpeed(s1[0])<=5 and traci.vehicle.getDistance(s1[0])>100:
              temp_length=traci.vehicle.getLength(s1[0])+traci.vehicle.getLength(s1[1])+5                                                                                                 
    		    traci.vehicle.remove(s1[1])
    		    traci.vehicle.setLength(s1[0],temp_length)              
    
    if len(s2)>=2:
    	if traci.vehicle.getDistance(s2[0])-traci.vehicle.getDistance(s2[1])<=20+traci.vehicle.getLength(s2[0]) and traci.vehicle.getSpeed(s2[0])<=5 and traci.vehicle.getDistance(s2[0])>100:
    		temp_length=traci.vehicle.getLength(s2[0])+traci.vehicle.getLength(s2[1])+5
    		traci.vehicle.remove(s2[1])
    		traci.vehicle.setLength(s2[0],temp_length)         
     
    if len(w1)>=2:
    	if traci.vehicle.getDistance(w1[0])-traci.vehicle.getDistance(w1[1])<=20+traci.vehicle.getLength(w1[0]) and traci.vehicle.getSpeed(w1[0])<=5 and traci.vehicle.getDistance(w1[0])>100:
    		temp_length=traci.vehicle.getLength(w1[0])+traci.vehicle.getLength(w1[1])+5
    		traci.vehicle.remove(w1[1])
    		traci.vehicle.setLength(w1[0],temp_length) 
     
    if len(w2)>=2:
    	if traci.vehicle.getDistance(w2[0])-traci.vehicle.getDistance(w2[1])<=20+traci.vehicle.getLength(w2[0]) and traci.vehicle.getSpeed(w2[0])<=5 and traci.vehicle.getDistance(w2[0])>100:
    		temp_length=traci.vehicle.getLength(w2[0])+traci.vehicle.getLength(w2[1])+5
    		traci.vehicle.remove(w2[1])
    		traci.vehicle.setLength(w2[0],temp_length) 
           
    if len(n1)>=2:
    	if traci.vehicle.getDistance(n1[0])-traci.vehicle.getDistance(n1[1])<=20+traci.vehicle.getLength(n1[0]) and traci.vehicle.getSpeed(n1[0])<=5 and traci.vehicle.getDistance(n1[0])>100:
    		temp_length=traci.vehicle.getLength(n1[0])+traci.vehicle.getLength(n1[1])+5
    		traci.vehicle.remove(n1[1])
    		traci.vehicle.setLength(n1[0],temp_length)        
     
    if len(n2)>=2:
    	if traci.vehicle.getDistance(n2[0])-traci.vehicle.getDistance(n2[1])<=20+traci.vehicle.getLength(n2[0]) and traci.vehicle.getSpeed(n2[0])<=5 and traci.vehicle.getDistance(n2[0])>100:
    		temp_length=traci.vehicle.getLength(n2[0])+traci.vehicle.getLength(n2[1])+5
    		traci.vehicle.remove(n2[1])
    		traci.vehicle.setLength(n2[0],temp_length)         
      
    if len(e1)>=2:
    	if traci.vehicle.getDistance(e1[0])-traci.vehicle.getDistance(e1[1])<=20+traci.vehicle.getLength(e1[0]) and traci.vehicle.getSpeed(e1[0])<=5 and traci.vehicle.getDistance(e1[0])>100:
    		temp_length=traci.vehicle.getLength(e1[0])+traci.vehicle.getLength(e1[1])+5
    		traci.vehicle.remove(e1[1])
    		traci.vehicle.setLength(e1[0],temp_length) 
    
    if len(e2)>=2:
    	if traci.vehicle.getDistance(e2[0])-traci.vehicle.getDistance(e2[1])<=20+traci.vehicle.getLength(e2[0]) and traci.vehicle.getSpeed(e2[0])<=5 and traci.vehicle.getDistance(e2[0])>100:
    		temp_length=traci.vehicle.getLength(e2[0])+traci.vehicle.getLength(e2[1])+5
    		traci.vehicle.remove(e2[1])
    		traci.vehicle.setLength(e2[0],temp_length)