# """
# 1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。
# 5. 退出购物车
# """


# 定义商品类
class Good:
    def __init__(self, name, price, num):
        self.name = name
        self.price = price
        self.num = num

    def __str__(self):
        return f"商品名称: {self.name}, 商品价格: {self.price}, 商品数量: {self.num}"


# 定义购物车类
class Shopping:
    def __init__(self):
        self.goods = [Good("鼠标", 90, 1)]  # 购物车商品列表

    # 购物车方法1:添加
    def add(self):
        good_name = input("请输入商品的名字：")
        for g in self.goods:
            if good_name == g.name:
                print("该商品已经存在，无法添加")
                return
        good_price = input("请输入商品的价格：")
        good_num = input("请输入商品的数量：")

        g = Good(good_name, good_price, good_num)  # 创建商品实例
        self.goods.append(g)  # 将商品实例添加到商品列表中
        print("商品添加成功！")
        print(f"添加的商品信息为{g}")

    # 购物车方法2:修改
    def update(self):
        good_name = input("请输入要修改的商品名字:")
        for g in self.goods:
            if g.name == good_name:
                good_price = input("请输入修改的商品的价格：")
                good_num = input("请输入修改的商品的数量：")
                g.price = good_price
                g.num = good_num
                print("修改成功！")
                print(f"修改后的商品信息为：{g}")
                return
        print("该商品不存在，无法修改")

    # 购物车方法3:删除
    def delete(self):
        good_name = input("请输入要删除的商品名字:")
        for g in self.goods:
            if g.name == good_name:
                self.goods.remove(g)
                print("删除成功！")
                return
        print("该商品不存在，无法删除")

    # 购物车方法4:查询
    def search(self):
        good_name = input("请输入要查询的商品名字：")
        for g in self.goods:
            if g.name == good_name:
                print(f"商品信息：{g}")
                return
        print("该商品不存在，无法查询")

    # 运行购物车
    def running(self):
        while True:
            action = input("请输入您要进行的操作")
            match action:
                case "1":
                    self.add()
                case "2":
                    self.update()
                case "3":
                    self.delete()
                case "4":
                    self.search()
                case "5":
                    print("退出系统")
                case _:
                    print("操作错误")


# 调用购物车运行
s = Shopping()
s.running()
