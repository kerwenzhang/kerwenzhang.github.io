#-*- coding:utf-8 -*-

import urllib.request
import sys
import re
from bs4 import BeautifulSoup
import Write

URL = 'http://www.iciba.com/'

while True:
	try:
		word = input("Please input a word (or press CTRL+C to exit):")
	except KeyboardInterrupt:
		print("\n Exit.")
		sys.exit(1)
	except EOFError:
		print("\n Exit.")
		sys.exit(1)
	if not word:
		break
	
	url = URL + word
	
	# Search words
	f = urllib.request.urlopen(url)
	reader = f.read()
	reader = reader.decode('UTF-8')
	
	# user BeautifulSoup to analysis 
	soup = BeautifulSoup(''.join(reader), "html.parser")
	
	result1 = soup.findAll("ul",{"class":"base-list"})
	if not result1:
		print ("Sorry, failed to translate the word")
		continue
	Write.WriteToFile("")
	
	sys.stdout.write('\n')
	for item in result1:
		aa = item.find("span",{"class":"prop"})
		bb = item.findAll("p")
		Write.AppendToFile(aa.contents[0])
		for i in bb:
			str1 = i.contents[0].strip()
			newStr=""
			x_list = str1.split(' ')
			for data in x_list:
				data = data.strip()
				if(len(data)==0):
					continue
				newStr += data
				newStr += " "
			Write.AppendToFile(newStr)
			sys.stdout.write("\n")
	
	Write.AppendToFile("Example:")
	results2 = soup.findAll("div",{"class":"section-p"},limit=3)			
	for item in results2:
		order = item.find("span",{"class":"p-order"})
		Write.AppendToFile(order.contents[0])
		english = item.find("p",{"class":"p-english"})
		Write.AppendToFile(english.contents[0])
		chinese = item.find("p",{"class":"p-chinese"})
		Write.AppendToFile(chinese.contents[0])
	sys.stdout.write("\n")
	sys.stdout.write("\n")