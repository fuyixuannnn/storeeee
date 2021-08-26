# 1.实现输入10个数字，并打印10个数的求和结果
# a = []
# for i in range (10):
#     b = input("请输入数值：")
#     a.append(float(b))
# for i in a:
#     s = round(sum(a),5)
# print("总和为",s)

# 2.从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数
# a = []
# for i in range (10):
#     b = input("请输入数值：")
#     a.append(float(b))
# for i in a:
#     m = max(a)
#     s = round(sum(a),5)
#     average = avg = s/10
# print("最大值=",m)
# print("总和=",s)
# print("平均值=",average)

# 3.使用random模块，如何产生 50~150之间的数
# import random
# num = random.randint(50,150)
# print(num)

# 4.从键盘输入任意三边，判断是否能形成三角形，若可以,则判断形成什么三角形
# （结果判断：等腰，等边，直角，普通，不能形成三角形)
# a = int(input("请输入第一条边(请输入正整数)："))
# b = int(input("请输入第二条边(请输入正整数)："))
# c = int(input("请输入第三条边(请输入正整数)："))
# if a+b>c and a+c>b and b+c>a and a != b and b != c and a != c and a^2 + b^2 != c^2 and a^2 + c^2 != b^2 and b^2 + c^2 != a^2:
#     print("这是一个普通三角形")
# elif a+b>c and a+c>b and b+c>a and a == b == c and a^2 + b^2 != c^2 and a^2 + c^2 != b^2 and b^2 + c^2 != a^2:
#     print("这是一个等边三角形")
# elif a+b>c and a+c>b and b+c>a and a == b or b == c or a == c and a^2 + b^2 != c^2 and a^2 + c^2 != b^2 and b^2 + c^2 != a^2:
#     print("这是一个等腰三角形")
# elif a+b>c and a+c>b and b+c>a and a != b and b != c and a != c and a^2 + b^2 == c^2 or a^2 + c^2 == b^2 or b^2 + c^2 == a^2:
#     print("这是一个直角三角形")
# elif a+b>c and a+c>b and b+c>a and a == b or b == c or a == c and a^2 + b^2 == c^2 or a^2 + c^2 == b^2 or b^2 + c^2 == a^2:
#     print("这是一个等腰直角三角形")
# else :
#     print("不能构成三角形")

# 5.有以下两个数，使用+，-号实现两个数的调换
# a = int(input("数字a="))
# b = int(input("数字b="))
# a = a + b
# b = a - b
# a = a - b
# print("(a,b)=",a,b)

# 6.实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# count = 0
# user_name = "root"
# user_password = "admin"
# name = input("请输入用户名：")
# if name == user_name:
#     while count < 3:
#         password = input ("登录密码：")
#         if password == user_password:
#             print("欢迎登录~")
#             break
#         else:
#             print("密码错误！")
#             count += 1
#     else:
#         print("对不起，您的账号因连续输入三次错误密码被锁定。")
# else:
#     print("用户名错误！")

# 7.打印正三角形
# rows = int(input("输入行数："))
# for i in range(0,rows):
#     for j in range(0, rows - i):
#         print(end=" ")
#     for k in range(rows - i, rows+1):
#         print("*", end=" ")
#     print("")

# 8.
