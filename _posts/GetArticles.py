# -*- coding: utf-8 -*-  
from bs4 import BeautifulSoup
import requests
import urllib.request
import re


firstPage="http://cl.efqxi.com/thread0806.php?fid=7"
preURL="http://cl.efqxi.com/"
pageHtml="http://cl.efqxi.com/thread0806.php?fid=7&search=&page="
searchDepth=10

def GetHTMLSoup(url):
    page = requests.get(url)
    page.encoding = page.apparent_encoding
    soup = BeautifulSoup(page.text, "html.parser")
    return soup

def Output(pre, url, element):
    try:
        f=open('C:\\Users\\Kerwen\\Desktop\\articles.txt','a')
        f.write(str(pre))
        f.write(str(url))
        f.write('    ')
        f.write(str(element))
        f.write('\n')
    except:
        temp=10

def OutputString(message):
    try:
        f=open('C:\\Users\\Kerwen\\Desktop\\articles.txt','a')
        f.write(message)
        f.write('\n')
    except:
        print("")

def HasPictures(title):
    strTitle = str(title)
    index = strTitle.find('P]')
    if(strTitle.find('P]') >0 ):
        return True
    return False
def FindArticlesWithPictureInSinglePage(html):
    soup = GetHTMLSoup(html)
    body = soup.body
    for i in body.find_all('td', attrs={"style": "text-align:left;padding-left:8px"}):                     
        for j in i.find('a'):
            if(HasPictures(j)):
                parent = j.parent        
                Output(preURL, parent['href'], j)


            
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
        Output(preURL,parent['href'], j)
        

        
def SearchGooArticleInSinglePage(html):
    soup = GetHTMLSoup(html)
    body = soup.body
    for i in body.find_all('td', attrs={"style": "text-align:left;padding-left:8px"}):  
        if(HasGoodArticles(i)):
             FindGoodArticle(i)


            
def SearchWithKeyWord(KeyWord):
    SearchWithKeyWordInSinglePage(KeyWord, firstPage)
    for i in range(1,searchDepth):
        SearchWithKeyWordInSinglePage(KeyWord, pageHtml+str(i))

def SearchWithKeyWordInSinglePage(KeyWord, html):
    soup = GetHTMLSoup(html)
    body = soup.body
    for i in body.find_all('td', attrs={"style": "text-align:left;padding-left:8px"}):
        for j in i.find('a'):
            title = str(j)
            if (title.find(KeyWord)>0):
                parent = j.parent
                Output(preURL, parent['href'], j)


def FindArticlesWithPictures():
    FindArticlesWithPictureInSinglePage(firstPage)
    for i in range(1, searchDepth):
          FindArticlesWithPictureInSinglePage(pageHtml+str(i))

def SearchGoodArticles():
    SearchGooArticleInSinglePage(firstPage)
    for i in range(1,searchDepth):
        SearchGooArticleInSinglePage(pageHtml+str(i))

def SearchWithKeyWords(keys):
    list=keys.split(' ')
    if list:
        for KeyWord in list:
            OutputString(KeyWord)
            SearchWithKeyWord(KeyWord)

# Main Entry
#SearchWithKeyWords("求助")
#FindArticlesWithPictures()
SearchGoodArticles()

    


