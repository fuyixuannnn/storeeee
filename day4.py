# 循环遍历所有的key
# dict = {"k1":"v1","k2":"v2","k3":"v3"}
# for i in dict:
#     print(i,"",end="")

# 循环遍历出所有的value
# dict = {"k1":"v1","k2":"v2","k3":"v3"}
# for i in dict:
#     print(dict[i],"",end="")

# 在字典中增加一个键值对,"k4":"v4"
# dict = {"k1":"v1","k2":"v2","k3":"v3"}
# print(dict)
# dict["k4"] = "v4"
# print(dict)

# 水果超市-小明根据水果名称查询其价格
# dict = {"苹果":"32.8","香蕉":22,"葡萄":15.5}
# print("水果超市有苹果，香蕉，葡萄")
# while True:
#     for i in dict:
#         fruit = input("请输入想要查询的水果：")
#         print(i,"的价格为￥",dict[i])

# 水果超市-小明购买了苹果、草莓、香蕉，小刚购买了葡萄、橘子、樱桃，
# 从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里
# fruits = {"苹果": "12.3",
#           "草莓": "4.5",
#           "香蕉": "6.3",
#           "葡萄": "5.8",
#           "橘子": "6.4",
#           "樱桃": "15.8"}
# info = {"小明": {"fruit": {"苹果": 12.3, "草莓": 4.5, "香蕉": 6.3}},
#         "小刚": {"fruit": {"葡萄": 5.8, "橘子": 6.4, "樱桃": 15.8}}}
# value_ming = sum(info["小明"]["fruit"].values())
# value_gang = sum(info["小刚"]["fruit"].values())
# print("小明一共消费￥",value_ming)
# print("小刚一共消费￥",value_gang)
# info["小明"]["money"] = value_ming
# info["小刚"]["money"] = value_gang
# print(info)

# 编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}
# a = [21, 21, 21, 56, 56, 56, 10, 10, 10, 56, 56, 56, 56, 56, 56]
# dic = {}
# for i in a:
#     if i not in dic:
#         dic[i] = 1
#     elif i in dic:
#         dic[i] = dic[i] + 1
# print(dic)

# 将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
# names = [
#     ["刘备","56","男","106","IBM",500,"50"],
#     ["大乔","19","女","230","微软",501,"60"],
#     ["小乔","19","女","210","Oracle",600,"60"],
#     ["张飞","45","男","230","Tencent",700 ,"10"]
# ]
# staff ={}
# for i in names:
#     name = i[0]
#     staff[name] = {
#         "年龄": i[1],
#         "性别": i[2],
#         "编号": i[3],
#         "任职公司": i[4],
#         "薪资": i[5],
#         "部门编号": i[6]
#     }
# print(staff)
