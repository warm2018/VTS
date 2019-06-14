# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 10:25:42 2018

@author: shengyu
"""

"""
构建zone2 区域的 车辆编队模型：
时间离散化为 0.01秒； zone1区域暂时仅用于得到对应的g；
class CAR_L():
    t0=0 # 到达zone2时间
    td=0   # 离开zone2时间
    g=0     
    v=0   
    a=0
    x=0    #离交叉口距离
    pass
"""
# fist step :初始化模型；

from CRESULT import Result
from gurobipy import *
from CINPUT import Input
from optimiza_function import optimize_av

case0=Input()
case0.d=   [[98, 24], [0, 0], [177, 24],      [0, 24]]
case0.v=   [[10,  1], [0, 0], [3.6, 1], [0, 0.003]]
case0.n=   [[5.0, 1], [0, 0], [5.0, 1.0],     [0, 1.0]]
case0.dis= [[0,0], [0,0], [0,0], [0,0]]

x=Result()
x=optimize_av(case0)
print(x.cycle)
print(x.csta)
print(x.cphi)
















