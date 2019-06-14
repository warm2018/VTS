"""
生成随机车辆
"""
from random import *
 # make tests reproducible
N = 3600  # number of time steps   
straight_turn = 1. / 40
left_trun = 1. / 80
right_turn= 1. / 80
vehNr=[[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]];
with open("intersection.rou.xml", "w") as routes:
    print("""<routes>
    <vType id="ty_through" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="20" guiShape="passenger"/>
    <vType id="ty_left" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="3" maxSpeed="20" guiShape="passenger"/>
    <route id="0011" edges="001i 004o"/>
    <route id="0021" edges="002i 001o"/>
    <route id="0031" edges="003i 002o"/>
    <route id="0041" edges="004i 003o"/>
    <!--above are 001 intersection's connections  LEFT TURN  routes-->
    <route id="0012" edges="001i 003o"/>
    <route id="0022" edges="002i 004o"/>
    <route id="0032" edges="003i 001o"/>
    <route id="0042" edges="004i 002o"/>
    <!--above are 00 intersection's connections STRAIGHT TURN routes-->
    <route id="0013" edges="001i 002o 0010 104i 103o"/>
    <route id="0023" edges="002i 003o 0001"/>
    <route id="0033" edges="003i 004o"/>
    <route id="0043" edges="004i 001o"/>
    <!--above are 00 intersection's connections RIGHT TURN routes-->
    <!--*********************ONE 00 INTERSECTION**************************   -->
     2222222222222222222222222222222222222222222222222222222222
    <route id="1011" edges="101i 104o"/>
    <route id="1021" edges="102i 101o"/>
    <route id="1031" edges="103i 102o"/>
    <route id="1041" edges="104i 103o"/>
    <!--above are 001 intersection's connections  LEFT TURN  routes-->
    <route id="1012" edges="101i 103o"/>
    <route id="1022" edges="102i 104o"/>
    <route id="1032" edges="103i 101o"/>
    <route id="1042" edges="104i 102o"/>
    <!--above are 00 intersection's connections STRAIGHT TURN routes-->
    <route id="1013" edges="101i 102o"/>
    <route id="1023" edges="102i 103o"/>
    <route id="1033" edges="103i 104o"/>
    <route id="1043" edges="104i 101o"/>
    <!--above are 00 intersection's connections RIGHT TURN routes-->
    <!--*********************ONE 10 INTERSECTION**************************   -->

    <route id="1111" edges="111i 114o"/>
    <route id="1121" edges="112i 111o"/>
    <route id="1131" edges="113i 112o"/>
    <route id="1141" edges="114i 113o"/>
    <!--above are 001 intersection's connections  LEFT TURN  routes-->
    <route id="1112" edges="111i 113o"/>
    <route id="1122" edges="112i 114o"/>
    <route id="1132" edges="113i 111o"/>
    <route id="1142" edges="114i 112o"/>
    <!--above are 00 intersection's connections STRAIGHT TURN routes-->
    <route id="1113" edges="111i 112o"/>
    <route id="1123" edges="112i 113o"/>
    <route id="1133" edges="113i 114o"/>
    <route id="1143" edges="114i 111o"/>
    <!--above are 00 intersection's connections RIGHT TURN routes-->
    <!--*********************ONE 11 INTERSECTION**************************   -->

    <route id="0111" edges="011i 014o"/>
    <route id="0121" edges="012i 011o"/>
    <route id="0131" edges="013i 012o"/>
    <route id="0141" edges="014i 013o"/>
    <!--above are 001 intersection's connections  LEFT TURN  routes-->
    <route id="0112" edges="011i 013o"/>
    <route id="0122" edges="012i 014o"/>
    <route id="0132" edges="013i 011o"/>
    <route id="0142" edges="014i 012o"/>
    <!--above are 00 intersection's connections STRAIGHT TURN routes-->
    <route id="0113" edges="011i 012o"/>
    <route id="0123" edges="012i 013o"/>
    <route id="0133" edges="013i 014o"/>
    <route id="0143" edges="014i 011o"/>
    <!--above are 00 intersection's connections RIGHT TURN routes-->
    <!--*********************ONE 01 INTERSECTION**************************   -->""", file=routes)#产生路径
    for i in range(N):
        if random.uniform(0, 1)<left_trun:
            print('    <vehicle id="0011_%i" type="ty_through" route="0011" depart="%i" departspeed="%i"/>' % (vehNr[0][5], i,15), file=routes )
            vehNr[0][5]+=1 ###给交叉口00编号为5的车道产生到达率为left_turn的左转车辆。
        if random.uniform(0, 1)<straight_turn:
            print('    <vehicle id="0012_%i" type="ty_through" route="0012" depart="%i" departspeed="%i"/>' % (vehNr[0][4], i,15), file=routes )
            vehNr[0][4]+=1 
        if random.uniform(0, 1)<right_turn:
            print('    <vehicle id="0013_%i" type="ty_through" route="0013" depart="%i" departspeed="%i"/>' % (vehNr[0][8], i,15), file=routes )
            vehNr[0][8]+=1
        if random.uniform(0, 1)<left_trun:
            print('    <vehicle id="0041_%i" type="ty_through" route="0041" depart="%i" departspeed="%i"/>' % (vehNr[0][7], i,15), file=routes )
            vehNr[0][7]+=1 
        if random.uniform(0, 1)<straight_turn:
            print('    <vehicle id="0042_%i" type="ty_through" route="0042" depart="%i" departspeed="%i"/>' % (vehNr[0][6], i,15), file=routes )
            vehNr[0][6]+=1 
        if random.uniform(0, 1)<right_turn:
            print('    <vehicle id="0043_%i" type="ty_through" route="0043" depart="%i" departspeed="%i"/>' % (vehNr[0][9], i,15), file=routes )
            vehNr[0][9]+=1
        #********************************************************THE GENERATEOR OF INTERSECTION 00 *********************************************

    for i in range(N):
        if random.uniform(0, 1)<left_trun:
            print('    <vehicle id="1011_%i" type="ty_through" route="1011" depart="%i" departspeed="%i"/>' % (vehNr[1][5], i,15), file=routes )
            vehNr[1][5]+=1 
        if random.uniform(0, 1)<straight_turn:
            print('    <vehicle id="1012_%i" type="ty_through" route="1012" depart="%i" departspeed="%i"/>' % (vehNr[1][4], i,15), file=routes )
            vehNr[1][4]+=1 
        if random.uniform(0, 1)<right_turn:
            print('    <vehicle id="1013_%i" type="ty_through" route="1013" depart="%i" departspeed="%i"/>' % (vehNr[1][8], i,15), file=routes )
            vehNr[1][8]+=1
        if random.uniform(0, 1)<left_trun:
            print('    <vehicle id="1021_%i" type="ty_through" route="1021" depart="%i" departspeed="%i"/>' % (vehNr[1][3], i,15), file=routes )
            vehNr[1][3]+=1 
        if random.uniform(0, 1)<straight_turn:
            print('    <vehicle id="1022_%i" type="ty_through" route="1022" depart="%i" departspeed="%i"/>' % (vehNr[1][2], i,15), file=routes )
            vehNr[1][2]+=1 
        if random.uniform(0, 1)<right_turn:
            print('    <vehicle id="1023_%i" type="ty_through" route="1023" depart="%i" departspeed="%i"/>' % (vehNr[1][9], i,15), file=routes )
            vehNr[1][9]+=1
        #********************************************************THE GENERATEOR OF INTERSECTION 10 *********************************************

    for i in range(N):
        if random.uniform(0, 1)<left_trun:
            print('    <vehicle id="1131_%i" type="ty_through" route="1131" depart="%i" departspeed="%i"/>' % (vehNr[2][1], i,15), file=routes )
            vehNr[2][1]+=1 
        if random.uniform(0, 1)<straight_turn:
            print('    <vehicle id="1132_%i" type="ty_through" route="1132" depart="%i" departspeed="%i"/>' % (vehNr[2][0], i,15), file=routes )
            vehNr[2][0]+=1 
        if random.uniform(0, 1)<right_turn:
            print('    <vehicle id="1133_%i" type="ty_through" route="1133" depart="%i" departspeed="%i"/>' % (vehNr[2][8], i,15), file=routes )
            vehNr[2][8]+=1
        if random.uniform(0, 1)<left_trun:
            print('    <vehicle id="1121_%i" type="ty_through" route="1121" depart="%i" departspeed="%i"/>' % (vehNr[2][3], i,15), file=routes )
            vehNr[2][3]+=1 
        if random.uniform(0, 1)<straight_turn:
            print('    <vehicle id="1122_%i" type="ty_through" route="1122" depart="%i" departspeed="%i"/>' % (vehNr[2][2], i,15), file=routes )
            vehNr[2][2]+=1 
        if random.uniform(0, 1)<right_turn:
            print('    <vehicle id="1123_%i" type="ty_through" route="1123" depart="%i" departspeed="%i"/>' % (vehNr[2][9], i,15), file=routes )
            vehNr[2][9]+=1
        #********************************************************THE GENERATEOR OF INTERSECTION 11 *********************************************


    for i in range(N):
        if random.uniform(0, 1)<left_trun:
            print('    <vehicle id="0131_%i" type="ty_through" route="0131" depart="%i" departspeed="%i"/>' % (vehNr[3][1], i,15), file=routes )
            vehNr[3][1]+=1 
        if random.uniform(0, 1)<straight_turn:
            print('    <vehicle id="0132_%i" type="ty_through" route="0132" depart="%i" departspeed="%i"/>' % (vehNr[3][0], i,15), file=routes )
            vehNr[3][0]+=1 
        if random.uniform(0, 1)<right_turn:
            print('    <vehicle id="0133_%i" type="ty_through" route="0133" depart="%i" departspeed="%i"/>' % (vehNr[3][8], i,15), file=routes )
            vehNr[3][8]+=1
        if random.uniform(0, 1)<left_trun:
            print('    <vehicle id="0141_%i" type="ty_through" route="0141" depart="%i" departspeed="%i"/>' % (vehNr[3][7], i,15), file=routes )
            vehNr[3][7]+=1 
        if random.uniform(0, 1)<straight_turn:
            print('    <vehicle id="0142_%i" type="ty_through" route="0142" depart="%i" departspeed="%i"/>' % (vehNr[3][6], i,15), file=routes )
            vehNr[3][6]+=1 
        if random.uniform(0, 1)<right_turn:
            print('    <vehicle id="0143_%i" type="ty_through" route="0143" depart="%i" departspeed="%i"/>' % (vehNr[3][9], i,15), file=routes )
            vehNr[3][9]+=1
        #********************************************************THE GENERATEOR OF INTERSECTION 01 *********************************************
        # 01 is the number of intersection , 1 is the arm number ,and 1 says it's left


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    