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
    name = ""

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

class worker(person):
    def work(self, work):
        print(p.name, "正在干活，今天的任务是", work)

class student(person):
    num = ""

    def study(self, subject):
        print(p.name, "正在学习", subject)

    def sing(self, songname):
        print(p.name, "正在唱", songname)

p = person()
p.name = "小李子"
p.set_gender("男")
p.set_age(88)
w = worker()
w.work("刨土")
s = student()
s.num = "00171565"
s.study("挖掘机")
s.sing("死了都要挖")

