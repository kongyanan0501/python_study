"""
set 集合
"""

# 定义
s1 = {1, 4, 5, 2, 6, 7, 1}
print(s1)
print(type(s1))

# 定义空集合
s2 = set()
print(s2)


# 常用方法
# 1. add() —— 添加元素
s = {1, 2, 3}
s.add(4)
print(s)  # {1, 2, 3, 4}
s.add(2)  # 已存在，不重复添加
print(s)  # {1, 2, 3, 4}

# 2. remove() / discard() —— 删除元素
s = {1, 2, 3}
s.remove(2)  # 删除 2，不存在会报 KeyError
s.discard(99)  # 删除 99，不存在也不报错
print(s)  # {1, 3}

# 3. union() / | —— 并集
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}
print(a | b)  # 同上

# 4. intersection() / & —— 交集
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))  # {2, 3}
print(a & b)  # 同上

# 5. difference() / - —— 差集
a = {1, 2, 3}
b = {2, 3, 4}
print(a.difference(b))  # {1}，在 a 中但不在 b 中
print(a - b)  # 同上

# 6. pop() —— 随机删除并返回一个元素
# 集合无序，pop() 会删除并返回任意一个元素（不是“最后一个”）
s = {3, 1, 4, 1, 5}
x = s.pop()
print(x)  # 可能是 1, 3, 4, 5 中的任意一个
print(s)  # 剩余 4 个元素
# 空集合调用 pop() 会报错
s2 = set()
# s2.pop()  # KeyError: 'pop from an empty set'

# 7. clear() —— 清空集合
# 删除集合中所有元素，集合变为空集合。
s = {1, 2, 3, 4, 5}
print(s)  # {1, 2, 3, 4, 5}
s.clear()
print(s)  # set()
print(len(s))  # 0


###案例1
# 学生选课统计

# 根据提供的班级学生的选课情况，完成如下需求：

# 1. 找出同时选修了法语和艺术的学生
# 2. 找出同时选修了所有四门课程的学生
# 3. 找出选修了足球，但是没有选修篮球的学生
# 4. 统计每一个学生选修的课程数量

# ## 数据
# 选修足球学生名单
football_set = {
    "王林",
    "曾牛",
    "徐立国",
    "遁天",
    "天运子",
    "韩立",
    "厉飞雨",
    "乌丑",
    "紫灵",
}

# 选修篮球学生名单
basketball_set = {
    "张铁",
    "墨居仁",
    "王林",
    "姜老道",
    "曾牛",
    "王蝉",
    "韩立",
    "天运子",
    "李化元",
    "厉飞雨",
    "云露",
}

# 选修法语学生名单
french_set = {
    "许木",
    "王卓",
    "十三",
    "虎咆",
    "姜老道",
    "天运子",
    "红蝶",
    "厉飞雨",
    "韩立",
    "曾牛",
}

# 选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}


# 1. 找出同时选修了法语和艺术的学生
fa_set = football_set.intersection(french_set)
print(f"同时选秀足球和法语的学生：,{fa_set}")
# 方法2
fa_set = football_set & french_set
print(f"同时选秀足球和法语的学生：,{fa_set}")

# 2. 找出同时选修了所有四门课程的学生
all_set = football_set & basketball_set & french_set & art_set
print(f"同时选修四门课程的学生：,{all_set}")

# 3. 找出选修了足球，但是没有选修篮球的学生
f_not_bas = football_set.difference(basketball_set)
print(f"选择足球但是没有选择篮球的学生：,{f_not_bas}")
# 方式2
f_not_bas2 = football_set - basketball_set
print(f"选择足球但是没有选择篮球的学生：,{f_not_bas2}")
# 方式3  集合推导式
f_not_bas3 = {s for s in football_set if s not in basketball_set}
print(f"选择足球但是没有选择篮球的学生：,{f_not_bas3}")

# 4. 统计每一个学生选修的课程数量
# 获取学生名单
all_student_set = football_set | basketball_set | french_set | art_set
# 获取每一个学生选修的课程数量
all_student_list = [*football_set, *basketball_set, *french_set, *art_set]
for s in all_student_set:
    print(f"{s}选修了{all_student_list.count(s)}课程")
