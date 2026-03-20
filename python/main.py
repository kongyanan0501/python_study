# ### 导入自定义模块
# import my_fun

# # 使用模块中的功能
# print(my_fun.PI)
# print(my_fun.NAME)

# my_fun.log_separator01()
# my_fun.log_separator02()


# ###导入自定义模块中的功能
# from my_fun import log_separator01, log_separator03, PI, NAME
from my_fun import *

# 使用模块中的功能
print(PI)
print(NAME)  # 因为在my_fun模块中定义的__all__中没有功能NAME

log_separator01()
log_separator03()  # 因为在my_fun模块中定义的__all__中没有功能log_separator03
