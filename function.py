import pyautogui #Biblioteca automação
import win32gui, win32con
import time

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
            pyautogui.alert('Erro ao localizar o botão reproduzir, verifique se você abriu a janela de Reprodução de Equipamento.\n'
                            'Se você ja esta com a janela aberta, coloque a câmera do personagem em uma posição mais limpa (ex. olhando para o Céu),'
                            ' ou a janela em outra coordenada.\n','I.A do John', 'OK')
            input("Presione qualquer tecla para fechar....")

    return BotaoReproduzir