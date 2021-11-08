
class computer:
    attribute = None
    size = None
    sleeptime = None
    color = None
    weight = None
    cup = None
    ssd = None
    usb = None

    def playgame(self,name,game):
        print("我叫",name,"我喜欢玩",game,"我的电脑是",self.attribute,"我的cup是",self.cup)

    def dowork(self,work):
        print("我的电脑待机时长是",self.sleeptime,"可以轻松的",work)

c = computer()
c.attribute = "惠普暗影精灵4"
c.size = "15.6寸"
c.sleeptime = "1 hour"
c.color = "black"
c.weight = "5.4kg"
c.cup = "I7-8750H"
c.ssd = "16G"
c.usb = "1T"
c.playgame("刘华强","英雄联盟")
c.dowork("写代码")












