# #循环
# #1 while循环 while 条件表达式(值为布尔型)，只在满足条件时循环
a = 0
while a < 10:
    print(a,end = " ")
    a += 1

# #案例 奇偶数之和
#偶数和
total = 0
a = 0
while a <= 100:
    if a % 2 == 0 :
        total += a
    a += 1
print("total=",total)
#奇数和
total = 0
a = 0
while a <= 100:
    if a % 2 == 1 :
        total += a
    a += 1
#else: #可有可无，作用循环结束时执行下面代码
print("total=",total)


# #2 for循环(轮询遍历) for 元素 in 待处理数据集: ，只在已知的循环次数内循环
str1 = "I'm a string"
for i in str1:
    print(i,end = "")
#else:#可有可无，同上

# #案例1 计算偶数和
"""
需用到range(start,end(除去end)，step)作用生成规则的数字序列
可有三种使用方式
range(end(除去end))从0到end(除去end)，若没有start和step则默认为0和1
range(start,end(除去end))从start到end(除去end)
range(start,end(除去end)，step)从star开始到end(除去end)一次间隔一个step
"""
total1 = 0
total2 = 0
for i in range(1,101):
    if i % 2 == 0:
        total1 += i
print(total1)
for i in range(0,101,2):
  total2 += i
print(total2)

#案例2 3的倍数数字和
sum1 = 0
for i in range(100,501):
    if i % 3 == 0:
        sum1 += i
print(sum1)


#3 嵌套循环
#案例1 打印一个长方形
m = int(input("宽:"))
n = int(input("高:"))
for a in range(m):
    for b in range(n):
        print("*",end = "\t")
    print()

#案例2 计算器
for i in range(1,10):#控制行
    for j in range(1,i+1):#控制列
        print(f"{j}×{i}={j * i}",end = "\t")
    print()

#案例3 打印国际象棋
m = int(input("宽:"))
for a in range(m):
    if a % 2 == 0:
        for b in range(m):
            if b % 2 == 0:
                print("▣",end = "\t")
            else:
                print("▢",end = "\t")
    else:
        for b in range(m):
            if b % 2 == 0:
                print("▢", end="\t")
            else:
                print("▣", end="\t")
    print()

#案例4 登录操作
while True:
    username = input("请输入用户名:")
    password = input("请输入密码:")
    if username == "" or password == "":
        print("用户名和密码不能为空!")
        continue
    if username == "a" and password == "123":
        print("欢迎您!")
        break
    elif username == "b" and password == "456":
        print("欢迎您!")
        break
    elif username == "c" and password == "789":
        print("欢迎您!")
        break
    else:
        print("登陆失败!用户或密码错误!")

#案例5 猜数字
import random
num = random.randint(1,101)
z = 0
while True:
    z += 1
    n = int(input("请猜数字:"))
    if n > num:
        print("猜大了")
    elif n < num:
        print("猜小了")
    else:
        print("恭喜你,猜对了!")
        print(f"你用了{z}次")
        print(f"所猜数字是{num}")
        break

#案例6 累加1-1000包含1000中5的倍数
total = 0
for i in range(0,10001,5):
    total += i
print(total)