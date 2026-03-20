"""
循环综合案例1
1.正确的用户名和密码为admin/666
2.输入用户名密码进行登录，直到登录成功，程序结束运行，如果登录失败，则继续输入用户名和密码进行登录。
3.输入的用户名和密码不能为空
"""

# break：只能够出现在循环中，表示接受跳出循环的含义
# continue：只能出现在循环中，表示中断本次循环，直接进入下一次循环

###案例1:
# while循环
while True:
    # 输入用户和密码
    username = input("请输入用户名：")
    password = input("请输入密码：")
    # 校验用户名和密码
    if username == "admin" and password == "666":
        print("登陆成功！")
        break
    elif username == "" or password == "":
        print("输入的用户名或密码不能为空！")
    else:
        print("登陆失败，请重新输入！")


# while循环
while True:
    # 输入用户和密码
    username = input("请输入用户名：")
    password = input("请输入密码：")
    # 校验用户名和密码
    if username == "" or password == "":
        print("输入的用户名或密码不能为空！")
        continue
    if username == "admin" and password == "666":
        print("登陆成功！")
        break  #
    else:
        print("登陆失败，请重新输入！")


"""
循环综合案例2:
正确的用户名和密码为admin/888，root/999，5次登录机会,输入错误五次，不允许再操作了。
"""

count = 0
while count < 5:
    username = input("请输入用户名：")
    password = input("请输入密码：")

    if username == "admin" and password == "888":
        print("登陆成功")
        break
    elif username == "root" and password == "999":
        print("登陆成功")
        break
    else:
        print("登陆失败")
    count += 1

    if count == 5:
        print("输出五次，不能操作了")


"""
猜数字游戏
"""

import random

random_num = random.randint(1, 100)

while True:
    num = int(input("请输入一个数字："))
    if num > random_num:
        print("猜大了")
    elif num < random_num:
        print("猜小了")
    else:
        print("猜对了")
        break
print("随机数字是：", random_num)


"""
将1-1000之间（含1000）所有的5的倍数的数字累加起来
"""
total = 0
for i in range(1, 1001):
    if i % 5 == 0:
        total += i
print("1-1000之间所有5的倍数累加为:", total)


"""
统计字符串 "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd" 字符串中有多少个a和k。
"""
total = 0
for i in "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd":
    if i == "a" or i == "k":
        total += 1
print(f"a和k出现的次数: {total}")
