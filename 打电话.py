


class People:
    __username = ""
    __sex = ""
    __age = 0
    __phone = None
    # def __init__(self,username,sex,age):
    #     self.__username = username
    #     self.__sex = sex
    #     self.__age = age
    def setUsername(self,username):
        self.__username = username
    def getUsername(self):
        return self.__username
    def setSex(self,sex):
        self.__sex = sex
    def getSex(self):
        return self.__sex
    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age
    def setPhone(self,phone):
        self.__phone = phone
    def getPhone(self):
        return self.__phone

    def fa(self):
        print("你伤害了我，还一笑而过，你爱的贪婪我爱的懦弱，眼泪流过，回忆是多余的，刻骨铭心就这样一笑而过")







class Phone:
    __money = 0         #话费
    __brand = ""        #品牌
    __battery = ""      #电池
    __screen = ""       #屏幕大小
    __standby = ""      #待机时间
    __integral = ""     #积分
    # def __init__(self,money,brand,battery,screen,standby,integral):
    #     self.__money = money
    #     self.__brand = brand
    #     self.__battery = battery
    #     self.__screen = screen
    #     self.__standby = standby
    #     self.__integral = integral
    def setMoney(self,money):
        self.__money = money
    def getMoney(self):
        return self.__money
    def setBrand(self,brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand
    def setBattery(self,battery):
        self.__battery = battery
    def getBattery(self):
        return self.__battery
    def setScreen(self,screen):
        self.__screen = screen
    def getScreen(self):
        return self.__screen
    def setStandby(self,standby):
        self.__standby = standby
    def getStandy(self):
        return self.__standby
    def setIntegral(self,integral):
        self.__integral = integral
    def getIntegral(self):
        return self.__integral
    def da(self):
        hao = input("请输入您要拨打的电话号码")
        if hao!="" or self.__money>1:
            time = input("请输入通话时长")
            time = int(time)
            if time>0 and time<10:
                self.__money = time
                self.__integral = time * 15
                print("本次通话总共消费了",self.__money,"元，累计积分",self.__integral,"分")
            elif time >= 10 and time < 20:
                self.__money = time * 0.8
                self.__integral = time * 39
                print("本次通话总共消费了",self.__money,"元，累计积分",self.__integral,"分")
            elif time >=20:
                self.__money = time * 0.65
                self.__integral = time *48
                print("本次通话总共消费了",self.__money,"元，累计积分",self.__integral,"分")
        else:
            print("请求错误，请重新输入")

p = Phone()
p.setMoney = "3毛"
p.Brand = "华为"
p.setBattery = "1000mAH"
p.setScreen = "6英寸"
p.setStandby = "12H"
p.setIntegral = "0"



pe = People()

pe.setUsername = "jason"
pe.setSex = "男"
pe.setAge = 22
pe.setPhone = 110
pe.setPhone=p

pe.fa()
p.da()



















