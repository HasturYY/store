
class monkey:
    attribute = None
    __gender = None
    color = None
    weight = None

    def setgender(self,gender):
        if gender == "male" or gender == "female":
            self.__gender = gender

        else:
            print("别瞎搞")
    def getgendet(self):
        return self.__gender

    def makefire(self,material,method):
        print("快看这有一直",self.color,"的",self.__gender,self.attribute,"在用",material,method)
    def studystudy(self,study):
        print("即使这是一只",self.weight,"的胖猩猩也无法阻挡它",study,"的心")

mk = monkey()
mk.attribute = "红毛猩猩"
mk.setgender("male")
mk.color = "green"
mk.weight = "200kg"

mk.makefire("木头","钻木取火")
mk.studystudy("Learn to dance")



















