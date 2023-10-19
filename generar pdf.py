#para instalar usas pip install reportlab

import reportlab
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

# initializing variables with values
fileName = 'certificado.pdf'
documentTitle = 'sample' #no se si esto tiene uso pero ahi va jsjsj
title = 'Technology'
subTitle = 'The largest thing now!!'
textLines = [
    'Technology makes us aware of',
    'the world around us.',
]
image = 'image.jpg'
 
# creating a pdf object
pdf = canvas.Canvas(fileName)
 
# setting the title of the document
pdf.setTitle(documentTitle)
 
# creating the title by setting it's font 
# and putting it on the canvas
pdf.setFont('Helvetica',36)
"""hay un archivo llamado _fontdata.py, alli estan los tipos de letra"""
pdf.drawCentredString(300, 770, title)
 
# creating the subtitle by setting it's font, 
# colour and putting it on the canvas
pdf.setFillColorRGB(0, 0, 255)
pdf.setFont("Courier-Bold", 24)
pdf.drawCentredString(290, 720, subTitle)
 
# drawing a line
pdf.line(30, 710, 550, 710)
 
# creating a multiline text using 
# textline and for loop
text = pdf.beginText(40, 680)
text.setFont("Courier", 18)
text.setFillColor(colors.red)
for line in textLines:
    text.textLine(line)
pdf.drawText(text)
 
# drawing a image at the 
# specified (x.y) position
#pdf.drawInlineImage(image, 130, 400) #insertar el escudo de ingenieria o que
 
# saving the pdf
pdf.save()
