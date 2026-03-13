#输入-输出
#1 input() 输入操作符，会捕捉用户输入的信息并将其转为字符串型
s = input("请输入一个数：")
print(s)
#案例模拟ATM机取款
total = 10000
password = input("请输入密码：")
print(f"密码正确为：{password}")
num = input("请输入取款金额：")
print(f"取款成功，还剩余：{total-int(num)}" ) #因为{}会把数据全转为字符串类型，所以在此要使用类型转换
#2 print() 输出操作符，将结果输出出来
print(123)
print("Hello")
print(1 + 2)

#运算符
#1 算数运算符 + - * / // % **
print("10+4=",10+4)
print("10-4=",10-4)
print("10*4=",10*4)
print("10/4=",10/4)
print("10//4=",10//4)
print("10%4= ",10%4)
print("10**4=",10**4)
#案例1 输入俩个数并计算
num1 = float(input("输入数一："))  #input()会把输入的数转换为字符串类型，所以使用类型转换
num2 = float(input("输入数二："))
print("相加为",num1 + num2)
print("相减为",num1 - num2)
print("相乘为",num1 * num2)
print("相除为",num1 / num2)  #浮点数会发生精度损失原因是二进制不能准确的表示所有小数
#案例2 计算三个整数的平均数
num1 = float(input("输入数一："))
num2 = float(input("输入数二："))
num3 = float(input("输入数3："))
print("三个数的平均数为：",(num1 + num2 + num3) / 3)
#案例3 计算梯形面积
l1 = float(input("输入上底："))
l2 = float(input("输入下底："))
h  = float(input("输入高：" ))
print("该梯形面积为：",(l1 + l2 ) * h /2)
#案例4 计算圆周长和面积
import math
r = float(input("输入半径："))
print("该圆面积为：",math.pi * r **2,"/n周长为：",2 * math.pi * r)
#案例5 身体质量指数BMI
wei = float(input("输入您的体重(kg)："))
hei = float(input("输入您的身高(m)："))
BMI = wei / (hei ** 2)
print("您的BMI指数为:{}".format(BMI))
#2 赋值运算符
n = 2
n += 2  #等同于n = n+2，以下同上
print(n)
n -= 2
print(n)
n *= 2
print(n)
n /= 2
print(n) #有浮点数参与运算的话数据回转换为浮点数
n %= 2
print(n)
n //= 2
print(n)
n **= 2
print(n)
#3 比较运算符 > < == >= <= !=
print("100是否等于100",100 == 100)
print("100是否不等100",100 != 100)
print("100是否小于等于100",100 <= 100)
print("100是否大于等于100",100 >= 100)
print("100大于100",100 > 100)
print("100小于100",100 < 100)
#4 逻辑运算符 and or not(逻辑非取反，且not只能用于单个表达式)
#案例判断是否在区间
n = float(input("请输入一个数："))
print(f"{n}是否在[20,60]?",n>=20 and n<=60)
# print(f"{n}是否在?", 20 <= n <= 60)#简化
n = float(input("请输入一个数："))
print(f"{n}是否不在[20,60]?",n<=20 or n>=60)
#not运算符
n = float(input("请输入一个数："))
print(f"{n}是否大于20?",not n <= 20)
print(not True)   # 输出: False
print(not False)  # 输出: True