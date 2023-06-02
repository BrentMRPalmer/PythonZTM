# PDF

import PyPDF2

# rb means "read binary" - let's the computer read the file as a binary file
with open('dummy.pdf', 'rb') as file:
	reader = PyPDF2.PdfFileReader(file)
	page = reader.getPage(0)
	with open('tilt.pdf', 'wb') as new_file:
		writer = PyPDF2.PdfFileWriter()
		writer.addPage(page.rotateClockwise(180))
		writer.write(new_file)
