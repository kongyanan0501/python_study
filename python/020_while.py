"""
while
"""

###打印十遍“人生苦短，我用python”
i = 0
while i < 10:
    print("人生苦短，我用python")
    i += 1
else:
    print("循环结束")


# 案例1:计算1-100之间所有偶数的累加之和
total = 0  # 记录累加之和
i = 1  # 循环开始数字
while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1
else:
    print(f"1-100之间的偶数之和：{total}")
