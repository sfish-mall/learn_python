#类
#类定义
#内部定义对象
class Cla:
    a = 1#类属性，通用属性
    b = 2
    def __init__(self,a,b):#对象初始化self即所要定义的对象名，当对象名定义完成时self会自主转换为所定义的对象名
        self.a1 = a#对象属性，私有属性
        self.b1 = b
    def add(self):#对象方法（类里面定义叫方法类外定义加函数）
        return self.a1+self.b1
    def __eq__(self, other):#魔法方法调用时会自主判断执行无需操作
        return self.a==other.a and self.a==other.a
#外部定义对象(不推荐)
class Cla1:
    pass
cla = Cla1()
cla.a = 1
cla.s = "s"

