
from PIL import Image
import pytesseract

img = Image.open('img/texto_ejemplo.png')
txt = pytesseract.image_to_string(img)

print(txt)
