# # 教务管理系统
# 采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互。

# ## 功能需求

# ### 1. 添加学生成绩
# 根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中。
# 1.1. 输入学生姓名、语文成绩、数学成绩、英语成绩
# 1.2. 检查学生姓名是否已存在，如果学生不存在，再添加（存在则不添加）
# 1.3. 验证成绩范围（0-100 分）
# 1.4. 创建学生对象并添加到系统

# ### 2. 修改学生成绩
# 根据输入的学生姓名，修改对应的学生成绩。
# 2.1. 输入要修改的学生姓名
# 2.2. 根据姓名查找该学生，显示该生当前成绩信息
# 2.3. 输入新的语文、数学、英语成绩
# 2.4. 更新学生成绩数据

# ### 3. 删除学生成绩
# 根据输入的学生姓名，删除对应的学生成绩。

# ### 4. 查询指定学生成绩
# 根据输入的学生姓名，查找对应的学生成绩，并输出。
# 4.1. 输出格式为：`姓名:张三 | 语文:85 | 数学:90 | 英语:88 | 总分:263`

# ### 5. 展示全部学生成绩
# 展示出系统中所有学生的成绩。


class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = int(chinese)
        self.math = int(math)
        self.english = int(english)

    def __str__(self):
        return f"姓名:{self.name} | 语文:{self.chinese} | 数学: {self.math}| 英语:{self.english} | 总分:{self.chinese + self.math + self.english}"

    # 修改学生成绩
    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english


class Edu:
    def __init__(self):
        init_s = Student("南瓜", 100, 100, 100)
        self.stu_list: list[Student] = [init_s]

    def add(self):
        stu_name = input("请输入学生姓名：")
        # 判断学生是否存在
        for s in self.stu_list:
            if s.name == stu_name:
                print("该学生已经存在，无法添加")
                return
        # 插入
        stu_chinese_score = int(input("请输入学生语文成绩："))
        stu_math_score = int(input("请输入数学成绩："))
        stu_english_score = int(input("请输入英语成绩："))

        # 判断分数是否在1-100之间
        if (
            0 <= stu_chinese_score <= 100
            and 0 <= stu_math_score <= 100
            and 0 <= stu_english_score <= 100
        ):
            s1 = Student(stu_name, stu_chinese_score, stu_math_score, stu_english_score)
            self.stu_list.append(s1)
            print("添加成功")
            print(s1)
        else:
            print("各科成绩必须在1-100之间")

    def update(self):
        stu_name = input("请输入要修改的学生姓名：")
        # 根据学生姓名找到该学生的信息
        for s in self.stu_list:
            if s.name == stu_name:
                print(f"该学生当前成绩为：{s}")
                # 修改成绩
                stu_chinese_score = int(input("请输入学生语文成绩："))
                stu_math_score = int(input("请输入数学成绩："))
                stu_english_score = int(input("请输入英语成绩："))
                # 判断分数是否在1-100之间
                if (
                    0 <= stu_chinese_score <= 100
                    and 0 <= stu_math_score <= 100
                    and 0 <= stu_english_score <= 100
                ):
                    s.update_score(stu_chinese_score, stu_math_score, stu_english_score)
                    print("修改成功")
                    print(s)
                    return
                else:
                    print("该成绩必须在1-100之间")
        print("该学生不存在，无法修改")

    def delete(self):
        stu_name = input("请输入要删除的学生姓名：")
        # 根据学生姓名找到该学生的信息
        for s in self.stu_list:
            if s.name == stu_name:
                self.stu_list.remove(s)
                print("删除成功")
                return

        print("未找到该学生，删除失败")

    def search(self):
        stu_name = input("请输入要查询的学生姓名：")
        for s in self.stu_list:
            if s.name == stu_name:
                print(s)
                return
        print("该学生不存在")

    def layout(self):
        for s in self.stu_list:
            print(s)

    def run(self):
        print("欢迎使用教务管理系统")
        while True:
            print(
                "1.添加学生信息 2.修改学生信息 3.删除学生信息 4.查询指定学生信息 5.展示全部学生信息 6.退出系统"
            )

            action = input("请输入您要进行的操作：")
            match action:
                case "1":
                    self.add()
                case "2":
                    self.update()
                case "3":
                    self.delete()
                case "4":
                    self.search()
                case "5":
                    self.layout()
                case "6":
                    print("退出系统，拜拜")
                case _:
                    print("操作错误")


e1 = Edu()
e1.run()
