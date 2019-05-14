import pandas
import xlwt

list = ["abc", "pqr","qwe"]
data={'name':["india", "pak","sri"],
      'city':["pune","mumbai", "delhi"]}


def Convert_NaN_Anything(cell):
    global count
    if(cell=='csk'):
        count=count+1
        print("Th" + count)
        return 'y'
    return cell

pdexcel = pandas.read_excel("G:\\Python Training\\Python Training - Ethans\\ExcelXlrd.xlsx",
                            converters={'Anything':Convert_NaN_Anything})
pdDataframe_Series = pandas.DataFrame(pdexcel)
print(pdDataframe_Series)
#pdDataframe_Series.to_excel("test.xls", index=False, columns=['Name','Team'])
