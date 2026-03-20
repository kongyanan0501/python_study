"""
函数参数类型
"""


# 加
def add(x, y):
    return x + y


# 减
def subtract(x, y):
    return x - y


# 乘
def multiply(x, y):
    return x * y


# 除
def divide(x, y):
    return x / y


def calc(x, y, oper):
    return oper(x, y)


print(calc(10, 20, add))
