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

dinheiro = int(input('Digite a quantidade de moeda: '))
QuantRolete = int(input('Digite a quantidade de reliquia: '))

if dinheiro < 1500000000 and dinheiro % 1500000 !=  0:
    money = (int(dinheiro/1500000) * 1500000) - dinheiro
    pyautogui.click(1784, 994)#Clica em derrubar moeda
    time.sleep(1)
    pyautogui.press('backspace')
    time.sleep(0.5)
    pyautogui.write(str(money))
    time.sleep(1)
    pyautogui.press('enter')


contador = (1500000000 - dinheiro) / 1500000
rolete = int(QuantRolete/10)

def main():
    time.sleep(5) #espera 5 segundos ate iniciar
    fianlizador = 0
    global contador

    while(fianlizador <= rolete): #Faça enquanto tiver reliquia no bag
        contador+=1
        fianlizador+=1

        if contador >= 1001: #Se atingir o maximo de moedas, irar pegar mais moedas
            moeda()

        pyautogui.click(139, 996) #CLica no botao Reproduzir
        time.sleep(2) #Espera 2 segundos para forjar o item
        #pyautogui.click(446,980) #CLica no botao de pegar o novo add
        pyautogui.moveTo(175, 785) #Move o mouse para cima do item
        time.sleep(1.5)

        imagem = pyautogui.screenshot('pw.bmp')
        area = (670, 485, 724, 570) #Defino o tamanho e o local da area a ser corada na imagem
        cropped_img = imagem.crop(area) #Corta a area na imagem onde ficam os adds
        #cropped_img.show() #Mostra a imagem cortada
        
        img_op = PIL.ImageOps.invert(cropped_img) #Inverte as cores para facilitar a leitura dos adds
        #img_op.show()
        adds = ocr.image_to_string(img_op) # Coloca o texto na variavel adds
        #print(adds)
        
        teste = re.split(r'[^0-9A-Za-z]+',adds)
        #print(teste)

        seis = teste.count("6")
        cinco = teste.count("5")
        print('6%: ', seis)
        print('5%: ', cinco)

        if seis >= 4:
            exit()
        #if seis >=3 and cinco >= 1:
         #   exit()
        '''if seis >=2 and cinco >=2:
            exit()'''



def moeda():
    global contador
    contador = 1
    pyautogui.click(173,1060)#clica no element
    time.sleep(2)
    pyautogui.click(320,972)#clica no outro pessonagem
    time.sleep(2)
    pyautogui.doubleClick(925,475) #clica no Npc
    time.sleep(1)
    pyautogui.click(122,876)#clica em vender
    time.sleep(1)
    pyautogui.rightClick(1605, 844)#clica com direito no cupom
    time.sleep(1)
    pyautogui.press('backspace')
    time.sleep(0.5)
    pyautogui.write('150')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(300, 927)#Clica em vender
    time.sleep(1)
    pyautogui.press('y')
    time.sleep(1)
    pyautogui.press('y')
    time.sleep(1)
    pyautogui.click(324, 534)#Clica em fechar
    time.sleep(1)
    pyautogui.press('b')
    time.sleep(1)
    pyautogui.click(1784, 994)#Clica em derrubar moeda
    time.sleep(1)
    pyautogui.click(164, 968)#Clica em maximo
    time.sleep(1)
    pyautogui.click(79, 998)#Clica em OK
    time.sleep(1)
    pyautogui.press('1')#pega a moeda
    pyautogui.press('1')
    time.sleep(1)
    pyautogui.click(1784, 994)#Clica em derrubar moeda
    time.sleep(1)
    pyautogui.click(163, 968)#Clica em maximo
    time.sleep(1)
    pyautogui.click(79, 998)#Clica em OK
    time.sleep(1)
    pyautogui.press('1')#pega a moeda
    pyautogui.press('1')
    time.sleep(1)
    pyautogui.press('b')
    time.sleep(3)
    pyautogui.click(173,1060)#clica no element
    time.sleep(2)
    pyautogui.click(96,981)#clica no outro personagem
    time.sleep(2)



if __name__ == '__main__': # chamada da funcao principal
    main() # chamada da função main