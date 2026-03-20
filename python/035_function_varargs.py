"""
函数 不定长参数
"""

"""
位置参数  *args ->元组
"""


###需求：根据输入的数据，计算数据中的最小值，最大值，平均值
def calc_data(*args):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    return min_data, max_data, avg_data


print(calc_data(1, 5, 8, 3, 9))


"""
关键字参数  **kwargs  ->字典
"""


###需求：根据输入的数据，计算数据中的最小值，最大值，平均值
def calc_data(*args, **kwargs):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    if kwargs.get("round") is not None:
        avg_data = round(avg_data, kwargs.get("round"))
    if kwargs.get("print"):
        print(f"计算出来的最小值：{min_data}, 最大值：{max_data}, 平均值：{avg_data}")
    return min_data, max_data, avg_data


print(calc_data(2, 5, 8, 3, 5, 6, round=1, print=True))
print(calc_data(111.1, 222, 8, 3, 9, round=2, print=True))
