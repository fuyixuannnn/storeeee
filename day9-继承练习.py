'''
人：
属性（私有化）：年龄，性别，姓名
    工人：
    属性：年龄，性别，姓名
    行为：干活
        学生：
        属性：年龄，性别，姓名，学号
        行为：学习，唱歌
'''


class person:
    __age = 0
    __gender = ""
    __name = ""

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("年龄非法")
    def get_age(self):
        return self.__age

    def set_gender(self, gender):
        if gender == "男" or gender == "女":
            self.__gender = gender
        else:
            print("性别非法！")
    def get_gender(self):
        return self.__gender

    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name


class worker(person):
    def work(self, work):
        print(p.get_name(), "正在干活，今天的任务是", work)


class student(person):
    num = ""

    def study(self, subject):
        print(p.get_name(), "正在学习", subject)

    def sing(self, songname):
        print(p.get_name(), "正在唱", songname)


p = person()
p.set_name("小李子")
p.set_gender("男")
p.set_age(88)
w = worker()
w.work("刨土")
s = student()
s.num = "00171565"
s.study("挖掘机")
s.sing("死了都要挖")

'''
老手机
属性：品牌
行为：打电话
    新手机（继承）
    属性：品牌
    行为：打电话、介绍
'''

import time
class oldphone:
    __brand = ""

    def set_brand(self, brand):
        self.__brand = brand
    def get_brand(self):
        return self.__brand

    def call(self, phonenum):
        print("正在给", phonenum, "打电话")
        for i in range(6):
            print(".",end="")
            time.sleep(1)

class newphone(oldphone):

    def call(self, phonenum):
        print("正在拨号中...")
        super().call(phonenum)

    def introduce(self):
        print(o.get_brand(), "的手机很好用")

o = oldphone()
o.set_brand("诺基亚")
o.call("12345678900")
n = newphone()
n.call("01012345678")
n.introduce()
