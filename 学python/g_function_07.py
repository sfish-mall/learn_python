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
