# import libraries
import docx

# function to open and read file into text
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText('C:\\Users\\john\\Downloads\\demo.docx'))