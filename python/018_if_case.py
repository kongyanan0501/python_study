"""
if循环的案例
"""

###案例1: 根据输入的三个边的边长（正整数），判定是等边三角形，等腰三角形，普通三角形，还是不能构成三角形。
a = int(input("请输出第一条边长："))
b = int(input("请输出第二条边长："))
c = int(input("请输出第三条边长："))
# 如果两边之和大于第三边，是三角形。
if a + b > c and a + c > b and b + c > a:
    # 如果三条边相等，则是等边三角形
    if a == b == c:
        print(f"{a} {b} {c} 可以构成等边三角形")
    # 如果两条边相等，则是等腰三角形
    elif a == b or a == c or a == c:
        print(f"{a} {b} {c} 可以构成等腰三角形")
    else:
        print(f"{a} {b} {c} 可以构成普通三角形")
# 否则不是三角形
else:
    print(f"{a} {b} {c} 不能构成三角形")


###案例2: 电费计算
charge = int(input("请输入您的用电度数："))
# 第一档：2880度以下，电费单价0.4883元/度
if charge <= 2880:
    bill = charge * 0.4883
    print(f"您的用电度数为：{charge} , 电费为 {bill}")
# 第二档：2880-4800度，电费单价0.5383元/度
if 2880 < charge < 4800:
    bill = charge * 0.5383
    print(f"您的用电度数为：{charge} , 电费为 {bill}")
# 第三档：4800度以上，电费单价0.7883元/度
if charge >= 4800:
    bill = charge * 0.7883
    print(f"您的用电度数为：{charge} , 电费为 {bill}")
