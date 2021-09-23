import pymysql

host="localhost"
user="root"
password="123456"
database="bank"

def update(sql,param):
    con = pymysql.connect(host=host,user=user,password=password,database=database)
    cursor = con.cursor()
    cursor.execute(sql,param)
    con.commit()
    cursor.close()
    con.close()

def select(sql, param):
    con = pymysql.connect(host="localhost", user='root', password='123456', database='bank')
    cursor = con.cursor()
    cursor.execute(sql, param)
    con.commit()
    data = cursor.fetchall()
    cursor.close()
    con.close()
    return data

import random
class bank:
    def initial(self, bank_name = "青岛银行", max_user = 100):
        self.bank_name = bank_name
        self.max_user = max_user

    def welcome(self):
        print("==============================================")
        print("|--------------青岛银行账户管理系统--------------|")
        print("|------------1、开户              ------------|")
        print("|------------2、取钱              ------------|")
        print("|------------3、存钱              ------------|")
        print("|------------4、转账              ------------|")
        print("|------------5、查询              ------------|")
        print("|------------6、退出              ------------|")
        print("==============================================")

    def userinfo(self):
        param = []
        account = random.randint(00000000,99999999)
        username = input ("请输入用户名：")
        print("您的账号为：", account)
        password = input ("清输入密码：")
        country = input ("请输入国家：")
        province = input ("请输入省份：")
        street = input ("请输入街道：")
        door = input ("请输入门牌号：")
        balance = 0
        param = [account, username, password, country, province, street, door, balance]
        return param

    def adduser(self, param):
        sql1 = "select count(*) from bank"
        data1 = select(sql1, [])
        if len(data1) > self.max_user:
            print("用户库已满！")
        sql2 = "select * from bank where account = %s"
        data2 = select(sql2, param[0])
        if len(data2) != 0:
            print("用户已存在！")
        else:
            sql3 = "insert into bank values(%s, %s, %s, %s, %s, %s, %s, %s)"
            update(sql3, param)
            print("开户成功！")

    def saving(self):
        account = input ("请输入账号：")
        sql1 = "select * from bank where account = %s"
        data1 = select(sql1, account)
        if len(data1) != 0:
            money = float( input ("请输入存入的金额：￥"))
            sql2 = "update bank set balance = balance + %s where account = %s"
            update(sql2, (money,account))
        else:
            print("账号不存在！")

    def withdrawing(self):
        account = input ("请输入账号：")
        sql1 = "select * from bank where account = %s"
        data1 = select(sql1, account)
        if len(data1) != 0:
            money = float( input("请输入取出的金额：￥"))
            if money > data1[0][7]:
                print("余额不足！")
            else:
                sql2 = "update bank set balance = balance - %s where account = %s"
                update(sql2, (money, account))
        else:
            print("账号不存在！")

    def transfer(self):
        faccount = input ("请输入转出账号：")
        taccount = input ("请输入转入账号：")
        sql1 = "select * from bank where account = %s"
        sql2 = "select * from bank where account = %s"
        data1 = select(sql1, faccount)
        data2 = select(sql2, taccount)
        if len(data1) != 0 and len(data2) != 0:
            money = input ("请输入转账金额：￥")
            sql3 = "update bank set balance = balance - %s where account = %s"
            sql4 = "update bank set balance = balance + %s where account = %s"
            update(sql3, (money, faccount))
            update(sql4, (money, taccount))
        else:
            print("账号不存在！")

    def query(self):
        account = input ("请输入账号：")
        sql = "select * from bank where account = %s"
        data = select(sql, account)
        if len(data) != 0:
            info = '''
                    用户名：%s
                    账号：%s
                    密码：%s
                    用户居住地址：%s
                    余额：%s元
                    开户行名称：%s
                    '''
            print(info % (data[0][1], account, data[0][2], data[0][3] + data[0][4] + data[0][5] + data[0][6], data[0][7], self.bank_name))
        else:
            print("该账号不存在！")

b = bank()
while True:
    b.welcome()
    b.initial()
    begin = input("请选择业务编号：")
    if begin == "1":
        b.adduser(b.userinfo())
    elif begin == "2":
        b.withdrawing()
    elif begin == "3":
        b.saving()
    elif begin == "4":
        b.transfer()
    elif begin == "5":
        b.query()
    elif begin == '6':
        print("欢迎下次使用~")
        break
    else:
        print("输入非法！")