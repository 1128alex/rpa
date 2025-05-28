import pyautogui

# sleep(t): halt of t seconds
pyautogui.sleep(3)
print(pyautogui.position())

# # click(x, y): click at (x, y)
# pyautogui.click(520, 198, duration=1)

# mouseDown(): push down click
pyautogui.mouseDown()
# mouseUp(): release click
pyautogui.mouseUp()

# # click multiple times
# pyautogui.doubleClick()
# pyautogui.click(clicks=500)

# mouse drag
pyautogui.mouseDown(430, 292)
pyautogui.moveTo(636, 462)
pyautogui.mouseUp()

# rightClick(): right click at (x, y)
# middleClick(): middle(wheel) click at (x, y)

pyautogui.moveTo()
# dragTo(): drag to coordinate
pyautogui.dragTo()
# drag(): dragging relatively
pyautogui.drag()

# scroll():
# positive: upward
# negative: downward
pyautogui.scroll(300)
