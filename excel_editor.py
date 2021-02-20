import openpyxl
import os

os.chdir(r'C:\\Users\\john\\Downloads')

wb = openpyxl.load_workbook()
print(wb.get_sheet_names())

sheet_one = wb.get_sheet_by_name('Sheet')

sheet_one['A1'].VALUE == None
sheet_one['A1'].VALUE == 42
sheet_one['A2'].VALUE == 'Hello'

wb.save('example.xlsx')

sheet2 = wb.create_sheet()
print(wb.get_sheet_names())

print(sheet2.title)

sheet2.title = 'MyNewSheetName'
print(wb.get_sheet_names())
wb.save('example2.xlsx')

wb.crdate_sheet(index =0, tittle = 'My Other Sheet')
wb.save('example3.xlsx')