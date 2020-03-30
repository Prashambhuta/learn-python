#! usr/bin/env python3

"""
Editing excel spreadsheets

"""

import openpyxl
import os

# change the working directory
try:
    os.mkdir('other')
except FileExistsError:
    pass
os.chdir('other')

# create a NEW Workbook

# create a workbook_object
# this will create a new workbook object with sheet: Sheet
workbook_object = openpyxl.Workbook()

# check name of sheet
print(workbook_object.get_sheet_names())

# create a sheet object
sheet = workbook_object.get_sheet_by_name('Sheet')

# add data to cell just like dictionary or list
sheet['A1'] = "Sr No"
sheet['B1'] = "Name"
sheet['C1'] = "Age"

# save workbook object in harddrive
workbook_object.save('example1.xlsx')

# adding new sheet and making it the first sheet
sheet2 = workbook_object.create_sheet(title='Sheet2', index=0)

# change name of existing sheet
sheet.title = 'Sheet1'

workbook_object.save('example1.xlsx')

