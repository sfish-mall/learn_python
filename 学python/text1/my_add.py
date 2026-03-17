#加法模块
def add(num1, num2):
    return num1 + num2
#用来测试该模块当在该模块__name__ == __main__，在该模块外调用时__name__ == 模块名
if __name__ == '__main__':
    print("来了")