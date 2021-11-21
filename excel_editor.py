# import libraries
import openpyxl
import os

# set the file path
os.chdir(r'C:\\Users\\john\\Downloads')

# call the library
wb = openpyxl.load_workbook()
print(wb.get_sheet_names())

# call only one sheet by name
sheet_one = wb.get_sheet_by_name('Sheet')

# fill a column with value
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