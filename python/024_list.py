"""
list列表
"""

##解包：将列表这一容器解开成一个一个独立的元素
##组包：将多个值合并到一个容器

s = [3, 4, 6, 9, 44, 66, 88, "hello", True]
print(type(s))


###访问列表元素
# 获取
print(s[0])  # 正向索引，从0开始
print(s[-1])  # 反向索引，从-1开始

# 修改
s[1] = "a"
print(s[1])
print(s)

# 注意！如果指定的索引超出范围，将会报错list assignment index out of range
s[10] = 2
print[3]

# 删除
del s[3]
print(s)

# 遍历列表的每一个元素
for i in s:
    print(i)


###列表切片
s = ["a", "b", "r", "t", "g", "p"]
# 切片操作 s[开始索引:结束索引:步长]
print(s[0:3:1])
print(type(s[0:3:1]))
print(s[:3:1])
print(s[:3:])
print(s[0:5:2])


###列表方法
# append() 在列表尾部追加元素
s = ["w", "e", "r", "d", "l", "p"]
s.append(0)
print(s)

# insert（）在指定索引之前，插入元素
s = ["w", "e", "r", "d", "l", "p"]
s.insert(1, 999)
print(s)

# remove（元素）移除列表中第一个匹配到的元素
s = ["w", "e", "r", "d", "l", "p"]
s.remove("p")
print(s)

# pop() 删除列表中指定索引位置的元素并返回（如果未指定，默认删除最后一个）
s = ["w", "e", "r", "d", "l", "p"]
s.pop(2)
print(s)

# sort() 对列表进行排序，列表中的数据类型必须一致，才可以进行排序
s = ["w", "e", "r", "d", "l", "p"]
s.sort()
print(s)

# reverse() 反转列表元素
s = ["w", "e", "r", "d", "l", "p"]
s.reverse()
print(s)


###案例1:将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值，最大值和平均值。
# 定义列表(空列表)
num_list = []
# 将用户输入的10个数字存入列表
for i in range(10):
    num = int(input("请输入一个有效数字："))
    num_list.append(num)
print("数字列表：", num_list)
# 排序
num_list.sort()
print("排序后的列表:", num_list)
# 输出其中的最小值，最大值，平均值
min_num = num_list[0]
max_num = num_list[9]
aver = sum(num_list) / len(num_list)  # sum()求和  len(获取元素的个数/列表的长度)

print("最大值为：", max_num)
print("最小值为：", min_num)
print("平均值为：", aver)


###案例2: 合并两个列表中的元素，并对合并的结果进行处理（去除列表中的重复元素）
num_list1 = [3, 9, 5, 7, 4, 8, 3]
num_list2 = [1, 5, 7, 8]
# 合并列表
for num in num_list2:
    num_list1.append(num)
print("合并后的原始列表：", num_list1)

# 去除重复后的列表
new_list = []
for num in num_list1:
    # 判断new_list中是否存在
    if num not in new_list:
        new_list.append(num)
print("去除重复后的列表：", new_list)


###案例2 解包法
num_list = [*num_list1, *num_list2]
print("合并后的原始列表：", num_list)

# 去除重复后的列表
new_list = []
for num in num_list:
    # 判断new_list中是否存在
    if num not in new_list:
        new_list.append(num)
print("去除重复后的列表：", new_list)


###案例2:组包法
num_list = num_list1 + num_list2
print("合并后的原始列表：", num_list)

# 去除重复后的列表
new_list = []
for num in new_list:
    # 判断new_list中是否存在
    if num not in new_list:
        new_list.append(num)
print("去除重复后的列表：", new_list)


##案例3:生成1-20的平方列表
num_list = []
for i in range(1, 21):
    num_list.append(i**2)
print(num_list)

##案例3----列表推导式:按照一个规则快速生成一个列表的方法---语法格式：【要插入的值 for i in 序列/列表 if 条件】
num_list = [i**2 for i in range(1, 21)]
print(num_list)


##案例4: 从一个数字列表中提取所有偶数，并计算其平方，组成一个新的列表。
num_list = [2, 3, 5, 8, 9, 4, 1]
new_list = [i**2 for i in num_list if i % 2 == 0]
print(new_list)


###案例5. 将如下多个列表合并为一个列表，并去重重复元素，排好序（升序）后输出到控制台。
list1 = ["M", "A", "C", "E", "F", "G", "H", "L", "N", "I", "J", "K", "O"]
list2 = ["X", "Z", "T", "Y", "D", "E", "F", "G"]
list3 = ["W", "A", "S", "D"]

# 合并新列表
new_list1 = list1 + list2 + list3
# 去除重复元素
new_list2 = []
for i in new_list1:
    if i not in new_list2:
        new_list2.append(i)
# 排序
new_list2.sort()
print(new_list2)


###案例6: 将如下列表中的正数提取出来，封装为一个新的列表。
list5 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]

new_list = [i for i in list5 if i > 0]
print("正数列表：", new_list)


###案例7. 将如下列表中能被3 或 5整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表。
list4 = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
]

new_list = [i**2 for i in list4 if i % 3 == 0 or i % 5 == 0]
print(new_list)
