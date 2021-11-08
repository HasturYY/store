from DBUtils import update
from DBUtils import select
import random

class bank:
    def welcome(self):
        print("***************************")
        print("*    中国工商银行          *")
        print("*     账户管理系统         *")
        print("***************************")
        print(" ")
        print("*1、开户                   *")
        print("*2、存钱                   *")
        print("*3、取钱                   *")
        print("*4、转账                   *")
        print("*5、查询                   *")
        print("*6、欢迎下次光临            *")
        print("****************************")
    # #初始化银行
    # bank={}
    # #'Frank': {'account': 24275182, 'password': '123456', 'country': '中国', 'province': '山东', 'steert': '曹县', 'door': '001', 'money': 0, 'bank_name': '保熟银行'}
    # #定义一个开户银行
    bank_name="埃塞俄比亚银行"
    # #定义添加到银行 定义函数元素对应元素  不是名称对名称
    #
    #
    def bankadd(self):
        # 定义用户入参
        account = random.randint(10000000, 99999999)
        name = input("请输入您的名称")
        password = input("请输入您的密码")
        print("请输入你的详细信息")
        country = input("\t\t请输入您的国籍")  # \t ==tab
        province = input("\t\t请输入您的省份")
        steert = input("\t\t请输入您的街道")
        door = input("\t\t请输入您的门牌号")

        sql = "select count(*) from users"
        param = []
        data = select(sql,param)
        print(data)
        if data[0][0] >= 100:
            return print("本银行已满请到其他银行开户")

        sql1 = "select * from users where username = %s"
        param1 = [name]
        data1 = select(sql1,param1)#((),)
        if len(data1) != 0:
            return print("用户已存在")

        sql2 = "insert into users value(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param2 = [account,name,password,country,province,steert,door,self.bank_name,0]
        update(sql2,param2)
        return print("恭喜你开户成功，一下是您的相信信息")


    def access(self):
        name = input('请输入用户名：')
        sql = "select * from users where username = %s"
        param = [name]
        date=select(sql,param)
        print(type(date))
        if len(date) !=0:
            money = int(input('请输入存储金额：'))
            sql = "update users set money = money + %s where username = %s"
            param = [money,name]
            update(sql,param)
            return  print('存储成功！以下是您的详细信息。')

        else:return print('没得')


    def take(self):
        name = input('请输入用户名：')
        password = int(input('请输入密码：'))

        sql="select * from users where username = %s"
        param = [name]
        date = select(sql,param)
        paswd = date[0][2]
        manei = date[0][8]
        print(manei)
        if len(date) != 0:
            if password ==paswd:
                money=int(input('请输入取款金额'))
                if money <=manei:
                    sql="update users set money = money - %s where username = %s"
                    param=[money,name]
                    update(sql,param)
                    return   print('取款成功！；您的账户余额为：')

                else:
                    return print('余额不足')
            else:
                return print('密码错误')
        else:
            return print('么得')


    def shift(self):
        off_name = input('请输入转出用户名')
        on_name = input('请输入转入用户名')
        off_passwd = int(input('请输入转出用户密码'))
        off_money = int(input('请输入转出的金额'))
        sql = "select * from users where username = %s "
        param = [off_name]
        datex = select(sql,param)

        sql = "select * from users where username = %s "

        param = [on_name]
        date = select(sql,param)
        print(date)
        date1 = datex[0][2]
        date2 = datex[0][8]
        # date3 = date[1][8]
        print(date1,date2,date,datex)
        if len(date) >= 1 and len(datex) >= 1:
            if off_passwd == date1:
                if off_money <=date2:
                    sql = "update users set money = money - %s where username = %s"
                    param = [off_money,off_name]
                    update(sql,param)
                    sql1 = "update users set money = money + %s where username = %s"
                    param1 = [off_money, on_name]
                    update(sql1, param1)
                    return print('转账成功')
                else:
                    return print('no money')
            else:
                return print('no passwd')
        else:
            return print('么得')

    def seek(self):
        name = input('请输入用户名')
        passwd = int(input('请输入密码'))
        sql = "select * from users where username = %s"
        param = [name]
        data = select(sql, param)
        if len(data) != 0:
            sql1 = "select password from users where username =%s "
            param1 = [name]
            data1 = select(sql1, param1)
            print(data1)
            data2=data1[0][0]
            print(type(passwd),type(data2))
            if passwd == data2:
                print('ok')
                sql = "select * from users where username = %s"
                param = [name]
                date = select(sql, param)
                print(date)
                info = '''
                        ------------个人信息------------
                                   用户名:%s
                                   账号：%s
                                   密码：*****
                                   国籍：%s
                                   省份：%s
                                   街道：%s
                                   门牌号：%s
                                   余额：%s
                                   开户行名称：%s
                        ******************************
                        '''
                print(info % (date[0][1], date[0][0], date[0][3], date[0][4], date[0][5], date[0][6], date[0][8], date[0][7]))
            else:
                return print('密码错误')
        else:
            return print('用户名错误')
    def go(self):
        while False==0:
            index=int(input("请输入您需要的业务"))
            if index ==1:
                print("开户")
                self.bankadd()
                print(bank)
            elif index ==2:
                print("存钱")
                self.access()
            elif index ==3:
                print("取钱")
                self.take()
            elif index ==4:
                print("转账")
                self.shift()
            elif index ==5:
                print("查询")
                self.seek()
            elif index ==6:
                print("下次光临")
                break
        print(bank)

b = bank()
b.welcome()
b.go()
