'''
全年的销售总额
每件衣服的销售（件数）占比
每件衣服的月销售占比
每件衣服的销售额占比
最畅销的衣服是那种
每个季度最畅销的衣服
全年销量最低的衣服
'''

import xlrd
from typing import Dict

wb = xlrd.open_workbook("2020年每个月的销售情况.xlsx")

def annual_sale():
    sum = 0
    annual_sum = 0
    for m in range(0, 12):
        sheet = wb.sheet_by_index(m)
        for i in range(1, sheet.nrows):
            data = sheet.row_values(i)
            sum += data[2] * data[4]
        annual_sum += sum
    print("全年的销售总额为：%.2f" % annual_sum)

def percentage_sale():
    dic1 = {}
    for m in range (0, 12):
        sheet = wb.sheet_by_index(m)
        for i in range(1, sheet.nrows):
            data = sheet.row_values(i)
            if data[1] not in dic1:
                dic1[data[1]] = {"单价": data[2], "销售量": data[4]}
            else:
                dic1[data[1]]["销售量"] += data[4]
    amount = 0
    for key1, value1 in dic1.items():
        amount += value1["销售量"]
    for key2, value2 in dic1.items():
        per = value2["销售量"] / amount *100
        print(key2, "的销售(件数)占比为：%.2f%%" % per)

def percentage_month_sale():
    dic2 = {}
    for m in range(0, 12):
        sheet = wb.sheet_by_index(m)
        month = str(m+1) + "月"
        dic2[month] = {}
        for i in range(1, sheet.nrows):
            data = sheet.row_values(i)
            if data[1] not in dic2[month]:
                dic2[month][data[1]] = {"销售量": data[4]}
            else:
                dic2[month][data[1]]["销售量"] += data[4]
    amount = 0
    for key1, value1 in dic2.items():
        for kay2, value2 in value1.items():
            amount += value2["销售量"]
    for key3, value3 in dic2.items():
        for key4, value4 in value3.items():
            per = value4["销售量"] / amount * 100
            print(key3, key4, "的销售量在全年的销售量占比为：%.2f%%" % per)

def salable():
    dic3 = {}
    for m in range(0, 12):
        sheet = wb.sheet_by_index(m)
        for i in range(0, sheet.nrows):
            data = sheet.row_values(i)
            if data[1] not in dic3:
                dic3[data[1]] = data[4]
            else:
                dic3[data[1]] += data[4]
    max_amount = max(dic3, key=dic3.get)
    min_amount = min(dic3, key=dic3.get)
    print("最畅销的衣服是：%s，销量最低的衣服是：%s" % (max_amount, min_amount))

def quarter_sale():
    dic4 = {"第一季度": {}, "第二季度": {}, "第三季度": {}, "第四季度": {}}
    for m in range(0, 12):
        if m in [1, 2, 3]:
            sheet = wb.sheet_by_index(m)
            for i in range(1, sheet.nrows):
                data = sheet.row_values(i)
                if data[1] not in dic4["第一季度"]:
                    dic4["第一季度"][data[1]] = data[4]
                else:
                    dic4["第一季度"][data[1]] += data[4]
        elif m in [4, 5, 6]:
            sheet = wb.sheet_by_index(m)
            for i in range(1, sheet.nrows):
                data = sheet.row_values(i)
                if data[1] not in dic4["第二季度"]:
                    dic4["第二季度"][data[1]] = data[4]
                else:
                    dic4["第二季度"][data[1]] += data[4]
        elif m in [7, 8, 9]:
            sheet = wb.sheet_by_index(m)
            for i in range(1, sheet.nrows):
                data = sheet.row_values(i)
                if data[1] not in dic4["第三季度"]:
                    dic4["第三季度"][data[1]] = data[4]
                else:
                    dic4["第三季度"][data[1]] += data[4]
        else:
            sheet = wb.sheet_by_index(m)
            for i in range(1, sheet.nrows):
                data = sheet.row_values(i)
                if data[1] not in dic4["第四季度"]:
                    dic4["第四季度"][data[1]] = data[4]
                else:
                    dic4["第四季度"][data[1]] += data[4]
    for key, value in dic4.items():
        quar_max_amount = max(value, key=value.get)
        print(key, "最畅销的衣服是：", quar_max_amount)
        pass

def welcome():
    print("--------请选择你要执行的操作---------")
    print("--------1、全年的销售总额-----------")
    print("--------2、每件衣服的销售（件数）占比")
    print("--------3、每件衣服的月销售占比------")
    print("4、最畅销的衣服是哪种、销量最低的是哪种")
    print("--------5、每个季度最畅销的衣服-------")

while True:
    welcome()
    choice = int(input("请选择要执行的操作："))
    if choice == 1:
        annual_sale()
        pass
    if choice == 2:
        percentage_sale()
        pass
    if choice == 3:
        percentage_month_sale()
        pass
    if choice == 4:
        salable()
        pass
    if choice == 5:
        quarter_sale()
        pass
    else:
        print("请重新选择操作")
