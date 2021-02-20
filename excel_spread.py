import openpyxl
import os

os.chdir(r'C:\\Users\\john\\Downloads')

workbook = openpyxl.load_workbook('example.xlsx')
print(type(workbook))

sheet_one = workbook.get_sheet_by_name('Sheet1')
print(type(sheet_one))

print(workbook.get_sheet_names())

cellA1 = sheet_one['A1']
print(cellA1.value)

print(str(sheet_one['A1']))

cellB1 = sheet_one['B1']
print(cellB1.value)

cellC1 = sheet_one['C1']
print(cellC1.value)

sheet_one.cell(row=1, column=2)

for i in range(1,8):
    print(i, sheet.cell(row=i, column=2).value)