import pymysql


def update(sql, param):
    con = pymysql.connect(host="localhost", user='root', password='123456', database='bank')
    cursor = con.cursor()
    cursor.execute(sql, param)
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

bank_name = "工商银行"

def welcome():
    print("==============================================")
    print("|--------------工商银行账户管理系统--------------|")
    print("|------------1、开户              ------------|")
    print("|------------2、取钱              ------------|")
    print("|------------3、存钱              ------------|")
    print("|------------4、转账              ------------|")
    print("|------------5、查询              ------------|")
    print("|------------6、退出              ------------|")
    print("==============================================")


def bank_adduser(account, username, password, country, province, street, door):
    sql1 = "select count(*) from bank"
    data = select(sql1, [])
    if len(data) >= 100:
        return 3
    sql2 = "select * from bank where account = %s"
    data = select(sql2, [account])
    if len(data) != 0:
        return 2
    sql3 = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s)"
    param = [account, username, password, country, province, street, door, 0]
    update(sql3, param)
    return 1


def adduser():
    username = input("请输入您的用户名")
    account = random.randint(10000000, 99999999)
    print("账号为", account)
    password = input("请输入您的密码")
    print("请输入您的地址")
    country = input("\t\t请输入您的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    status = bank_adduser(account, username, password, country, province, street, door)
    if status == 3:
        print("再等等吧~")
    elif status == 2:
        print("用户已存在！")
    elif status == 1:
        print("开户成功！")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：%s
                    国家：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s元
                    开户行名称：%s
                '''
        print(info % (username, account, password, country, province, street, door, 0, bank_name))


# 存钱功能
def saving():
    account = int(input("请输入账号(返回请输入0)："))
    sql = "select * from bank where account = %s"
    data = (sql, [account])
    if len(data) != 0:
        money = float(input("请输入放入的金额：￥"))
        sql = "update bank set balance = balance + %s"
        update(sql, (money, account))
        # print("您的余额为：", )
    else:
        return False


# 取钱功能
def withdrawing():
    account = int(input("请输入账号："))
    sql1 = "select * from bank where account = %s"
    data1 = select(sql1, [account])
    if len(data1) != 0:
        print("您的余额为：", data1[0][7])
        money = float(input("请输入要取出的金额：￥", ))
        if money <= data1[0][7]:
            sql2 = "update bank set balance = balance - %s where account = %s"
            update(sql2, (money, account))
            sql3 = "select balance from bank where account = %s"
            data3 = select(sql3, account)
            print("您的余额为：", data3[0][0])
        else:
            print("余额不足！")
    else:
        print("账号不存在！")
        return False


# 转账
def transfer():
    faccount = int(input("请输入转出账号"))
    taccount = int(input("请输入转入账号"))
    sql1 = "select * from bank where account = %s"
    sql2 = "select * from bank where account = %s"
    data1 = select(sql1, faccount)
    data2 = select(sql2, taccount)
    print(data1, data2)
    if len(data1) != 0 and len(data2) != 0:
        print("账户余额为：￥", data1[0][7])
        money = float(input("请输入转账金额：￥"))
        if money <= data1[0][7]:
            sql3 = "update bank set balance = balance - %s WHERE account = %s"
            update(sql3, (money, faccount))
            sql4 = "update bank set balance = balance + %s WHERE account = %s"
            update(sql4, (money, taccount))
        else:
            print("余额不足！")
    else:
        print("账号不存在！")


# 查询功能
def query():
    account = int(input("请输入想要查询的账号："))
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
        print(info % (data[0][1], account, data[0][2], data[0][3]+data[0][4]+data[0][5]+data[0][6], data[0][7], bank_name))
    else:
        print("该账号不存在！")


while True:
    welcome()
    begin = input("请选择业务编号：")
    if begin == "1":
        adduser()
    elif begin == "2":
        withdrawing()
    elif begin == "3":
        saving()
    elif begin == "4":
        transfer()
    elif begin == "5":
        query()
    elif begin == '6':
        print("欢迎下次使用~")
        break
    else:
        print("输入非法！")
