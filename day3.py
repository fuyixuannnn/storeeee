'''
商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金额
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在：
                金钱足够：
                    成功加入购物车
                    余额减去对应价格
                不够：
                    '穷鬼，去买其他商品'
            商品不存在：
                输入错误
            输入q或Q，退出并结算，打印小条
任务：
    1.打印小票，合并同类计数
    2.10张iPhone优惠券（8折），20张HUAWEI优惠券（9折）
        进入商城可随机抽取一张优惠券，在最后结算时使用优惠券对相应商品打折
'''
# 抽奖
import random
print("欢迎欢迎~ 恭喜获得抽奖机会！您可抽取一张特定优惠券")
input("点击回车就可以抽奖了哦~")
num = random.randint(1,30)
if 0 < num < 11:
    print("恭喜你!获得iPhone8折优惠券！")
    coupon = 3
    discount = 0.8
if 10 < num < 31:
    print("恭喜你！获得HUAWEI9折优惠券")
    coupon = 1
    discount = 0.9

# 商品
shop = [
    ["机械革命",15000],
    ["HUAWEI watch",1200],
    ["MAC PC",13000],
    ["Iphone 54 plus",45000],
    ["辣条",2.5],
    ["老干妈",13]
]

# 初始化您的余额
money = input("请输入您的钱包余额:")
money = int(money)

# 3.准备一个空的购物车
mycart = []

# 买东西

while True:
    # 展示商品
    for index,value in enumerate(shop): # 枚举，将角标和商品整体都打印
        print(index,"  ",value)
    # 请输入您要的商品
    chose = input("请输入您要的商品：")

    # 看是否存在
    if chose.isdigit():  # 是否能被看成数字：
        chose = int(chose)
        # 看商品是否存在
        if chose > len(shop) - 1:
            print("您要的商品不存在！")
        else:
            # 看钱是否足够
            if money > shop[chose][1]:
                mycart.append(shop[chose])
                if chose == coupon:
                    discount_money = shop[chose][1] * discount
                    coupon = 100
                    money = money - discount_money
                    print("恭喜，成功添加购物车，优惠券已使用。您的余额还剩：￥",money)
                else:
                    money = money - shop[chose][1]
                    print("恭喜，成功添加购物车，您的余额还剩：￥",money)
            else:
                if money < shop[chose][1]:
                    print("对不起，穷鬼，余额不足，请到别的商城去购买！")
    elif chose == 'q' or chose == 'Q':
        print("欢迎下次光临！")
        break
    else:
        print("对不起，您的输入商品不存在！别瞎弄!")

# 打印购物小条
dic = {}
for i in mycart:
    if i[0] not in dic:
        dic[i[0]] = 1
    else:
        dic[i[0]] = dic[i[0]] + 1
print("以下是您的购物小条，请拿好：")
print("------------------商城------------------")
for i in dic:
    print(i,dic[i])
print("您的钱包余额还剩: ",money)
print("-----------------------------------------")

