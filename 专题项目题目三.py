
class People:
    __name = ''
    __gender = ''
    __age = 0
    __cost = 0   # 剩余话费
    __brand = ''   # 品牌
    __battery = 0  # 电池容量
    __size = 0    # 屏幕大小
    __standby = 0   # 最大待机时长
    __integral = 0  # 积分

    def setname(self,name):
        if name == "":
            print("前来着何人？")
        elif len(name)>6 :
            print("少数民族等名字长只输入名即可")
        else:
            self.__name = name
    def getname(self):
        return self.__name

    def setgender(self,gender):
        if gender != "男" and gender != "女" :
            print("你谁啊你")
        else:
            self.__gender = gender
    def getgender(self):
        return self.__gender

    def setage(self,age):
        if 140>age>0:
            self.__age = age
        else:
            print("那个星球的？")
    def getage(self):
        return self.__age

    def setcost(self,cost):
        if cost<0:
            print("gun")
        else:
            self.__cost = cost
    def getcost(self):
        return self.__cost

    def setbrand(self,brand):
        self.__brand = brand
    def getbrand(self):
        return self.__brand

    def setbattery(self,battery):
        if battery<0:
            print("你太阳能的？")
        else:
            self.__battery = battery
    def getbattery(self):
        return self.__battery

    def setsize(self,size):
        self.__size = size
    def getsize(self):
        return self.__size

    def setstandby(self,standby):
        self.__standby = standby
    def getstandby(self):
        return self.__standby

    def setintegral(self,integral):
        self.__integral = integral
    def getintegral(self):
        return self.__integral



    def showphone(self):
        print('姓名', self.__name, '\n性别', self.__gender, '\n年龄', self.__age, '\n所拥有的手机剩余话费',
              self.__cost, '元！\n手机品牌', self.__brand, '\n手机电池容量', self.__battery, '%\n屏幕大小',
              self.__size, '寸\n最大待机时长', self.__standby, '分钟\n所拥有积分：', self.__integral)

p = People()
p.setname(input('输入姓名'))
p.setgender(input('输入性别'))
p.setage(int(input('输入年龄')))
p.setcost(float(input('输入手机剩余话费')))
p.setbrand(input('输入手机品牌'))
p.setbattery(float(input('输入电池容量')))
p.setsize(int(input('输入手机屏幕大小')))
p.setstandby(int(input('输入手机最大待机时长')))
p.setintegral(int(input('输入拥有积分')))

p.showphone()

huafei = p.getcost()
jifen = p.getintegral()


while False == 0:
    a = int(input("需要打电话话还是发短信，1发短信，2打电话"))

    if a == 1:
        xun = input()
        print("短信内容为：",a)
    elif a == 2:
        numb = (int(input("请输入要拨打的电话")),)
        if len(numb) != 11:
            print("需要大陆手机号")
        elif p.getcost()<1 or p.getcost() == 0:
            print("拨打失败")
        else:
             b = int(input("请输入你要打多长时间"))
             if 10>=b>0:
                 money = b*1
                 if huafei>=money:
                     huafei = huafei -money
                     print("本次通话使用了",money,"话费，您还剩余",huafei,"话费")
                     jifen = jifen + 15*b
                     print("本次获得",15*b,"积分","您现在有",jifen,"积分")
                 else:
                     print("没钱你聊啥呢？")
             elif 20>=b>10:
                 money = b*0.8
                 if money>=huafei:
                     huafei = huafei - money
                     print("本次通话使用了", money, "话费，您还剩余", huafei, "话费")
                     jifen = jifen +39*b
                     print("本次获得", 39 * b, "积分", "您现在有", jifen, "积分")
                 else:
                      print("没钱你聊啥呢？")
             elif b<0:
                 print("别瞎搞")
             else:
                 money = 0.65*b
                 if huafei >= money:
                     huafei = huafei - money
                     print("本次通话使用了", money, "话费，您还剩余", huafei, "话费")
                     jifen = jifen + 48 * b
                     print("本次获得", 48 * b, "积分", "您现在有", jifen, "积分")
                 else:
                     print("没钱你聊啥呢？")
    else:
        print("别瞎搞")


            









