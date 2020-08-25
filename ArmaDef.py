import pytesseract as ocr
from PIL import Image
import PIL
import PIL.ImageOps
import time
import pyautogui #Biblioteca automação
import re
from string import punctuation

ocr.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

time.sleep(5) #espera 5 segundos ate iniciar

fianlizador = 0

while(fianlizador == 0):

    pyautogui.click(259,991) #CLica no botao Reproduzir
    time.sleep(1) #Espera 2 segundos para forjar o item

    imagem = pyautogui.screenshot('ArmaDef.bmp')
    #imagem.show() # mostrar a imagem
    
    area = (328, 825, 410, 935) #Defino o tamanho e o local da area a ser corada na imagem
    cropped_img = imagem.crop(area) #Corta a area na imagem onde ficam os adds
    #cropped_img.show() #Mostra a imagem cortada
    img_op = PIL.ImageOps.invert(cropped_img) #Inverte as cores para facilitar a leitura dos adds
    #img_op.show()
    txt_adds = ocr.image_to_string(img_op) #Extrai o texto da imagem e coloca na variavel
    #print(txt_adds)
    
    adds = re.split(r'[^0-9A-Za-z]+',txt_adds) #Separa os palavras em lista
    #print(adds)
    
    print('Defesa: ',adds.count("Defesa"))

    if adds.count("Defesa") >= 5:
        pyautogui.click(425, 977)
        fianlizador = 1
        pyautogui.alert('PARABÉNS MARCOS, CONSEGUIMOS UMA ARMA FULL NIVEL DE DEFESA.')
        exit()

    if adds.count("Defesa" == 4):
        pyautogui.click(425, 977)
    else:
        pyautogui.click(96, 975) #CLica no botao Manter atributo
        time.sleep(1.5)