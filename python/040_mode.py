"""
mode 模块
"""

###倒入模块---调用方式：模块名.功能名/别名.功能名
import random
import random as rd

for i in range(100):

    random.randint(1, 100)
    print(random.randint(1, 100))


###导入模块中的功能 ----调用方式：功能名/别名
from random import randint
from random import randint as rint
from random import *


for i in range(100):
    print(randint(1, 100))
