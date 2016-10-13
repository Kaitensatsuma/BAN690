import PyPDF2

print("What PDF do you want to scrape text from?")
pdf_file = PyPDF2.PdfFileReader(open(str(input()), 'rb'))
print("And where do you want to write to?")
text_file = str(input())
container = ''
iterations = range(pdf_file.numPages)

with open(text_file,'w') as file:
    for x in iterations:
        container = pdf_file.getPage(x).extractText()
        file.write(container)

