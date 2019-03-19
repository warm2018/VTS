
from test_class import Result

ress = []
test_result_a = Result()
a = test_result_a.csta
test_result_b = Result()
for value in test_result_b.csta: 
    ress.append(value)
b = test_result_b.csta
print(a,b,id(a),id(b),ress,id(ress))
 
##不可变类型：数值、字符串、元组
##可变类型：字典、列表、

