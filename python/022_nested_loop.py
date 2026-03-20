"""
嵌套循环
"""

###打印一个长度为10，宽度为5的长方形
m = int(input("请输入长方形的长度："))
n = int(input("请输入长方形的宽度: "))

for i in range(n):  # 控制行
    for i in range(m):  # 控制列
        print("*", end="  ")
    print()


###打印九九乘法表
for i in range(1, 10):  # 控制行
    for j in range(1, i + 1):  # 控制列
        print(f"{j} x {i} = {j * i}", end="\t")
    print()


###案例1:根据输入的直角边的边长，打印等腰直接三角形
# 行
for i in range(1, 6):
    # 列
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


###案例2:根据输入的数字，打印对应的数字金字塔
# 行
num = int(input("请输出一个数字："))
# 行
for i in range(1, num + 1):
    # 列
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


##案例3:打印国际象棋棋盘
# 行
for i in range(1, 9):
    # 列
    for j in range(1, 9):
        odd_row = j % 2 == 1  # 奇数行
        odd_col = i % 2 == 1  # 奇数列

        # 奇数行内
        if odd_row:
            if odd_col:
                print("黑", end=" ")
            else:
                print("白", end=" ")
        else:
            # 偶数行内
            if odd_col:
                print("白", end=" ")
            else:
                print("黑", end=" ")
    # 换行
    print()


###案例3:打印国际象棋棋盘
for i in range(1, 9):
    for j in range(1, 9):
        row_add_col_equal_even = (i + j) % 2 == 0
        if row_add_col_equal_even:
            print("黑", end=" ")
        else:
            print("白", end=" ")
    print()
