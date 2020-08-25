import pytesseract as ocr
from PIL import Image
import PIL
import pytesseract #screenshot
import PIL.ImageOps
import time
import pyautogui #Biblioteca automação
import ctypes  #Janela de aviso

import re
from string import punctuation

ocr.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

time.sleep(5) #espera 5 segundos ate iniciar

fianlizador = 0

while(fianlizador == 0):

    pyautogui.click(139, 996) #CLica no botao Reproduzir
    time.sleep(2) #Espera 2 segundos para forjar o item
    #pyautogui.click(446,980) #CLica no botao de pegar o novo add
    pyautogui.moveTo(175, 785) #Move o mouse para cima do item
    time.sleep(1.5)
    imagem = pyautogui.screenshot('pw.bmp')
    area = (574, 394, 625, 482) #Defino o tamanho e o local da area a ser corada na imagem
    cropped_img = imagem.crop(area) #Corta a area na imagem onde ficam os adds
    #cropped_img.show() #Mostra a imagem cortada
    
    img_op = PIL.ImageOps.invert(cropped_img) #Inverte as cores para facilitar a leitura dos adds
    #img_op.show()
    adds = ocr.image_to_string(img_op) # Coloca o texto na variavel adds
    #print(adds)
    
    teste = re.split(r'[^0-9A-Za-z]+',adds)
    #print(teste)

    onze = teste.count("11") + teste.count("411") + teste.count("44") + teste.count("41")
    doze = teste.count("12") + teste.count("412") + teste.count("42")

    print('11: ', onze)
    print('12: ', doze)
    
    if doze >= 4:
        ctypes.windll.user32.MessageBoxW(0, "PARABÉNS MARCOS, CONSEGUIMOS FULL 12 de int", "Gideon", 0)
        exit()
    if onze >= 3 and doze >= 1:
        ctypes.windll.user32.MessageBoxW(0, "PARABÉNS MARCOS, CONSEGUIMOS ", "Gideon", 0)
        exit()
    if onze >= 2 and doze >= 2:
        ctypes.windll.user32.MessageBoxW(0, "PARABÉNS MARCOS, CONSEGUIMOS", "Gideon", 0)
        exit()
    if onze >= 1 and doze >= 3:
        ctypes.windll.user32.MessageBoxW(0, "PARABÉNS MARCOS, CONSEGUIMOS", "Gideon", 0)
        exit()