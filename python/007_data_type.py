"""
数据类型
"""

# type()函数可以用来获取变量中存储的数据的类型
print(type("hello"))  # str
print(type(10))  # int
print(type(3.4))  # float
print(type(True))  # bool
print(type(None))  # NoneType

num = 5.0
print(
    type(num)
)  # num变量本身是没有类型的，type（变量）输出的类型是变量中存储的数据的类型。


# isinstance()函数可以用来判断一个变量是否是某个类型
print(isinstance(num, int))
print(isinstance(num, float))
print(isinstance(num, bool))
