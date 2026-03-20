"""
输入与输出
"""

# 获取键盘上的数据
name = input("请输入您的名字：")
age = input("请输入您的年龄：")

print(f"你的名字是 {name} , 你的年龄是 {age}")


# """
# 案例1:银行卡中有10000元，现在进行取款操作，取款完毕后，展示其银行卡余额。
# 步骤：
# 1.输入密码
# 2.输入取款金额
# 3.计算余额并输出
# """

total = 10000
password = input("请输入密码：")
cash = int(input("请输入取款金额："))
print("您的卡内余额为：", total - cash)
print(f"您的卡内余额为：{total - cash}")
