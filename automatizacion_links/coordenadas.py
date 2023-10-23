import pyautogui

# Muestra las coordenadas del cursor del mouse en tiempo real
try:
    while True:
        x, y = pyautogui.position()
        print(f"Coordenadas del mouse: X = {x}, Y = {y}", end="\r")
except KeyboardInterrupt:
    print("\nTerminado.") 

