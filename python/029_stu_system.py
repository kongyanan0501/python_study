# """
# 案例2:
# # 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
# # 1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# # 2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# # 3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
# # 4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# # 5. 列出所有学生：展示出所有学生信息并输出。
# # 6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
# # 7. 退出系统。
# """

# 定义空字典：
sys = {
    "南瓜": {"语文": 90, "数学": 80, "英语": 70},
    "西瓜": {"语文": 80, "数学": 90, "英语": 78},
    "东瓜": {"语文": 66, "数学": 79, "英语": 65},
    "北瓜": {"语文": 55, "数学": 89, "英语": 96},
}
# sys = {"name"： {"chinese":chinese_point，"math":math_point，"english":english_point}，"西瓜"： {"语文":90，"数学":80，"英语":70}，... , ...}

# 打印教务系统
print("欢迎使用教务管理系统～～～")
menu = """
########### 教务管理系统 ##########

#         1.添加学生信息         #
#         2.修改学生信息        #
#         3.删除学生信息         #
#         4.查询学生信息         #
#         5.列出所有学生       #
#         6.统计班级成绩       #
#         7.退出教务系统         #

          ###########
"""
print(menu)

while True:
    # 提示操作
    action = input("请输入您要进行的操作：")
    match action:
        # 1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
        case "1":
            student_name = input("请输入学生姓名：")
            if student_name in sys:
                print("该学生已经存在，请勿重复添加！")
                continue
            else:
                student_chinese = input("请输入语文成绩：")
                student_math = input("请输入数学成绩：")
                student_english = input("请输入英语成绩：")

                sys[student_name] = {
                    "语文": student_chinese,
                    "数学": student_math,
                    "英语": student_english,
                }
                print("添加成功！")
                print(
                    f"学生姓名：{student_name}, 语文成绩：{student_chinese}, 数学成绩: {student_math}, 英语成绩:{student_english}"
                )
                continue

        # 2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
        case "2":
            student_name = input("请输入要修改的学生姓名：")
            if student_name not in sys:
                print("该学生不存在,无法修改！")
                continue
            else:
                student_chinese = input("请输入修改后的语文成绩：")
                student_math = input("请输入修改后的数学成绩：")
                student_english = input("请输入修改后的英语成绩：")

                sys[student_name] = {
                    "语文": student_chinese,
                    "数学": student_math,
                    "英语": student_english,
                }
                print("修改成功！")
                print(
                    f"学生姓名：{student_name}, 语文成绩：{student_chinese}, 数学成绩: {student_math}, 英语成绩:{student_english}"
                )
                continue

        # 3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
        case "3":
            student_name = input("请输入要删除的学生姓名：")
            if student_name not in sys:
                print("该学生不存在,无法删除！")
                continue
            else:
                del sys[student_name]
                print("删除成功！")
                print(sys)
                continue

        # 4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
        case "4":
            student_name = input("请输入要查询的学生姓名：")
            if student_name not in sys:
                print("该学生不存在,无法查询！")
                continue
            else:
                # "南瓜": {"语文": 90, "数学": 80, "英语": 70}
                student_info = sys[student_name]  # {"语文": 90, "数学": 80, "英语": 70}
                student_chinese_point = student_info["语文"]
                student_math_point = student_info["数学"]
                student_english_point = student_info["英语"]
                print(
                    f"{student_name}的成绩信息为: 语文：{student_chinese_point}, 数学：{student_math_point}, 英语：{student_english_point}"
                )
                continue

        # 5. 列出所有学生：遍历所有学生信息并输出。
        case "5":
            for student, student_info in sys.items():  # for k, v in d.items():
                print(f"{student}:{student_info}")
                continue

        # 6. 统计班级成绩
        case "6":
            # chinese_list = []
            # math_list = []
            # english_list = []
            # for name, info in sys.items():
            #     chinese_list.append(info["语文"])
            #     math_list.append(info["数学"])
            #     english_list.append(info["英语"])
            chinese_list = [info["语文"] for name, info in sys.items()]
            math_list = [info["数学"] for name, info in sys.items()]
            english_list = [info["英语"] for name, info in sys.items()]

            # 最高分、最低分、平均分
            print(
                "语文 - 最高分:",
                max(chinese_list),
                "最低分:",
                min(chinese_list),
                "平均分:",
                sum(chinese_list) / len(chinese_list),
            )
            print(
                "数学 - 最高分:",
                max(math_list),
                "最低分:",
                min(math_list),
                "平均分:",
                sum(math_list) / len(math_list),
            )
            print(
                "英语 - 最高分:",
                max(english_list),
                "最低分:",
                min(english_list),
                "平均分:",
                sum(english_list) / len(english_list),
            )
            # 最高分学员
            for name, info in sys.items():
                if info["语文"] == max(chinese_list):
                    print("语文最高分学员:", name)
                    break
            for name, info in sys.items():
                if int(info["数学"]) == max(math_list):
                    print("数学最高分学员:", name)
                    break
            for name, info in sys.items():
                if int(info["英语"]) == max(english_list):
                    print("英语最高分学员:", name)
                    break
            continue

        case "7":
            print("退出教务系统～")
            break

        case _:
            print("操作错误！请重新选择～")
