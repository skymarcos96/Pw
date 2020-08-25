import pytesseract as ocr
from PIL import Image
import PIL
import PIL.ImageOps
import time
import pyautogui #Biblioteca automação
import re
from string import punctuation
import win32gui, win32con
import os


agora = r'Tesseract-OCR\tesseract.exe'

ocr.pytesseract.tesseract_cmd=agora

print('O que deseja fazer?\n')
opcion = input('1- Tentar pegar o set full dex.\n2- Tentar pegar arma full def.\n')
exit()



def main():
    Menu(opcion)

def Menu(opcion):
    if opcion == 1:
        RoleteSet()
    if opcion == 2:
        ArmaDef()

def ArmaDef():
    print("Olá, iremos tentar pegar sua arma full def.\n")
    time.sleep(2)
    hwnd = win32gui.FindWindow(None, 'PW Play Fun')
    win32gui.SetForegroundWindow(hwnd)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)

    time.sleep(2) #espera 5 segundos ate iniciar

    while(1):

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
            pyautogui.alert('PARABÉNS MARCOS, CONSEGUIMOS UMA ARMA FULL NIVEL DE DEFESA.')
            exit()

        if adds.count("Defesa" == 4):
            pyautogui.click(425, 977)
        else:
            pyautogui.click(96, 975) #CLica no botao Manter atributo
            time.sleep(1.5)


def RoleteSet():
    
    QuantRolete = input("Quantas Escultura da Reforja você possui?\n")

    hwnd = win32gui.FindWindow(None, 'PW Play Fun')
    win32gui.SetForegroundWindow(hwnd)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)

    BotaoReproduzir = pyautogui.locateCenterOnScreen(r'image\botaoReproduzirOn.png', confidence=0.9)

    if(BotaoReproduzir == None):
        BotaoReproduzir = pyautogui.locateCenterOnScreen(r'image\botaoReproduzirOff.png', confidence=0.9)
    if(BotaoReproduzir == None):
        pyautogui.alert('Erro ao localizar o botão reproduzir, coloque a câmera do personagem em uma posição mais limpa(ex. olhando para o Céu) ou troque a janela de Produção de Equipamento de posição.','Gidon', 'OK')
        input("Presione Enter para continuar....")

    AreaAdds_X, AreaAdds_Y = {}, {}

    AreaAdds_X[0], AreaAdds_X[1] = int(BotaoReproduzir[0]+65), int(BotaoReproduzir[0]+205)
    AreaAdds_Y[0], AreaAdds_Y[1] = int(BotaoReproduzir[1]-170), int(BotaoReproduzir[1]-50)

    rolete = int(QuantRolete)/2
    finalizador = 0
    Adddex = False

    while(finalizador <= rolete):
        finalizador+=1
        pyautogui.click(BotaoReproduzir[0],BotaoReproduzir[1]) #CLica no botao Reproduzir
        time.sleep(1.5)

        imagem = pyautogui.screenshot(r'image\screenShot.bmp')
    
        area = (AreaAdds_X[0], AreaAdds_Y[0], AreaAdds_X[1], AreaAdds_Y[1]) #Defino o tamanho e o local da area a ser corada na imagem
        cropped_img = imagem.crop(area) #Corta a area na imagem onde ficam os adds
        #cropped_img.show() #Mostra a imagem cortada

        img_op = PIL.ImageOps.invert(cropped_img) #Inverte as cores para facilitar a leitura dos adds
        #img_op.show()
        adds = ocr.image_to_string(img_op) # Coloca o texto na variavel adds
        #print(adds)

        
        teste = re.split(r'[^0-9A-Za-z]+',adds)
        #print(teste)

        destreza = 0
        deztreza = teste.count('Destreza')+teste.count('Dectreza')
        if destreza >= 4:
            pyautogui.click(BotaoReproduzir[0]+155,BotaoReproduzir[1]-15) #CLica em segurar o novo add
            pyautogui.alert('Parabéns Luor, conseguimos uma parte do set full Destreza ','Gideon','Adoro')
            os.remove(r'image\screenShot.bmp')
            exit()    
        if deztreza == 3:
            pyautogui.click(BotaoReproduzir[0]+155,BotaoReproduzir[1]-15) #CLica em segurar o novo add
            Adddex = True
        else:
            pyautogui.click(BotaoReproduzir[0]-170,BotaoReproduzir[1]-15) #Clica em manter o antigo add
            time.sleep(1.5)

        if finalizador == rolete and Adddex == True:
            pyautogui.alert('Desculpe Luor, nossos recursos acabaram e só conseguimos uma parte do set com 3 add de Destreza ','Gideon','OK')
            os.remove(r'image\screenShot.bmp')