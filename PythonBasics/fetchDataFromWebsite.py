import requests
import bs4
import re
import pandas



response = requests.get("https://www.hubertiming.com/results/2017GPTR10K")
x =bs4.BeautifulSoup(response.text, 'html.parser')
print(response)
all_rows = x.find_all("tr")
list_rows=[]
#print(all_links)
for row_link in all_rows:
    all_cells = row_link.find_all("td")
    all_cells_str = str(all_cells)
    print(all_cells_str)
    clean = re.compile('<.*?>')
    print("test", clean)
    clean1 = (re.sub(clean,' ',all_cells_str))
    list_rows.append(clean1)
pd = (pandas.DataFrame(list_rows).head())

#all_cells_str = str(all_cells)
#cleanText = bs4.BeautifulSoup(all_cells_str,"lxml").get_text()
#print(cleanText)