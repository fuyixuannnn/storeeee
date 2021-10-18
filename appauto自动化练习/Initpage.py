import xlrd


class Initpage:
    wb = xlrd.open_workbook("sina.xls")
    sheet = wb.sheet_by_index(0)
    login_data = []
    for i in range(0, sheet.nrows):
        data = sheet.row_values(i, 0, 3)
        dict = {
            "username": data[0],
            "password": data[1],
            "expect": data[2]
        }
        login_data.append(dict)

