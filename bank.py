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
    if len(bank)>=100:
        return 3
    elif name in bank:
        return 2
    else:
        bank[name]={
            "account":account,
            "password":password,
            "country":country,
            "province":province,
            "steert":steert,
            "door":door,
            "money":0,
            "bank_name":bank_name
        }
        return 1

def access1(name):
    if name in bank:
        print("余额：%d"%bank[name]['money'])
        money=int(input('请输入存储金额：'))+bank[name]['money']
        bank[name]['money']=money
        return True
    else:
        return False

def take1(name,password,take_money):
    if name in bank:
        if password == bank[name]['password']:
            if take_money <= bank[name]['money']:
                bank[name]['money']=bank[name]['money']-take_money
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

def shift1(off_name,on_name,off_passwd,off_money):
    if off_name in bank and on_name in bank:
        if off_passwd == bank[off_name]['password']:
            if off_money<=bank[off_name]['money']:
                bank[off_name]['money']-=off_money

                bank[on_name]['money']+=off_money


                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

def seek1(name,passwd):
    if name in bank:
        if passwd == bank[name]['password']:
            return 0
        else:
            return 2
    else:
        return 1

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
               '''
        # 每个元素都可传入%
        print(info % (name, account, country, province, steert, door, bank[name]["money"], bank_name))

def access():
    name=input('请输入用户名：')
    num1=access1(name)
    if num1==True:
        print('存储成功！以下是您的详细信息。')
        info='''
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
        '''
        print(info % ( name,  bank[name]['account'], bank[name]['country'], bank[name]['province'],bank[name]['steert'] , bank[name]['door'], bank[name]["money"], bank_name))
    elif num1==False:
        print('没得')

def take():
    name = input('请输入用户名：')
    password=input('请输入密码：')
    take_money=int(input('请输入取出金额：'))
    num2=take1(name,password,take_money)
    if num2==0:
        print('取款成功！；您的账户余额为：%d'%bank[name]['money'])
    elif num2==1:
        print('么得')
    elif num2==2:
        print('密码错误')
    elif num2==3:
        print('余额不足')

def shift():
    off_name=input('请输入转出用户名')
    on_name=input('请输入转入用户名')
    off_passwd=input('请输入转出用户密码')
    off_money=int(input('请输入转出的金额'))
    num3=shift1(off_name,on_name,off_passwd,off_money)
    if num3==0:
        print('转账成功，转出用户余额：%d'%bank[off_name]['money'],'转入用户余额：%d'%bank[on_name]['money'])
        print('转账成功')
    elif num3==1:
        print('么得')
    elif num3==2:
        print('no passwd')
    elif num3==3:
        print('no money')

def seek():
    name=input('请输入用户名')
    passwd=input('请输入密码')
    num4=seek1(name,passwd)
    if num4==0:
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
                '''
        print(info % (name, bank[name]['account'], bank[name]['country'], bank[name]['province'], bank[name]['steert'],
                      bank[name]['door'], bank[name]["money"], bank_name))
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