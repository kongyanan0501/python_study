"""
实例属性/类属性
"""


class Car:
    # 类属性
    wheel = 4
    tax_rate = 0.1

    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = float(c_price)
        self.wheel = 2  # 实例属性

    def running(self):
        print(f"{self.name}正在高速行驶中")

    def total_cost(self, discount, rate):
        total_cost = self.price * discount + self.price * rate
        return total_cost


c1 = Car("红色", "X7", "宝马", "800000")
# 通过实例对象查找属性时，会先查找实例属性，实例属性不存在时，再查找类属性。
print(c1.wheel)

# 通过类名访问类属性
print(Car.wheel)
