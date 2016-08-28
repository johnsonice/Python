import PyPDF2
import os

pdfFile = open('test.pdf','rb')
reader = PyPDF2.PdfFileReader(pdfFile)
print reader.numPages                   # get page number

page = reader.getPage(0)                # get certain page
print page.extractText()                # extract text of the page

## loop through all pages
for pageNum in range(reader.numPages):
        content = reader.getpage(pageNum).extractText
