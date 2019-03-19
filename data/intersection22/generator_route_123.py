"""
生成随机车
"""
import random

def generator(a):
    N = 3600  # number of time steps 
    if a==1:
        left_trun = 1. / 10
        straight_turn = 1. / 10
        right_turn = 1. / 10
    if a==2:
        left_trun=1./10
        straight_turn=1./ 10
        right_turn = 1. / 10
    if a==3:
        left_trun = 1./4.5
        straight_turn = 1./4.5
        right_turn = 1. / 4.5      
    vehNr=[[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]];
    with open("intersection.rou.xml", "w") as routes:
        print("""<routes>
        <vType id="ty_through" accel="2" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="20" guiShape="passenger" lcStrategic="1000000000" lcCooperative="0.0"  lcAssertive="100"/>
        <vType id="ty_left" accel="2" decel="4.5" sigma="0.5" length="5" minGap="3" maxSpeed="20" guiShape="passenger" lcStrategic="1000000000000" lcCooperative="0.0" lcAssertive="100" />
        <route id="0012" edges="a1i a4o"/>
        <route id="0022" edges="a2i a1o"/>
        <route id="0032" edges="a3i a2o"/>
        <route id="0042" edges="a4i a3o 0001 d1i d3o"/>
        <!--above are 001 intersection's connections  LEFT TURN  routes-->
        <route id="0011" edges="a1i a3o 0001 d1i d4o"/>
        <route id="0021" edges="a2i a4o"/>
        <route id="0031" edges="a3i a1o"/>
        <route id="0041" edges="a4i a2o 0010 b4i b2o"/>
        <!--above are 00 intersection's connections STRAIGHT TURN routes-->
        <route id="0010" edges="a1i a2o 0010  b4i b3o 1011 c1i c3o"/>
        <route id="0020" edges="a2i a3o"/>
        <route id="0030" edges="a3i a4o"/>
        <route id="0040" edges="a4i a1o"/>
        <!--above are 00 intersection's connections RIGHT TURN routes-->
        <!--*********************ONE 00 INTERSECTION**************************   -->

        <route id="1012" edges="b1i b4o 1000 a2i a4o"/> 
        <route id="1022" edges="b2i b1o"/>
        <route id="1032" edges="b3i b2o"/>
        <route id="1042" edges="b4i b3o"/>
        <!--above are 001 intersection's connections  LEFT TURN  routes-->
        <route id="1011" edges="b1i b3o 1011 c1i c4o 1101 d2i d4o"/>
        <route id="1021" edges="b2i b4o 1000 a2i a1o"/>
        <route id="1031" edges="b3i b1o"/>
        <route id="1041" edges="b4i b2o"/>
        <!--above are 00 intersection's connections STRAIGHT TURN routes-->
        <route id="1010" edges="b1i b2o"/>
        <route id="1020" edges="b2i b3o 1011 c1i c3o"/>
        <route id="1030" edges="b3i b4o"/>
        <route id="1040" edges="b4i b1o"/>
        <!--above are 00 intersection's connections RIGHT TURN routes-->
        <!--*********************ONE 10 INTERSECTION**************************   -->

        <route id="1112" edges="c1i c4o"/>
        <route id="1122" edges="c2i c1o 1110 b3i b1o"/>
        <route id="1132" edges="c3i c2o"/>
        <route id="1142" edges="c4i c3o"/>
        <!--above are 001 intersection's connections  LEFT TURN  routes-->
        <route id="1111" edges="c1i c3o"/>
        <route id="1121" edges="c2i c4o 1101 d2i d4o"/>
        <route id="1131" edges="c3i c1o 1110 b3i b4o 1000 a2i a3o 0001 d1i d3o"/>
        <route id="1141" edges="c4i c2o"/>
        <!--above are 00 intersection's connections STRAIGHT TURN routes-->
        <route id="1110" edges="c1i c2o"/>
        <route id="1120" edges="c2i c3o"/>
        <route id="1130" edges="c3i c4o 1101 d2i d3o"/>
        <route id="1140" edges="c4i c1o"/>
        <!--above are 00 intersection's connections RIGHT TURN routes-->
        <!--*********************ONE 11 INTERSECTION**************************   -->

        <route id="0112" edges="d1i d4o"/>
        <route id="0122" edges="d2i d1o"/>
        <route id="0132" edges="d3i d2o 0111 c4i c3o"/>
        <route id="0142" edges="d4i d3o"/>
        <!--above are 001 intersection's connections  LEFT TURN  routes-->
        <route id="0111" edges="d1i d3o"/>
        <route id="0121" edges="d2i d4o"/>
        <route id="0131" edges="d3i d1o 0100 a3i a1o"/>
        <route id="0141" edges="d4i d2o 0111 c4i c2o"/>
        <!--above are 00 intersection's connections STRAIGHT TURN routes-->
        <route id="0110" edges="d1i d2o"/>
        <route id="0120" edges="d2i d3o"/>
        <route id="0130" edges="d3i d4o"/>
        <route id="0140" edges="d4i d1o 0100 a3i a2o"/>
        <!--above are 00 intersection's connections RIGHT TURN routes-->
        <!--*********************ONE 01 INTERSECTION**************************-->""", file=routes)#产生路径
        for i in range(N):
            if random.uniform(0, 1)<left_trun:
                print('    <vehicle id="a12_%i" type="ty_through" route="0012" depart="%i" departspeed="%i"/>' % (vehNr[0][5], i,15), file=routes )
                vehNr[0][5]+=1 ###给交叉口00编号为5的车道产生到达率为left_turn的左转车辆。
            if random.uniform(0, 1)<straight_turn:
                print('    <vehicle id="a11_%i" type="ty_through" route="0011" depart="%i" departspeed="%i"/>' % (vehNr[0][4], i,15), file=routes )
                vehNr[0][4]+=1 
            if random.uniform(0, 1)<right_turn:
                print('    <vehicle id="a10_%i" type="ty_through" route="0010" depart="%i" departspeed="%i"/>' % (vehNr[0][8], i,15), file=routes )
                vehNr[0][8]+=1
            if random.uniform(0, 1)<left_trun:
                print('    <vehicle id="a42_%i" type="ty_through" route="0042" depart="%i" departspeed="%i"/>' % (vehNr[0][7], i,15), file=routes )
                vehNr[0][7]+=1 
            if random.uniform(0, 1)<straight_turn:
                print('    <vehicle id="a41_%i" type="ty_through" route="0041" depart="%i" departspeed="%i"/>' % (vehNr[0][6], i,15), file=routes )
                vehNr[0][6]+=1 
            if random.uniform(0, 1)<right_turn:
                print('    <vehicle id="a40_%i" type="ty_through" route="0040" depart="%i" departspeed="%i"/>' % (vehNr[0][9], i,15), file=routes )
                vehNr[0][9]+=1
            #********************************************************THE GENERATEOR OF INTERSECTION 00 *********************************************
            if random.uniform(0, 1)<left_trun:
                print('    <vehicle id="b12_%i" type="ty_through" route="1012" depart="%i" departspeed="%i"/>' % (vehNr[1][5], i,15), file=routes )
                vehNr[1][5]+=1 
            if random.uniform(0, 1)<straight_turn:
                print('    <vehicle id="b11_%i" type="ty_through" route="1011" depart="%i" departspeed="%i"/>' % (vehNr[1][4], i,15), file=routes )
                vehNr[1][4]+=1 
            if random.uniform(0, 1)<right_turn:
                print('    <vehicle id="b10_%i" type="ty_through" route="1010" depart="%i" departspeed="%i"/>' % (vehNr[1][8], i,15), file=routes )
                vehNr[1][8]+=1
            if random.uniform(0, 1)<left_trun:
                print('    <vehicle id="b22_%i" type="ty_through" route="1022" depart="%i" departspeed="%i"/>' % (vehNr[1][3], i,15), file=routes )
                vehNr[1][3]+=1 
            if random.uniform(0, 1)<straight_turn:
                print('    <vehicle id="b21_%i" type="ty_through" route="1021" depart="%i" departspeed="%i"/>' % (vehNr[1][2], i,15), file=routes )
                vehNr[1][2]+=1 
            if random.uniform(0, 1)<right_turn:
                print('    <vehicle id="b20_%i" type="ty_through" route="1020" depart="%i" departspeed="%i"/>' % (vehNr[1][9], i,15), file=routes )
                vehNr[1][9]+=1
            #********************************************************THE GENERATEOR OF INTERSECTION 10 *********************************************
            if random.uniform(0, 1)<left_trun:
                print('    <vehicle id="c32_%i" type="ty_through" route="1132" depart="%i" departspeed="%i"/>' % (vehNr[2][1], i,15), file=routes )
                vehNr[2][1]+=1 
            if random.uniform(0, 1)<straight_turn:
                print('    <vehicle id="c31_%i" type="ty_through" route="1131" depart="%i" departspeed="%i"/>' % (vehNr[2][0], i,15), file=routes )
                vehNr[2][0]+=1 
            if random.uniform(0, 1)<right_turn:
                print('    <vehicle id="c30_%i" type="ty_through" route="1130" depart="%i" departspeed="%i"/>' % (vehNr[2][8], i,15), file=routes )
                vehNr[2][8]+=1
            if random.uniform(0, 1)<left_trun:
                print('    <vehicle id="c22_%i" type="ty_through" route="1122" depart="%i" departspeed="%i"/>' % (vehNr[2][3], i,15), file=routes )
                vehNr[2][3]+=1 
            if random.uniform(0, 1)<straight_turn:
                print('    <vehicle id="c21_%i" type="ty_through" route="1121" depart="%i" departspeed="%i"/>' % (vehNr[2][2], i,15), file=routes )
                vehNr[2][2]+=1 
            if random.uniform(0, 1)<right_turn:
                print('    <vehicle id="c20_%i" type="ty_through" route="1120" depart="%i" departspeed="%i"/>' % (vehNr[2][9], i,15), file=routes )
                vehNr[2][9]+=1
            #********************************************************THE GENERATEOR OF INTERSECTION 11 *********************************************
            if random.uniform(0, 1)<left_trun:
                print('    <vehicle id="d32_%i" type="ty_through" route="0132" depart="%i" departspeed="%i"/>' % (vehNr[3][1], i,15), file=routes )
                vehNr[3][1]+=1 
            if random.uniform(0, 1)<straight_turn:
                print('    <vehicle id="d31_%i" type="ty_through" route="0131" depart="%i" departspeed="%i"/>' % (vehNr[3][0], i,15), file=routes )
                vehNr[3][0]+=1 
            if random.uniform(0, 1)<right_turn:
                print('    <vehicle id="d30_%i" type="ty_through" route="0130" depart="%i" departspeed="%i"/>' % (vehNr[3][8], i,15), file=routes )
                vehNr[3][8]+=1
            if random.uniform(0, 1)<left_trun:
                print('    <vehicle id="d42_%i" type="ty_through" route="0142" depart="%i" departspeed="%i"/>' % (vehNr[3][7], i,15), file=routes )
                vehNr[3][7]+=1 
            if random.uniform(0, 1)<straight_turn:
                print('    <vehicle id="d41_%i" type="ty_through" route="0141" depart="%i" departspeed="%i"/>' % (vehNr[3][6], i,15), file=routes )
                vehNr[3][6]+=1 
            if random.uniform(0, 1)<right_turn:
                print('    <vehicle id="d40_%i" type="ty_through" route="0140" depart="%i" departspeed="%i"/>' % (vehNr[3][9], i,15), file=routes )
                vehNr[3][9]+=1
            #********************************************************THE GENERATEOR OF INTERSECTION 01 *********************************************
            # 01 is the number of intersection , 1 is the arm number ,and 1 says it's left   

            
            
            
            
            
            
            
            
            
            
            
            
            
            
    