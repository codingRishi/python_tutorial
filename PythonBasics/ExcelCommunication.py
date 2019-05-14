import xlrd as xl

location = "G:\\Python Training\\Python Training - Ethans\\ExcelXlrd.xlsx"
workbook = xl.open_workbook(location)
sheet = workbook.sheet_by_index(0)
print("Number of Rows" , sheet.nrows)

datai=[]
dataRow = []
for r in range(sheet.nrows):
    for c in range(sheet.ncols):
        cell = sheet.cell(r, c)
        if(cell.value!=''):
            datai.append(cell.value)
print(datai)

for num in range(sheet.nrows):
    cell = sheet.cell(num,3)
    if(cell.value!=''):
        print(cell.value)


for ce in range(sheet.ncols):
        cell = sheet.cell(0, ce)
        if(cell.value=='Team') :
            indexOfCell = ce
print("index of desired cell : " , indexOfCell)