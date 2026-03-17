#测试调用模块
import my_add#调用模块
print(my_add.add(1,2))
my_add.add(1,2)
import my_mul as m#调用模块并重新起名
print(m.mul(2,2))
from my_minu import minus#调用模块功能
print(minus(1,2))
from my_minu import minus as mi#调用模块功能并为功能重新起名
print(mi(2,2))
from my_minu import *#调用模块所有功能
print(minus(1,2))