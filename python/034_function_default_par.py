"""
函数 默认参数
"""


# 定义函数
def reg_stu(name, age, gender="男", city="大连"):
    print(f"注册成功，姓名：{name} ,年龄：{age}, 性别：{gender},城市: {city}")
    return {"name": name, "age": age, "gender": gender, "city": city}


# 调用函数
stu = reg_stu("韩立", 29)
print(stu)  # result:注册成功，姓名：韩立 ,年龄：29, 性别：男,城市: 大连

stu = reg_stu("紫菱", 19, "女")
print(stu)  # result:注册成功，姓名：紫菱 ,年龄：19, 性别：女,城市: 大连

stu = reg_stu("紫菱", 19, city="北京")
print(stu)  # result:注册成功，姓名：紫菱 ,年龄：19, 性别：男,城市: 北京
