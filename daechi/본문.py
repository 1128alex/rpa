import pyautogui
from pyautogui import ImageNotFoundException


def safe_locate_on_screen(*args, **kwargs):
    try:
        return pyautogui.locateOnScreen(*args, **kwargs, confidence=0.9)
    except ImageNotFoundException:
        return None


pyautogui.hotkey("alt", "tab")

pyautogui.click(900, 500)

pyautogui.hotkey("ctrl", "v")
pyautogui.sleep(0.3)
pyautogui.hotkey("ctrl", "a")

pyautogui.sleep(0.3)

fontSize = safe_locate_on_screen("font-size.png")
if fontSize is None:
    exit()

pyautogui.click(fontSize)
pyautogui.write("5")
pyautogui.sleep(0.2)
pyautogui.write(["enter"])

# pyautogui.click(500, 500)
pyautogui.sleep(0.2)
pyautogui.write(["pageup"])

pyautogui.sleep(0.2)
pyautogui.write(["down"])
pyautogui.sleep(0.2)
pyautogui.write(["down"])
pyautogui.sleep(0.2)
pyautogui.write(["down"])
pyautogui.sleep(0.2)
pyautogui.write(["down"])
pyautogui.sleep(0.2)
pyautogui.write(["home"])
pyautogui.sleep(0.2)

for i in range(40):
    pyautogui.hotkey("shift", "down")
    # pyautogui.hotkey("ctrl", "u")
    # pyautogui.click(safe_locate_on_screen("white.png"))
    pyautogui.write(["right"])
    pyautogui.write(["end"])
    pyautogui.write(["right"])
    pyautogui.write(["home"])

pyautogui.hotkey("ctrl", "a")
pyautogui.sleep(0.2)
pyautogui.click(fontSize)
pyautogui.sleep(0.2)
pyautogui.write("10")
pyautogui.sleep(0.2)
pyautogui.write(["enter"])
