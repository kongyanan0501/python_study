"""
match
"""

###案例1
day = input("请输入星期几（1-7）：")
match day:
    case "1":
        print("周一：工作会议日")
    case "2":
        print("周二：学习培训日")
    case "3":
        print("周三：项目开发日")
    case "4":
        print("周四：代码审查日")
    case "5":
        print("周五：马上周末日")
    case "6" | "7":
        print("周末放松日")
    case _:
        print("输入有错误")


###案例2: 实现一个计算器，可以实现 + - * /运算，用户需要运算的两个数以及运算符后，就可以进行运算。
num1 = float(input("请输入第一个数："))
num2 = float(input("请输入第一个数："))
opera = input("请输入运算符号：")

match opera:
    case "+":
        print(f"{num1} + {num2} 的值为：", num1 + num2)
    case "-":
        print(f"{num1} - {num2} 的值为：", num1 - num2)
    case "*":
        print(f"{num1} * {num2} 的值为：", num1 * num2)
    case "/" if num2 != 0:
        print(f"{num1} / {num2} 的值为：", num1 / num2)
    case _:
        print("输入错误！")


###案例3:简单游戏
# - 上 / w /W             角色向上移动
# - 下 / s / S              角色向下移动
# - 左 / a / A             角色向左移动
# - 右 / d / D             角色向右移动
# - 跳 / " "(空格)        角色跳跃
# - 攻击 / j / J            角色发动攻击
# - 退出 / esc / ESC    角色退出游戏

opera = input("请输入操作: ")

match opera:
    case "w" | "W" | "上":
        print("角色向上移动")
    case "s" | "S" | "下":
        print("角色向下移动")
    case "a" | "A" | "左":
        print("角色向左移动")
    case "d" | "D" | "右":
        print("角色向右移动")
    case " " | "跳":
        print("角色跳跃")
    case "j" | "J" | "攻击":
        print("角色攻击")
    case "esc" | "ESC" | "退出":
        print("角色退出游戏")
    case _:
        print("非法操作, 不支持!!!")
