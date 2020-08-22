#!/usr/bin/env python
# coding: utf-8

# In[16]:


from urllib.request import urlopen

html = urlopen('https://www.mystore411.com')
print(html.read())


# In[17]:


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.mystore411.com')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)


# In[18]:


from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("https://www.mystore411.com")
except HTTPError as e:
    print("The server returned an HTTP error")
except URLError as e:
    print("The server could not be found!")
else:
    print(html.read())


# In[19]:


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("https://www.mystore411.com")
if title == None:
    print("Title could not be found")
else:
    print(title)


# In[20]:


titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print([title for title in titles])


# In[21]:


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.mystore411.com')
bs = BeautifulSoup(html, 'html.parser')

for category in bs.find('ul',{'class':'sidemenu'}).children:
    print(category)


# In[22]:


for search_letters in bs.find('div',{'id':'breadcrumb'}).children:
    print(search_letters)


# In[23]:


for search_A in bs.find('ol',{'id':'sl_popular'}).children:
    print(search_A)


# In[28]:


bs.find_all('ol', {'id':'sl_popular'})


# In[29]:


bs.find('ol', {'id':'sl_popular'}).li

