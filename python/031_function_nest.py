"""
函数嵌套
"""


###函数的嵌套调用
def function_a():
    print("a...after")
    function_b()
    print("a...after")


def function_b():
    print("b...after")
    function_c()
    print("b...after")


def function_c():
    print("c...after")


function_a()

print("函数调用完毕")


###案例1:定义一个函数，根据传入的底和高计算三角形的面积
def triangle_area(b, h):
    area = b * h / 2
    return area


triangle_area(10, 20)

print(f"底为10,高为20的三角形的面积:{triangle_area(10, 20)}")


###案例2: 定义一个函数，计算传入的字符串中元音字母的个数（元音字母为aeiouAEIOU）
def count_aeiou(s):
    num = 0  # s = hello
    for w in s:
        if w in "aeiouAEIOU":
            num += 1
    return num


print(count_aeiou("helloworld"))


###案例3: 定义一个函数，计算传入的班级学生高考列表中成绩的最高分，最低分，平均分（保留一位小数），并返回
def class_score(score_list):
    max_score = max(score_list)
    min_score = min(score_list)
    avg_score = round(sum(score_list) / len(score_list), 1)
    return max_score, min_score, avg_score


s_list = [45, 67, 44, 67, 34, 12, 89]

class_score(s_list)

max_score, min_score, avg_score = class_score(s_list)

print("最高分：", max_score)
print("最低分：", min_score)
print("平均分：", avg_score)


###作业 1. 分数等级
# 定义一个函数，根据传入的分数，计算对应的分数等级并返回。
# - 分数 >= 90: A
# - 分数 >= 75: B
# - 分数 >= 60: C
# - 分数 < 60: D
def score_level(s):
    if s >= 90:
        return "A"
    elif s >= 75:
        return "B"
    elif s >= 60:
        return "C"
    else:
        return "D"


print(score_level(80))


## 作业 2. 回文串判断
# 定义一个函数，用于判断一个字符串是否是回文串，返回 bool 值。
# - 把字符串反转，如果和原字符串相同，就是回文串
# - 例如："level"、"radar"、"黄山落叶松叶落山黄"
def is_palindrome(s):
    """判断字符串是否是回文串，返回 bool 值"""
    return s == s[::-1]


s = "qwerewq"
print(is_palindrome(s))


# ## 作业3. 时间转换
# 定义一个函数，完成时间转换功能，将传入的秒转换为小时、分钟、秒。
def time_change(s):
    h = s // 3600  # // 是整除，3600 秒 = 1 小时，得到小时数（去掉小数）
    m = (
        s % 3600
    ) // 60  # seconds % 3600：去掉整小时后剩下的秒数，// 60：再除以 60 得到分钟数
    s = (
        s % 3600
    ) % 60  # (seconds % 3600)：去掉整小时后的秒数，% 60：再对 60 取余，得到不足 1 分钟的秒数
    return f"3772 = {h}小时  {m}分钟  {s}秒"


print(time_change(3772))


# ## 作业4. 三角形类型判定
# 定义一个函数，根据传入的三角形三个边的边长，判定三角形的类型。
# - 等边三角形
# - 等腰三角形
# - 普通三角形
# - 不能构成三角形
def what_triangles(side_list):
    a, b, c = side_list
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "等边三角形"
        elif a == b or a == c or b == c:
            return "等腰三角形"
        else:
            return "普通三角形"
    else:
        return "不能构成三角形"


side_list = [1, 2, 3]
print(what_triangles(side_list))
