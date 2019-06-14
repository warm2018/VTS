""" 
         line.split(' ')[5]  代表第line行的id;
         line.split(' ')[17] 代表第line行的waiting time;
         
""" 
def Get_Delay():
    import re   
    nphase=8
    direction=[ 'n2_', 'n1_', 'e2_', 'e1_', 's2_', 's1_', 'w2_', 'w1_']  
    ncar =[0,0,0,0,0,0,0,0]     
    delay=[0,0,0,0,0,0,0,0] 
    temp=0
    with open("tripinfo.xml", "r") as routes:
        with open("delay.xml", "w") as route:
            for line in routes:
                if line!='</tripinfos>\n':           
                    line=line.strip("\n")
                    print(line, file=route)
    with open("delay.xml", "r") as routes:    
        for line in routes:# line 指代每一行;
            temp=temp+1
            if temp>65:
                for i in range(nphase):
                    if line.split(' ')[5][4:7]==direction[i]:
                        ncar[i]=ncar[i]+1
                        delay[i]=delay[i]+int(re.sub("\D","",line.split(' ')[18][10:]))/100
    for i in range(nphase):
        delay[i]=delay[i]/ncar[i]    
    return delay            

    
    
    
    
    
    
    
    
    
    