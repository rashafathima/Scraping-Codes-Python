# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 08:46:29 2022

@author: Rasha
"""

import PyPDF2 #importing packages
import re
a = open('C:/Users/Rasha/Downloads/sample.pdf','rb')
pdfread = PyPDF2.PdfFileReader(a) #using file reader function to traverse the pdf
print(pdfread.numPages) #finding the number of pages in the pdf. In our case we had 2
pageobj = pdfread.getPage(0) #extracting the first page
b = re.compile(r'Address:\d{1,5}\s\w+,\s\w+,\s\w+') #setting up regular expression
x = pageobj.extractText() #extracting all text from first page
c = b.findall(x) #finding all the text from first page that matches with our re
for i in c: #printing all addresses in separate lines
    print(i)