from DBUtils import update
from DBUtils import select
import random
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
#初始化银行
bank={}
#'Frank': {'account': 24275182, 'password': '123456', 'country': '中国', 'province': '山东', 'steert': '曹县', 'door': '001', 'money': 0, 'bank_name': '保熟银行'}
#定义一个开户银行
bank_name="埃塞俄比亚银行"
#定义添加到银行 定义函数元素对应元素  不是名称对名称


def bankadd(account,name,password,country,province,steert,door):

    sql = "select count(*) from users"
    param = []
    data = select(sql,param,mode="one")
    if data[0] >= 100:
        return 3

    sql1 = "select * from users where username = %s"
    param1 = [name]
    data1 = select(sql1,param1)#((),)
    if len(data1) != 0:
        return 2

    sql2 = "insert into users value(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account,name,password,country,province,steert,door,bank_name,0]
    update(sql2,param2)
    return 1

    # if len(bank)>=100:
    #     return 3
    # elif name in bank:
    #     return 2
    # else:
    #     bank[name]={
    #         "account":account,
    #         "password":password,
    #         "country":country,
    #         "province":province,
    #         "steert":steert,
    #         "door":door,
    #         "money":0,
    #         "bank_name":bank_name
    #     }
    #     return 1

def access1(name):

    sql = "select * from users where username = %s"
    param = [name]
    date=select(sql,param)
    print(type(date))
    if len(date) !=0:
        money = int(input('请输入存储金额：'))
        sql = "update users set money = money + %s where username = %s"
        param = [money,name]
        update(sql,param)
        return True
    else:return False

    # if name in bank:
    #     print("余额：%d"%bank[name]['money'])
    #     money=int(input('请输入存储金额：'))+bank[name]['money']
    #     bank[name]['money']=money
    #     return True
    # else:
    #     return False

def take1(name,password):

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
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1


    # if name in bank:
    #     if password == bank[name]['password']:
    #         if take_money <= bank[name]['money']:
    #             bank[name]['money']=bank[name]['money']-take_money
    #             return 0
    #         else:
    #             return 3
    #     else:
    #         return 2
    # else:
    #     return 1

def shift1(off_name,on_name,off_passwd,off_money):

    sql = "select * from users where username = %s or username = %s order by username"
    param = [off_name,on_name]
    date = select(sql,param)
    print(date)
    date1 = date[0][2]
    date2 = date[0][8]
    date3 = date[1][8]
    print(date1,date2,date3)
    if len(date) >= 2:
        if off_passwd == date1:
            if off_money <=date2:
                sql = "update users set money = money - %s where username = %s"
                param = [off_money,off_name]
                update(sql,param)
                sql1 = "update users set money = money + %s where username = %s"
                param1 = [off_money, on_name]
                update(sql1, param1)
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

    # if off_name in bank and on_name in bank:
    #     if off_passwd == bank[off_name]['password']:
    #         if off_money<=bank[off_name]['money']:
    #             bank[off_name]['money']-=off_money
    #
    #             bank[on_name]['money']+=off_money
    #
    #
    #             return 0
    #         else:
    #             return 3
    #     else:
    #         return 2
    # else:
    #     return 1

def seek1(name,passwd):

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
            return 0
        else:
            return 2
    else:
        return 1

    # if name in bank:
    #     if passwd == bank[name]['password']:
    #         return 0
    #     else:
    #         return 2
    # else:
    #     return 1

#定义用户入参
def useradd():
    account=random.randint(10000000,99999999)
    name=input("请输入您的名称")
    password=input("请输入您的密码")
    print("请输入你的详细信息")
    country=input("\t\t请输入您的国籍")#\t ==tab
    province=input("\t\t请输入您的省份")
    steert=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    num=bankadd(account,name,password,country,province,steert,door)
    if num ==3:
        print("本银行已满请到其他银行开户")
    elif num== 2:
        print("用户已存在")
    elif num==1:
        print("恭喜你开户成功，一下是您的相信信息")
        # info = '''
        #            ------------个人信息------------
        #            用户名:%s
        #            账号：%s
        #            密码：*****
        #            国籍：%s
        #            省份：%s
        #            街道：%s
        #            门牌号：%s
        #            余额：%s
        #            开户行名称：%s
        #        '''
        # # 每个元素都可传入%
        # print(info % (name, account, country, province, steert, door, bank[name]["money"], bank_name))

def access():
    name=input('请输入用户名：')
    num1=access1(name)
    if num1==True:
        print('存储成功！以下是您的详细信息。')
        # info='''
        # ------------个人信息------------
        #            用户名:%s
        #            账号：%s
        #            密码：*****
        #            国籍：%s
        #            省份：%s
        #            街道：%s
        #            门牌号：%s
        #            余额：%s
        #            开户行名称：%s
        # '''
        # print(info % ( name,  bank[name]['account'], bank[name]['country'], bank[name]['province'],bank[name]['steert'] , bank[name]['door'], bank[name]["money"], bank_name))
    elif num1==False:
        print('没得')

def take():
    name = input('请输入用户名：')
    password=int(input('请输入密码：'))
    num2=take1(name,password)
    if num2==0:
        print('取款成功！；您的账户余额为：')
    elif num2==1:
        print('么得')
    elif num2==2:
        print('密码错误')
    elif num2==3:
        print('余额不足')

def shift():
    off_name=input('请输入转出用户名')
    on_name=input('请输入转入用户名')
    off_passwd=int(input('请输入转出用户密码'))
    off_money=int(input('请输入转出的金额'))
    num3=shift1(off_name,on_name,off_passwd,off_money)
    if num3==0:
        print('转账成功')
    elif num3==1:
        print('么得')
    elif num3==2:
        print('no passwd')
    elif num3==3:
        print('no money')

def seek():
    name=input('请输入用户名')
    passwd=int(input('请输入密码'))
    num4=seek1(name,passwd)
    if num4==0:
        print('ok')
        sql="select * from users where username = %s"
        param=[name]
        date=select(sql,param,mode='one')
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
        print(info % (date[1],date[0],date[3],date[4],date[5],date[6],date[8],date[7]))
    elif num4==1:
        print('用户名错误')
    elif num4==2:
        print('密码错误')


while False==0:
    index=int(input("请输入您需要的业务"))
    if index ==1:
        print("开户")
        useradd()
        print(bank)
    elif index ==2:
        print("存钱")
        access()
    elif index ==3:
        print("取钱")
        take()
    elif index ==4:
        print("转账")
        shift()
    elif index ==5:
        print("查询")
        seek()
    elif index ==6:
        print("下次光临")
        break
print(bank)