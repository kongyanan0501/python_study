"""
元组
"""

# 定义元祖
t1 = (5, 6, 2, 8, 9)
print(t1)
print(type(t1))


# 索引访问
print(t1[0])
print(t1[-1])


# 切片
print(t1[0:4:1])


# count()   统计元素的个数
print(t1.count(8))


# index()   获取元素的索引（第一个元素的位置）
print(t1.index(8))


###注意点
# 空元组
t2 = ()
print(t2)
print(type(t2))


# 单元素的元组必须加逗号
t3 = (300,)
print(t3)
print(type(t3))


# 元组组包
t1 = (5, 6, 2, 8, 0, 5, 1)
t2 = 5, 6, 2, 8, 9, 0, 5, 1


# 元素解包
# 基础解包（变量数量与容器数量的元素一致
a, b, c, d, e, f, g = t1
print(a, b, c, d, e, f, g)

# *扩展解包（*收集剩余的所有元素，封装到list中）
first, second, *other, last = t1
print(first)
print(second)
print(*other)
print(last)


###案例1: 交换两个变量。a = 10,b =20
a = 10
b = 20
a, b = b, a
print(a)
print(b)


###案例2  现有三个变量，分别为：a = 100, b=200,c=300, 现需将这三个变量值进行交换，将a,b,c的值分别复之给c,a,b,并将其输出到控制台
a = 100
b = 200
c = 300
c, a, b = a, b, c
print(a)
print(b)
print(c)



##案例3  根据以下成绩单
# 计算每个学生的总分，各科平均分，然后一并输出出来
# 统计各科成绩的最低分。最高分，平均分
# 查找成绩优秀（平均分大于90）的学生，并输出

# 计算每个学生的总分，各科平均分，然后一并输出出来
students = (
  ("s001", "王林", 85, 92, 78),
  ("s002", "李幕", 92, 88, 85),
  ("s003", "十三", 78, 85, 82),
  ("s004", "曾牛", 88, 78, 91),
  ("s005", "周铁", 95, 96, 89)
)
# 计算每个学生的总分，各科平均分，然后一并输出出来
print("学号 \t 姓名 \t 语文 \t 数学 \t 英语 \t 总分 \t 平均分")
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t{avg:.1f}")
# 统计各科成绩的最低分。最高分，平均分
chinese_scores = [s[2]for s in students]
math_scores = [s[3]for s in students]
english_scores = [s[4]for s in students]

print(f"语文最低分{min(chinese_scores)},最高分{max(chinese_scores)}, 平均分{sum(chinese_scores)/len(chinese_scores)}")
print(f"数学最低分{min(math_scores )},最高分{max(math_scores)}, 平均分{sum(math_scores)/len(math_scores)}")
print(f"语文最低分{min(english_scores)},最高分{max(english_scores)}, 平均分{sum(english_scores)/len(english_scores)}")

# 查找成绩优秀（平均分大于90）的学生，并输出
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    if avg >90:
      print(f"{s[1]}成绩优秀，平均分为{avg:.1f}")




##案例3  解包法
# 计算每个学生的总分，各科平均分，然后一并输出出来
# 统计各科成绩的最低分。最高分，平均分
# 查找成绩优秀（平均分大于90）的学生，并输出

# 计算每个学生的总分，各科平均分，然后一并输出出来
students = (
  ("s001", "王林", 85, 92, 78),
  ("s002", "李幕", 92, 88, 85),
  ("s003", "十三", 78, 85, 82),
  ("s004", "曾牛", 88, 78, 91),
  ("s005", "周铁", 95, 96, 89)
)
# 计算每个学生的总分，各科平均分，然后一并输出出来
print("学号 \t 姓名 \t 语文 \t 数学 \t 英语 \t 总分 \t 平均分")

for s in students:
    id,name,chinese,math,english = s
    total = chinese + math + english 
    avg = total / 3
    print(f"{id} \t {name} \t {chinese} \t {math} \t {english} \t {total} \t {avg:.1f}")
# 统计各科成绩的最低分。最高分，平均分
chinese_scores = [s[2]for s in students]
math_scores = [s[3]for s in students]
english_scores = [s[4]for s in students]

print(f"语文最低分{min(chinese_scores)},最高分{max(chinese_scores)}, 平均分{sum(chinese_scores)/len(chinese_scores)}")
print(f"数学最低分{min(math_scores )},最高分{max(math_scores)}, 平均分{sum(math_scores)/len(math_scores)}")
print(f"语文最低分{min(english_scores)},最高分{max(english_scores)}, 平均分{sum(english_scores)/len(english_scores)}")

# 查找成绩优秀（平均分大于90）的学生，并输出
for id,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    if avg >90:
      print(f"{name}成绩优秀，平均分为{avg:.1f}")