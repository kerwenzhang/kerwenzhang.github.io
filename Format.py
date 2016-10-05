''' 
This script is used to format MarkDown file.
1. Add blank space for each line
2. If meet code, add tab and \r automatically
3. Add markdown header automatically, include create time
'''

# -*- coding: utf-8 -*-

#---------------------------------------------------------------

# Read data from a file

def ReadMDFile (strFilePath):
	message=""

	# check file path existance	

	import os
	result = os.path.isfile(strFilePath)
	if( result == False ):
		message= "Could not find the file. Please check again."
		return "",False,message
	
	# read the date to a string list

	fo = open(strFilePath,"r", encoding="utf-8")
	fileData = fo.readlines()
	fo.close()
	return fileData,True,message

#----------------------------------------------------------------	

# Check MD style header existance

def IsHeaderExist(fileList):
	if fileList[0] == "---\n" and fileList[6] == "---\n":
		return True
	else:
		return False
		
	
#----------------------------------------------------------------	

# Generate MarkDown header

def GenerateHeader(title, categories, tags):
	header = ["---","layout: post", "title: ", "date:   ", "categories: ", "tags: ", "---", "", "* content", "{:toc}", ""]
	header[2] += title
	
	# Get current time

	import datetime;
	currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	header[3] += currentTime
	
	#categories

	header[4] += "[" + categories + "]"
	
	# tags

	tags = "[" + tags +"]"
	header[5] += tags
	return header

#----------------------------------------------------------------	

# Format contents, add space for each description line, add white line for code's begin and end

def FormatData(lineData):
	length = len(lineData);
	index=0
	while (index < length):
		line = lineData[index].strip('\n')
		if(IsWhiteLine(line)):
			index +=1
			continue
		
		if IsHeader(line):
			if IsNotLastLine(index, length) :
				if (IsWhiteLine(lineData[index + 1]) is False):				
					lineData.insert(index + 1,"\n")
					length +=1
			index +=1
			continue
			
		if IsCodeLine(line):
			if IsNotLastLine(index, length) :
				if (IsDescription(lineData[index + 1]) or IsHeader(lineData[index + 1])):
					lineData.insert(index + 1,"\n")
					length +=1
			index += 1
			continue
		
		if line.endswith("   ") is False:
			line += "   "		
		if IsNotLastLine(index, length):
			if (IsCodeLine(lineData[index +1]) or IsHeader(lineData[index + 1])):
				lineData.insert(index +1, "\n")
				length += 1
			lineData[index] = line + "\n"		
		index +=1
	return

#----------------------------------------------------------------	

def IsHeader(line):
	line = line.strip()
	if line.startswith("#") or line.startswith("##") or line.startswith("###") or line.startswith("####"):
		return True
	return False

#----------------------------------------------------------------		

def IsWhiteLine(line):
	if(len(line.strip()) is 0):
		return True
	return False

#----------------------------------------------------------------		

def IsCodeLine(line):
	if(line[0] == "\t" ):
		return True
	return False

#----------------------------------------------------------------		

def IsDescription(line):
	if(IsWhiteLine(line) is False):
		if(IsCodeLine(line) is False):
			if IsHeader(line) is False:
				return True
	return False

#----------------------------------------------------------------		

def IsNotLastLine(index, length):
	if index < length -1:
		return True
	return False

#----------------------------------------------------------------	

def IsSubString(SubStrList,Str):  
	''''' 

	#判断字符串Str是否包含序列SubStrList中的某一个子字符串 

	#>>>SubStrList=['F','EMS','txt'] 

	#>>>Str='F06925EMS91.txt' 

	#>>>IsSubString(SubStrList,Str)#return True  

	'''  
	for substr in SubStrList:  
		if (substr in Str):  
			return True  
  
	return False  

#----------------------------------------------------------------	

def GetFileList(FindPath,FlagStr=[]):  
	''''' 

	#获取目录中指定的文件名 

	#>>>FlagStr=['F','EMS','txt'] #要求文件名称中包含这些字符 

	#>>>FileList=GetFileList(FindPath,FlagStr) # 

	'''  
	import os  
	# Check the directory exist
	if(os.path.isdir(FindPath)==False):
	   return 
	FileList=[]  
	FileNames=os.listdir(FindPath)  
	if (len(FileNames)>0):  
	   for fn in FileNames:  
		   if (len(FlagStr)>0):  

			   #返回指定类型的文件名  

			   if (IsSubString(FlagStr,fn)):  
				   fullfilename=os.path.join(FindPath,fn)  
				   FileList.append(fullfilename)  
		   else:  

			   #默认直接返回所有文件名  

			   fullfilename=os.path.join(FindPath,fn)  
			   FileList.append(fullfilename)  
  
	#对文件名排序  

	if (len(FileList)>0):  
		FileList.sort()  
  
	return FileList  	

#----------------------------------------------------------------

def FormatMDFile(filePath):
	linelists,result,message = ReadMDFile(filePath)
	if (result == False):
		print (message)
		return -1

	result = IsHeaderExist(linelists)

	if result is False :

		# Add MD header

		title = linelists[0].strip('\n')
		categories = linelists[1].strip('\n')
		tags = linelists[2].strip('\n')
		header = GenerateHeader(title, categories, tags)
		for index in range(len(header)):
			header[index] += "\n"
	
		lineData = linelists[4:]
	else:
		header = linelists[0:11]
		lineData = linelists[11:]

	# Format each line

	FormatData(lineData)

	newLinelists = header + lineData

	if newLinelists==linelists:
		return 0
	fo = open(filePath,"w", encoding="utf-8")
	fo.writelines(newLinelists)
	fo.close()
	return 1

#----------------------------------------------------------------

# Main Entry

import os
folder = "E:\kerwenzhang.github.io\_posts"
fileFlag = [".md",".txt"]
FileLists = GetFileList(folder, fileFlag)
if not FileLists:
        print("Could not find any file under",folder)
        exit()

fileListChanged =[]
for file in FileLists:
	result = FormatMDFile(file)
	if (result < 0):
		print ("Failed to format file : ", file)
		exit()
	else:
		if(result > 0):
			fileListChanged.append(file)			

if len(fileListChanged) == 0 :
	print ("No file need to be formated.")
	exit()

print ("Following files have been formated:")
for file in fileListChanged:
	print (file)
print("\n")
print("---------------------------")
print("Total Num:", len(fileListChanged))
