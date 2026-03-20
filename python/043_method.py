"""
实例方法
"""


class Car:
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = float(c_price)
        print("Car类型的对象初始化完毕, 对象属性已经添加完毕")

    def running(self):
        print(f"{self.brand}{self.name}正在高速行驶中")

    def total_cost(self, discount, rate):
        total_cost = self.price * discount + self.price * rate
        return total_cost


c1 = Car("红色", "BMW", "x7", "800000")
c1.running()
total = c1.total_cost(0.1, 0.9)
print(f"提车的总价为{total}")
