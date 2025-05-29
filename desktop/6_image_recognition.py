import pyautogui

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


# when the automation component is not shown right away
