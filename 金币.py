'''
猜字游戏：
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环

'''
# import random
# #              20，10
# randint=random.randint(10, 20)#随机生成数字的范围：int   []
# print(randint)
# i=0
# while i<10:
#     num=int(input("请输入您猜的数字"))
#     if num==randint:
#         print("恭喜你猜对了")
#         break  # 退出
#     elif num>randint:
#         print("猜大了")
#     elif num<randint:
#         print("猜笑了")
#     else:
#         print("猜错了,继续猜")
#     i=i+1

#任务：开始金币有5个金币，每猜一次减一个为0就退出（or充钱）猜错3次也退出

glod=5
while glod>=0:
    import random
    randint=random.randint(0,10)
    i=int(input("请输入数字："))
    if 1==randint:
        print("金币+1")
        glod=glod+1
        print(glod)
    else:
        print("cuo")
        glod=glod-1
        print(glod)
        if glod==0:
            Qb=(int(input('+充Q币不,充1，不充随便')))
            if Qb==1:
                glod=(int(input("充多少？")))
            else:
                print("滚吧，穷逼")
                break


















