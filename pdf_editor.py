# import modules
import PyPDF2
import os

# specify the path
os.chdir(r'C:\\Users\\john\\Downloads')

pdf1File = open('meetingminutes1.pdf','rb')
pdf2File = open('meetingminutes2.pdf','rb')

reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

open('combinedminutes.pdf','wb')