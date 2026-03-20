"""
数据容器 string
"""

s = "hello-python"

print(s[4])   #正向索引
print(s[-1])   #反向索引

for i in s:
  print (i)



##切片
print(s[0:5:1])
print(s[:5:1])
print(s[0:5:])
print(s[0:5:2])
print(s[-1:-7:-1])



##字符串 常用方法
s = "Hello-Python-Hello-World"

#find() 查找指定字符串第一次出现的索引位置
index = s.find("-")
print(index)

#count()  统计子字符串在指定字符串中出现的次数
c = s.count("o")
print(c)

#upper()    转为大写
su = s.upper()
print(su)

#lower()   转小写
sl = s.lower()
print(sl)

#split  将字符串按照指定字符串切割封装到列表中-列表
slist = s.split("-")
print(slist)

#strip  去除字符串两端的空白字符或指定子符
ss = s.strip("H")
print(ss)

#replace  将字符串中的指定子串替换为新的内容
sr = s.replace("Hello", "Bye")
print(sr)

#startswith() / endswith() 判断字符串是否是以指定的字符串开头 / 结尾，返回布尔值
print(s.startswith("Hello"))
print(s.endswith("Hello"))


print(s)  #原始字符串没有改变




###案例1 邮箱格式验证：用户输入一个邮箱，验证邮箱格式是否正确（包含一个@和至少一个.）
mail =input("请输入邮箱：")

if mail.count("@") == 1 and mail.count(".") >=1:
  print("输入的邮箱正确")
else:
  print("输入的邮箱错误")


##案例1 ----------  使用in判断
mail =input("请输入邮箱：")

if mail.count("@") == 1 and "." in mail:
  print("输入的邮箱正确")
else:
  print("输入的邮箱错误")




### 案例2. 输入一个字符串, 判断该字符串是否是回文(两边对称) 。  回文"黄山落叶松叶落山黄"  "上海自来水来自海上"
str = input("请输入一个字符串：")
left = 0
right = len(str) - 1
flag = True

while left < right:
  if str[left] != str[right]:
    flag = False
    break
  left += 1
  right -= 1

if flag:
  print("是回文")
else:
  print("不是回文")



# ###案例2---方法2
str = input("请输入一个字符串：")
if str == str[::-1]:
  print("是回文")
else:
  print("不是回文")