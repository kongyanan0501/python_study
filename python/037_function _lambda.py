"""
匿名函数
"""

###输出一行-------
# # def outline():
#     print("---------")

outline = lambda: print("----------")
outline()

###计算两个数之和
# def add(x, y):
#     return x + y
# add(10, 20)
# print(add(10, 20))

add = lambda x, y: x + y
print(add(10, 20))


###完成如下列表的排序顺序，按照每一个元素的字符个数，从小到大排序
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
print(data_list)

data_list.sort()
data_list.sort(key=lambda item: len(item))
print(data_list)
