import pyautogui
from pyautogui import ImageNotFoundException


# locateOnScreen(): find the image from current screen
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)

# pyautogui.click(file_menu)

# # when none of the image file exists on the current screen
# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)  # output: None

# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i)

# faster speed
# # 1. Grayscale
# trash_icon = pyautogui.locateOnScreen("file_menu.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# # 2. Set range
# trash_icon = pyautogui.locateOnScreen(
#     "file_menu.png", region=(1488, 623, 1881 - 1488, 137)
# )
# pyautogui.moveTo(trash_icon)

# # 3. Set accuracy
# trash_icon = pyautogui.locateOnScreen(
#     "file_menu.png", confidence=0.9
# )  # confidence level: 0.9
# pyautogui.moveTo(trash_icon)


def safe_locate_on_screen(*args, **kwargs):
    try:
        return pyautogui.locateOnScreen(*args, **kwargs)
    except ImageNotFoundException:
        return None


# when the automation component is not shown right away
# # 1. Wait until the image is shown
# file_menu_notepad = safe_locate_on_screen("file_menu_notepad.png")
# while file_menu_notepad is None:
#     file_menu_notepad = safe_locate_on_screen("file_menu_notepad.png")
#     print("fail")

# pyautogui.click(file_menu_notepad)

# 2. Wait for a certain time (Timeout)
import time
import sys

timeout = 10
start = time.time()
file_menu_notepad = None
while file_menu_notepad is None:
    file_menu_notepad = safe_locate_on_screen("file_menu_notepad.png")
    end = time.time()
    if end - start > timeout:
        print("시간 종료")
        sys.exit()


def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target


def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print("f[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()


# pyautogui.click(file_menu_notepad)

my_click("file_menu_notepad.png", 10)
