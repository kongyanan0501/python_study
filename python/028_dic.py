"""
dic 字典
key不能重复,(如果重复,后面的值会覆盖前面的值),key必须是不可变类型.(str,int,float,tuple)
"""

# 空字典
d1 = {}
d2 = dict()

# 直接定义
d3 = {"name": "张三", "age": 18, "city": "北京"}
print(d3)
print(type(d3))

# key必须是不可变类型，不能是list,set
# d4 = {[1,2],(3,6)}   #不可以会报错

# 访问
print(d3["age"])  # 获取
d3["age"] = 20  # 修改
print(d3)


# 字典的常用操作
# 1. 增 / 改
d = {"name": "王五", "age": 18, "city": "北京"}
d["high"] = "180"  # 添加
d["name"] = "张三"  # 修改
print(d)

# 2. 查
d = {"name": "王五", "age": 20}
print(d["name"])  # 根据key直接访问，键不存在会报错
print(d.get("age"))  # 根据key直接访问，键不存在会报错
print(d.keys())  # 获取所有的key
print(d.values())  # 获取所有的value
print(d.items())  # 获取所有的键值对   key:value


# 3. 删
d = {"name": "王五", "age": 18, "city": "北京"}
del d["key"]  # 删除指定键
del d["name"]
print(d)

d.pop("key")  # 删除并返回值
del_age = d.pop("age")
print(del_age)
print(d)


# 遍历
d = {"name": "王五", "age": 18, "city": "北京"}
for k in d.keys():
    print(f"{k}:{d[k]}")

for item in d.items():
    print(item)

for k, v in d.items():
    print(f"{k}:{v}")


#### 案例1：购物车管理系统

# 开发一个购物车管理系统，实现商品信息的**添加、修改、删除、查询**功能。系统使用**字典结构**存储商品数据，通过**控制台菜单**与用户交互。

## 功能需求

### 1. 添加购物车

# - 提示用户输入：**商品名称**、**价格**、**数量**
# - 将输入信息保存到购物车

### 2. 修改购物车

# - 用户输入要修改的**商品名称**
# - 再输入该商品的**新价格**、**新数量**
# - 更新购物车中对应商品的信息

### 3. 删除购物车

# - 用户输入要删除的**商品名称**
# - 根据名称从购物车中移除该商品

# ### 4. 查询购物车

# - 展示购物车中所有商品信息
# - 显示格式：`商品名称: xxx, 商品价格: xxx, 商品数量: xxx`

### 5. 退出购物车

###方式1:
# 制作menu
print("欢迎使用购物车管理系统～～～")
menu = """
########### 购物车系统 ##########

#         1.添加购物车          #
#         2.修改购物车          #
#         3.删除购物车          #
#         4.查询购物车          #
#         5.退出购物车          #

          ###########
"""
print(menu)
# 定义字典
shopping_cart = {
    "鸡蛋": {"price": 2.0, "num": 3},
    "牛奶": {"price": 5.5, "num": 2},
    "苹果": {"price": 6.0, "num": 5},
    "大米": {"price": 3.5, "num": 2},
    "食用油": {"price": 45.0, "num": 1},
    "酱油": {"price": 12.0, "num": 1},
    "面包": {"price": 8.0, "num": 3},
    "香蕉": {"price": 4.5, "num": 4},
    "酸奶": {"price": 3.0, "num": 6},
    "方便面": {"price": 5.0, "num": 5},
    "矿泉水": {"price": 2.0, "num": 12},
}
# shopping_cart = {"good":{"price":200,"num":1}...}

# 确认用户操作
while True:
    choice = input("请输入您要进行的操作：")

    match choice:
        case "1":  # 添加购物车
            good_name = input("请输入商品的名称：")
            good_price = float(input("请输入商品的价格："))
            good_num = int(input("请输入商品的数量："))
            if good_name in shopping_cart:
                print("该商品已存在，重新选择～")
            else:
                shopping_cart[good_name] = {"price": good_price, "num": good_num}
                print("商品添加完毕～")

        case "2":  # 修改购物车
            good_name = input("请输入要修改的商品的名称：")
            if good_name not in shopping_cart:
                print("该商品不存在，无法修改，重新选择～")
            else:
                good_price = float(input("请输入最新商品的价格："))
                good_num = int(input("请输入最新商品的数量："))
                shopping_cart[good_name] = {"price": good_price, "num": good_num}
                print("商品修改完毕～")

        case "3":  # 删除购物车
            good_name = input("请输入要删除的商品的名称：")
            if good_name not in shopping_cart:
                print("该商品不存在，无法删除，重新选择～")
            else:
                del shopping_cart[good_name]
                print("商品删除完毕～")

        case "4":  # 查询购物车
            for good_name, good_info in shopping_cart.items():
                print(
                    f"商品名称：{good_name}, 商品价格：{good_info['price']}, 商品数量: {good_info['num']}"
                )
        case "5":
            print("退出购物车～")  # 退出购物车
            break

        case _:
            print("操作错误！请重新输入～")


###案例1-----方法2:
print("欢迎使用购物车管理系统～～～")
menu = """
########### 购物车系统 ##########

#         1.添加购物车          #
#         2.修改购物车          #
#         3.删除购物车          #
#         4.查询购物车          #
#         5.退出购物车          #

          ###########
"""
print(menu)

shopping_cart = {
    "鸡蛋": {"price": 2.0, "num": 3},
    "牛奶": {"price": 5.5, "num": 2},
    "苹果": {"price": 6.0, "num": 5},
    "大米": {"price": 3.5, "num": 2},
    "食用油": {"price": 45.0, "num": 1},
    "酱油": {"price": 12.0, "num": 1},
    "面包": {"price": 8.0, "num": 3},
    "香蕉": {"price": 4.5, "num": 4},
    "酸奶": {"price": 3.0, "num": 6},
    "方便面": {"price": 5.0, "num": 5},
    "矿泉水": {"price": 2.0, "num": 12},
}

while True:
    action = input("请输入您要进行的操作：")
    match action:
        case "1":
            good_name = input("请输入您要添加的商品名称：")
            if good_name in shopping_cart:
                print("该商品已存在")
                continue
            else:
                good_price = input("请输入您要添加的商品价格：")
                good_num = input("请输入您要添加的商品数量：")
                shopping_cart[good_name] = {"price": good_price, "num": good_num}
                print("添加成功")
                print(shopping_cart)

        case "2":
            good_name = input("请输入您要修改的商品名称：")
            if good_name not in shopping_cart:
                print("该商不存在，无法修改")
                continue
            else:
                good_price = input("请输入修改后的商品价格：")
                good_num = input("请输入修改后的商品数量：")
                shopping_cart[good_name] = {"price": good_price, "num": good_num}
                print("修改成功")
                print(shopping_cart)

        case "3":
            good_name = input("请输入您要删除的商品名称：")
            if good_name not in shopping_cart:
                print("该商不存在，无法删除")
                continue
            else:
                del shopping_cart[good_name]
                print("删除成功")
                print(shopping_cart)
        case "4":
            good_name = input("请输入您要查询的商品名称：")
            if good_name not in shopping_cart:
                print("该商不存在，无法查询")
                continue
            else:
                good_info = shopping_cart[good_name]
                good_price = good_info["price"]
                good_num = good_info["num"]
                print(f"{good_name},价格：{good_price},数量：{good_num}")
        case _:
            "操作错误！"
