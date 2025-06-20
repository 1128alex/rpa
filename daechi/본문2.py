import pyautogui
from pyautogui import ImageNotFoundException


def safe_locate_on_screen(*args, **kwargs):
    try:
        return pyautogui.locateOnScreen(*args, **kwargs, confidence=0.9)
    except ImageNotFoundException:
        return None


pyautogui.hotkey("alt", "tab")

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
pyautogui.write(["left"])

pyautogui.sleep(0.2)
pyautogui.write(["down"])
pyautogui.sleep(0.2)
pyautogui.write(["down"])
pyautogui.sleep(0.2)
pyautogui.write(["home"])
pyautogui.sleep(0.2)

lineNum = 45

for i in range(lineNum):
    pyautogui.hotkey("shift", "down")
    pyautogui.hotkey("ctrl", "u")
    pyautogui.click(safe_locate_on_screen("white.png"))
    pyautogui.write(["end"])
    pyautogui.write(["backspace"])

    # j = 0
    # word_check = safe_locate_on_screen("55.png")
    # while word_check is None and j != 50:
    #     pyautogui.write(" ")
    #     pyautogui.sleep(0.1)
    #     word_check = safe_locate_on_screen("55.png")
    #     j += 1

    pyautogui.write(["right"])
    pyautogui.write(["end"])
    pyautogui.write(["right"])
    pyautogui.write(["home"])

# for k in range(lineNum * 2):
#     pyautogui.hotkey("shift", "up")
