fileName = 'MyDoc.pdf'
documentTitle = 'Document1'
title = 'DISNEYLAND'
subTitle = 'Two Themed Park!'

textLines = [
 'Disneyland Park, originally Disneyland,',
 'is the first of two theme parks built at the',
 'Disneyland Resort in Anaheim, California, opened', 
 'on July 17, 1955. It is the only theme park', 
 'designed and built to completion under the', 
 'direct supervision of Walt Disney.'
]
image = 'disneyland.jpg'
#Create document 
from reportlab.pdfgen import canvas 

pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)

# Sub Title 
# RGB - Red Green and Blue
pdf.setFillColorRGB(0, 0, 255)
pdf.setFont("Courier-Bold", 24)
pdf.drawCentredString(290,720, subTitle)

# 3) Draw a line
pdf.line(30, 710, 550, 710)
pdf.drawInlineImage(image, 100, 200)

from reportlab.lib import colors

text = pdf.beginText(40, 680)
text.setFont("Courier", 18)
text.setFillColor(colors.red)
for line in textLines:
    text.textLine(line)

pdf.drawText(text)

pdf.save()