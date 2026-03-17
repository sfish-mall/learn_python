"""函数是组织好的，可重复调用的，有特定功能的代码片段 def 函数名(参数（形参）列表): 可以有多个参数多个返回值
                                                 函数体
                                                 return 返回值
"""
# #1 函数定义(函数使用都是先定义后调用且只有在调用时才执行) 定义时可以有参数或返回值也可以没有
# def func1():
#     print("****************************")
# def func2(x,y):
#     return x + y
# def func3(x,y,r):
#     """
#     该函数是计算长方形面积和圆面积以及圆周长
#     :param x: 长方形长
#     :param y: 长方形宽
#     :param r: 圆半径
#     :return: 长方形面积 圆面积 圆周长
#     """#函数说明文档可用help()关键字查看文档内容，也可以用光标放在函数上查看
#     return x * y,(r**2) * 3.14,2 * 3.14 * r
# def func4(name,age,cite="灵气大陆",major="普通人"):#定义默认形参，同样默认形参必须在未默认形参后面
#     print(f"名字:{name} \t年龄:{age} \t城市:{cite} \t专业:{major}")
# func1()#函数调用
# func2(1,2)#函数调用时所传参数时实参，函数内部是形参
# al = func3(2,5,6)#多返回值函数赋值时会自动组成一个元组赋值
# print(al)
# print(type(al))
# func4("王林",18,"灵气大陆","修仙者")#位置传参或位置参数
# func4(name="李慕婉",age=18,cite="灵气大陆",major="修仙者")#关键字传参或关键字参数
# func4("李老道",22,cite="灵气大陆",major="修仙者")#位置传参+关键字传参，注意位置参数必须在关键字参数前
# func4("李平",10)#没传递参数的会默认为函数默认形参
# #1.1 变量作用域
# aug = 0#全局变量，作用域是整个代码
# def f():
#     aug =180#局部变量,出函数自动销毁，但是在函数中如果全局变量与局部变量名字相同则会优先使用局部变量
#     print(aug)
# f()
# print(aug)
#
# def f_1():
#     global aug#如果想在函数中使用并修改全局变量则须使用global关键字
#     aug =180
#     print(aug)
# f_1()
# print(aug)

# #案例1 计算三角形面积
# def triangle_area(b,h):
#     return (b * h) / 2
# b = float(input("输入底:"))
# h = float(input("输入高:"))
# print(f"面积为：{triangle_area(b,h)}")
# #案例2 判断字符串中元音字母个数
# def letters_num(s):
#     num = 0
#     for i in s:
#         if i in "aeiouAEIOU":
#             num += 1
#     print(f"元音字母个数有{num}")
# str1 = input("请输入字符串:")
# letters_num(str1)
# #案例3 计算班级学生分数
# def s_score(list1):
#     return max(list1),min(list1),round(sum(list1)/len(list1),2)
# max1, min1, sum1 = s_score([91,62,83,74,65,96,76,80,95])
# print(max1,min1,sum1)
# #案例4 计算分数等级
# def score_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 75:
#         return "B"
#     elif score >= 60:
#         return "C"
#     else:
#         return "D"
# score1 = float(input("输入学生分数:"))
# print(f"该学生评级为:{score_grade(score1)}")
# #案例5 判断回文串
# def pal_check(s):
#     if s == s[::-1]:
#         return '是回文'
#     else:
#         return '不是回文'
# str2 = input("请输入文本:")
# print(pal_check(str2))
# #案例6 时间转换
# def time_reverse(s):
#     print(f"{s}秒等于{round(s / 60,4)}分")
#     print(f"{s}秒等于{round(s / 3600,4)}小时")
#     print(f"{s}秒等于{s}秒")
# times = float(input("请输入几秒: "))
# time_reverse(times)
# #案例7 判断三角形类型
# def triangle_type(x,y,z):
#     if x + y < z or x + z < y or y + z < x:
#         return "不能构成三角形"
#     elif x == y == z:
#         return "等边三角形"
#     elif x == y or y == z or x == z:
#         return "等腰三角形"
#     else:
#         return "普通三角形"
# print(triangle_type(1, 1, 3))


# #2 函数不定长参数
# def func_1(*args,**kwargs):#*args不定长位置参数，用来接受收多个位置参数；**kwargs不定长关键字参数，用来接受多个关键字参数
#     return args,kwargs
# print(func_1(1,2,3,a = 1,b = 2,c = 3))


# #3 函数传参类型
# #3.1 普通参数:数字、布尔、列表、元组、字符串、集合、字典等
# def f(num,b,list1,tuple1,str1,set1,dict1):
#     return num,b,list1,tuple1,str1,set1,dict1
# print(f(1,True,[1,2,3],(1,2,3),"我是谁",{1,2,3},{"a":1,"b":2,"c":3}))

# #3.2 函数参数
# def z(x,y):
#     print(f"{x+y}")
# def z1(q, w, zero):
#     return zero(q, w)
# print(z1(1,2,z))
#
#
# #4 匿名函数 #一般作为高级函数的参数
# arr = lambda a1 , b1 :a1 + b1
# print(arr(1,2))
# #匿名函数使用案例
# list_l = ["C","Java","C++","Python","Jack","PHP","Go","JavasCript","Rust"]
# list_l.sort()
# print(list_l)
# list_l.sort(key=lambda item : len(item))#匿名函数典型使用场景
# print(list_l)
# list_l.sort(key=lambda item : len(item), reverse=True)
# print(list_l)

# #案例1 阶乘
# def func_2(x):#递归操作
#     if x == 1:
#         return 1
#     else:
#         return x * func_2(x - 1)
# x = int(input("请输入所要阶乘的数字:"))
# print(func_2(x))
# #案例2 电商订单计算器
# def func_3(*args,coupon = 0,score = 0,express):
#     list_price = [s[1] * s[2]for s in args]
#     total_price = sum(list_price)
#     if total_price >= 5000 and coupon < total_price:
#         total_price -= coupon
#     if total_price >= 5000 and  score // 100 < total_price:
#         total_price -= score//100
#     return total_price + express
# print(f"所需金额:{func_3(("鼠标",900,10),("键盘",1800,2),("耳机",190,3),coupon=20,score=5000,express=10)}")


# #5 类型注解 就是给变量、函数参数、返回值标上类型以便于阅读，IDE提示，静态检索，方便运行
# #5.1 基础变量注解
# name : str = "黄山落叶松也落山黄"
# num : int = 5
# float1 : float = 1.1
# is_student : bool = True
# n:None = None#空类型注解
# #不进行注解若赋值对应字面量，python解释器会自主进行注解
# name1  = "黄山落叶松叶落山黄"
# num1 = 5
# float_1 = 1.1
# is_student1 = True
# #5.2 函数参数+返回值注解
# def func1(s: str,i:int,is_student_1:bool,f : float) ->tuple [str,int,bool,float] :
#     return s,i,is_student_1,f
# #5.3 容器元素注解
# nums : list[int | str] = [1,2,3,4,"a"]#多类型注解
# strs : str = "黄山落叶松叶落山黄"
# tuples : tuple[int | str] = (1,2,3,4,"b")
# sets : set[int | str] = {1,2,3,4,"str"}
# dicts : dict[str,int] = {"a": 1,"b":2,"c":3,"d":4}
# #5.4 类注解
# class FClass:
#     def __init__(self,name:str,num:int):
#         self.name = name
#         self.num = num
# #5.5 任意类型（不推荐）
# x : any = 123
# print(x)


# #包调用,起名的就不写了
# import text1.my_mul
# print(text1.my_mul.mul(2,3))
# from text1 import my_minu
# print(my_minu.minus(2,3))
# from text1.my_mul import mul
# print(mul(2,3))

