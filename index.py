import pyautogui as py

# VARIÁVEIS
computador_off = 0
buscador_whatsapp_x = 283
buscador_whatsapp_y = 258
py.PAUSE = 3
posicao_buscador_whatsapp = 0
posicao_primeira_celula = 0

# APRESENTAÇÃO

print("=========================")
print("Este programa tem como objetivo automatizar a o envio de boletos para permissionários com base nos parâmetros fornecidos.")
print("A estimativa é de que o processo levará cerca de 50 segundos por envio de boleto.")
print("Instruções importantes:")
print("1 - Para alternar entre janelas, use as teclas, em conjunto, na ordem 'Alt + Tab'.")
print("2 - Durante o processo de alternância de pastas, evite usar o mouse.")
print("3 - Enquanto o bot (robô) estiver ativo, certifique-se de que a alternância de janelas ocorra do terminal para a página de boletos (usando 'Alt + Tab').")
print("=========================")
# PASSOS PARA O SUCESSO DA EXECUÇÃO DO BOT
print("1 - Vá para o seu Whatsapp.")
print("2 - Coloque o cursor do mouse no buscador do whatsapp.")
input("3 - Volte para o terminal 'alt' + 'tab' sem mexer no mouse.")
posicao_buscador_whatsapp = py.position()
print("4 - Vá para o páginas de boletos.")
print("5 - Coloque o cursor do mouse na célula que informa o contato do recebedor.")
print("6 - Volte para o terminal 'alt' + 'tab' sem mexer no mouse.")
posicao_primeira_celula = py.position()
print("=========================")
print("1 - Ao usar esse bot o computador estará, até o término da execução do processo, inutilizável.")
print("2 - Garanta que a ordem das abas seja:")
print("3 - Terminal (aba atual) -> Whatsapp -> Planilha -> Página de boletos")
print("4 - Para organizar basta segurar a tecla 'alt' e apertar 'tab' para ordenar as telas.")
print("5 - Sem esta organização o bot não funcionará de forma adequada.")
input("Aperte enter para continuar: ")

def perguntar_desligar_computador():
    global computador_off
    
    computador_off = input("Gostaria que o computador fosse desligado após a operação?\n(1) - Sim\n(2) - Não\nDigite: ")
    if(computador_off == "1"):
        print("=========================")
        print("O computador desligará após a execução do script")
    elif(computador_off == "2"):
        print("=========================")
        print("O computador não será desligado!")
        print("=========================")
    else:
        print("=========================")
        print("Opção inválida")
        perguntar_desligar_computador()

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

perguntar_desligar_computador()
for i in range(1):   
    # FOCANDO NAS JANELAS - APENAS UMA VEZ
    proxima_janela(1)
    proxima_janela(2)
    proxima_janela(3)
    py.PAUSE = 1
    proxima_janela(1)
    
    if(i == 0):
        # COPIANDO VALOR NA CÉLULA DA PLANILHA
        py.moveTo(posicao_primeira_celula.x, posicao_primeira_celula.y)
        print(f"{i + 1}° execução - movendo cursor para célula")
        py.click()
        
    print(f"{i + 1}° execução - clicando na célula")
    py.hotkey("ctrl", "c")
    print(f"{i + 1}° execução - copiando valor da célula")
    
    # NA PÁGINA DO WHATSAPP - BUSCA NOME DO CONTATO
    proxima_janela(2)
    py.moveTo(posicao_buscador_whatsapp.x, posicao_buscador_whatsapp.y)
    print(f"{i + 1}° execução - cursor no buscador do whatsapp")
    py.click()
    print(f"{i + 1}° execução - clicando no buscador")
    limpa_campos()
    py.hotkey("ctrl", "v")
    print(f"{i + 1}° execução - colando valor no buscador")
    py.press("tab")
    py.press("tab")
    py.press("enter")
    print(f"{i + 1}° execução - entrando na chat do recebedor")
    
    # NA PÁGINA DA PLANILHA - COPIANDO NOME DO RECEBEDOR
    proxima_janela(1)
    py.press("left")
    py.hotkey("ctrl", "c")
    py.press("right")
    py.press("down")

    # NA PÁGINA DE BOLETOS - COPIANDO BOLETO COM NOME DO RECEBEDOR
    proxima_janela(2)
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

if(computador_off == "1"):
    py.hotkey("win","d")
    py.hotkey("alt","f4")
    # py.press("enter")
print("Execução finalizada!")
    
    # NA PÁGINA DA PLANILHA - COPIA NOME DO RECEBEDOR