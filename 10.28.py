
import xlrd
# import math
# import xlwt

wb=xlrd.open_workbook(filename="2020年每个月的销售情况.xlsx",encoding_override=True)

l=0
for i in range(12):
    st=wb.sheet_by_index(i)
    rowd=st.col_values(2,1)
    rowds=st.col_values(4,1)
    for j in range(len(rowd)):
        k=rowds[j]*rowd[j]
        l+=k
print("总销量",round(l,2))

u = 0
for p in range(12):
    std=wb.sheet_by_index(p)
    cold=std.col_values(4,1)
    for o in range(len(cold)):
        y = cold[o]
        u+=y
print("平均每日销量",round(u/365))

r1=0
yrf=[]
nzk=[]
fy=[]
pc=[]
tx=[]
cs=[]
my=[]
mj=[]
xxz=[]
py=[]
xxk=[]
wy=[]
qbk=[]
for q in range(12):
    sts=wb.sheet_by_index(q)
    colds=sts.col_values(1,1)
    colder=sts.col_values(4,1)
    r1=0
    yrf = []
    nzk = []
    fy = []
    pc = []
    tx = []
    cs=[]
    my=[]
    mj=[]
    xxz=[]
    py=[]
    xxk=[]
    wy=[]
    qbk=[]
    for w in range(len(colds)):
        r=colder[w]
        r1+=r
        if colds[w]=="羽绒服" :
            yrf.append(colder[w])
        elif colds[w]=="牛仔裤":
            nzk.append(colder[w])
        elif colds[w]=="风衣":
            fy.append(colder[w])
        elif colds[w]=="皮草":
            pc.append(colder[w])
        elif colds[w]=="T恤":
            tx.append(colder[w])
        elif colds[w]=="衬衫":
            cs.append(colder[w])
        elif colds[w]=="棉衣":
            my.append(colder[w])
        elif colds[w]=="马甲":
            mj.append(colder[w])
        elif colds[w]=="小西装":
            xxz.append(colder[w])
        elif colds[w]=="皮衣":
            py.append(colder[w])
        elif colds[w]=="休闲裤":
            xxk.append(colder[w])
        elif colds[w]=="卫衣":
            wy.append(colder[w])
        elif colds[w]=="铅笔裤":
            qbk.append(colder[w])

    print("羽绒服月占比"'%f%%'%((sum(yrf)/r1)*100))
    print("牛仔裤月占比"'%f%%'%((sum(nzk)/r1)*100))
    print("风衣月占比"'%f%%'%((sum(fy)/r1)*100))
    print("皮草月占比"'%f%%'%((sum(pc)/r1)*100))
    print("T恤月占比"'%f%%' % ((sum(tx) / r1) * 100))
    print("衬衫月占比"'%f%%' % ((sum(cs) / r1) * 100))
    print("棉衣月占比"'%f%%' % ((sum(my) / r1) * 100))
    print("马甲月占比"'%f%%' % ((sum(mj) / r1) * 100))
    print("小西装月占比"'%f%%' % ((sum(xxz) / r1) * 100))
    print("皮衣月占比"'%f%%' % ((sum(py) / r1) * 100))
    print("休闲裤月占比"'%f%%' % ((sum(xxk) / r1) * 100))
    print("卫衣月占比"'%f%%' % ((sum(wy) / r1) * 100))
    print("铅笔裤月占比"'%f%%' % ((sum(qbk) / r1) * 100))




