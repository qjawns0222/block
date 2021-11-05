import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'tes/tesseract.exe'
img = Image.open("베트나.png")
text = pytesseract.image_to_string(img, lang='vie')
print(text)
