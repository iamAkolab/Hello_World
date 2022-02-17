# import modules
import PyPDF2
import os

# specify the path
os.chdir(r'C:\\Users\\john\\Downloads')

# files to open
pdf1File = open('meetingminutes1.pdf','rb')
pdf2File = open('meetingminutes2.pdf','rb')

# read the files
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

# create the writer object
writer = PyPDF2.PdfFileWriter()

# create a loop to open the pages
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

# create a loop to open the pages
for pageNum in range(reader2.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

# open with write
open('combinedminutes.pdf','wb')