import pyautogui

# screenshot(): take a screenshot
img = pyautogui.screenshot()
img.save('screenshot.png')

pyautogui.mouseInfo()
# 28,18, 34, 167, 242 #22A7F2

pixel = pyautogui.pixel(28, 18)
print(pixel)  # Output: (34, 167, 242)

# pixelMatchesColor(): check if the pixel color matches
print(pyautogui.pixelMatchesColor(28, 18, (34, 167, 242)))  # True
print(pyautogui.pixelMatchesColor(28, 18, pixel))  # True
print(pyautogui.pixelMatchesColor(28, 18, (34, 167, 243)))  # False

