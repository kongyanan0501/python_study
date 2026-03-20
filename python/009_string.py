"""
字符串拼接
"""

s1 = "人生苦短" "我用python" ", ok"
print(s1)

s2 = "人生苦短"
s3 = "我用python"
print("龟述说：" + s2 + " , " + s3)


# """
# 案例
# str(int数字) -> 将int数字转换为str字符串
# """

# 输出 "大家好，我是涛哥，今年18岁，学习的专业是软件工程，爱好python、java"

name = "涛哥"
age = "18"
major = "软件工程"
hobbies = "python、java"
print(
    "大家好，我是"
    + name
    + " ,今年"
    + str(age)
    + "岁，学习的专业是"
    + major
    + "，爱好"
    + hobbies
)
