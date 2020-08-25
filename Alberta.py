#!/usr/bin/env python
# coding: utf-8

# In[46]:


from urllib.request import urlopen

html = urlopen('https://www.mystore411.com/store/list_state/2176/Alberta/Canada/7-Eleven-store-locations')
print(html.read())


# In[47]:


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.mystore411.com/store/list_state/2176/Alberta/Canada/7-Eleven-store-locations')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)


# In[48]:


bs.find('span', {'itemprop':'name'})


# In[49]:


td=bs.find_all('td', {'class':'dotrow'})
td


# In[61]:


import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.mystore411.com/store/list_state/2176/Alberta/Canada/7-Eleven-store-locations')
bs = BeautifulSoup(html, 'html.parser')
# The main comparison table is currently the first table on the page
table = bs.findAll('table',{'class':'table1'})[0]
rows = table.findAll('td')

csvFile = open('mytest.csv', 'wt+')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text().encode('utf-8'))
        writer.writerow(csvRow)
finally:
    csvFile.close()
    
    
 


# In[70]:


import requests
import csv
from bs4 import BeautifulSoup as bs

url = urlopen("https://www.mystore411.com/store/list_state/2176/Alberta/Canada/7-Eleven-store-locations")
soup = bs(url, 'html.parser')

filename = "test2.csv"
csv_writer = csv.writer(open(filename, 'w'))


for tr in soup.find_all("tr"):
    data = []
    # for headers ( entered only once - the first time - )
    for th in tr.find_all("th"):
        data.append(th.text)
    if data:
        print("Inserting headers : {}".format(','.join(data)))
        csv_writer.writerow(data)
        continue

    for td in tr.find_all("td"):
        if td.a:
            data.append(td.a.text.strip())
        else:
            data.append(td.text.strip())
    if data:
        print("Inserting data: {}".format(','.join(data)))
csv_writer.writerow(data)
        

