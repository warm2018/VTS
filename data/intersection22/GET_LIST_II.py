import traci
def get_list_II(IDList):
    n1=list();
    n2=list();
    e1=list();
    e2=list();	
    s1=list();
    s2=list();
    w1=list();
    w2=list();        
    for i in range(len(IDList)):
        if IDList[i].find("n1") != -1:
            n1.append(IDList[i])
        elif IDList[i].find("n2") != -1:
            n2.append(IDList[i])
        elif IDList[i].find("e1") != -1:
            e1.append(IDList[i])
        elif IDList[i].find("e2") != -1:
            e2.append(IDList[i])
        elif IDList[i].find("s1") != -1:
            s1.append(IDList[i])
        elif IDList[i].find("s2") != -1:
            s2.append(IDList[i])
        elif IDList[i].find("w1") != -1:
            w1.append(IDList[i])
        else:
            w2.append(IDList[i])
    n1=sorted(n1,key=lambda x:int(x[3:]))
    n2=sorted(n2,key=lambda x:int(x[3:]))
    e1=sorted(e1,key=lambda x:int(x[3:]))
    e2=sorted(e2,key=lambda x:int(x[3:]))
    s1=sorted(s1,key=lambda x:int(x[3:]))
    s2=sorted(s2,key=lambda x:int(x[3:]))
    w1=sorted(w1,key=lambda x:int(x[3:]))
    w2=sorted(w2,key=lambda x:int(x[3:]))
    return [n2,n1,e2,e1,s2,s1,w2,w1]
        
 
    