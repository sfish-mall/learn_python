#条件判断语句 if
score = float(input("输入你的成绩："))
if score >= 60 and score<90:
    print("成绩及格")
if score <60:
    print("成绩不及格")
if score >=90 and score <100:
    print("成绩优秀")
if score == 100:
    print("满分")
#案例 登录页面
my_account = 18806
my_password = 10086
account = int(input("请输入账号："))
password = int(input("请输入密码："))
if account == my_account and password ==my_password:
    print("登陆成功!\n欢迎您!")
if account != my_account or password != my_password:
    print("登录失败!\n账号或密码错误!")
#if...else双分支
my_account = 18806
my_password = 10086
account = int(input("请输入账号："))
password = int(input("请输入密码："))
if account == my_account and password ==my_password:
    print("登陆成功!\n欢迎您!")
else:
    print("登录失败!\n账号或密码错误!")
#案例1 算闰年平年
Year = int(input("请输入年份"))
if Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0:
    print(f"{Year}是闰年")
else:
    print(f"{Year}平年")
#案例2 奇偶数
num = int(input("请输入数字："))
if num % 2 == 0 :
    print(f"{num}是偶数")
else:
    print(f"{num}是奇数")
#案例3 判断正负
num1 = int(input("请输入数字："))
if num1 > 0 :
    print(f"{num}是正数")
elif num1 < 0 :
    print(f"{num}是负数")
else:
    print("零")
#if...elif...else多分支（轮询遍历）
#案例1 三角形判别
a = float(input("请输入a边长："))
b = float(input("请输入b边长："))
c = float(input("请输入c边长："))
if a + b >c and a + c > b and c + b > a :
    if a == b and b == c :
        print("等边三角形")
    elif (a == b and b != c) or (a == c and c != b) or (b == c and c != a) :
        print("等腰三角形")
    else:
        print("三角形")
else:
    print("此三边无法构成三角形")
#案例2 计算电费
electric = float(input("请输入用电度数："))
if electric <   2880:
    print(f"属于第一档，所需{electric * 0.4883}元")
elif electric >= 2880 and electric <= 4800:
    print(f"属于第二档，所需{electric * 0.5383}元")
else:
    print(f"属于第三档，所需{electric*0.7883}元")
#match...case...模式匹配
#案例1 计算器
a = float(input("输入第一个数字："))
b = float(input("输入第二个数字："))
sign = input("输入(+ - * /)：")
match sign:
    case "+":
        print(f"{a}+{b}={a + b}：")
    case "-":
        print(f"{a}+{b}={a - b}：")
    case "*":
        print(f"{a}+{b}={a * b}：")
    case "/" if b != 0:
        print(f"{a}+{b}={a / b}：")
    case _:
        print("仅支持 +-*/ 运算！")
#案例2 游戏操作
while True:
    cmd = input("请输入:")
    match cmd:
        case "上" | "w":
            print("角色向上移动")
        case "下" | "s":
            print("角色向下移动")
        case "左" | "a":
            print("角色向左移动")
        case "右" | "d":
            print("角色向右移动")
        case "跳" | " ":  # 空格输入
            print("角色跳")
        case "攻击" | "j":
            print("角色攻击")
        case "退出" | "esc":
            print("退出游戏")
            break
        case _:  # 通配符，匹配所有未命中的情况
            print("未知指令，无对应动作")