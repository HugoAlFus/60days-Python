from PIL import Image
from pdf2docx import Converter

path = "../../assets/example/"
img_jpg = "cat.jpg"
img_png = "cat.png"

img = Image.open(path + img_jpg)
img.save(path+img_png)

pdf_file = "sample.pdf"
docx_file = "sample.docx"

cv = Converter(path + pdf_file)
cv.convert(path + docx_file, start=0, end=None)
cv.close()
