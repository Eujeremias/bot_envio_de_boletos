import pyautogui as py

# PRIMEIRA EXECUÇÃO

tempo_de_espera =  1

def proxima_janela(quantidade_de_janela):
    if(quantidade_de_janela == 1):
        py.hotkey("alt", "tab")
    elif(quantidade_de_janela == 2):
        py.keyDown("alt")
        py.press("tab")
        py.press("tab")
        py.keyUp("alt")
    elif(quantidade_de_janela == 3):
        py.keyDown("alt")
        py.press("tab")
        py.press("tab")
        py.press("tab")
        py.keyUp("alt")

def limpa_campos():
    py.hotkey("ctrl", "a")
    py.press("backspace")

# FOCANDO NAS JANELAS - APENAS UMA VEZ
proxima_janela(1)
proxima_janela(2)
proxima_janela(3)
py.PAUSE = tempo_de_espera

# COPIANDO VALOR NA CÉLULA DA PLANILHA
proxima_janela(1)
py.moveTo(1317, 373)
py.click()
py.hotkey("ctrl", "c")

# ------------------------------------ #

buscador_whatsapp_x = 283
buscador_whatsapp_y = 258

for i in range(2):     
    # NA PÁGINA DO WHATSAPP - BUSCA NOME DO CONTATO
    proxima_janela(2)
    py.moveTo(buscador_whatsapp_x, buscador_whatsapp_y)
    py.click()
    limpa_campos()
    py.hotkey("ctrl", "v")
    py.press("tab")
    py.press("tab")
    py.press("enter")
    
    # NA PÁGINA DA PLANILHA - COPIANDO NOME DO RECEBEDOR
    proxima_janela(1)
    py.press("left")
    py.hotkey("ctrl", "c")
    py.press("right")
    py.press("down")

    # NA PÁGINA DE BOLETOS - COPIANDO BOLETO COM NOME DO RECEBEDOR
    proxima_janela(3)
    py.hotkey("ctrl", "f")
    limpa_campos()
    py.hotkey("ctrl", "v")
    py.press("enter")
    py.press("down")
    py.hotkey("ctrl", "c")
    
    # NA PÁGINA DO WHATSAPP - ENVIANDO BOLETO PARA RECEBEDOR
    proxima_janela(2)
    py.hotkey("ctrl", "v")
    py.write("Segue o documento referente ao meix de {meix}")
    py.press("enter")
    
    # VOLTANDO AO FOCO
    proxima_janela(1)
    proxima_janela(2)
    proxima_janela(3)
    proxima_janela(3)
    proxima_janela(1)
    
    proxima_janela(1)
    proxima_janela(2)
    proxima_janela(3)
    py.PAUSE = tempo_de_espera
    proxima_janela(1)
    

    
    # NA PÁGINA DA PLANILHA - COPIA NOME DO RECEBEDOR