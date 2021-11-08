
import time
class kongtiao:
    __name = ""
    __money = 0
    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name
    def setmoney(self,money):
        if money>0:
            self.__money = money
        else:
            print("你买冰箱你还给我钱你是瞧不起我吗？")
    def getmoney(self):
        return self.__money
    def showkongtiao(self):
        print("欢迎使用", self.__name, "牌空调，此空调价格为：", self.__money)
    def shiyongkongtiao(self):
        while True:
            print("开机请按1")
            a = int(input())
            if a == 1:
                print("空调开机了，选择定时关闭请按1")
                b = int(input())
                if b == 1:
                    print("请选则定时的时间")
                    c = int(input())
                    if c>0:
                        print("空调将在", c, "秒后关闭")
                        for i in range(c):
                            print(end="")
                        time.sleep(c)
                        print("已关机")
                        break
                    else:
                        print("不欢迎罗志祥")
                        pass
                else:
                        print("你马上就被无限电费掏空你")
                        pass
            else:
                print("开机都不会你还玩吗？")
                pass

kt = kongtiao()
print("输入您要购买的品牌")
name1 = input()
kt.setname(name1)
print("你的预算是？")
a = int(input())
kt.setmoney(a)
kt.showkongtiao()
kt.shiyongkongtiao()

















