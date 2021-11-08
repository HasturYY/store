
class car:
    user = ""
    size = 0
    wheel = 0
    color = ""
    weight = ""
    storage = ""

    def aotorace(self,solo):
        print(self.user,"P",self.size,"具有",solo,"的能力")

    def house(self,long):
        print(self.user,"型号为",self.size, "系最新的", long, "版颜色为：",self.color)

    def lingmu(self,taitou):
        print(self.user,"只有",self.wheel,"个轱辘，但它可以进行",taitou)

    def crs(self,country):
        print(self.user,"具有",country,"的能力")

    def tolaji(self,carman,hour):
        print("此款车为：",self.user,"他可以变成",carman,"他强大的储存量可以存放",self.storage,"油,可以支撑他变身",hour,"小时")

pg = car()
pg.user = "法拉利"
pg.size = 1
pg.wheel = 4
pg.color = "red"
pg.weight = "3.5T"
pg.storage = "50L"
pg.aotorace("赛车")#功能

bmw = car()
bmw.user = "宝马"
bmw.size = 9
bmw.wheel = 4
bmw.color = "orange"
bmw.weight = "45T"
bmw.storage = "60L"
bmw.house("X9SR")#功能

lm = car()
lm.user = "铃木"
lm.size = 3
lm.wheel = 2
lm.color = "green"
lm.weight = "1.5T"
lm.storage = "10L"
lm.lingmu("精神小伙龙抬头")#功能

fw = car()
fw.user = "五菱宏光"
fw.size = 0
fw.wheel = 3
fw.color = "black"
fw.weight = "2T"
fw.storage = "25L"
fw.crs("越野飙车激情狂欢")#功能

tlj = car()
tlj.user = "拖拉机蓝翔plus ss"
tlj.size = 9
tlj.wheel = 8
tlj.color = "red and yellow"
tlj.weight = "50T"
tlj.storage = "505L"
tlj.tolaji("大黄蜂",10)#功能


