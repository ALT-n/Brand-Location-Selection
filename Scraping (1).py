#!/usr/bin/env python
# coding: utf-8

# In[5]:


from urllib.request import urlopen

html = urlopen('https://www.mystore411.com')
print(html.read())


# In[6]:


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.mystore411.com')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)


# In[7]:


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


# In[8]:


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


# In[9]:


titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print([title for title in titles])


# In[10]:


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.mystore411.com')
bs = BeautifulSoup(html, 'html.parser')

for category in bs.find('ul',{'class':'sidemenu'}).children:
    print(category)


# In[11]:


for search_letters in bs.find('div',{'id':'breadcrumb'}).children:
    print(search_letters)


# In[12]:


for search_A in bs.find('ol',{'id':'sl_popular'}).children:
    print(search_A)


# In[13]:


bs.find_all('ol', {'id':'sl_popular'})


# In[14]:


bs.find('ol', {'id':'sl_popular'}).li


# In[15]:


from urllib.request import urlopen
from bs4 import BeautifulSoup 

for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])


# In[16]:


from urllib.request import urlopen 
from bs4 import BeautifulSoup 
import re

for link in bs.find('div', {'id':'main'}).find_all(
    'a', href=re.compile('^(/store/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])


# In[17]:


links = [link for link in bs(response, parseOnlyThese=SoupStrainer('a')) if link.find("Alberta") != -1]
print(links)


# In[ ]:


pip install requests


# In[18]:


from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re


url = "https://www.mystore411.com/"
r = link.find(url)
soup = BeautifulSoup(r.content)

Alberta_links = lambda tag: (getattr(tag, 'name', None) == 'span' and
                           'itemprop' in tag.attrs and
                           'Alberta' in tag.get_text().lower())
results = soup.find_all(Alberta_links)


# In[19]:


class Website:

    def __init__(self, name, url, targetPattern, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.targetPattern = targetPattern
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Content:

    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        print('URL: {}'.format(self.url))
        print('TITLE: {}'.format(self.title))
        print('BODY:\n{}'.format(self.body))


# In[20]:


from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re
import re


class Crawler:
    def __init__(self, site):
        self.site = site
        self.visited = []

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''

    def parse(self, url):
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, self.site.titleTag)
            body = self.safeGet(bs, self.site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()

    def crawl(self):
        """
        Get pages from website home page
        """
        bs = self.getPage(self.site.url)
        targetPages = bs.find('div', {"id":'a'}).find_all('span', href=re.compile(self.site.targetPattern))
        for targetPage in targetPages:
            targetPage = targetPage.attrs['href']
            if targetPage not in self.visited:
                self.visited.append(targetPage)
                if not self.site.absoluteUrl:
                    targetPage = '{}{}'.format(self.site.url, targetPage)
                self.parse(targetPage)


reuters = Website('Reuters', 'https://www.mystore411.com/', '^(/Alberta/)',
                  False, 'h1', 'div.span')
crawler = Crawler(reuters)
crawler.crawl()


# In[23]:


from bs4 import BeautifulSoup as sp
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re

for link in sp.findAll('div', {'id':'main'}).find_all(
    'a', href=re.compile('^(/Alberta/)((?!:).)*$')):
    if 'span' in link.attrs:
        print(link.attrs['span'])


# In[24]:


from bs4 import BeautifulSoup
import urllib.request

html_page = urllib.request.urlopen("https://www.mystore411.com")
soup = BeautifulSoup(html_page, "html.parser")
for link in soup.findAll('a', href=re.compile('/Alberta/):
    print(link.get('href'))


# In[25]:


def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/"
                            +ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country_code")
links = getLinks("/wiki/Python_(programming_language)")
while(len(links) > 0):
    for link in links:
        print("-------------------")
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP+" is from "+country)
newLink = links[random.randint(0, len(links)-1)].attrs["href"]
links = getLinks(newLink)


# In[ ]:


pip install GooglePlaces


# In[ ]:


pip install googleapiclient


# In[26]:


from googleapiclient.discovery import build 


# In[27]:


import requests

params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
r = requests.post("https://www.mystore411.com", data=params)
print(r.text)


# In[28]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen('https://www.mystore411.com/{}'.format(articleUrl))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id':'main'}).findAll('a', 
        href=re.compile('^(/Alberta/)((?!:).)*$'))

def getHistoryIPs(pageUrl):
    #Format of revision history pages is: 
    #http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace('/Alberta/', '')
    historyUrl = 'https://www.mystore411.com'.format(pageUrl)
    print('history url is: {}'.format(historyUrl))
    html = urlopen(historyUrl)
    bs = BeautifulSoup(html, 'html.parser')
    #finds only the links with class "mw-anonuserlink" which has IP addresses 
    #instead of usernames
    ipAddresses = bs.findAll('a', {'itemprop':'name'})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

links = getLinks('/Alberta/')

while(len(links) > 0):
    for link in links:
        print('-'*20) 
        historyIPs = getHistoryIPs(link.attrs['href'])
        for historyIP in historyIPs:
            print(historyIP)

    newLink = links[random.randint(0, len(links)-1)].attrs['href']
    links = getLinks(newLink)


# In[ ]:


pip install socks


# In[ ]:


pip install socket


# In[29]:


# Must have the TOR service running on port 9150 while running this
import socks
import socket
from urllib.request import urlopen

socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket
print(urlopen('http://icanhazip.com').read())


# In[32]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('https://www.mystore411.com/store/list_state/2176/Alberta/Canada/7-Eleven-store-locations{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href=re.compile('^(/Canada/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks('')

