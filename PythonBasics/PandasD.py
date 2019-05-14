import pandas

pd = pandas.read_excel("G:\\Python Training\\Python Training - Ethans\\bollywood.xlsx")
#pd1 = pd[[pd.Director==('G. V. Sane')],['Year', 'Title']]
#print(pd
 #     [[pd.Director.str.contains('G. V. Sane')] and  [pd.Cast.str.contains('unknown')]].
  #    groupby(['Director', 'Year']).size())


#print(pd.groupby(['Director', 'Year']).size())
print(pd.groupby(['Director']).size().sort_values(ascending=False).head(5))
pd.groupby(['Director']).size().sort_values(ascending=False).head(5)

#pd.groupby([])



#print(pd1)