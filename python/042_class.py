"""
面向对象 class
"""


### 定义类--------------不推荐
class Car:
    pass


# 创建对象
c1 = Car()
pass

# 动态的为对象添加属性
c1.color = "red"
c1.brand = "BWM"
c1.name = "x5"
c1.price = "500000"

print(c1)
print(c1.brand)
print(c1.__dict__)  # 会将对象中的所有属性以字典的形式输出出来


###定义类----------------推荐
class Car:
    # __init__方法是初始化的方法，会在对象创建时自动调用，可以在该方法中为对象设置对应的属性
    # self：是第一个参数，表示当前所创建出来的实例对象
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price


# 创建对象
c1 = Car("蓝色", "BMW", "X7", "800000")
print(c1.__dict__)

c2 = Car("红色", "BKQ", "X9", "700000")
print(c2.__dict__)
