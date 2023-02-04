import openpyxl

# 获取工作簿
book = openpyxl.load_workbook('params.xlsx')

# 获取工作表
sheet = book.active

# 获取单元格数据
a_1 = sheet['A1'].value
# print(a_1)
c_3 = sheet.cell(column=3, row=3).value
# print("c_3", c_3)

# 获取多个单元格
cells = sheet["A1":"C3"]
print(type(cells), cells)
