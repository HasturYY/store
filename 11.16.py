from collections import Counter
index = open(file="baidu_x_system.log",mode="r+")
ff = dict(Counter(index.readlines()))
print([key for key,value in ff.items()if value > 1])
print({key: value for key,value in ff.items() if value > 1})