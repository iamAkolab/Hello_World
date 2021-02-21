import PyPDF2
import os

os.chdir(r'C:\\Users\\john\\Downloads')

pdfFile = open('meetingminutes1.pdf','rb')

reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)

page1 = reader.getPage(0)
print(page1.extractText())

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())