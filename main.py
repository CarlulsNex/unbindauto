import pyautogui
import pyperclip
import time

print("Iniciando o script...")

time.sleep(1)  # Tempo para você preparar a janela do site

print("Tentando localizar o botão Tickets...")
tickets_button = pyautogui.locateCenterOnScreen('tickets_button.png')
if tickets_button:
    print("Botão Tickets encontrado, clicando...")
    pyautogui.click(tickets_button)
else:
    print("Botão Tickets não encontrado!")

time.sleep(1)

print("Tentando localizar o botão Desvinculo P2P...")
desvinculo_button = pyautogui.locateCenterOnScreen('desvinculo_button.png')
if desvinculo_button:
    print("Botão Desvinculo P2P encontrado, clicando...")
    pyautogui.click(desvinculo_button)
else:
    print("Botão Desvinculo P2P não encontrado!")

time.sleep(1)

print("copiando nome")
pyautogui.tripleClick(106,259)
pyautogui.hotkey('ctrl','c')

print("trocando tab")
pyautogui.hotkey('ctrl','tab')
pyautogui.click(428,162)
pyautogui.hotkey('ctrl','v')
print("voltando pro movi")
pyautogui.hotkey('ctrl','shift','tab')
pyautogui.tripleClick(61,285)
pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('ctrl','tab')
pyautogui.click(1057,168)
pyautogui.hotkey('ctrl','v')
pyautogui.click(517,214)
pyautogui.hotkey('ctrl','v')
pyautogui.click(1018,211)
pyautogui.typewrite("Hikvision")

pyautogui.hotkey('ctrl','shift','tab')
pyautogui.tripleClick(156,391)
pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('ctrl','tab')
pyautogui.click(1040,256)
pyautogui.hotkey('ctrl','v')

pyautogui.hotkey('ctrl','shift','tab')
pyautogui.click(833,293)

pyautogui.tripleClick(103,472)
pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('ctrl','tab')
print("parte serial")
def processar_texto(texto):
    # Função para dividir o texto e armazenar as partes em uma lista
    partes = texto.split('/')  # Divide o texto em partes com base na barra "/"
    return [parte.strip() for parte in partes]  # Remove espaços e retorna a lista

# Loop contínuo para verificar e processar o texto até que não haja mais "/"
while True:
    # Copiar o texto (assumindo que o texto já está selecionado)
    pyautogui.hotkey('ctrl', 'c')

    # Acessar o texto da área de transferência
    texto_copiado = pyperclip.paste()

    # Verificar se contém "/"
    if '/' in texto_copiado:
        # Se o texto contém "/", separa e armazena as partes
        partes = processar_texto(texto_copiado)
        
        # Processar cada parte do texto separadamente
        for i, parte in enumerate(partes):
            pyperclip.copy(parte)  # Define a parte atual na área de transferência
            create = pyautogui.locateCenterOnScreen('create.png')
            pyautogui.click(create)
            pyautogui.click(839,296)
            pyautogui.hotkey('ctrl', 'v') 
            pyautogui.click(1119,300)  
            time.sleep(6)
            pyautogui.click(850,458)
            pyautogui.typewrite("Desvinculo P2P")
            pyautogui.click(855,503)
            pyautogui.typewrite("Desvinculo P2P")
            pyautogui.click(1212,578)
            time.sleep(0.5)


        # Se o texto já foi processado, não precisa continuar o loop
        print("Todas as partes foram processadas.")
        break
    else:
        # Se não há mais barras no texto, sair do loop
        print("O texto não contém mais barras. Saindo do loop.")
        break

    # Adicione um pequeno delay para evitar loops muito rápidos
    pyautogui.sleep(1)