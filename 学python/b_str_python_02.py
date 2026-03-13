#字符串
#1 字符串定义三种'',"",""" """
str1 = ' my string1 '
print(str1)
str2 = " my string2 "
print(str2)
str3 = """ my string3 """
print(str3)
#注：如果字符串中出现所对应的引号，那么该引号会与前面的引号结合报错
#这时候可以用转义字符或者用与字符串中不同的引号来定义
str4 = " I'm a string4 "
print(str4)
str4 = ' I\'m a string4 '
print(str4)
str5 = """ 我" a string5 """
print(str5)
str5 = """ "我\" a string5 """
print(str5)
#转义字符\


#字符串拼接
#1 直接字面量拼接
Str = "人生苦短" "我用python"
print(Str)
#2 字符串变的拼接'+'
Str1 = "人生苦短"
Str2 = "我用python"
print("龟叔说：" + Str1+ "," + Str2)
#案例
name = "Cao"
age = 21 #这里是整型’+‘只能用于字符串拼接所以要用str（）把整型转为字符串型
pro = "智能科学与技术"
hobby = "python, C"
print("我叫" +name+ ",今年" +str(age)+ "岁，专业是" +pro+ ",爱好有" +hobby)


#字符串格式化
#1 通过%s|%(变量/表达式)占位符，谨记前面有多少个%s后面就有多少个值
name = "Cao"
age = 21
pro = "智能科学与技术"
hobby = "python, C"
print("我叫%s,今年%s岁，专业是%s,爱好有%s"%(name,age,pro,hobby))
#2 通过f...{}...(主流推荐)
name = "Cao"
age = 21
pro = "智能科学与技术"
hobby = "python, C"
print(f"我叫{name},今年{age}岁，专业是{pro},爱好有{hobby}")
#3 通过{}... .format()
name = "Cao"
age = 21
pro = "智能科学与技术"
hobby = "python, C"
print("我叫{},今年{}岁，专业是{},爱好有{}".format(name,age,pro,hobby))