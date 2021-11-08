'''
i.	人：年龄，性别，姓名。

ii.	现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。

iii.	现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。

'''

class Person:
    __age = 0
    __sex = ''
    __name = ''
    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name

    def setage(self,age):
        self.__age = age
    def getage(self):
        return self.__age

    def setsex(self,sex):
        self.__sex = sex
    def getsex(self):
        return self.__sex

class Worker(Person):
    def work(self):
        print(super().getname(),'正在干活')



class Student(Person):
    __num = 0
    def setnum(self,num):
        self.__num = num
    def getnum(self):
        return self.__num

    def study(self):
        print(super().getname(),'学习')

    def sing(self):
        print(super().getname(),'唱歌')

w = Worker()
w.setname('张三')
w.age = 10
w.sex = '男'
w.work()

s = Student()
s.setage(29)
s.setname('李四')
s.setsex('女')
s.setnum(23)
s.study()
s.sing()