import random
list = []
# 生成一个包含20个随机整数的列表
for i in range(20):
    num = random.choice(range(10))
    list.append(num)
print("list长度: ", len(list))
print("未排序list: ", list)
list[0::2] = sorted(list[1::2], reverse=True)
print("排序list: ", list)