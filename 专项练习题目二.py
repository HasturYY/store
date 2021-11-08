
class student:
    __user = ""
    __age = 0

    def setuser(self,user):
        if user == "":
            print("你没名字你玩啥呢？")
        elif len(user)>6:
            print("名字过长只填名字即可")
        else:
            self.__user = user
    def getuser(self):
        return self.__user

    def setage(self,age):
        if 16< age <26 :
            self.__age = age
        else:
            print("不符合大学生年龄")
    def getage(self):
        return self.__age

    def showme(self):
        print("大家好，我叫",self.__user,"今年",self.__age,"岁了")


    def compare(self, student):  # self代表我自己    student代表另一个人
        if self.__age > student.getage():
            print("我比同桌大", (self.__age - student.getage()), "岁！")
        elif self.__age < student.getage():
            print("我比同桌小", (student.getage() - self.__age), "岁！")
        else:
            print("我俩一样大！")

s = student()
s.setuser("阿强")
s.setage(21)
s.showme()

# 同桌
st = student()
st.setuser("张三")
st.setage(20)
# 比较
s.compare(st)


















