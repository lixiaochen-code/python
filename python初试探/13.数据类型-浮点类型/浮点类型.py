a = 3.1415926
print(a, type(a))
n1 = 1.1
n2 = 2.2
n3 = 3.1
# 浮点类型储存不精确
# 计算的时候，可能会出现小数位不确定的情况
print(n1 + n2)
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))
print(n1 + n3)