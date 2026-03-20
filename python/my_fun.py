# __all__指定from...import*导入的是哪些功能
__all__ = ["log_separator01", "log_separator02", "PI"]


# 常量（不会发生变化的数据，常量的名称为全部大写）
PI = 3.1415926
NAME = "黑马"


# 函数
def log_separator01():
    print("-" * 30)


def log_separator02():
    print("+" * 30)


def log_separator03():
    print("#" * 30)


def log_separator04():
    print("*" * 30)


# 测试函数
# __name__:python中的内置变量，表示当前模块的名字（直接运行当前模块，__name__的值为“__main__”）,当该模块被导入时，__name__的值就是模块名
# 执行当前文件，则会执行如下代码。如果被当作模块导入，不会执行
if __name__ == "__main__":
    log_separator01()
