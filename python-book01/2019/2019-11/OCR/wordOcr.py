import pytesseract
from PIL import Image

#pytesseract.pytesseract.tesseract_cmd = r'd://Program Files (x86)/Tesseract-OCR/tesseract.exe'
#text = pytesseract.image_to_string(Image.open(r'D:\Python\python-book01\2019\2019-11\jiangOCR\one.jpg'))


pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

text = pytesseract.image_to_string(Image.open(r'D:\Python\python-book01\2019\2019-11\jiangOCR\poem.jpeg'),lang='chi_sim')
print(text)