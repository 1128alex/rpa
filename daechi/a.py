import pyautogui
from pyautogui import ImageNotFoundException

pyautogui.hotkey("alt", "tab")

for i in range(8):
    pyautogui.write(["backspace", "right", "end", "right"])
