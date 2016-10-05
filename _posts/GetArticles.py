# -*- coding: utf-8 -*-  
from bs4 import BeautifulSoup
import requests
import urllib.request
import re


html="http://cl.efqxi.com/thread0806.php?fid=7"
preURL="http://cl.efqxi.com/"
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
#req = urllib.request.Request(url=html, headers=headers)  
#htmlSource = urllib.request.urlopen(req).read().decode('gbk')
#soup = BeautifulSoup(htmlSource, "html.parser")



def GetHTMLSoup(url):
    page = requests.get(url)
    page.encoding = page.apparent_encoding
    soup = BeautifulSoup(page.text, "html.parser")
    return soup

def Output(message):
    try:
        print(message)
    except:
        print("error")

def HasPictures(title):
    strTitle = str(title)
    index = strTitle.find('P]')
    if(strTitle.find('P]') >0 ):
        return True
    return False
def FindArticlesWithPicture(element):
    for j in element.find('a'):
        if(HasPictures(j)):
            parent = j.parent        
            print(preURL,parent['href'], "   ",sep='',end=""),
            Output(j)
def HasGoodArticles(element):
    lists = element.find_all('font')
    if(lists):
        for i in lists:
            content = str(i)
            if(content.find('分+') >0):
                return True
    return False

def FindGoodArticle(element):
    for j in element.find('a'):
        parent = j.parent        
        print(preURL,parent['href'], "   ",sep='',end=""),
        Output(j)
def SearchArticle(html):
    soup = GetHTMLSoup(html)
    body = soup.body
    for i in body.find_all('td', attrs={"style": "text-align:left;padding-left:8px"}):  
        #FindArticlesWithPicture(i)
        if(HasGoodArticles(i)):
             FindGoodArticle(i)
# Main Entry

pageHtml="http://cl.efqxi.com/thread0806.php?fid=7&search=&page="
SearchArticle(html)
for i in range(1,10):
    SearchArticle(pageHtml+str(i))

    

#page = requests.get(html)
#print(page.encoding, page.apparent_encoding)
#page.encoding = page.apparent_encoding

#soup = BeautifulSoup(page.text, "html.parser")
#try:
#    print(soup.prettify())
#except Exception as err:
#    print(err)
#http://cl.efqxi.com/htm_data/7/1610/2091884.html