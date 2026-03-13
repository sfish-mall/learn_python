#容器
#1 列表list 语法 列表名 = [元素1，元素2，元素3...] 列表元素有序，可迭代，可修改，可重复且元素类型可不同但总体是列表类型
list_a = [1,2,2,3,4,'a','b','c',True,1.2,2.4]
print(list_a)

#1.1 列表索引 注:列表索引不允许超出列表范围
print(list_a[0])#正向索引,从0开始
print(list_a[-1])#反向索引,从-1开始

#1.2 列表遍历(迭代)
for i in list_a:
    print(i,end = " ")   #索引的是元素不是下标不要写成print(list_a[i])

#1.3 列表增删改查
#查
print(list_a)
#增
list_a.append(10)#append()方法在列表末尾添加元素
print(list_a)
list_a.insert (1,'d')#insert()方法在指定位置之前插入元素
print(list_a)
#删
del list_a[0]#用到del (所要删除的索引元素) 关键字
print(list_a)
#改
list_a [2] = 1
print(list_a)

#1.4 列表切片 列表[start:end(不包含):step] 无指定默认为[0:-1:1],里面为元素的索引且正反索引都可
print(list_a[::])
print(list_a[:])#同上一样步长前面:可省略，start后面不行因为要与索引区分
print(list_a[0:6:])
print(list_a[0:6:2])
print(list_a[-10:-4:])
print(list_a[-10:-4:2])

#1.5 列表常见方法
list_a.append(12)
print(list_a)
list_a.insert(1,'d')
print(list_a)
a = list_a.pop()#pop删除指定元素并返回值，无指定则默认末尾
print(list_a)
print(a)
b = list_a.pop(1)#
print(list_a)
print(b)
list_a.remove(2)#移除所匹配列表到的第一个值
print(list_a)
list_b = [2,8,6,3,4,2,9,7]
list_b.sort()#列表排序无指定默认升序，前提是元素类型相同
print(list_b)
list_a.reverse()#反转列表
print(list_a)

#案例1 输入10个数字并存储到一个列表中,对列表进行排序,输出最大、最小和平均值
list_c = []
j = 1
for i in range(10):
    c = int(input(f"输入第{j}个数字:"))
    list_c.append(c)
    j += 1
list_c.sort()
print(list_c)
print(max(list_c))
print(min(list_c))
print(sum(list_c) / len(list_c))

#案例2 合并列表元素并去重
list1 = []
for i in range(10):
    a = int(input("列表一的元素:"))
    list1.append(a)
list2 = []
for i in range(10):
    a = int(input("列表二的元素:"))
    list2.append(a)
print(list1, list2)
list3 = [*list1,*list2]#解包
print(list3)
list4 = []
for j in list3:
    if j not in list4:#元素 in 列表 表示该元素是否在该列表中输出布尔值 注意判断条件别写错了
        list4.append(j)
print(list4)

#案例3 生成1-20平方列表
list0 = [i**2 for i in range(1,21)]
#使用列表推导式：按照一定的规则快速生成一个列表的方法 [要插入的值(变量/表达式等都可) for i in 序列/列表 条件判断语句]
print(list0)

#案例4 从数字列表中提取所有偶数并计算平方，组成一个新列表
list_0 = [i**2 for i in list0 if i%2 == 0]
print(list_0)


#2 字符串str '' "" """ """#有序、可重复、不可修改且类型都是字符串
str1 = "abcdefg,hello python!"#特点、索引及遍历同列表一样
print(str1)

#2.1 字符串切片
str2 = str1[:]
print(str2)
str2 = str1[8:-1]
print(str2)
str2 = str1[8:-1:2]
print(str2)

#2.2 字符串常见的方法 注：字符串所有的方法都不修改原字符串
str3 = str1.find("hello")#匹配指定字符串首次索引的位置并返回，找不到返回-1
print(str3)
str3 = str1.count("e")#返回该指定字符在该字符串出现的次数
print(str3)
str3 = str1.replace("o","E")#替换字符
print(str3)
str3 = str1.lower()#将字符串全变为小写
print(str3)
str3 = str1.upper()#将字符串全变为大写
print(str3)
str3 = str1.split(",")#按照指定符号分割字符串并组成一个列表,未指定按空格
print(str3)
str3 = str1.split()
print(str3)
str3 = str1.strip()#剔除字符串两端的指定字符，未指定按空格
print(str3)
str3 = str1.strip(",")
print(str3)
str3 = str1.startswith("a")#判断字符串是否以指定字符开头
print(str3)
str3 = str1.startswith("h")
print(str3)

#案例1 邮箱注册页面（必须包含一个@和至少一个.）
email = input("请输入你要注册的邮箱：")
if email.count("@") == 1 and "." in email :#或者email.count(".") >= 1
    print("注册成功！")
else:
    print("注册失败！")

#案例2 判断回文
str1 = input("输入：")
if str1[::-1] == str1:
    print("该字符串是回文字符串")
else:
    print("不是回文")

#案例3 转大写并遍历
str1 = input("输入：")
str2 = str1.upper()
list1 = [*str2]
print(list1)
for i in list1:
    print(i)


#3 元组tuple 元组名 = (元素1，元素2，元素3....) 有序(可通过索引访问)，可重复，不可修改（与列表比元组只不可修改其他一致）
tuple1 = (1,2,2,3,"人生苦短，我用python",True)
print(tuple1)
print(type(tuple1))
tuple2 = ()#空元组或者tuple3 = tuple()
tuple3 = tuple()
print(tuple2)
print(type(tuple2))
tuple_01 = (1,)#对于定义的元组里只有一个元素必须在元素后面加一个","，否则解释器会解释为一个字面量

#3.1 元组切片
tuple_1 = tuple1[:4:]
print(tuple_1)
tuple_1 = tuple1[4:5]
print(tuple_1)
tuple_1 = tuple1[0::2]
print(tuple_1)

#3.2 元组常见方法
tuple_1 = tuple1.count(2)
print(tuple_1)
tuple_1 = tuple1.count(3)
print(tuple_1)
tuple_1 = tuple1.index(2)#获取指定元素的第一个索引
print(tuple_1)

#3.3 元组的组包与解包
tuple_2 = (1,2,2,3)#像这样将多个值合并到一个容器中（元组，列表）称为组包
tuple_3 = (4,5,6,7)
t1 = 1,2,3,4    #组包时时也可以不加括号
t2 = 4,5,6,7
a1,b1,c1,d1 = tuple_2 #像这样将容器（元组，列表）解开成独立的元素，分别赋值给多个变量称为解包，此处为基础解包
a2,*b2,c2 = t1#拓展解包，a2为接收首元素，c2为接收末尾元素，*b2将其他元素组成一个列表

