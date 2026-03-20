"""
if条件判断
"""

# 案例1 完成登录功能的实现（正确的正好和密码是18888888/666888）
username = input("请输入用户名：")
password = input("请输入密码：")

if username == "18888888" and password == "666888":
    print("登陆成功")
else:
    print("登陆失败")

# 案例2:判断是闰年还是平年。非整百年，且能被4整除的是闰年。整百年必须被400整除才是闰年。
year = int(input("请输入年份："))
if year % 100 != 0 and year % 4 == 0 or year % 100 == 0 and year % 400 == 0:
    print(f"{year} 是闰年")
else:
    print(f"{year} 是平年")

# 案例3:判断输入的数字是奇数还是偶数
num = int(input("请输入数字："))
if num % 2 == 0:
    print(f"{num} 是偶数")
else:
    print(f"{num} 是奇数")

# 案例4:判断是否成年
age = int(input("请输入年龄："))
if age >= 18:
    print("您已经成年")
else:
    print("您未成年")
