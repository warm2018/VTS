import traci

def Platoon_Intersection(IDList_result,Binary):
    n=3
    mingap = 1.5
    length = 10*n-5
    Lane_length = 150
    n2=IDList_result[0];n1=IDList_result[1];      
    e2=IDList_result[2];e1=IDList_result[3];
    s2=IDList_result[4];s1=IDList_result[5];
    w2=IDList_result[6];w1=IDList_result[7];
    Platoon_number = [0,0,0,0,0,0,0,0]
    Platoon_member = []
    Platoon_length = [0,0,0,0,0,0,0,0]    
#    if len(s1)>=2:
#    	if traci.vehicle.getDistance(s1[0])-traci.vehicle.getDistance(s1[1])<=20+traci.vehicle.getLength(s1[0]) and traci.vehicle.getSpeed(s1[0])<=5 and traci.vehicle.getDistance(s1[0])>100:
#    		temp_length=traci.vehicle.getLength(s1[0])+traci.vehicle.getLength(s1[1])+5                                                                                                 
#    		traci.vehicle.remove(s1[1])
#    		traci.vehicle.setLength(s1[0],temp_length)     
#################################################################################################################       
#################################################################################################################   
#######s1
# 对每条车道上的车队进行组队，形成火车
    if len(s1) >= 1:
        Platoon_length[5] = traci.vehicle.getLength(s1[0])
        Platoon_number[5] = 1
    if len(s1) >= 2 and Platoon_number[5] <= 8:
        Platoon_member5 = []
        if traci.vehicle.getLanePosition(s1[0])- traci.vehicle.getLanePosition(s1[1]) <= 20 :
            traci.vehicle.setMinGap(s1[1],mingap)
            Platoon_length[5] = traci.vehicle.getLength(s1[0]) + mingap + traci.vehicle.getLength(s1[1])
            Platoon_number[5] = 2
            Platoon_member5.append(s1[0])
            Platoon_member5.append(s1[1])

        if len(s1) >=3 and Platoon_number[5] >= 2 :
            if traci.vehicle.getLanePosition(s1[1]) - traci.vehicle.getLanePosition(s1[2]) <= 20 :
                traci.vehicle.setMinGap(s1[2],mingap)
                Platoon_length[5] = Platoon_length[5] + traci.vehicle.getLength(s1[2]) + mingap
                Platoon_number[5] = 3
                Platoon_member5.append(s1[2])

        if len(s1) >= 4 and Platoon_number[5] >= 3:
            if traci.vehicle.getLanePosition(s1[2]) - traci.vehicle.getLanePosition(s1[3]) <= 20 :
                traci.vehicle.setMinGap(s1[3],mingap)
                Platoon_length[5] = Platoon_length[5] + traci.vehicle.getLength(s1[3]) + mingap 
                Platoon_number[5] = 4
                Platoon_member5.append(s1[3])

        if len(s1) >= 5 and Platoon_number[5] >= 4:
            if traci.vehicle.getLanePosition(s1[3]) - traci.vehicle.getLanePosition(s1[4]) <= 20:
                traci.vehicle.setMinGap(s1[4],mingap)
                Platoon_length[5] = Platoon_length[5] + traci.vehicle.getLength(s1[4]) + mingap 
                Platoon_number[5] = 5 
                Platoon_member5.append(s1[4])

        if len(s1) >= 6 and Platoon_number[5] >= 5 :
            if traci.vehicle.getLanePosition(s1[4]) - traci.vehicle.getLanePosition(s1[5]) <= 20 :
                traci.vehicle.setMinGap(s1[5],mingap)
                Platoon_length[5] = Platoon_length[5] + traci.vehicle.getLength(s1[5]) + mingap
                Platoon_number[5] = 6 
                Platoon_member5.append(s1[5])
        if len(s1) >= 7 and Platoon_number[5] >= 6 :
            if traci.vehicle.getLanePosition(s1[5]) - traci.vehicle.getLanePosition(s1[6]) <= 20 :
                traci.vehicle.setMinGap(s1[6],mingap)
                Platoon_length[5] = Platoon_length[5] + traci.vehicle.getLength(s1[6]) + mingap
                Platoon_number[5] = 7 
                Platoon_member5.append(s1[6])
        if len(s1) >= 8 and Platoon_number[5] >= 7:
            if traci.vehicle.getLanePosition(s1[6]) - traci.vehicle.getLanePosition(s1[7]) <= 20 :
                traci.vehicle.setMinGap(s1[7],mingap)
                Platoon_length[5] = Platoon_length[5] + traci.vehicle.getLength(s1[7]) + mingap
                Platoon_number[5] = 8 
                Platoon_member5.append(s1[7])
        if Platoon_number[5] >= 1 and Binary[5] == 1:
            for vehicle in Platoon_member5:
                traci.vehicle.setSpeedMode(vehicle,22)
                traci.vehicle.setSpeed(vehicle,8)
                traci.vehicle.setAccel(vehicle,2)
        if Binary[5] != 1:
            for vehicle in Platoon_member5:
                traci.vehicle.setSpeedMode(vehicle,31)  
#*********************************ONE Approach********************************************
#*****************************************************************************************
    if len(s2) >= 1 :
        Platoon_length[4] = traci.vehicle.getLength(s2[0])
        Platoon_number[4] = 1
    if len(s2) >= 2 and Platoon_number[4] <= 8:
        Platoon_member4 = []
        if traci.vehicle.getLanePosition(s2[0]) - traci.vehicle.getLanePosition(s2[1]) <= 15 :
            traci.vehicle.setMinGap(s2[1],mingap)
            Platoon_length[4] = traci.vehicle.getLength(s2[0]) + mingap + traci.vehicle.getLength(s2[1])
            Platoon_number[4] = 2
            Platoon_member4.append(s2[0])
            Platoon_member4.append(s2[1])

        if len(s2) >=3  and Platoon_number[4] >= 2:
            if traci.vehicle.getLanePosition(s2[1]) - traci.vehicle.getLanePosition(s2[2]) <= 15 :
                traci.vehicle.setMinGap(s2[2],mingap)
                Platoon_length[4] = Platoon_length[4] + traci.vehicle.getLength(s2[2]) + mingap
                Platoon_number[4] = 3
                Platoon_member4.append(s2[2])

        if len(s2) >= 4 and Platoon_number[4] >= 3 :
            if traci.vehicle.getLanePosition(s2[2]) - traci.vehicle.getLanePosition(s2[3]) <= 15 :
                traci.vehicle.setMinGap(s2[3],mingap)
                Platoon_length[4] = Platoon_length[4] + traci.vehicle.getLength(s2[3]) + mingap 
                Platoon_number[4] = 4
                Platoon_member4.append(s2[3])

        if len(s2) >= 5 and Platoon_number[4] >= 4:
            if traci.vehicle.getLanePosition(s2[3]) - traci.vehicle.getLanePosition(s2[4]) <= 15 :
                traci.vehicle.setMinGap(s2[4],mingap)
                Platoon_length[4] = Platoon_length[4] + traci.vehicle.getLength(s2[4]) + mingap 
                Platoon_number[4] = 5 
                Platoon_member4.append(s2[4])

        if len(s2) >= 6 and Platoon_number[4] >= 5 :
            if traci.vehicle.getLanePosition(s2[4]) - traci.vehicle.getLanePosition(s2[5]) <= 15 :
                traci.vehicle.setMinGap(s2[5],mingap)
                Platoon_length[4] = Platoon_length[4] + traci.vehicle.getLength(s2[5]) + mingap
                Platoon_number[4] = 6 
                Platoon_member4.append(s2[5])
        if len(s2) >= 7 and Platoon_number[4] >= 6:
            if traci.vehicle.getLanePosition(s2[5]) - traci.vehicle.getLanePosition(s2[6]) <= 15 :
                traci.vehicle.setMinGap(s2[6],mingap)
                Platoon_length[4] = Platoon_length[4] + traci.vehicle.getLength(s2[6]) + mingap
                Platoon_number[4] = 7 
                Platoon_member4.append(s2[6])
        if len(s2) >= 8 and Platoon_number[4] >= 7:
            if traci.vehicle.getLanePosition(s2[6]) - traci.vehicle.getLanePosition(s2[7]) <= 15 :
                traci.vehicle.setMinGap(s2[7],mingap)
                Platoon_length[4] = Platoon_length[4] + traci.vehicle.getLength(s2[7]) + mingap
                Platoon_number[4] = 8 
                Platoon_member4.append(s2[7])
        if Platoon_number[4] >= 1 and Binary[4] == 1:
            for vehicle in Platoon_member4:
                traci.vehicle.setSpeedMode(vehicle,22)
                traci.vehicle.setSpeed(vehicle,8)
                traci.vehicle.setAccel(vehicle,2)
        if Binary[4] != 1:
            for vehicle in Platoon_member4:
                traci.vehicle.setSpeedMode(vehicle,31)          
#*********************************ONE Approach********************************************
#*****************************************************************************************
    if len(w1) >= 1 :
        Platoon_length[7] = traci.vehicle.getLength(w1[0])
        Platoon_number[7] = 1
    if len(w1) >= 2 and Platoon_number[7] <= 8:
        Platoon_member7 = []
        if traci.vehicle.getLanePosition(w1[0]) - traci.vehicle.getLanePosition(w1[1]) <= 15 :
            traci.vehicle.setMinGap(w1[1],mingap)
            Platoon_length[7] = traci.vehicle.getLength(w1[0]) + mingap + traci.vehicle.getLength(w1[1])
            Platoon_number[7] = 2
            Platoon_member7.append(w1[0])
            Platoon_member7.append(w1[1])

        if len(w1) >=3 and Platoon_number[7] >= 2:
            if traci.vehicle.getLanePosition(w1[1]) - traci.vehicle.getLanePosition(w1[2]) <= 15 :
                traci.vehicle.setMinGap(w1[2],mingap)
                Platoon_length[7] = Platoon_length[7] + traci.vehicle.getLength(w1[2]) + mingap
                Platoon_number[7] = 3
                Platoon_member7.append(w1[2])

        if len(w1) >= 4 and Platoon_number[7] >= 3:
            if traci.vehicle.getLanePosition(w1[2]) - traci.vehicle.getLanePosition(w1[3]) <= 15 :
                traci.vehicle.setMinGap(w1[3],mingap)
                Platoon_length[7] = Platoon_length[7] + traci.vehicle.getLength(w1[3]) + mingap 
                Platoon_number[7] = 4
                Platoon_member7.append(w1[3])

        if len(w1) >= 5 and Platoon_number[7] >= 4:
            if traci.vehicle.getLanePosition(w1[3]) - traci.vehicle.getLanePosition(w1[4]) <= 15 :
                traci.vehicle.setMinGap(w1[4],mingap)
                Platoon_length[7] = Platoon_length[7] + traci.vehicle.getLength(w1[4]) + mingap 
                Platoon_number[7] = 5 
                Platoon_member7.append(w1[4])

        if len(w1) >= 6 and Platoon_number[7] >= 5 :
            if traci.vehicle.getLanePosition(w1[4]) - traci.vehicle.getLanePosition(w1[5]) <= 15 :
                traci.vehicle.setMinGap(w1[5],mingap)
                Platoon_length[7] = Platoon_length[7] + traci.vehicle.getLength(w1[5]) + mingap
                Platoon_number[7] = 6 
                Platoon_member7.append(w1[5])
        if len(w1) >= 7 and Platoon_number[7] >= 6:
            if traci.vehicle.getLanePosition(w1[5]) - traci.vehicle.getLanePosition(w1[6]) <= 15 :
                traci.vehicle.setMinGap(w1[6],mingap)
                Platoon_length[7] = Platoon_length[7] + traci.vehicle.getLength(w1[6]) + mingap
                Platoon_number[7] = 7 
                Platoon_member7.append(w1[6])
        if len(w1) >= 8 and Platoon_number[7] >= 7:
            if traci.vehicle.getLanePosition(w1[6]) - traci.vehicle.getLanePosition(w1[7]) <= 15 :
                traci.vehicle.setMinGap(w1[7],mingap)
                Platoon_length[7] = Platoon_length[7] + traci.vehicle.getLength(w1[7]) + mingap
                Platoon_number[7] = 8 
                Platoon_member7.append(w1[7])
        if Platoon_number[7] >= 1 and Binary[7] == 1:
            for vehicle in Platoon_member7:
                traci.vehicle.setSpeedMode(vehicle,22)
                traci.vehicle.setSpeed(vehicle,8)
                traci.vehicle.setAccel(vehicle,2)
        if Binary[7] != 1:
            for vehicle in Platoon_member7:
                traci.vehicle.setSpeedMode(vehicle,31)  
#*********************************ONE Approach********************************************
#*****************************************************************************************
    if len(w2) >= 1 :
        Platoon_length[6] = traci.vehicle.getLength(w2[0])
        Platoon_number[6] = 1       
    if len(w2) >= 2 and Platoon_number[6] <= 8:
        Platoon_member6 = []
        if traci.vehicle.getLanePosition(w2[0]) - traci.vehicle.getLanePosition(w2[1]) <= 15 :
            traci.vehicle.setMinGap(w2[1],mingap)
            Platoon_length[6] = traci.vehicle.getLength(w2[0]) + mingap + traci.vehicle.getLength(w2[1])
            Platoon_number[6] = 2
            Platoon_member6.append(w2[0])
            Platoon_member6.append(w2[1])

        if len(w2) >=3 and Platoon_number[6] >= 2:
            if traci.vehicle.getLanePosition(w2[1]) - traci.vehicle.getLanePosition(w2[2]) <= 15 :
                traci.vehicle.setMinGap(w2[2],mingap)
                Platoon_length[6] = Platoon_length[6] + traci.vehicle.getLength(w2[2]) + mingap
                Platoon_number[6] = 3
                Platoon_member6.append(w2[2])

        if len(w2) >=4 and Platoon_number[6] >= 3:
            if traci.vehicle.getLanePosition(w2[2]) - traci.vehicle.getLanePosition(w2[3]) <= 15 :
                traci.vehicle.setMinGap(w2[3],mingap)
                Platoon_length[6] = Platoon_length[6] + traci.vehicle.getLength(w2[3]) + mingap 
                Platoon_number[6] = 4
                Platoon_member6.append(w2[3])

        if len(w2) >=5 and Platoon_number[6] >= 4:
            if traci.vehicle.getLanePosition(w2[3]) - traci.vehicle.getLanePosition(w2[4]) <= 15 :
                traci.vehicle.setMinGap(w2[4],mingap)
                Platoon_length[6] = Platoon_length[6] + traci.vehicle.getLength(w2[4]) + mingap 
                Platoon_number[6] = 5 
                Platoon_member6.append(w2[4])

        if len(w2) >= 6 and Platoon_number[6] >= 5:
            if traci.vehicle.getLanePosition(w2[4]) - traci.vehicle.getLanePosition(w2[5]) <= 15 :
                traci.vehicle.setMinGap(w2[5],mingap)
                Platoon_length[6] = Platoon_length[6] + traci.vehicle.getLength(w2[5]) + mingap
                Platoon_number[6] = 6 
                Platoon_member6.append(w2[5])
        if len(w2) >=7 and Platoon_number[6] >= 6:
            if traci.vehicle.getLanePosition(w2[5]) - traci.vehicle.getLanePosition(w2[6]) <= 15 :
                traci.vehicle.setMinGap(w2[6],mingap)
                Platoon_length[6] = Platoon_length[6] + traci.vehicle.getLength(w2[6]) + mingap
                Platoon_number[6] = 7 
                Platoon_member6.append(w2[6])
        if len(w2) >=8 and Platoon_number[6] >= 7:
            if traci.vehicle.getLanePosition(w2[6]) - traci.vehicle.getLanePosition(w2[7]) <= 15 :
                traci.vehicle.setMinGap(w2[7],mingap)
                Platoon_length[6] = Platoon_length[6] + traci.vehicle.getLength(w2[7]) + mingap
                Platoon_number[6] = 8 
                Platoon_member6.append(w2[7])
        if Platoon_number[6] >= 1 and Binary[6] == 1:
            for vehicle in Platoon_member6:
                traci.vehicle.setSpeedMode(vehicle,22)
                traci.vehicle.setSpeed(vehicle,8)
                traci.vehicle.setAccel(vehicle,2)
        if Binary[6] != 1:
            for vehicle in Platoon_member6:
                traci.vehicle.setSpeedMode(vehicle,31)  
#*********************************ONE Approach********************************************
#*****************************************************************************************
          
#######n1 
    if len(n1) >= 1:
        Platoon_length[1] = traci.vehicle.getLength(n1[0])
        Platoon_number[1] = 1        
    if len(n1) >= 2 and Platoon_number[1] <= 8:
        Platoon_member1 = []        
        if traci.vehicle.getLanePosition(n1[0]) - traci.vehicle.getLanePosition(n1[1]) <= 15 :
            traci.vehicle.setMinGap(n1[1],mingap)
            Platoon_length[1] = traci.vehicle.getLength(n1[0]) + mingap + traci.vehicle.getLength(n1[1])
            Platoon_number[1] = 2
            Platoon_member1.append(n1[0])
            Platoon_member1.append(n1[1])

        if len(n1) >=3 and Platoon_number[1] >= 2:
            if traci.vehicle.getLanePosition(n1[1]) - traci.vehicle.getLanePosition(n1[2]) <= 15 :
                traci.vehicle.setMinGap(n1[2],mingap)
                Platoon_length[1] = Platoon_length[1] + traci.vehicle.getLength(n1[2]) + mingap
                Platoon_number[1] = 3
                Platoon_member1.append(n1[2])

        if len(n1) >= 4 and Platoon_number[1] >= 3:
            if traci.vehicle.getLanePosition(n1[2]) - traci.vehicle.getLanePosition(n1[3]) <= 15 :
                traci.vehicle.setMinGap(n1[3],mingap)
                Platoon_length[1] = Platoon_length[1] + traci.vehicle.getLength(n1[3]) + mingap 
                Platoon_number[1] = 4
                Platoon_member1.append(n1[3])

        if len(n1) >= 5 and Platoon_number[1] >= 4:
            if traci.vehicle.getLanePosition(n1[3]) - traci.vehicle.getLanePosition(n1[4]) <= 15:
                traci.vehicle.setMinGap(n1[4],mingap)
                Platoon_length[1] = Platoon_length[1] + traci.vehicle.getLength(n1[4]) + mingap 
                Platoon_number[1] = 5 
                Platoon_member1.append(n1[4])

        if len(n1) >= 6 and Platoon_number[1] >= 5:
            if traci.vehicle.getLanePosition(n1[4]) - traci.vehicle.getLanePosition(n1[5]) <= 15 :
                traci.vehicle.setMinGap(n1[5],mingap)
                Platoon_length[1] = Platoon_length[1] + traci.vehicle.getLength(n1[5]) + mingap
                Platoon_number[1] = 6 
                Platoon_member1.append(n1[5])
        if len(n1) >= 7 and Platoon_number[1] >= 6:
            if traci.vehicle.getLanePosition(n1[5]) - traci.vehicle.getLanePosition(n1[6]) <= 15 :
                traci.vehicle.setMinGap(n1[6],mingap)
                Platoon_length[1] = Platoon_length[1] + traci.vehicle.getLength(n1[6]) + mingap
                Platoon_number[1] = 7 
                Platoon_member1.append(n1[6])
        if len(n1) >= 8 and Platoon_number[1] >= 7:
            if traci.vehicle.getLanePosition(n1[6]) - traci.vehicle.getLanePosition(n1[7]) <= 15 :
                traci.vehicle.setMinGap(n1[7],mingap)
                Platoon_length[1] = Platoon_length[1] + traci.vehicle.getLength(n1[7]) + mingap
                Platoon_number[1] = 8 
                Platoon_member1.append(n1[7])
        if Platoon_number[1] >= 1 and Binary[1] == 1:
            for vehicle in Platoon_member1:
                traci.vehicle.setSpeedMode(vehicle,22)
                traci.vehicle.setSpeed(vehicle,8)
                traci.vehicle.setAccel(vehicle,2)
        if Binary[1] != 1:
            for vehicle in Platoon_member1:
                traci.vehicle.setSpeedMode(vehicle,31)  
#*********************************ONE Approach********************************************
#*****************************************************************************************
          
#######n2
    if len(n2) >= 1:
        Platoon_length[0] = traci.vehicle.getLength(n2[0])
        Platoon_number[0] = 1         
        if len(n2) >= 2 and Platoon_number[0] <= 8:
            Platoon_member0 = []
            if traci.vehicle.getLanePosition(n2[0]) - traci.vehicle.getLanePosition(n2[1]) <= 20 :
                traci.vehicle.setMinGap(n2[1],mingap)
                Platoon_length[0] = traci.vehicle.getLength(n2[0]) + mingap + traci.vehicle.getLength(n2[1])
                Platoon_number[0] = 2
                Platoon_member0.append(n2[0])
                Platoon_member0.append(n2[1])

            if len(n2) >=3 and Platoon_number[0] >= 2:
                if traci.vehicle.getLanePosition(n2[1]) - traci.vehicle.getLanePosition(n2[2]) <= 20 :
                    traci.vehicle.setMinGap(n2[2],mingap)
                    Platoon_length[0] = Platoon_length[0] + traci.vehicle.getLength(n2[2]) + mingap
                    Platoon_number[0] = 3
                    Platoon_member0.append(n2[2])

            if len(n2) >= 4 and Platoon_number[0] >= 3:
                if traci.vehicle.getLanePosition(n2[2]) - traci.vehicle.getLanePosition(n2[3]) <= 20 :
                    traci.vehicle.setMinGap(n2[3],mingap)
                    Platoon_length[0] = Platoon_length[0] + traci.vehicle.getLength(n2[3]) + mingap 
                    Platoon_number[0] = 4
                    Platoon_member0.append(n2[3])
            if len(n2) >= 5 and Platoon_number[0] >= 4:
                if traci.vehicle.getLanePosition(n2[3]) - traci.vehicle.getLanePosition(n2[4]) <= 20 :
                    traci.vehicle.setMinGap(n2[4],mingap)
                    Platoon_length[0] = Platoon_length[0] + traci.vehicle.getLength(n2[4]) + mingap 
                    Platoon_number[0] = 5 
                    Platoon_member0.append(n2[4])

            if len(n2) >= 6 and Platoon_number[0] >= 5:
                if traci.vehicle.getLanePosition(n2[4]) - traci.vehicle.getLanePosition(n2[5]) <= 20 :
                    traci.vehicle.setMinGap(n2[5],mingap)
                    Platoon_length[0] = Platoon_length[0] + traci.vehicle.getLength(n2[5]) + mingap
                    Platoon_number[0] = 6 
                    Platoon_member0.append(n2[5])
            if len(n2) >= 7 and Platoon_number[0] >= 6:
                if traci.vehicle.getLanePosition(n2[5]) - traci.vehicle.getLanePosition(n2[6]) <= 20 :
                    traci.vehicle.setMinGap(n2[6],mingap)
                    Platoon_length[0] = Platoon_length[0] + traci.vehicle.getLength(n2[6]) + mingap
                    Platoon_number[0] = 7 
                    Platoon_member0.append(n2[6])
            if len(n2) >= 8 and Platoon_number[0] >= 7:
                if traci.vehicle.getLanePosition(n2[6]) - traci.vehicle.getLanePosition(n2[7]) <= 20 :
                    traci.vehicle.setMinGap(n2[7],mingap)
                    Platoon_length[0] = Platoon_length[0] + traci.vehicle.getLength(n2[7]) + mingap
                    Platoon_number[0] = 8 
                    Platoon_member0.append(n2[7])
            if Platoon_number[0] >= 1 and Binary[0] == 1:
                for vehicle in Platoon_member0:
                    traci.vehicle.setSpeedMode(vehicle,22)
                    traci.vehicle.setSpeed(vehicle,8)
                    traci.vehicle.setAccel(vehicle,2)
            if Binary[0] != 1:
                for vehicle in Platoon_member0:
                    traci.vehicle.setSpeedMode(vehicle,31)  
#*********************************ONE Approach********************************************
#*****************************************************************************************
      

            
#######e1
    if len(e1) >= 1:
        Platoon_length[3] = traci.vehicle.getLength(e1[0])
        Platoon_number[3] = 1         
    if len(e1) >= 2 and Platoon_number[3] <= 8:
        Platoon_member3 = []
        if traci.vehicle.getLanePosition(e1[0]) - traci.vehicle.getLanePosition(e1[1]) <= 15 :
            traci.vehicle.setMinGap(e1[1],mingap)
            Platoon_length[3] = traci.vehicle.getLength(e1[0]) + mingap + traci.vehicle.getLength(e1[1])
            Platoon_number[3] = 2
            Platoon_member3.append(e1[0])
            Platoon_member3.append(e1[1])

        if len(e1) >=3 and Platoon_number[3] >= 2:
            if traci.vehicle.getLanePosition(e1[1]) - traci.vehicle.getLanePosition(e1[2]) <= 15 :
                traci.vehicle.setMinGap(e1[2],mingap)
                Platoon_length[3] = Platoon_length[3] + traci.vehicle.getLength(e1[2]) + mingap
                Platoon_number[3] = 3
                Platoon_member3.append(e1[2])

        if len(e1) >= 4 and Platoon_number[3] >= 3:
            if traci.vehicle.getLanePosition(e1[2]) - traci.vehicle.getLanePosition(e1[3]) <= 15 :
                traci.vehicle.setMinGap(e1[3],mingap)
                Platoon_length[3] = Platoon_length[3] + traci.vehicle.getLength(e1[3]) + mingap 
                Platoon_number[3] = 4
                Platoon_member3.append(e1[3])

        if len(e1) >= 5 and Platoon_number[3] >= 4:
            if traci.vehicle.getLanePosition(e1[3]) - traci.vehicle.getLanePosition(e1[4]) <= 15:
                traci.vehicle.setMinGap(e1[4],mingap)
                Platoon_length[3] = Platoon_length[3] + traci.vehicle.getLength(e1[4]) + mingap 
                Platoon_number[3] = 5 
                Platoon_member3.append(e1[4])

        if len(e1) >= 6 and Platoon_number[3] >= 5:
            if traci.vehicle.getLanePosition(e1[4]) - traci.vehicle.getLanePosition(e1[5]) <= 15 :
                traci.vehicle.setMinGap(e1[5],mingap)
                Platoon_length[3] = Platoon_length[3] + traci.vehicle.getLength(e1[5]) + mingap
                Platoon_number[3] = 6 
                Platoon_member3.append(e1[5])
        if len(e1) >= 7 and Platoon_number[3] >= 6:
            if traci.vehicle.getLanePosition(e1[5]) - traci.vehicle.getLanePosition(e1[6]) <= 15 :
                traci.vehicle.setMinGap(e1[6],mingap)
                Platoon_length[3] = Platoon_length[3] + traci.vehicle.getLength(e1[6]) + mingap
                Platoon_number[3] = 7 
                Platoon_member3.append(e1[6])
        if len(e1) >= 8 and Platoon_number[3] >= 7:
            if traci.vehicle.getLanePosition(e1[6]) - traci.vehicle.getLanePosition(e1[7]) <= 15:
                traci.vehicle.setMinGap(e1[7],mingap)
                Platoon_length[3] = Platoon_length[3] + traci.vehicle.getLength(e1[7]) + mingap
                Platoon_number[3] = 8 
                Platoon_member3.append(e1[7])
        if Platoon_number[3] >= 1 and Binary[3] == 1:
            for vehicle in Platoon_member3:
                traci.vehicle.setSpeedMode(vehicle,22)
                traci.vehicle.setSpeed(vehicle,8)
                traci.vehicle.setAccel(vehicle,2)
        if Binary[3] != 1:
            for vehicle in Platoon_member3:
                traci.vehicle.setSpeedMode(vehicle,31)  
#*********************************ONE Approach********************************************
#*****************************************************************************************
          
#######e2
    if len(e2) >= 1 :
        Platoon_length[2] = traci.vehicle.getLength(e2[0])
        Platoon_number[2] = 1         
    if len(e2) >= 2 and Platoon_number[2] <= 8:
        Platoon_member2 = []
        if traci.vehicle.getLanePosition(e2[0]) - traci.vehicle.getLanePosition(e2[1]) <= 15:
            traci.vehicle.setMinGap(e2[1],mingap)
            Platoon_length[2] = traci.vehicle.getLength(e2[0]) + mingap + traci.vehicle.getLength(e2[1])
            Platoon_number[2] = 2
            Platoon_member2.append(e2[0])
            Platoon_member2.append(e2[1])

        if len(e2) >=3 and Platoon_number[2] >= 2:
            if traci.vehicle.getLanePosition(e2[1]) - traci.vehicle.getLanePosition(e2[2]) <= 15 :
                traci.vehicle.setMinGap(e2[2],mingap)
                Platoon_length[2] = Platoon_length[2] + traci.vehicle.getLength(e2[2]) + mingap
                Platoon_number[2] = 3
                Platoon_member2.append(e2[2])

        if len(e2) >= 4 and Platoon_number[2] >= 3:
            if traci.vehicle.getLanePosition(e2[2]) - traci.vehicle.getLanePosition(e2[3]) <= 15 :
                traci.vehicle.setMinGap(e2[3],mingap)
                Platoon_length[2] = Platoon_length[2] + traci.vehicle.getLength(e2[3]) + mingap 
                Platoon_number[2] = 4
                Platoon_member2.append(e2[3])

        if len(e2) >= 5 and Platoon_number[2] >= 4:
            if traci.vehicle.getLanePosition(e2[3]) - traci.vehicle.getLanePosition(e2[4]) <= 15:
                traci.vehicle.setMinGap(e2[4],mingap)
                Platoon_length[2] = Platoon_length[2] + traci.vehicle.getLength(e2[4]) + mingap 
                Platoon_number[2] = 5 
                Platoon_member2.append(e2[4])

        if len(e2) >= 6 and Platoon_number[2] >= 5:
            if traci.vehicle.getLanePosition(e2[4]) - traci.vehicle.getLanePosition(e2[5]) <= 15:
                traci.vehicle.setMinGap(e2[5],mingap)
                Platoon_length[2] = Platoon_length[2] + traci.vehicle.getLength(e2[5]) + mingap
                Platoon_number[2] = 6 
                Platoon_member2.append(e2[5])
        if len(e2) >= 7 and Platoon_number[2] >= 6:
            if traci.vehicle.getLanePosition(e2[5]) - traci.vehicle.getLanePosition(e2[6]) <= 15 :
                traci.vehicle.setMinGap(e2[6],mingap)
                Platoon_length[2] = Platoon_length[2] + traci.vehicle.getLength(e2[6]) + mingap
                Platoon_number[2] = 7 
                Platoon_member2.append(e2[6])
        if len(e2) >= 8 and Platoon_number[2] >= 7:
            if traci.vehicle.getLanePosition(e2[6]) - traci.vehicle.getLanePosition(e2[7]) <= 15 :
                traci.vehicle.setMinGap(e2[7],mingap)
                Platoon_length[2] = Platoon_length[2] + traci.vehicle.getLength(e2[7]) + mingap
                Platoon_number[2] = 8 
                Platoon_member2.append(e2[7])
        if Platoon_number[2] >= 1 and Binary[2] == 1:
            for vehicle in Platoon_member2:
                traci.vehicle.setSpeedMode(vehicle,22)
                traci.vehicle.setSpeed(vehicle,8)
                traci.vehicle.setAccel(vehicle,2)
        if Binary[2] != 1:
            for vehicle in Platoon_member2:
                traci.vehicle.setSpeedMode(vehicle,31)  
#*********************************ONE Approach********************************************
#*****************************************************************************************
    print("the length of every lane is")
    print(Platoon_length)
    print("the number of every lane is")
    print(Platoon_number)
    return Platoon_length


def Outlist_speedset(Single_IdList,Single_LaneList):    
    ####INIitialize the every direction's List
    for i in range(len(Single_LaneList)):
        if Single_LaneList[i].find("o") != -1:
            traci.vehicle.setSpeed(Single_IdList[i],-1)            
          
          
          
          
          
#################################################################################################################          
#################################################################################################################           
#     
#    if len(w1)>=2:
#    	if traci.vehicle.getLanePosition(w1[0])-traci.vehicle.getLanePosition(w1[1])<=20+traci.vehicle.getLength(w1[0]) and traci.vehicle.getSpeed(w1[0])<=5 and traci.vehicle.getLanePosition(w1[0])>100:
#    		temp_length=traci.vehicle.getLength(w1[0])+traci.vehicle.getLength(w1[1])+5
#    		traci.vehicle.remove(w1[1])
#    		traci.vehicle.setLength(w1[0],temp_length) 
#     
#    if len(w2)>=2:
#    	if traci.vehicle.getLanePosition(w2[0])-traci.vehicle.getLanePosition(w2[1])<=20+traci.vehicle.getLength(w2[0]) and traci.vehicle.getSpeed(w2[0])<=5 and traci.vehicle.getLanePosition(w2[0])>100:
#    		temp_length=traci.vehicle.getLength(w2[0])+traci.vehicle.getLength(w2[1])+5
#    		traci.vehicle.remove(w2[1])
#    		traci.vehicle.setLength(w2[0],temp_length) 
#           
#    if len(n1)>=2:
#    	if traci.vehicle.getLanePosition(n1[0])-traci.vehicle.getLanePosition(n1[1])<=20+traci.vehicle.getLength(n1[0]) and traci.vehicle.getSpeed(n1[0])<=5 and traci.vehicle.getLanePosition(n1[0])>100:
#    		temp_length=traci.vehicle.getLength(n1[0])+traci.vehicle.getLength(n1[1])+5
#    		traci.vehicle.remove(n1[1])
#    		traci.vehicle.setLength(n1[0],temp_length)        
#     
#    if len(n2)>=2:
#    	if traci.vehicle.getLanePosition(n2[0])-traci.vehicle.getLanePosition(n2[1])<=20+traci.vehicle.getLength(n2[0]) and traci.vehicle.getSpeed(n2[0])<=5 and traci.vehicle.getLanePosition(n2[0])>100:
#    		temp_length=traci.vehicle.getLength(n2[0])+traci.vehicle.getLength(n2[1])+5
#    		traci.vehicle.remove(n2[1])
#    		traci.vehicle.setLength(n2[0],temp_length)         
#      
#    if len(e1)>=2:
#    	if traci.vehicle.getLanePosition(e1[0])-traci.vehicle.getLanePosition(e1[1])<=20+traci.vehicle.getLength(e1[0]) and traci.vehicle.getSpeed(e1[0])<=5 and traci.vehicle.getLanePosition(e1[0])>100:
#    		temp_length=traci.vehicle.getLength(e1[0])+traci.vehicle.getLength(e1[1])+5
#    		traci.vehicle.remove(e1[1])
#    		traci.vehicle.setLength(e1[0],temp_length) 
#    
#    if len(e2)>=2:
#    	if traci.vehicle.getLanePosition(e2[0])-traci.vehicle.getLanePosition(e2[1])<=20+traci.vehicle.getLength(e2[0]) and traci.vehicle.getSpeed(e2[0])<=5 and traci.vehicle.getLanePosition(e2[0])>100:
#    		temp_length=traci.vehicle.getLength(e2[0])+traci.vehicle.getLength(e2[1])+5
#    		traci.vehicle.remove(e2[1])
#    		traci.vehicle.setLength(e2[0],temp_length)