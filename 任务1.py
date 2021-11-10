import time
from threading import Thread
money = 0
basket = 0
class Cook1(Thread):
    name = ''
    egg = 0
    money1 = 0
    def run(self) -> None:
        while time.perf_counter() <= 100:
            global basket
            if basket < 500:
                basket += 1
                self.egg += 1
                self.money1 = self.egg *2.5
                print(self.name,self.egg)
            elif basket >= 500:
                time.sleep(3)
                if basket < 500:
                    continue
                else:
                    print('满了')
        print(self.name,'做了',self.egg,'个蛋挞，赚了',self.money1,'元')

class user(Thread):
    name = ''
    money2 =5000
    egg = 0
    count = 0
    def run(self) -> None:
        while time.perf_counter() <= 100:
            global basket
            global money
            if self.money2 > 0:
                if basket > 0:
                    self.money2 -= 3
                    self.egg += 1
                    basket -= 1
                    money += 3
                    print(self.name,self.money2)
                elif basket == 0:
                    print('没了')
                    time.sleep(4)
            else:
                print('没钱了')
                break
        print(self.name,'还剩',self.money2)
        # print('总销售额为',money)
# class Boos(Thread):
#     money = 0
#     def run(self) -> None:
#         start = time.time()
#         while True:
#             end = time.time()
#             if int(end -start) ==3:
#                 print('时间到了')
#                 break
        # while True:
        #     global basket
        #
        #     if time.perf_counter() >= 10:
        #         cmoney =  Cook1.egg * 2.5
        #
        #         print(cmoney,self.money)
        #         break
        #     else:
        #         self.money = user.egg * 3

c =Cook1()
c1 =Cook1()
c2 =Cook1()
u =user()
u1 =user()
u2 =user()
u3 =user()
u4 =user()
u5 =user()
u.name = 'a1'
u1.name = 'a2'
u2.name = 'a3'
u3.name = 'a4'
u4.name = 'a5'
u5.name = 'a6'

c.name = '张三'
c1.name = '李四'
c2.name = '王五'
c.start()
c1.start()
c2.start()
u.start()
u1.start()
u2.start()
u3.start()
u4.start()
u5.start()
