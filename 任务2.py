'''
考查知识点：继承的传递性
按要求定义类
要求：
1、定义厨师类，有姓名和年龄的属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的无参数的蒸饭方法；
2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
3、定义厨师的子类的子类，重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
4、定义测试类，创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，对厨师类中的姓名和年龄属性赋值，并获取赋值后的属性值打印到控制台上；
5、使用厨师的孙子类对象调用该对象除了getXxx与setXxx以外的其他方法；

'''
class Cook:
    __name = ''
    __age  = 0

    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name

    def setage(self,age):
        self.__age = age
    def getage(self):
        return self.__age

    def steam(self):
        print('蒸饭')

class Cook1(Cook):
    def fry(self):
        print('炒菜')

class Cook2(Cook1):
    def steam(self):
        print('蒸啊')

    def fry(self):
        print('炒啊')

c = Cook2()
c.setname('张三')
c.setage(12)
print(c.getname(),c.getage())
c.fry()
c.steam()
