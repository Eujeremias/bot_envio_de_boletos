import pyautogui as py
import keyboard as kb

# VARIÁVEIS
computador_off = 0
buscador_whatsapp_x = 283
buscador_whatsapp_y = 258
py.PAUSE = 2
posicao_buscador_whatsapp = 0
posicao_primeira_celula = 0
quantidade_de_boletos = 0
mes = ""

# FUNÇÕES
def perguntar_desligar_computador():
    global computador_off
    refazer = 0
    
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
    
    refazer = int(input("Gostaria de refazer a operação?\n(1) - Sim\n(2) - Não\nDigite:  "))
    if(refazer == 1):
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


# APRESENTAÇÃO

def apresentacao():
    
    # ACESSANDO VARIÁVEIS GLOBAIS
    global quantidade_de_boletos
    global mes
    global posicao_buscador_whatsapp
    global posicao_primeira_celula
    
    print("=========================")
    print("Este programa tem como objetivo automatizar o envio de boletos para permissionários com base nos parâmetros fornecidos.")
    print("A estimativa é de que o processo levará cerca de 1 minuto e meio por envio de boleto.")
    print("Instruções importantes:")
    print("1 - Para alternar entre janelas, use as teclas, em conjunto, na ordem 'Alt + Tab'.")
    print("2 - Durante o processo de troca de pastas, evite usar o mouse.")
    print("3 - Enquanto o bot (robô) estiver ativo, certifique-se de que a troca de janelas ocorra do terminal para a página de boletos (usando 'Alt + Tab').")
    print("=========================")
    # PASSOS PARA O SUCESSO DA EXECUÇÃO DO BOT
    print("1 - Vá para o seu Whatsapp.")
    print("2 - Coloque o cursor do mouse no buscador do whatsapp.")
    print("3 - Volte para o terminal utilizando 'alt' + 'tab' sem mexer no mouse.")
    input("Aperte 'enter' para continuar: ")
    posicao_buscador_whatsapp = py.position()
    print("4 - Vá para a planilha.")
    print("6 - Coloque o cursor do mouse na célula que informa o contato do recebedor.")
    print("7 - Volte para o terminal 'alt' + 'tab' sem mexer no mouse.")
    input("Aperte 'enter' para continuar: ")
    posicao_primeira_celula = py.position()
    print("=========================")
    print("1 - Ao usar esse bot o computador estará, até o término da execução do processo, inutilizável.")
    print("2 - Garanta que a ordem das abas seja:")
    print("3 - Terminal (aba atual) -> Whatsapp -> Planilha -> Página de boletos")
    print("4 - Para ordenar as abas realize a seguinte operação: segure 'alt' e pressione 'tab' duas vezes")
    print("5 - Depois disso, aperte em conjunto 'alt' + 'tab'. Assim retornará a este terminal")
    print("6 - Sem esta organização o bot não funcionará de forma adequada.")
    quantidade_de_boletos = int(input("Antes de iniciar, informe a quantidade de boletos que serão enviados: "))
    print(f"O bot enviará {quantidade_de_boletos} boletos.")
    print(f"Para enviar um boleto, demorá entorno de 1 minuto. Dado sua quantidade de boletos, demorará: {quantidade_de_boletos / 60} horas ")
    mes = input("Informe o mês dos boletos: ")
    
    perguntar_desligar_computador()

apresentacao()

for i in range(quantidade_de_boletos):   
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
    kb.write(f"Olá, tudo bem? Segue o boleto referente ao mês de {mes}. Por favor, confira os dados antes de efetuar o pagamento")
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
    py.press("enter")
print("Execução finalizada!")