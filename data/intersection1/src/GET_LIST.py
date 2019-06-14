import traci
from SORT import Sort_two


def Sort_two(List_a,List_b):##此函数表示将List_b按照List_a顺序排序
    if List_a !=[] and List_b != []:
        Index_number = []
        Listb_sort = []
        # 定义一个中间索引列表以及初始化结果的列表
        A_sort = sorted(List_a,reverse = True)
        ##将A排序
        for index_a in range(len(A_sort)):
            Index_number.append(List_a.index(A_sort[index_a]))
        ##将A排序后的列表对应原列表的索引找出来
        for index_b in Index_number:
            Listb_sort.append(List_b[index_b])
        #按照索引值从需要排序的列表中取出元素，行成一个与a排序后对应的列表
        return A_sort,Listb_sort
    ### 实现两个列表元素对的同步排序
    else: 
        return List_a,List_b
    

error = 1

def get_list(Single_IdList,Single_LaneList):    
    n1=list();
    n2=list();
    e1=list();
    e2=list();
    s1=list();
    s2=list();
    w1=list();
    w2=list(); 
    Position0 = []
    Position1 = []
    Position2 = []
    Position3 = []
    Position4 = []
    Position5 = []
    Position6 = []
    Position7 = []
    ####INIitialize the every direction's List
    for i in range(len(Single_LaneList)):
        if Single_LaneList[i].find("3i_2") != -1:
            n1.append(Single_IdList[i])
        elif Single_LaneList[i].find("3i_1") != -1:
            n2.append(Single_IdList[i])
        elif Single_LaneList[i].find("2i_2") != -1:
            e1.append(Single_IdList[i])
        elif Single_LaneList[i].find("2i_1") != -1:
            e2.append(Single_IdList[i])
        elif Single_LaneList[i].find("1i_2") != -1:
            s1.append(Single_IdList[i])
        elif Single_LaneList[i].find("1i_1") != -1:
            s2.append(Single_IdList[i])
        elif Single_LaneList[i].find("4i_2") != -1:
            w1.append(Single_IdList[i])
        elif Single_LaneList[i].find("4i_1") != -1:
            w2.append(Single_IdList[i])



    if len(n1)>0:
        for i in range(len(n1)):
            if traci.vehicle.getLanePosition(n1[i]) > 200-error:
                n1[i]=0					
    if len(n2)>0:
        for i in range(len(n2)):
            if traci.vehicle.getLanePosition(n2[i])-5.1>200-error:
                n2[i]=0	
					
    if len(e1)>0:
        for i in range(len(e1)):
            if traci.vehicle.getLanePosition(e1[i])-5.1>200-error:
                e1[i]=0	
    if len(e2)>0:
        for i in range(len(e2)):
            if traci.vehicle.getLanePosition(e2[i])-5.1>200-error:
                e2[i]=0	

    if len(s1)>0:
        for i in range(len(s1)):
            if traci.vehicle.getLanePosition(s1[i])-5.1>200-error:
                s1[i]=0	
    if len(s2)>0:
        for i in range(len(s2)):
            if traci.vehicle.getLanePosition(s2[i])-5.1>200-error:
                s2[i]=0						
	
    if len(w1)>0:
        for i in range(len(w1)):
            if traci.vehicle.getLanePosition(w1[i])-5.1>200-error:
                w1[i]=0	
    if len(w2)>0:
        for i in range(len(w2)):
            if traci.vehicle.getLanePosition(w2[i])-5.1>200-error:
                w2[i]=0		
##将找到的异常车辆从列表中剔除
    for i in range(len(n1)-1,-1,-1):
        if(n1[i]==0):
            del n1[i]
				
    for i in range(len(n2)-1,-1,-1):
        if n2[i]==0:
            del n2[i]
				
    for i in range(len(e1)-1,-1,-1):
        if e1[i]==0:
            del e1[i]		
    for i in range(len(e2)-1,-1,-1):
        if e2[i]==0:
            del e2[i]
				
    for i in range(len(s1)-1,-1,-1):
        if s1[i]==0:
            del s1[i]		
    for i in range(len(s2)-1,-1,-1):
        if s2[i]==0:
            del s2[i]	
				
    for i in range(len(w1)-1,-1,-1):
        if w1[i]==0:
            del w1[i]		
    for i in range(len(w2)-1,-1,-1):
        if w2[i]==0:
            del w2[i]		       
        #去除数组中的重复元素;
##sort the list in every direction and 
    print([n2,n1,e2,e1,s2,s1,w2,w1])
    if n2 != []:
        for ID_index in range(len(n2)):
            Position0.append(traci.vehicle.getLanePosition(n2[ID_index])-5.1)
    if n1 != []:
        for ID_index in range(len(n1)):
            Position1.append(traci.vehicle.getLanePosition(n1[ID_index])-5.1)
    if e2 != []:
        for ID_index in range(len(e2)):
            Position2.append(traci.vehicle.getLanePosition(e2[ID_index])-5.1)
    if e1 != []:
        for ID_index in range(len(e1)):
            Position3.append(traci.vehicle.getLanePosition(e1[ID_index])-5.1)
    if s2 != []:
        for ID_index in range(len(s2)):
            Position4.append(traci.vehicle.getLanePosition(s2[ID_index])-5.1)
    if s1 != []:
        for ID_index in range(len(s1)):
            Position5.append(traci.vehicle.getLanePosition(s1[ID_index])-5.1)
    if w2 != []:
        for ID_index in range(len(w2)):
            Position6.append(traci.vehicle.getLanePosition(w2[ID_index])-5.1)
    if w1 != []:
        for ID_index in range(len(w1)):
            Position7.append(traci.vehicle.getLanePosition(w1[ID_index])-5.1)
## get the Laneposition of every vehicle

    Position0,n2 = Sort_two(Position0, n2)
    Position1,n1 = Sort_two(Position1, n1)
    Position2,e2 = Sort_two(Position2, e2)    
    Position3,e1 = Sort_two(Position3, e1) 
    Position4,s2 = Sort_two(Position4, s2)    
    Position5,s1 = Sort_two(Position5, s1) 
    Position6,w2 = Sort_two(Position6, w2)    
    Position7,w1 = Sort_two(Position7, w1) 
    return [n2,n1,e2,e1,s2,s1,w2,w1],[Position0,Position1,Position2,Position3,Position4,Position5,Position6,Position7]
    
