import pyautogui

# sleep 1 for 1 second on every action
pyautogui.PAUSE = 1

# mouseInfo(): get mouse info of the current position
pyautogui.mouseInfo()

for i in range(5):
    pyautogui.move(100, 100)