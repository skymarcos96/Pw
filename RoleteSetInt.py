import pytesseract as ocr
from PIL import Image
import PIL
import pytesseract #screenshot
import PIL.ImageOps
import time
import pyautogui #Biblioteca automação
import os
import re
from string import punctuation
import win32gui, win32con

tesseract = r'Tesseract-OCR\tesseract.exe'

ocr.pytesseract.tesseract_cmd=tesseract

def main():

    QuantInt = int(input("Quantos adds de int vc quer?\n"))
    QuantRolete = input("Quantas Escultura da Reforja você possui?\n")

    rolete = int(QuantRolete)/2
    finalizador = 0

    ShowWindow() #Abre a Janela do pw

    BotaoReproduzir = LocateButton() #Localiza as coordenadas X e Y do botao reproduzir

    AreaAdds_X, AreaAdds_Y = {}, {}

    AreaAdds_X[0], AreaAdds_X[1] = int(BotaoReproduzir[0]+65), int(BotaoReproduzir[0]+92) #calcula a area do adds
    AreaAdds_Y[0], AreaAdds_Y[1] = int(BotaoReproduzir[1]-170), int(BotaoReproduzir[1]-54)

    while(finalizador <= rolete):

        pyautogui.click(BotaoReproduzir[0],BotaoReproduzir[1]) #CLica no botao Reproduzir
        time.sleep(1.5) #Espera 1.5 segundos para forjar o item

        imagem = pyautogui.screenshot(r'image\screenShot.bmp')
        area = (AreaAdds_X[0], AreaAdds_Y[0], AreaAdds_X[1], AreaAdds_Y[1]) #Defino o tamanho e o local da area a ser corada na imagem
        cropped_img = imagem.crop(area) #Corta a area na imagem onde ficam os adds
        #cropped_img.show() #Mostra a imagem cortada
        
        img_op = PIL.ImageOps.invert(cropped_img) #Inverte as cores para facilitar a leitura dos adds
        #img_op.show()
        txt_adds = ocr.image_to_string(img_op) #Extrai o texto da imagem e coloca na variavel
        #print(txt_adds)
        
        adds = re.split(r'[^0-9A-Za-z]+',txt_adds) #Separa os palavras em lista
        print(adds,'\n')
        
        intligencia = adds.count("Inteli") + adds.count("Intel") + adds.count("Inte") + adds.count("inte") + adds.count("intel")
        
        print(intligencia)

        if intligencia >= QuantInt:
            pyautogui.click(BotaoReproduzir[0]+155,BotaoReproduzir[1]-15) #CLica em segurar o novo add
            pyautogui.alert('Parabéns Vini, conseguimos uma parte do set com '+ QuantInt +' de Inteligência ','Gideon','OK')
            os.remove(r'image\screenShot.bmp')
            exit()
        else:
            pyautogui.click(BotaoReproduzir[0]-170,BotaoReproduzir[1]-15) #Clica em manter o antigo add
            time.sleep(1.5)



def ShowWindow():

    hwnd = win32gui.FindWindow(None, 'PW Play Fun')
    win32gui.SetForegroundWindow(hwnd)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    time.sleep(1)

def LocateButton():

    BotaoReproduzir = pyautogui.locateCenterOnScreen(r'image\botaoReproduzirOn.png', confidence=0.9)

    if(BotaoReproduzir == None):
        BotaoReproduzir = pyautogui.locateCenterOnScreen(r'image\botaoReproduzirOff.png', confidence=0.9)
        if(BotaoReproduzir == None):
            pyautogui.alert('Erro ao localizar o botão reproduzir, coloque a câmera do personagem em uma posição mais limpa(ex. olhando para o Céu) ou troque a janela de Produção de Equipamento de posição.','Gidon', 'OK')
            input("Presione Enter para continuar....")

    return BotaoReproduzir


if __name__ == '__main__': # chamada da funcao principal
    main() # chamada da função main