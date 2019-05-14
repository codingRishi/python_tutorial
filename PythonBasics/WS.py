import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.hubertiming.com/results/2017GPTR10K")
x =BeautifulSoup(response.text, 'html.parser')
single_table = x.find("table",{"id":"individualResults"})
trs = single_table.find_all("tr")
list_rows=[]

for tr in trs:
    list_row = []
    for td in tr.find_all("td"):
       list_row.append(td.text)
    list_rows.append(list_row)

print(list_rows[1])