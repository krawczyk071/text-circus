from PIL import ImageGrab, Image
import pyperclip
import pytesseract

# from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# myconfig = r"--psm 11 --oem 3"
# get screen from clipbord
img = ImageGrab.grabclipboard()

if img:
    text = pytesseract.image_to_string(img)
    ## you can save picture as backup
    # img.save('data/temp/clipboard_image.jpg')
    pyperclip.copy(text)
    print(text)
else:
    print('No image in the clipboard')