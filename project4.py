import pyttsx3
import PyPDF2

book = open("file.pdf","rb")

pdfReader= PyPDF2.PdfFileReader(book)

pages=pdfReader.numPages

print(pages)

speaker= pyttsx3.init()

page=pdfReader.getPage(4)

text=page.extractText()
print(text)
speaker.say(text)
speaker.runAndWait()