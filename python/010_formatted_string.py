"""
字符串格式化
"""

# 输出 "大家好，我是涛哥，今年18岁，学习的专业是软件工程，爱好python、java"

# 方式1:%s 占位符
name = "涛哥"
age = "18"
major = "软件工程"
hobbies = "python、java"
print(
    "大家好, 我是 %s , 今年 %s 岁 , 学习的专业是 %s , 爱好 %s"
    % (name, age, major, hobbies)
)


# 方式2: f"变量名/表达式"
print(f"大家好, 我是 {name} , 今年 {age} 岁 , 学习的专业是 {major} , 爱好 {hobbies}")
