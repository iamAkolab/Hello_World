# import all the modules
import PyPDF2
import os

# specify the path
os.chdir(r'C:\\Users\\john\\Downloads')

# file to open
pdfFile = open('meetingminutes1.pdf','rb')

# read the file
reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)

#read a page
page1 = reader.getPage(0)
print(page1.extractText())

# read all pages using loop
for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())