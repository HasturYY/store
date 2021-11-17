list = []
dict = {}
f = open(file="baidu_x_system.log",mode="r+",encoding='utf-8')
t = f.readlines()
# for i in range(len(t)):
#     x = t[i][:13]
for i in t:
    list = list + [i.split()[0]]
for i in list:
    dict[i] = dict.get(i,0) +1
print(dict)