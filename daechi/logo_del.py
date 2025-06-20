import pyautogui
from pyautogui import ImageNotFoundException


def safe_locate_on_screen(*args, **kwargs):
    try:
        return pyautogui.locateOnScreen(*args, **kwargs, confidence=0.9)
    except ImageNotFoundException:
        return None


pyautogui.hotkey("alt", "tab")

for i in range(30):
    pyautogui.sleep(0.3)

    # w = pyautogui.getWindowsWithTitle("동아(이) 5-6과 자료 - 파일 탐색기")[0]
    # if w.isActive == False:
    #     w.activate()

    pyautogui.write("2")
    pyautogui.write(["enter"])
    pyautogui.sleep(3)

    # pyautogui.moveTo(900, 500)
    active_window = pyautogui.getActiveWindow()
    center_x = active_window.left + active_window.width // 2
    center_y = active_window.top + active_window.height // 2
    pyautogui.click(center_x, center_y)

    logo = safe_locate_on_screen("logo.png")

    i = 0
    while logo is None and i != 5:
        pyautogui.scroll(-500)
        logo = safe_locate_on_screen("logo.png")
        print("fail")
        pyautogui.sleep(0.7)
        i += 1

    if logo is None:
        pyautogui.hotkey("alt", "f4")
        continue

    pyautogui.doubleClick(logo)
    pyautogui.sleep(0.7)
    pyautogui.click(logo)
    pyautogui.sleep(0.7)

    pyautogui.write(["delete"])
    pyautogui.sleep(0.5)
    pyautogui.hotkey("shift", "esc")
    pyautogui.sleep(0.5)

    pyautogui.hotkey("ctrl", "s")
    pyautogui.hotkey("alt", "f4")
