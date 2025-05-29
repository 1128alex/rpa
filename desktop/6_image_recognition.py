import pyautogui

# locateOnScreen(): find the image from current screen
file_menu = pyautogui.locateOnScreen("file_menu.png")
print(file_menu)

pyautogui.click(file_menu)

# # when none of the image file exists on the current screen
# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)  # output: None

for i in pyautogui.locateAllOnScreen("checkbox.png"):
    print(i)
    pyautogui.click(i)
