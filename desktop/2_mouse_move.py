import pyautogui

# mouse movement

# # moveTo(x, y): move mouse to the coordinate
# pyautogui.moveTo(960, 540)

# # duration
# pyautogui.moveTo(960, 540, duration=1)


# sequence
pyautogui.moveTo(100, 200, duration=1)
pyautogui.moveTo(200, 300, duration=1)
pyautogui.moveTo(300, 400, duration=1)

# move(x, y): move mouse relative to current location
pyautogui.move(100, -100, duration=1)
pyautogui.move(100, -100, duration=1)

# position(): current coordinate of mouse
print(pyautogui.position())
p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y)
