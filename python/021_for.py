"""
for循环
"""

###遍历输入的字符串
msg = input("请输入您要遍历的字符串：")
for i in msg:  # i表示遍历出来的元素，msg表示需要遍历的数据
    print(f"元素：{i}")
else:
    print("遍历结束！")

###案例1:计算1-100之间所有奇数之和
total = 0

for i in range(1, 101):
    if i % 1 == 0:
        total += i
        i += 1
else:
    print(f"1-100之间的所有奇数之和为:{total}")


###案例1:计算1-100之间所有奇数之和
total = 0

for i in range(1, 101, 2):
    total += i
    i += 1
else:
    print(f"1-100之间的所有奇数之和为:{total}")


###案例2:计算100-500之间所有3的倍数的数字之和
total = 0

for i in range(100, 501):
    if i % 3 == 0:
        total += i
        i += 1
else:
    print(f"100-500之间所有3的倍数的数字之和为：{total}")
