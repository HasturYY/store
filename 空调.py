

class Air:
    __brand = ""
    __price = 0

    def setBrand(self,brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand
    def setPrice(self,price):
        self.__price = price
    def getPrice(self):
        return self.__price
    def bhoot(self):
        print("空调开机了")
    def hour(self,hour):
        hour = int(hour)
        print(self.__brand,"空调将在",hour,"分钟后开机")
    def off(self,off):
        print(self.__brand,"空调将在",off,"分钟后关机")
    def show(self):
        print(self.__brand,"空调大酬宾，每台价格低至",self.__price,"元")

A = Air()
A.setBrand("海尔")
A.setPrice(4999)

print(A.getBrand(),"空调大酬宾，每台价格低至",A.getPrice(),"元")

A.show()
A.hour(3)
A.bhoot()
A.off(5)










