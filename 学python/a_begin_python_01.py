# 这是我的第一个python程序（这是一个注释）掌握输出
print("************")
print("* 白日依山尽 *")
print("* 黄河入海流 *")
print("* 欲穷千里目 *")
print("* 更上一层楼 *")
print("************")
print("键盘")  #字符串类型(注:只要有引号框起来的都是字符串型)
print("键盘")
print(12345)      # 整型
print(120.6)      # 浮点型
print("12345")    # 字符串类型
print(True)       # 布尔型
print("True")     # 字符串型
print(False)


#变量 用来存放单个数据的容器会发生改变
num1 = 12
print(num1)
num1 = num1 + 10
print(num1)
num1 = "hello"
print(num1)
num1 = True
print(num1)
num1 = False
print(num1)
#案例 变量的使用
new = 120.2
incr = 20
print("下一年的总量是:",new + incr)
new , incr = 120.2 , 20 #一条语句可以定义多个变量也可连续赋值
print("下一年的总量是:",new + incr)
#注 一个变量只能赋一个值,必须赋值才可已使用


#变量赋值
a , b , c = 100 , 200 , 300
d = a
a = c
c = b
b = d
print(a)
print(b)
print(c)
a = 100
b = 200
c = 300
# 一行代码完成交换
a, b, c = c, a, b
print(a, b, c)
#执行顺序：Python 先完整计算等号右侧所有值（基于变量原始值生成临时元组），再执行左侧的赋值；
#元组解包：右侧的多个值会被自动打包成元组，左侧的多个变量会按顺序 “解包” 接收元组的元素.所以可以执行值并不会被覆盖

#查看数据(字面量)变量类型
#1  type()
print("Hello")
print(True)
print(1)
print(1.2)
num = 1
nvm = 1.2
nve = True
ar = "Hello"
print(type(print("Hello")),
type(print(1)),
type(print(True)),
type(print(1.2)),
type(num),
type(nvm),
type(nve),
type(ar))
#2  isintance()实例
print(isinstance(num,int),
isinstance(num,float),
isinstance(num,bool))