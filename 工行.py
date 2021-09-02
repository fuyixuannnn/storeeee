print("==============================================")
print("|--------------青岛银行账户管理系统--------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank = {}
# 创建随机账号
import random

# 开户功能
bank_name = "青岛银行"


# 第一个对应第一个 不是名称对应名称
def bank_adduser(account, username, password, country, province, street, door):
    if len(bank) > 100:
        return 3
    if account in bank:
        return 2
    bank[account] = {
        "username": username,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "balance": 0,
        "bank_name": bank_name
    }
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
    stat = bank_adduser(account, username, password, country, province, street, door)
    if stat == 3:
        print("再等等吧~")
    elif stat == 2:
        print("用户已存在！")
    elif stat == 1:
        bank["account"] = account
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s元
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[account]["balance"], bank_name))


# 存钱功能
def saving():
    account = int(input("请输入账号(返回请输入0)："))
    if account in bank:
        save_amount = float(input("请放入金额：￥"))
        bank[account]["balance"] += save_amount
        print("当前余额：￥", bank[account]["balance"])
        switch = input("是否继续存钱？YES or NO")
        while True:
            if switch == "YES" or switch == "yes":
                save_amount = float(input("请放入金额：￥"))
                bank[account]["balance"] += save_amount
                print("当前余额：￥", bank[account]["balance"])
                switch = input("是否继续存钱？YES or NO")
            elif switch == "NO" or switch == "no":
                print("当前余额：￥", bank[account]["balance"])
                return False
            elif account == 0:
                print("当前余额：￥", bank[account]["balance"])
                return False
    else:
        return False


# def check_account(account):
#     if account not in bank:
#         return 1
#
#
# def check_password(account, password):
#     if account in bank and password != bank[account]["password"]:
#         return 2
#     bank[account] = {"password": password}
#
#
# def check_money(account):
#     if account in bank and bank[account]["balance"] < 0:
#         return 3


# 取钱功能
def withdrawing():
#     account = int(input("请输入账号："))
#     stat = check_account(account)
#     if stat == 1:
#         print("账号不存在")
#     else:
#         password = input("请输入密码：")
#         stat = check_password(account, password)
#         if stat == 2:
#             print("密码错误！")
#             return False
#         else:
#             money = float(input("请输入取出的金额：￥"))
#             bank[account]["balance"] -= money
#             stat = check_money(account)
#             while True:
#                 if stat == 3:
#                     print("余额不足！")
#                 else:
#                     print("当前余额：￥", bank[account]["balance"])
#                     switch = input("是否继续取钱？YES or NO")
#                     if switch == "YES" or switch == "yes":
#                         print("当前余额：￥", bank[account]["balance"])
#                         money = float(input("请输入取出的金额：￥"))
#                     elif switch == "NO" or switch == "no":
#                         return False


    account = int(input("请输入账号(返回请输入0)："))
    if account in bank:
        password = input("请输入密码：")
        if password == bank[account]["password"]:
            wd_amount = float(input("请取出金额：￥"))
            bank[account]["balance"] -= wd_amount
            if bank[account]["balance"] < 0:
                print("余额不足")
            else:
                print("当前余额：￥", bank[account]["balance"])
                switch = input("是否继续取钱？YES or NO")
                while True:
                    if switch == "YES" or switch == "yes":
                        wd_amount = float(input("请取出金额：￥"))
                        bank[account]["balance"] -= wd_amount
                        if bank[account]["balance"] < 0:
                            print("余额不足")
                        else:
                            print("当前余额：￥", bank[account]["balance"])
                            switch = input("是否继续取钱？YES or NO")
                    elif switch == "NO" or switch == "no":
                        print("当前余额：￥", bank[account]["balance"])
                        return False
                    elif account == 0:
                        print("当前余额：￥", bank[account]["balance"])
                        return False
        else:
            print("密码错误！")
    else:
        print("账号不存在！")
        return False

# 转账
def transfer():
    faccount = int(input("请输入转出账号"))
    taccount = int(input("请输入转入账号"))
    if faccount and taccount in bank:
        password = input("请输入转出账号密码")
        if password == bank[faccount]["password"]:
            print("当前余额为￥", bank[faccount]["balance"])
            money = float(input("请输入转账金额：￥"))
            if money <= bank[faccount]["balance"]:
                bank[faccount]["balance"] -= money
                bank[taccount]["balance"] += money
                print("转账成功！")
        else:
            print("密码错误！")
    else:
        print("账号不存在！")


# 查询功能
def query():
    account_number = int(input("请输入想要查询的账号："))
    if account_number in bank:
        pswd = input("请输入密码：")
        if pswd == bank[account_number]["password"]:
            print("密码正确！")
            info = '''
            用户名：%s
            账号：%s
            密码：%s 
            用户居住地址：%s
            余额：%s元
            开户行名称：%s
            '''
            print(info % (bank[account_number]["username"], account_number, bank[account_number]["password"],
                          bank[account_number]["country"] + bank[account_number]["province"] + bank[account_number][
                              "street"] + bank[account_number]["door"], bank[account_number]["balance"],
                          bank[account_number]["bank_name"]))
        else:
            print("密码错误")
    else:
        print("该账号不存在！")


while True:
    begin = input("请选择业务")
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
    else:
        print(6, "、退出")
        break
