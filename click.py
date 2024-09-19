import pyautogui
import time
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

