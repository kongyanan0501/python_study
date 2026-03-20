"""
包

注意:需要和包在同一目录路径下, 否则需要在包前面指定path
"""

# 导入模块
import utils.my_fun

utils.my_fun.log_separator01()


from utils import my_fun

my_fun.log_separator02()


from utils import *  # 注意：如果要通过from utils import* 导入包下的所有模块，需要在__init__.py文件中添加__all__["", ""]

my_fun.log_separator03()


# 导入模块中的功能
from utils.my_fun import log_separator04

log_separator04()
