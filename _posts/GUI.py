# -*- coding: UTF-8 -*-
from tkinter import *

class MainWindow:
	def __init__(self):
		self.frame = Tk()
		
		self.label_search = Label(self.frame, text = "Input a word:")
		self.text_search = Text(self.frame, height="1",width=30)
		self.label_Result = Label(self.frame, text = "Result from iciba:")
		self.text_Result = Text(self.frame, height="1",width=30)
		self.label_search.grid(row=0,column=0)
		self.text_search.grid(row=1,column=0)
		self.label_Result.grid(row=2,column=0)
		self.text_Result.grid(row=3,column=0)
		
		self.frame.mainloop()
frame = MainWindow()