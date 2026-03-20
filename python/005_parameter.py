"""
变量：程序中用来存储单个数据的容器，通常会把经常发生变化的数据存储在变量中。
"""

# 定义格式：变量名 = 数据
# python是动态类型语言，一个变量是可以存储不同类型的数据的

num = 11
print(num)

num = num + 1
print(num)

num = "ok"
print(num)

num = True
print(num)


# 案例1:
# 课程基础播放量为 20.7万,每月新增播放量为50万,请输出未来两个月每个月的播放量

base = 20.7
incr = 50
print("未来第一个月的播放总量：", base + incr)
print("未来第二个月的播放总量：", base + incr + incr)


base, incr = 20.7, 50
print("未来第一个月的播放总量：", base + incr)
print("未来第二个月的播放总量：", base + incr + incr)


# """
# 案例2:
# 现有两个变量a和b,a=10,b=20,请交换两个变量的值
# """

a = 10
b = 20

c = a
a = b
b = c
print(a, b)


# """
# 案例3:
# 现有三个变量，分别为a=100,b=200,c=300,现在需要将这三个变量值进行交换，将a b c 的值分别赋值给b c a
# """

a = 100
b = 200
c = 300

e = b
f = c

b = a
c = e
a = f

print(a, b, c)
