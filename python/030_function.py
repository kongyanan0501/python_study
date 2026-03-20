"""
函数 function
"""


### 函数定义
def out_line():
    print("------------")
    print("------------")


# print(out_line)  # 函数定义时不会直接执行，必须先定义，后执行

### 函数调用
out_line()


### 函数的参数与返回值
# 函数1:计算圆的面积
def circle_area(r):
    area = 3.14 * r * r
    return area


area = circle_area(2)
print(area)


# 函数2:计算长方形的面积
def rectangle_area(l, w):
    area = l * w
    return area


area = rectangle_area(10, 20)
print(area)


# 函数3:计算圆的面积，周长-------如果返回值有多个，用逗号分隔-------多个返回值会对应封装到元组中
def circle_area_length(r):
    return 3.14 * r * r, round(2 * 3.14 * r, 1)


al = circle_area_length(10)
print(al)  # 输出的结果是一个元组

area, length = circle_area_length(10)  # 元组解包
print(area)
print(length)
