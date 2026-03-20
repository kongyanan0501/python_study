"""
魔法方法
"""


class Car:
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car类型的对象初始化完,对象属性已经添加完毕")

    def running(self):
        print(f"{self.name}正在高速行驶中")

    def total_cost(self, discount, rate):
        total_cost = self.price * discount + self.price * rate
        return total_cost

    def __str__(self):
        return f"{self.color} {self.brand} {self.name} {self.price}"

    def __eq__(self, other):
        return (
            self.color == other.color
            and self.brand == other.brand
            and self.name == other.name
            and self.price == other.price
        )

    def __lt__(self, other):
        return self.price < other.price


c1 = Car("红色", "X7", "宝马", "800000")
c2 = Car("红色", "X7", "宝马", "800000")

print(c1)
print(c1 == c2)
print(c1 < c2)
