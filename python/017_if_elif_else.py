"""
if elif else 多条件判断
"""

### 案例1:判断输入的数字是正数，负数，还是0
num = int(input("请输入数字："))

if num > 0:
    print(f"{num} 是正数 ")
elif num < 0:
    print(f"{num} 是负数 ")
else:
    print(f"{num} 是0 ")


### 案例2:用户名：admin，密码123.用户名密码正确输入登录成功，否则提示用户名或者密码错误。
username = input("请输入用户名：")
password = input("请输入密码：")

if username == "admin" and password == "123":
    print("登陆成功！")
elif username == "root" and password == "456":
    print("登陆成功！")
else:
    print("用户名或密码错误！")


###案例3:根据输入的成绩判断成绩等级
point = int(input("请输入您的成绩："))
# 大于等于85分为优秀
if point > 85:
    print("您的成绩为优秀")
# 60-85分为及格
elif 60 <= point <= 85:
    print("您的成绩为及格")
# 否则就是不及格
else:
    print("您的成绩为不及格")


# 案例4:根据输入的商品总额和如下折扣规则，计算实际应付的金额。
total = int(input("请输入商品总额："))
# 金额 >= 500: 8折
if total >= 500:
    actual = total * 0.8
    print(f"实际应付 : {actual}")
# 300 <= 金额 < 500 : 9折
elif 300 <= total < 500:
    actual = total * 0.9
    print(f"实际应付 : {actual}")
# 100 <= 金额 < 300 : 95折
elif 100 <= total < 300:
    actual = total * 0.95
    print(f"实际应付 : {actual}")
# 金额 < 100:无折扣
else:
    print(f"实际应付：{total}")
