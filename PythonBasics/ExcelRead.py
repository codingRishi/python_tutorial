import xlrd

wb = xlrd.open_workbook("G:\\Python Training\\Python Training - Ethans\\ExcelXlrd.xlsx")
sheet = wb.sheet_by_index(0)

cell = sheet.cell(3,0)
print(cell.value)
print("Number of Rows : " , sheet.nrows)
print("Highest number of cell in any row : " , sheet.ncols)

