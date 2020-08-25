import pytesseract as ocr
from PIL import Image
import PIL
import pytesseract #screenshot
import pyscreenshot as pys
import PIL.ImageOps
import time
import pyautogui #Biblioteca automação
import ctypes  #Janela de aviso

import re
from string import punctuation

ocr.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

time.sleep(3)

pyautogui.mouseDown(button='right', x=30, y=859)
pyautogui.moveTo(30,990)
pyautogui.mouseUp(button='right')