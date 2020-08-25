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

    pyautogui.click(260,996) #CLica no botao Reproduzir
    time.sleep(1) #Espera 2 segundos para forjar o item
    #pyautogui.click(446,980) #CLica no botao de pegar o novo add
    #pyautogui.moveTo(1502,702) #Move o mouse para cima do item
    #time.sleep(1.5)

    imagem = pyautogui.screenshot('pw.bmp')
    area = (328, 825, 381, 930) #Defino o tamanho e o local da area a ser corada na imagem
    cropped_img = imagem.crop(area) #Corta a area na imagem onde ficam os adds
    #cropped_img.show() #Mostra a imagem cortada
    
    img_op = PIL.ImageOps.invert(cropped_img) #Inverte as cores para facilitar a leitura dos adds
    #img_op.show()
    txt_adds = ocr.image_to_string(img_op) #Extrai o texto da imagem e coloca na variavel
    #print(txt_adds)
    
    adds = re.split(r'[^0-9A-Za-z]+',txt_adds) #Separa os palavras em lista
    #print(adds)

    print(adds.count("Tempo"))

    if adds.count("Tempo") >= 4:
        pyautogui.click(425, 977)
        fianlizador = 1
        ctypes.windll.user32.MessageBoxW(0, "PARABÉNS MARCOS, CONSEGUIMOS UM PARTE R8 UP3 FULL INVOCAÇÃO.", "Gideon", 0)
    else:
        pyautogui.click(96, 975) #CLica no botao Manter atributo
        time.sleep(2)