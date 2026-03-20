"""
函数-变量作用域
"""

# 全局变量：在函数外部或函数内部都是可以访问的
num = 100


# 定义函数
def circle_area(r):
    # 局部变量
    pi = 3.14
    area = pi * r * r

    # 局部变量
    num = 10000
    print("num = ", num)  # 10000
    return area


# 调用函数
c_area = circle_area(10)
print(c_area)

print("num = ", num)  # 100  因为num=10000是局部变量，所以不会被调用


"""
修改函数内部的局部变量为全局变量
"""
###全局变量：在函数外部或函数内部都是可以访问的
num = 100


# 定义函数
def circle_area(r):
    # 局部变量
    pi = 3.14
    area = pi * r * r

    # 修改为全局变量
    global num  # 修改num为全局变量
    num = 10000
    print("num = ", num)  # 10000
    return area


# 调用函数
c_area = circle_area(10)
print(c_area)

print("num = ", num)  # 10000   调用了函数内部修改后的值10000
