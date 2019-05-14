import pandas


def conver_Neg_Rank(cell):
    if(cell==-2):

        return 0
    return cell


#Chunksize = 10**6
#for chunk in  pandas.read_excel("G:\\Python Training\\Python Training - Ethans\\bollywood.xls",Chunksize=Chunksize
 #                      ):
  #  process(chunk)
pd = pandas.read_excel("G:\\Python Training\\Python Training - Ethans\\bollywood.xlsx")

#
#print(pd.groupby(['Director', 'Year']).size())
print(pd.groupby(['Director']).size().sort_values(ascending=False).head(5))


#help(pd.loc)
#print(pd.head())
#pd.set_index('')

#print(pd.loc[,:])
#pd = pandas.read_excel("G:\\Python Training\\Python Training - Ethans\\ExcelXlrd.xlsx")
#print(pd.sort_values("Rank", ascending=True))

#pd.to_excel('modified.xls ', index=False)