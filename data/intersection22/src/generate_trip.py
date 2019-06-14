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
    with open("intersection_trip.xml", "w") as routes:
        print("""
        <?xml version="1.0" encoding="UTF-8"?>
        <!-- generated on 2018-11-05 17:19:39.085163 by $Id$
        options: -n intersection.net.xml -e 1000
        -->
        <routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">""", file=routes)#产生路径
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

