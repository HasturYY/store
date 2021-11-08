
class study:
    numb = None
    name =None
    age = None
    gender = None
    high = None
    weight = None
    achievement = None
    door = None
    phone = None

    def studystudy(self,what,time):
        print(self.name,"正在学习",what,"已经学习了",time)
    def playgame(self,game):
        print(self.name,"喜欢玩",game)
    def python(self,work,year,sum):
        print(self.name,"今年",self.age,"了，他正在",work,"已经写了",year,"一共写了",sum,"行代码")
    def numnum(self,*nums):
        print("nums:",nums)
        y = 0
        for i in nums:
            y += i
        print("正在求和总和为：",y)

st = study()
st.numb = 990717
st.name = "文一"
st.age = 18
st.gender = "man"
st.high = "180cm"
st.weight = "38kg"
st.achievement = "A-"
st.door = 30
st.phone = 4008208820

st.studystudy("混元功法","90天")
st.playgame("lol")
st.python("写代码","六个月了",10000)
a = 1
b = 2
c = 3
d = 4
st.numnum(a,b,c,d,a)












































