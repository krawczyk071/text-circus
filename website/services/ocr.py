from PIL import Image
import pytesseract
import os
from dotenv import load_dotenv
load_dotenv()

TES_PATH = os.environ.get("TES_PATH")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def OCR(img_file):
    try:
        text = pytesseract.image_to_string(Image.open(img_file), lang='eng')
        print(text)
        return text
    except:
        return 'error'
